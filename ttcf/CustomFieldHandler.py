from abc import ABC, abstractmethod

from pypaperless import Paperless
from pypaperless.models.common import CustomFieldType
from pypaperless.models.custom_fields import CustomFieldHelper

from ttcf.config import CustomFieldConfig, Types


class CustomFieldHandler(ABC):
    def __init__(self, custom_field_config: CustomFieldConfig, api: Paperless):
        self.config = custom_field_config
        self.api = api
        self.cfh = CustomFieldHelper(api)

    async def _find_custom_field(self):
        cfs = await self.api.custom_fields.all()
        for cf_id in cfs:
            if cf_id == self.config.id:
                return await self.api.custom_fields(cf_id)

        raise ValueError(f"No CustomField found for id: {self.config.id}")

    def need_work(self, doc):
        tagsset = set(doc.tags)
        idset = set([tag.id for tag in self.config.tags])
        selected_tag_id = idset.intersection(tagsset)
        return len(selected_tag_id) > 0

    async def _get_value(self, doc):
        tagsset = set(doc.tags)
        idset = set([tag.id for tag in self.config.tags])
        selected_tag_id = idset.intersection(tagsset)
        if len(selected_tag_id) == 1:
            selid = list(selected_tag_id)[0]
            result = [tag.value for tag in self.config.tags if tag.id == selid]
            return result[0] if result else None
        elif len(selected_tag_id) > 1:
            raise ValueError(f"too many tags set {selected_tag_id}")
        else:
            return None

    async def update_doc(self, doc):
        value_to_set = await self._get_value(doc)
        try:
            field = list(filter(lambda x: x.field == self.config.id, doc.custom_fields))[0]
        except IndexError:
            field = None
        if field is None or field.value is not value_to_set:
            if field is not None:
                field.value = value_to_set
            else:
                doc.custom_fields.append(self.cfh.draft(field=self.config.id, value=value_to_set))
            print(f"{doc.title} has now custom_fields: {doc.custom_fields}")
            await doc.update()

    @classmethod
    def for_config(cls, config: CustomFieldConfig, api: Paperless):
        if config.type == Types.BOOLEAN:
            return BooleanCustomFieldHandler(config, api)
        elif config.type == Types.SELECT:
            return SelectCustomFieldHandler(config, api)
        else:
            raise NotImplementedError(f"no handler implemented for type {config.type}")


class SelectCustomFieldHandler(CustomFieldHandler):
    def __init__(self, custom_field_config: CustomFieldConfig, api: Paperless):
        super().__init__(custom_field_config, api)
        self.options = None

    async def _get_value(self, doc):
        option_value = await super()._get_value(doc)
        return (await self._get_options()).index(option_value)

    async def _get_options(self):
        if self.options is None:
            custom_field = await self._find_custom_field()
            # noinspection PyProtectedMember
            self.options = custom_field._data["extra_data"]["select_options"]
        return self.options


class BooleanCustomFieldHandler(CustomFieldHandler):
    def __init__(self, custom_field_config: CustomFieldConfig, api: Paperless):
        super().__init__(custom_field_config, api)

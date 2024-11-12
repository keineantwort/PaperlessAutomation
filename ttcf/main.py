import asyncio

import yaml
from pypaperless.models.custom_fields import CustomFieldHelper

from pla import PaperlessAccess


async def main(paperless_access: PaperlessAccess):
    with open("ttcf.yaml", 'r') as the_yaml:
        config = yaml.safe_load(the_yaml)
        the_yaml.close()

        paperless = paperless_access.paperless()
        mapping = {}
        for tagm in config["tags"]:
            mapping[tagm["tag_id"]] = tagm["option_value"]

        custom_field_id = config["custom_field_id"]

        filters = {"tags__id__in": ",".join(map(str, mapping.keys()))}

        async with paperless:
            cfs = await paperless.custom_fields.all()
            cfo = None
            for cf_id in cfs:
                if cf_id == custom_field_id:
                    cfo = (await paperless.custom_fields(cf_id))._data["extra_data"]["select_options"]

            async with paperless.documents.reduce(**filters) as filtered:
                async for doc in filtered:
                    tagsset = set(doc.tags)
                    keyset = set(mapping.keys())
                    selected_tag_id = keyset.intersection(tagsset)
                    target = mapping[list(selected_tag_id)[0]]
                    target_pos = cfo.index(target)
                    field = list(filter(lambda x: x.field == custom_field_id, doc.custom_fields))[0]
                    if field is None or field.value is not target_pos:
                        if field is not None:
                            field.value = target_pos
                        else:
                            doc.custom_fields.append(CustomFieldHelper.draft(field=custom_field_id, value=target_pos))
                        print(f"{doc.title} has no custom_fields: {doc.custom_fields}")
                        await doc.update()
                    else:
                        print(f"{doc.id} \"{doc.title}\" already has the desired value \"{target}\" ({target_pos})")


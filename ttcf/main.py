import asyncio

import yaml
from pypaperless.models.common import CustomFieldType
from pypaperless.models.custom_fields import CustomFieldHelper

from pla import PaperlessAccess
from ttcf.CustomFieldHandler import CustomFieldHandler
from ttcf.config import Config


async def main(paperless_access: PaperlessAccess):
    config = Config()

    paperless = paperless_access.paperless()
    async with paperless:
        for field in config.fields:
            filters = {"tags__id__in": ",".join(map(str, [tag.id for tag in field.tags]))}

            handler = CustomFieldHandler.for_config(field, paperless)

            async with paperless.documents.reduce(**filters) as filtered:
                async for doc in filtered:
                    await handler.update_doc(doc)

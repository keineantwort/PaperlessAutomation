from pla import PaperlessAccess
from ttcf.CustomFieldHandler import CustomFieldHandler
from ttcf.config import Config


async def main(paperless_access: PaperlessAccess, document_id: int, config_file: str = "../ttcf.yaml"):
    config = Config(document_id=document_id,
                    config_file=config_file)

    paperless = paperless_access.paperless()
    async with paperless:
        for field in config.fields:
            handler = CustomFieldHandler.for_config(field, paperless)
            doc = await paperless.documents(config.document_id)

            if handler.need_work(doc):
                await handler.update_doc(doc)
                try:
                    await doc.update()
                except Exception as e:
                    print(f"Error: {e}")
            else:
                print(f"skipping document {doc.id} > {doc.title}")

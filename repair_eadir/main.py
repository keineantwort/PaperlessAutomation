import re
from datetime import datetime

import yaml

from pla import PaperlessAccess


def parse_document_string(input_string):
    pattern = r"^(\d{8})\s(.+?)\.(jpe?g)$"
    match = re.match(pattern, input_string, re.IGNORECASE)

    if match:
        date_raw = match.group(1)
        title = match.group(2)
        date = f"{date_raw[:4]}-{date_raw[4:6]}-{date_raw[6:]}"
        return date, title
    else:
        base_name = re.sub(r'\.(jpe?g)$', '', input_string, flags=re.IGNORECASE)
        return None, base_name


async def main(paperless_access: PaperlessAccess, document_id: int, config_file: str = "../repair_eadir.yaml"):
    paperless = paperless_access.paperless()
    async with paperless:
        count = 0
        async for tag in paperless.tags:
            if (tag.name.lower().endswith("jpeg") or tag.name.lower().endswith("jpg")) and tag.document_count > 0:
                count = count + 1
                print(f"---------------\nTag: {tag.id} > {tag.name} ({tag.document_count})")
                date, title = parse_document_string(tag.name)
                print(f"{date} > {title}")

                filters = {"tags__id__all": f"339, {tag.id}"}
                async with paperless.documents.reduce(**filters) as filtered:
                    async for doc in filtered:
                        if doc.title.endswith("_XL"):
                            print(f"{doc.title} > {doc.created}")
                            doc.title = title
                            doc.created = date
                            doc.created_date = date
                            doc.tags.remove(tag.id)
                            doc.tags.remove(339)
                            success = await doc.update()
                            if success:
                                print(f"Doc updated: {doc.title} ({doc.id})")
                            else:
                                print(f"!!!! COULD NOT UPDATE {doc.title} ({doc.id})")
                            pass
                        else:
                            success = await doc.delete()
                            if success:
                                print(f"{doc.title} ({doc.id}) deleted")
                            else:
                                print(f"!!!! COULD NOT DELETE {doc.title} ({doc.id})")
                success = await tag.delete()
                if success:
                    print(f"Tag {tag.name} deleted.")
                else:
                    print(f"!!!! COULD NOT DELETE {tag.name}")

                #if count == 1:
                #    break

from dataclasses import dataclass
from enum import Enum
from typing import Any, List

import yaml
from pypaperless.models.common import CustomFieldType


@dataclass
class ConfigType:
    cft: CustomFieldType
    name: str


class Types(Enum):
    BOOLEAN = ConfigType(cft=CustomFieldType.BOOLEAN, name="boolean")
    SELECT = ConfigType(cft=CustomFieldType.UNKNOWN, name="select")

    @classmethod
    def from_name(cls, name):
        for member in cls:
            if member.value.name == name:
                return member
        raise ValueError(f"No member found for name: {name}")


@dataclass
class TagConfig:
    id: int
    value: Any


@dataclass
class CustomFieldConfig:
    id: int
    type: Types
    tags: List[TagConfig]

    @classmethod
    def from_yaml(cls, yaml_dict: dict):
        tags = []
        for tag in yaml_dict["tags"]:
            tags.append(TagConfig(id=tag["tag_id"], value=tag["option_value"]))
        return cls(
            id=yaml_dict["custom_field_id"],
            type=Types.from_name(yaml_dict["type"]),
            tags=tags
        )


class Config:
    def __init__(self, document_id: int, config_file: str = "ttcf.yaml"):
        with open(config_file, 'r') as the_yaml:
            config = yaml.safe_load(the_yaml)
            the_yaml.close()

        self.fields = []
        for cf in config["fields"]:
            self.fields.append(CustomFieldConfig.from_yaml(cf))

        self.document_id = document_id

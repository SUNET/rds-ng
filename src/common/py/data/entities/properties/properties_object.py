from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from dataclasses_json import DataClassJsonMixin

from .properties_profile import ProfileID

PropertyValues = dict[str, Any]

@dataclass
class ProjectObject(DataClassJsonMixin):
    """
    A project object.

    Attributes:
        id: The ID of the object.
        value: The values of the object.
        refs: The references that the object holds to other objects, by their id.
    """

    id: str
    value: PropertyValues
    refs: List[str]
    type: str = ""
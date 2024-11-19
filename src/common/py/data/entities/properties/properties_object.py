from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from dataclasses_json import dataclass_json

from .properties_profile import ProfileID

PropertyValues = dict[str, Any]

@dataclass_json
@dataclass
class ProjectObject:
    """
    A project object.

    Attributes:
        id: The ID of the object.
        value: The values of the object.
        refs: The references that the object holds to other objects, by their id.
    """

    id: str
    value: Dict[str, Any]
    refs: List[str]
    type: Optional[str] = ""
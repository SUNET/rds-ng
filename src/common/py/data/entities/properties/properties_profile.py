from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

from dataclasses_json import dataclass_json

### should probably be in a separate folder, is this is not specific to metadata but to general properties

ProfileID = Tuple[str, str]

@dataclass_json
@dataclass
class ProfileMetadata:
    id: ProfileID
    displayLabel: str
    description: str

@dataclass_json
@dataclass
class ProfileClassInput:
    id: str
    label: str
    type: str
    description: Optional[str] = None
    example: Optional[str] = None
    options: Optional[List[str]] = field(default_factory=list)
    required: Optional[bool] = None

@dataclass_json
@dataclass
class ProfileClass:
    id: str
    displayLabel: str
    type: List[str]
    description: Optional[str] = None
    labelTemplate: Optional[str] = None
    required: Optional[bool] = False
    multiple: Optional[bool] = False
    example: Optional[str] = None
    input: Optional[List[ProfileClassInput]] = field(default_factory=list)

ProfileClassDictionary = dict[str, ProfileClass]

@dataclass_json
@dataclass
class PropertyProfile:
    metadata: ProfileMetadata
    layout: ProfileClass
    classes: Optional[ProfileClassDictionary] = field(default_factory=Dict)
    
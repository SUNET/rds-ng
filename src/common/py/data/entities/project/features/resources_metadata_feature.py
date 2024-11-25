import typing
from dataclasses import dataclass, field

from dataclasses_json import dataclass_json

from ...properties.properties_object import ProjectObject
from .project_feature import ProjectFeature, ProjectFeatureID

ResourcesMetadata = typing.Dict[
    str, typing.List[ProjectObject]
    ]



@dataclass_json
@dataclass
class ResourcesMetadataFeature(ProjectFeature):
    """
    Data class for the resources metadata project feature.
    """

    feature_id: typing.ClassVar[ProjectFeatureID] = "resources_metadata"

    metadata: ResourcesMetadata = field(default_factory=dict)

from enum import StrEnum


class ProjectUploadState(StrEnum):
    """
    The upload state of a project.
    """

    UNKNOWN = "unknown"

    DEFAULT = "default"
    UPLOADED = "uploaded"
    LOCKED = "locked"

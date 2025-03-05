from dataclasses import dataclass

from common.py.data.entities.project import ProjectExternalState


@dataclass(kw_only=True)
class ProjectVolatileState:
    """
    The volatile state of a project.

    Attributes:
        external_state: The project's external state.
        timestamp: The timestamp of the volatile state.
    """

    external_state: ProjectExternalState

    timestamp: float = 0.0

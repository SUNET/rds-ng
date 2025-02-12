from dataclasses import dataclass
from enum import StrEnum

from .logbook import ProjectJobHistoryRecordExtDataIDs
from .project import Project
from ..connector import ConnectorInstanceID


@dataclass(kw_only=True)
class ProjectExternalState:
    """
    A project's external state.

    Attributes:
        external_state: The state on the external service.
        external_id: The project ID within the external service.
    """

    class State(StrEnum):
        """
        The external state of a project.
        """

        UNKNOWN = "unknown"

        DEFAULT = "default"
        UPLOADED = "uploaded"
        LOCKED = "locked"

    external_state: State
    external_id: str


def get_external_project_state(
    project: Project, connector_instance: ConnectorInstanceID
) -> ProjectExternalState:
    """
    Retrieves the external state of a project consisting of its base upload state and external ID.

    Args:
        project: The project.
        connector_instance: The connector instance ID.

    Returns:
        The external state of the project.
    """

    from .logbook import get_most_recent_job_history_record_by_connector_instance

    if (
        record := get_most_recent_job_history_record_by_connector_instance(
            project, connector_instance, succeeded_only=True
        )
    ) is not None:
        state = ProjectExternalState.State.UPLOADED
        external_id = (
            record.ext_data[ProjectJobHistoryRecordExtDataIDs.EXTERNAL_ID]
            if ProjectJobHistoryRecordExtDataIDs.EXTERNAL_ID in record.ext_data
            else ""
        )
    else:
        state = ProjectExternalState.State.DEFAULT
        external_id = ""

    return ProjectExternalState(external_state=state, external_id=external_id)

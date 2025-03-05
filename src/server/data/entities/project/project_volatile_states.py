import time
import typing

from common.py.data.entities.connector import ConnectorInstanceID
from common.py.data.entities.project import ProjectExternalState, ProjectID

from .project_volatile_state import ProjectVolatileState


class ProjectVolatileStates:
    """
    A map of all project volatile states (mapped using the project and connector instance ID).
    """

    REFRESH_INTERVAL = 60 * 60  # Once per hour

    def __init__(self):
        self._states: typing.Dict[
            typing.Tuple[ProjectID, ConnectorInstanceID], ProjectVolatileState
        ] = {}

    def get(
        self, project_id: ProjectID, instance_id: ConnectorInstanceID
    ) -> ProjectVolatileState:
        """
        Gets the volatile state for a specific project and connector instance, creating a default one if necessary.

        Args:
            project_id: The project ID.
            instance_id: The connector instance ID.

        Returns:
            The volatile project state.
        """
        if not self.contains(project_id, instance_id):
            self._states[(project_id, instance_id)] = ProjectVolatileState(
                external_state=ProjectExternalState(
                    external_state=ProjectExternalState.State.UNKNOWN, external_id=""
                )
            )
        return self._states[(project_id, instance_id)]

    def contains(self, project_id: ProjectID, instance_id: ConnectorInstanceID) -> bool:
        """
        Checks whether a state is stored for a specific project and connector instance.

        Args:
            project_id: The project ID.
            instance_id: The connector instance ID.
        """
        return (project_id, instance_id) in self._states

    def needs_refresh(
        self, project_id: ProjectID, instance_id: ConnectorInstanceID
    ) -> bool:
        """
        Checks whether a state needs to be refreshed.

        Args:
            project_id: The project ID.
            instance_id: The connector instance ID.
        """
        state = self.get(project_id, instance_id)

        return (
            state.timestamp == 0
            or time.time() - state.timestamp >= self.REFRESH_INTERVAL
        )

    def refresh(self, project_id: ProjectID, instance_id: ConnectorInstanceID) -> None:
        """
        Updates the timestamp of a volatile state.

        Args:
            project_id: The project ID.
            instance_id: The connector instance ID.
        """
        self[project_id, instance_id].timestamp = time.time()

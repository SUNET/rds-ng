from ....data.entities.project import ProjectVolatileStates


class UserSessionData:
    """
    User-specific (volatile) data stored in the user's session.
    """

    def __init__(self):
        self._volatile_project_states = ProjectVolatileStates()

    def process(self) -> None:
        """
        Called periodically to perform recurring tasks.
        """

        self._volatile_project_states.update_outdated_states()

    @property
    def volatile_project_states(self) -> ProjectVolatileStates:
        return self._volatile_project_states

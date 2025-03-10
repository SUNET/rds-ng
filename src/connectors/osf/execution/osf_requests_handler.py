from common.py.api import ProjectExternalStateRenewalEvent
from ...base.data.types import ProjectExternalStateCallbacks

from ...base.execution import ConnectorRequestsHandler


class OSFRequestsHandler(ConnectorRequestsHandler):
    """
    OSF-specific class to deal with non-job related requests.
    """

    def renew_external_project_state(
        self,
        event: ProjectExternalStateRenewalEvent,
        *,
        callbacks: ProjectExternalStateCallbacks,
    ) -> None:
        # TODO
        pass

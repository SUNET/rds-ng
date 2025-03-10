from common.py.api import ProjectExternalStateRenewalEvent
from common.py.data.entities.project import ProjectExternalState

from ...base.data.types import ProjectExternalStateCallbacks
from ...base.execution import ConnectorRequestsHandler


class StubRequestsHandler(ConnectorRequestsHandler):
    """
    Stub-specific class to deal with non-job related requests.
    """

    def renew_external_project_state(
        self,
        event: ProjectExternalStateRenewalEvent,
        *,
        external_state: ProjectExternalState,
        callbacks: ProjectExternalStateCallbacks,
    ) -> None:
        from .stub_utils import process_external_project_state

        process_external_project_state(external_state)
        callbacks.invoke_done_callbacks(external_state)

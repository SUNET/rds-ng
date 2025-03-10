from common.py.api import ProjectExternalStateRenewalEvent
from common.py.core.messaging import Channel
from common.py.data.entities.connector import ConnectorInstanceID
from common.py.data.entities.project import ProjectExternalState
from common.py.data.entities.user import UserToken
from common.py.services import Service

from ..zenodo import ZenodoClient, ZenodoGetProjectCallbacks, ZenodoProjectObject
from ...base.data.types import ProjectExternalStateCallbacks
from ...base.execution import ConnectorRequestsHandler


class ZenodoRequestsHandler(ConnectorRequestsHandler):
    """
    Zenodo-specific class to deal with non-job related requests.
    """

    def renew_external_project_state(
        self,
        svc: Service,
        msg: ProjectExternalStateRenewalEvent,
        *,
        auth_channel: Channel,
        external_state: ProjectExternalState,
        callbacks: ProjectExternalStateCallbacks,
    ) -> None:
        def _get_project_done(project: ZenodoProjectObject) -> None:
            from .zenodo_utils import process_external_project_state

            process_external_project_state(project, external_state)
            callbacks.invoke_done_callbacks(external_state)

        def _get_project_failed(exc: Exception) -> None:
            callbacks.invoke_fail_callbacks(exc)

        if (
            client := self._create_client(
                svc,
                auth_channel=auth_channel,
                connector_instance=msg.connector_instance,
                user_token=msg.user_token,
            )
        ) is not None:
            get_project_callbacks = ZenodoGetProjectCallbacks()
            get_project_callbacks.done(_get_project_done)
            get_project_callbacks.failed(_get_project_failed)

            client.get_project(
                external_state.external_id, callbacks=get_project_callbacks
            )

    def _create_client(
        self,
        svc: Service,
        *,
        auth_channel: Channel,
        connector_instance: ConnectorInstanceID,
        user_token: UserToken,
    ) -> ZenodoClient:
        return ZenodoClient(
            self._comp,
            svc,
            connector_instance=connector_instance,
            auth_channel=auth_channel,
            user_token=user_token,
        )

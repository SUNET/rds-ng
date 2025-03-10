import abc
import typing

from common.py.api import ProjectExternalStateRenewalEvent
from common.py.component import BackendComponent
from common.py.core.messaging import Channel
from common.py.data.entities.project import ProjectExternalState
from common.py.services import Service

from ..data.types import ProjectExternalStateCallbacks


class ConnectorRequestsHandler(abc.ABC):
    """
    Base class to deal with non-job related requests.
    """

    def __init__(self, comp: BackendComponent):
        self._comp = comp

    def renew_external_project_state(
        self,
        service: Service,
        msg: ProjectExternalStateRenewalEvent,
        *,
        auth_channel: Channel,
        external_state: ProjectExternalState,
        callbacks: ProjectExternalStateCallbacks,
    ) -> None:
        """
        Called whenever an external project state needs to be renewed.

        Args:
            service: The service to handle the request.
            msg: The originating message.
            auth_channel: The channel for authorizations.
            external_state: The current external state.
            callbacks: Callbacks to be invoked upon completion.
        """
        raise NotImplementedError()


# pylint: disable=invalid-name
ConnectorRequestsHandlerType = typing.TypeVar(
    "ConnectorRequestsHandlerType", bound=ConnectorRequestsHandler
)

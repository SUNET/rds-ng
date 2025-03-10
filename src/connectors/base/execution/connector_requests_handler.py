import abc
import typing

from common.py.api import ProjectExternalStateRenewalEvent

from ..data.types import ProjectExternalStateCallbacks


class ConnectorRequestsHandler(abc.ABC):
    """
    Base class to deal with non-job related requests.
    """

    def renew_external_project_state(
        self,
        event: ProjectExternalStateRenewalEvent,
        *,
        callbacks: ProjectExternalStateCallbacks,
    ) -> None:
        """
        Called whenever an external project state needs to be renewed.

        Args:
            event: The originating event.
            callbacks: Callbacks to be invoked upon completion.
        """
        raise NotImplementedError()


# pylint: disable=invalid-name
ConnectorRequestsHandlerType = typing.TypeVar(
    "ConnectorRequestsHandlerType", bound=ConnectorRequestsHandler
)

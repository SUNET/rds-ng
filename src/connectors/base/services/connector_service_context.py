from common.py.services import ClientServiceContext

from ..execution import ConnectorJobsEngine, ConnectorRequestsHandler


class ConnectorServiceContext(ClientServiceContext):
    """
    Service context specific to connectors.
    """

    _jobs_engine: ConnectorJobsEngine | None = None
    _requests_handler: ConnectorRequestsHandler | None = None

    @staticmethod
    def set_jobs_engine(engine: ConnectorJobsEngine) -> None:
        """
        Sets the global connector jobs engine.

        Args:
            engine: The connector jobs engine.
        """
        ConnectorServiceContext._jobs_engine = engine

    @property
    def jobs_engine(self) -> ConnectorJobsEngine:
        """
        The connector jobs engine.

        Raises:
            RuntimeError: If the job engine hasn't been set.
        """
        if ConnectorServiceContext._jobs_engine is None:
            raise RuntimeError(
                "Tried to access the jobs engine prior to its assignment"
            )

        return ConnectorServiceContext._jobs_engine

    @staticmethod
    def set_requests_handler(handler: ConnectorRequestsHandler) -> None:
        """
        Sets the global connector requests handler.

        Args:
            handler: The connector requests handler.
        """
        ConnectorServiceContext._requests_handler = handler

    @property
    def requests_handler(self) -> ConnectorRequestsHandler:
        """
        The connector requests handler.

        Raises:
            RuntimeError: If the requests handler hasn't been set.
        """
        if ConnectorServiceContext._requests_handler is None:
            raise RuntimeError(
                "Tried to access the requests handler prior to its assignment"
            )

        return ConnectorServiceContext._requests_handler

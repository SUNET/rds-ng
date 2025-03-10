from common.py.component import BackendComponent
from common.py.services import Service


def create_projects_service(comp: BackendComponent) -> Service:
    """
    Creates the projects service.

    Args:
        comp: The main component instance.

    Returns:
        The newly created service.
    """

    from common.py.api import ProjectExternalStateRenewalEvent

    from .connector_service_context import ConnectorServiceContext

    svc = comp.create_service("Projects service", context_type=ConnectorServiceContext)

    @svc.message_handler(ProjectExternalStateRenewalEvent, is_async=True)
    def project_external_state_renewal(
        msg: ProjectExternalStateRenewalEvent, ctx: ConnectorServiceContext
    ) -> None:
        pass
        # TODO

    return svc

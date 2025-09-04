from common.py.data.entities.connector import ConnectorInstanceID
from common.py.data.entities.project import Project, ProjectExternalState
from common.py.data.entities.user import UserToken

from ...base.data.types import ProjectExternalStateCallbacks
from ...base.execution import ConnectorRequestsHandler


class InvenioRDMRequestsHandler(ConnectorRequestsHandler):
    """
    InvenioRDM-specific class to deal with non-job related requests.
    """

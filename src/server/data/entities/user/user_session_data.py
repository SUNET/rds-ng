import typing
from dataclasses import dataclass, field

from server.data.entities.project import ProjectVolatileStates
from server.networking.session.session import SessionID
from server.services import ServerServiceContext


@dataclass(kw_only=True)
class UserSessionData:
    """
    User-specific (volatile) data stored in the user's session.
    """

    volatile_project_states: ProjectVolatileStates = field(
        default_factory=ProjectVolatileStates
    )


def get_user_session_data(
    session_id: SessionID, ctx: ServerServiceContext
) -> UserSessionData:
    """
    Retrieves the volatile user data for the specified session, creating a default one if necessary.

    Args:
        session_id: The session ID.
        ctx: The server context.

    Returns:
        The session's user data.
    """

    session_key = "$_user_data_$"
    if session_key not in ctx.session_manager[session_id]:
        ctx.session_manager[session_id][session_key] = UserSessionData()
    return typing.cast(UserSessionData, ctx.session_manager[session_id][session_key])

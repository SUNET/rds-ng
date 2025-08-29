import typing

from ..authorization_strategy import AuthorizationStrategy
from ... import AuthorizationRequestPayload
from .....component import BackendComponent
from .....data.entities.authorization import AuthorizationSettings, AuthorizationToken
from .....data.entities.user import UserID, UserToken
from .....services import Service


class BasicStrategy(AuthorizationStrategy):
    """
    Basic authorization strategy.
    """

    Strategy: str = "basic"

    def __init__(
        self,
        comp: BackendComponent,
        svc: Service,
        *,
        user_token: UserToken | None = None,
        auth_token: AuthorizationToken | None = None,
        auth_private: AuthorizationSettings | None = None,
    ):
        super().__init__(
            comp,
            svc,
            BasicStrategy.Strategy,
            contents=(
                AuthorizationStrategy.ContentType.AUTH_LOGIN
                | AuthorizationStrategy.ContentType.AUTH_PASSWORD
            ),
            user_token=user_token,
            auth_token=auth_token,
            auth_private=auth_private,
        )

    def request_authorization(
        self,
        user_id: UserID,
        payload: AuthorizationRequestPayload,
        request_data: typing.Any,
    ) -> AuthorizationToken:
        # TODO
        pass
        # oauth2_data = self._get_oauth2_request_data(request_data)
        # client_secret = self._get_client_secret(payload.auth_bearer)
        #
        # response = requests.post(
        #     urllib.parse.urljoin(oauth2_data.token_host, oauth2_data.token_endpoint),
        #     data={
        #         "grant_type": "authorization_code",
        #         "client_id": oauth2_data.client_id,
        #         "client_secret": client_secret,
        #         "scope": oauth2_data.scope,
        #         "code": oauth2_data.auth_code,
        #         "redirect_uri": oauth2_data.redirect_url,
        #     },
        #     timeout=self._request_timeout,
        # )
        #
        # if response.status_code == HTTPStatus.OK:
        #     resp_data = response.json()
        #     try:
        #         self._verify_oauth2_token_data(resp_data)
        #
        #         return AuthorizationToken(
        #             user_id=user_id,
        #             auth_id=payload.auth_id,
        #             auth_type=payload.auth_type,
        #             auth_issuer=payload.auth_issuer,
        #             auth_issuer_url=payload.auth_issuer_url,
        #             auth_bearer=payload.auth_bearer,
        #             state=AuthorizationToken.TokenState.VALID,
        #             timestamp=time.time(),
        #             expiration_timestamp=self._get_expiration_timestamp(resp_data),
        #             refresh_attempts=0,
        #             strategy=self.strategy,
        #             token=typing.cast(
        #                 typing.Dict[any, str], self._create_oauth2_token(resp_data)
        #             ),
        #             data=typing.cast(
        #                 typing.Dict[any, str],
        #                 OAuth2TokenData(
        #                     token_host=oauth2_data.token_host,
        #                     token_endpoint=oauth2_data.token_endpoint,
        #                     client_id=oauth2_data.client_id,
        #                     scope=oauth2_data.scope,
        #                 ),
        #             ),
        #         )
        #     except Exception as exc:  # pylint: disable=broad-exception-caught
        #         raise RuntimeError(f"Invalid OAuth2 token received: {exc}")
        # else:
        #     raise RuntimeError(
        #         f"Unable to request access token: {format_oauth2_error_response(response)}"
        #     )

    def refresh_authorization(self, token: AuthorizationToken) -> None:
        # We simply reset the token so it continues to be valid
        super()._update_token_refresh_state(token, reset=True)

    def _get_token_content(
        self, token: AuthorizationToken, content: AuthorizationStrategy.ContentType
    ) -> typing.Any:
        # TODO
        return None
        # We only support a single content type, so no need to distinguish
        # oauth2_token, _ = self._get_oauth2_data_from_token(token)
        # return oauth2_token.access_token


def create_basic_strategy(
    comp: BackendComponent,
    svc: Service,
    *,
    user_token: UserToken | None = None,
    auth_token: AuthorizationToken | None = None,
    auth_private: AuthorizationSettings | None = None,
) -> BasicStrategy:
    """
    Creates a new OAuth2 strategy instance.

    Args:
        comp: The main component.
        svc: The service to use for message sending.
        user_token: An optional user token.
        auth_token: An optional authorization token.
        auth_private: Optional private authorization settings.

    Returns:
        The newly created strategy.
    """
    return BasicStrategy(
        comp,
        svc,
        user_token=user_token,
        auth_token=auth_token,
        auth_private=auth_private,
    )

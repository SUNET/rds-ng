---
sidebar_label: oauth2_types
title: integration.authorization.strategies.oauth2.oauth2_types
---

## OAuth2AuthorizationRequestData Objects

```python
@dataclass_json

@dataclass(frozen=True, kw_only=True)
class OAuth2AuthorizationRequestData()
```

OAuth2 authorization request data.

**Attributes**:

- `token_host` - The OAuth2 token host.
- `token_endpoint` - The OAuth2 token endpoint.
- `client_id` - The OAuth2 client ID.
- `auth_code` - The authorization code.
- `scope` - An optional access scope.
- `redirect_url` - The redirection URL.

## OAuth2Token Objects

```python
@dataclass_json

@dataclass(frozen=True, kw_only=True)
class OAuth2Token()
```

OAuth2 access token.

**Attributes**:

- `access_token` - The actual token.
- `token_type` - The type of the token.
- `refresh_token` - The refresh token (optional).

## OAuth2TokenData Objects

```python
@dataclass_json

@dataclass(frozen=True, kw_only=True)
class OAuth2TokenData()
```

OAuth2 additional token data.

**Attributes**:

- `token_host` - The OAuth2 token host.
- `token_endpoint` - The OAuth2 token endpoint.
- `client_id` - The OAuth2 client ID.
- `scope` - An optional access scope.


---
sidebar_label: authorization_token
title: data.entities.authorization.authorization_token
---

## AuthorizationToken Objects

```python
@dataclass_json

@dataclass(kw_only=True)
class AuthorizationToken()
```

A token holding authorization information for an external system.

**Attributes**:

- `user_id` - The user identifier.
- `auth_id` - The ID of this token.
- `auth_type` - The token type.
- `auth_issuer` - The entity that requires the authorization.
- `auth_bearer` - The bearer that will be authorized against.
- `state` - The state of the token.
- `timestamp` - The timestamp of the token.
- `expiration_timestamp` - Timestamp when the token becomes invalid; a value of 0 means that the token never becomes invalid.
- `refresh_attempts` - The number of refresh attempts.
- `strategy` - The token strategy (e.g., OAuth2).
- `auth_id`0 - The actual token data.
- `auth_id`1 - Arbitrary strategy data (usually configuration).

## TokenType Objects

```python
class TokenType(StrEnum)
```

Various token types.

## TokenState Objects

```python
class TokenState(StrEnum)
```

The state of a token.


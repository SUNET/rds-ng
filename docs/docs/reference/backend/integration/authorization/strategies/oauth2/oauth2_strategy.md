---
sidebar_label: oauth2_strategy
title: integration.authorization.strategies.oauth2.oauth2_strategy
---

## OAuth2StrategyPublicConfiguration Objects

```python
@dataclass_json

@dataclass(frozen=True, kw_only=True)
class OAuth2StrategyPublicConfiguration()
```

The OAuth2 strategy public configuration.

## OAuth2StrategyPrivateConfiguration Objects

```python
@dataclass_json

@dataclass(frozen=True, kw_only=True)
class OAuth2StrategyPrivateConfiguration()
```

The OAuth2 strategy private configuration.

## OAuth2Strategy Objects

```python
class OAuth2Strategy(AuthorizationStrategy)
```

OAuth2 authorization strategy.

#### create\_oauth2\_strategy

```python
def create_oauth2_strategy(
        comp: BackendComponent,
        svc: Service,
        *,
        user_token: UserToken | None = None,
        auth_token: AuthorizationToken | None = None,
        auth_private: AuthorizationSettings | None = None) -> OAuth2Strategy
```

Creates a new OAuth2 strategy instance.

**Arguments**:

- `comp` - The main component.
- `svc` - The service to use for message sending.
- `user_token` - An optional user token.
- `auth_token` - An optional authorization token.
- `auth_private` - Optional private authorization settings.
  

**Returns**:

  The newly created strategy.


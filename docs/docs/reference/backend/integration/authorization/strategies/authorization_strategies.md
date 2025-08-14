---
sidebar_label: authorization_strategies
title: integration.authorization.strategies.authorization_strategies
---

#### register\_authorization\_strategies

```python
def register_authorization_strategies() -> None
```

Registers all available authorization strategies.

When adding a new strategy, always register it here.

#### create\_authorization\_strategy

```python
def create_authorization_strategy(
    comp: BackendComponent,
    svc: Service,
    strategy: str,
    *,
    user_token: UserToken | None = None,
    auth_token: AuthorizationToken | None = None,
    auth_private: AuthorizationSettings | None = None
) -> AuthorizationStrategy
```

Creates an authorization strategy using the specified identifier.

**Arguments**:

- `comp` - The global component.
- `svc` - The service to use for message sending.
- `strategy` - The strategy identifier.
- `user_token` - An optional user token.
- `auth_token` - An optional authorization token.
- `auth_private` - Optional private authorization settings.
  

**Returns**:

  The newly created strategy.


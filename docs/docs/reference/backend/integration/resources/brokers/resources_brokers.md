---
sidebar_label: resources_brokers
title: integration.resources.brokers.resources_brokers
---

#### register\_resources\_brokers

```python
def register_resources_brokers() -> None
```

Registers all available resources brokers.

When adding a new broker, always register it here.

#### create\_resources\_broker

```python
def create_resources_broker(
        comp: BackendComponent,
        svc: Service,
        broker: str,
        config: typing.Any,
        *,
        user_token: UserToken,
        auth_token: AuthorizationToken | None = None,
        auth_token_refresh: bool = True) -> ResourcesBroker
```

Creates a resources broker using the specified identifier.

**Arguments**:

- `comp` - The global component.
- `svc` - The service used for message sending.
- `broker` - The broker identifier.
- `config` - The broker configuration as an arbitrary record.
- `user_token` - The user token.
- `auth_token` - An optional authorization token.
- `auth_token_refresh` - Whether expired authorization tokens should be refreshed automatically.
  

**Returns**:

  The newly created broker.


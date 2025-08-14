---
sidebar_label: filesystem_broker
title: integration.resources.brokers.filesystem.filesystem_broker
---

## FilesystemBrokerConfiguration Objects

```python
@dataclass_json

@dataclass(frozen=True, kw_only=True)
class FilesystemBrokerConfiguration()
```

The filesystem broker configuration.

## FilesystemBroker Objects

```python
class FilesystemBroker(ResourcesBroker)
```

Filesystem resources broker.

#### create\_filesystem\_broker

```python
def create_filesystem_broker(
        comp: BackendComponent,
        svc: Service,
        config: typing.Any,
        *,
        user_token: UserToken,
        auth_token: AuthorizationToken | None = None,
        auth_token_refresh: bool = True) -> FilesystemBroker
```

Creates a new filesystem broker instance, automatically configuring it.

**Arguments**:

- `comp` - The main component.
- `svc` - The service used for message sending.
- `config` - The broker configuration.
- `user_token` - The user token.
- `auth_token` - An optional authorization token.
- `auth_token_refresh` - Whether expired authorization tokens should be refreshed automatically.
  

**Returns**:

  The newly created broker.


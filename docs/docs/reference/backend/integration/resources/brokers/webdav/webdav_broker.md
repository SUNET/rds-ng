---
sidebar_label: webdav_broker
title: integration.resources.brokers.webdav.webdav_broker
---

## WebdavBrokerConfiguration Objects

```python
@dataclass_json

@dataclass(frozen=True, kw_only=True)
class WebdavBrokerConfiguration()
```

The WebDAV broker configuration.

## WebdavBroker Objects

```python
class WebdavBroker(ResourcesBroker)
```

WebDAV resources broker.

#### create\_webdav\_broker

```python
def create_webdav_broker(comp: BackendComponent,
                         svc: Service,
                         config: typing.Any,
                         *,
                         user_token: UserToken,
                         auth_token: AuthorizationToken | None = None,
                         auth_token_refresh: bool = True) -> WebdavBroker
```

Creates a new WebDAV broker instance, automatically configuring it.

**Arguments**:

- `comp` - The main component.
- `svc` - The service used for message sending.
- `config` - The broker configuration.
- `user_token` - The user token.
- `auth_token` - An optional authorization token.
- `auth_token_refresh` - Whether expired authorization tokens should be refreshed automatically.
  

**Returns**:

  The newly created broker.


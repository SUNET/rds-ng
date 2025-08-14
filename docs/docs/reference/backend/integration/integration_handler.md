---
sidebar_label: integration_handler
title: integration.integration_handler
---

## IntegrationHandler Objects

```python
class IntegrationHandler(abc.ABC)
```

Base class for integration handlers.

#### \_\_init\_\_

```python
def __init__(comp: BackendComponent,
             svc: Service,
             *,
             user_token: UserToken | None = None,
             auth_token: AuthorizationToken | None = None,
             auth_private: AuthorizationSettings | None = None)
```

**Arguments**:

- `comp` - The global component.
- `svc` - The service to use for message sending.
- `user_token` - An optional user token.
- `auth_token` - An optional authorization token.
- `auth_private` - Optional private authorization settings.


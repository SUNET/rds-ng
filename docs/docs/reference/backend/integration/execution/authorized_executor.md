---
sidebar_label: authorized_executor
title: integration.execution.authorized_executor
---

## AuthorizedExecutor Objects

```python
class AuthorizedExecutor(abc.ABC)
```

Class to execute arbitrary functions that require an authorization token. It also supports multiple attempts to execute the function.

#### \_\_init\_\_

```python
def __init__(comp: BackendComponent,
             svc: Service,
             *,
             auth_channel: Channel,
             auth_id: str,
             user_token: UserToken,
             max_attempts: int = 1,
             attempts_delay: float = 3.0)
```

**Arguments**:

- `comp` - The global component.
- `svc` - The service used for message sending.
- `auth_channel` - Channel to fetch authorization tokens from.
- `auth_id` - The ID of the authorization token to fetch.
- `user_token` - The user token.
- `max_attempts` - The number of attempts for each operation; cannot be less than 1.
- `attempts_delay` - The delay (in seconds) between each attempt.


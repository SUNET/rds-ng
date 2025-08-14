---
sidebar_label: user_token
title: data.entities.user.user_token
---

## UserToken Objects

```python
@dataclass_json

@dataclass(kw_only=True)
class UserToken()
```

A token identifying the currently authenticated user.

**Attributes**:

- `user_id` - The user identifier.
- `user_name` - The user display name.
- `system_id` - The user&#x27;s internal system ID.
- `access_id` - A well-formatted ID to access user resources.


---
sidebar_label: user
title: data.entities.user.user
---

## User Objects

```python
@dataclass_json

@dataclass(kw_only=True)
class User()
```

A user account.

**Attributes**:

- `user_id` - The user ID.
- `name` - The (display) name of the user.
- `user_settings` - The settings of the user.

## Settings Objects

```python
@dataclass_json

@dataclass
class Settings()
```

User settings (i.e., the settings a user configures in the UI) data.

**Attributes**:

- `connector_instances` - A list of all configured connector instances.


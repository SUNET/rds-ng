---
sidebar_label: connector_instance
title: data.entities.connector.connector_instance
---

## ConnectorInstance Objects

```python
@dataclass_json

@dataclass(kw_only=True)
class ConnectorInstance()
```

A configured connector instance (i.e., a connector the user has added to his configuration).

**Attributes**:

- `instance_id` - The ID of the connector instance.
- `connector_id` - The assigned connector.
- `name` - The name of this connector instance.
- `description` - The instance description.


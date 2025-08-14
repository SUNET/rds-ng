---
sidebar_label: project_job
title: data.entities.project.project_job
---

## ProjectJob Objects

```python
@dataclass_json

@dataclass(kw_only=True)
class ProjectJob()
```

A project job that is currently active.

**Attributes**:

- `user_id` - The ID of the user the job belongs to.
- `project_id` - The project ID.
- `connector_instance` - The connector instance ID.
- `timestamp` - The starting time.
- `progress` - The total progress (0.0 - 1.0).
- `message` - The current activity message.


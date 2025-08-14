---
sidebar_label: project_job_history_utils
title: data.entities.project.logbook.project_job_history_utils
---

#### get\_most\_recent\_job\_history\_record

```python
def get_most_recent_job_history_record(
    project: "Project",
    record_filter: JobHistoryRecordFilter | None = None
) -> ProjectJobHistoryRecord | None
```

Gets the most recent job history entry of a project.

**Arguments**:

- `project` - The project.
- `record_filter` - An optional record filter.
  

**Returns**:

  The most recent entry or **None** if none exists.

#### get\_most\_recent\_job\_history\_record\_by\_connector\_instance

```python
def get_most_recent_job_history_record_by_connector_instance(
        project: "Project",
        connector_instance: ConnectorInstanceID,
        *,
        succeeded_only: bool = False) -> ProjectJobHistoryRecord | None
```

Gets the most recent job history entry of a project for a specific connector instnace.

**Arguments**:

- `project` - The project.
- `connector_instance` - The connector instance ID.
- `succeeded_only` - Whether to include only success entries.
  

**Returns**:

  The most recent entry or **None** if none exists.


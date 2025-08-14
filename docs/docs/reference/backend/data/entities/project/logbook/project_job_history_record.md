---
sidebar_label: project_job_history_record
title: data.entities.project.logbook.project_job_history_record
---

## ProjectJobHistoryRecordExtDataIDs Objects

```python
class ProjectJobHistoryRecordExtDataIDs(enum.StrEnum)
```

Well-known IDs of extended data entries.

## ProjectJobHistoryRecord Objects

```python
@dataclass_json

@dataclass
class ProjectJobHistoryRecord(ProjectLogbookRecord)
```

A single record of a project&#x27;s job history.

**Attributes**:

- `connector_instance` - The connector instance ID.
- `success` - The success status (done or failed).
- `message` - An optional message (usually in case of an error).
- `ext_data` - Arbitrary extended data as a key-value dictionary.


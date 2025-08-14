---
sidebar_label: project_logbook_record
title: data.entities.project.logbook.project_logbook_record
---

## ProjectLogbookRecord Objects

```python
@dataclass_json

@dataclass
class ProjectLogbookRecord(abc.ABC)
```

Base class for all project logbook records.

**Attributes**:

- `record` - The record entry ID.
- `timestamp` - The timestamp of the record.
- `seen` - Whether the record has been seen by the user.


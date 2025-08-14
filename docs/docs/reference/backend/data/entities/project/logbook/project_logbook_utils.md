---
sidebar_label: project_logbook_utils
title: data.entities.project.logbook.project_logbook_utils
---

#### find\_logbook\_by\_type

```python
def find_logbook_by_type(
        project: "Project",
        logbook_type: ProjectLogbookType) -> typing.List[ProjectLogbookRecord]
```

Gets the logbook with the specified type of a project.

**Arguments**:

- `project` - The project.
- `logbook_type` - The logbook type.
  

**Returns**:

  The project logbook (contents); if the logbook doesn&#x27;t exist, an empty list is returned.

#### find\_logbook\_record\_by\_id

```python
def find_logbook_record_by_id(records: typing.List[ProjectLogbookRecord],
                              record: RecordID) -> ProjectLogbookRecord | None
```

Searches for a project logbook record by its record ID within a list of records.

**Arguments**:

- `records` - The list of records.
- `record` - The record to search for.
  

**Returns**:

  The found record or **None** otherwise.

#### get\_next\_record\_id

```python
def get_next_record_id(records: typing.List[ProjectLogbookRecord]) -> RecordID
```

Retrieves the next record ID of the project logbook.

**Arguments**:

- `records` - The existing records.
  

**Returns**:

  The next ID, starting at 1.

#### append\_logbook\_record

```python
def append_logbook_record(records: typing.List[ProjectLogbookRecord],
                          record: ProjectLogbookRecord) -> None
```

Appends an entry to a project logbook, automatically assigning the next record ID.

**Arguments**:

- `records` - The list of records.
- `record` - The record to append.


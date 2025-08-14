---
sidebar_label: project
title: data.entities.project.project
---

## Project Objects

```python
@dataclass_json

@dataclass(kw_only=True)
class Project()
```

Data for a single **Project**.

**Attributes**:

- `project_id` - The unique project identifier.
- `user_id` - The ID of the user this project belongs to.
- `creation_time` - A UNIX timestamp of the project creation time.
- `resources_path` - The resources path of the project.
- `title` - The title of the project.
- `description` - An optional project description.
- `status` - The project status.
- `features` - All project features.
- `options` - All project options.
- `logbook` - The project&#x27;s logbook.

## Status Objects

```python
class Status(IntEnum)
```

The status of a project.

## Features Objects

```python
@dataclass_json

@dataclass(kw_only=True)
class Features()
```

Data for all **Project** features.

**Attributes**:

- `project_metadata` - The project metadata feature.
- `resources_metadata` - The resources metadata feature.
- `dmp` - The data management plan feature.
- `shared_objects` - Project-wide shared metadata objects.

## Options Objects

```python
@dataclass_json

@dataclass
class Options()
```

Class holding all options of a **Project**.

**Attributes**:

- `optional_features` - A list of all user-enabled optional features.
- `use_all_connector_instances` - Whether all available connector instances should be used.
- `active_connector_instances` - List of connector instances to use for the project (if *use_all_connector_instances* is false).
- `ui` - Arbitrary UI options.

## Logbook Objects

```python
@dataclass_json

@dataclass(kw_only=True)
class Logbook()
```

Class holding all logbook records of a project.

**Attributes**:

- `job_history` - All job history records.


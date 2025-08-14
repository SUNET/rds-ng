---
sidebar_label: project_external_state
title: data.entities.project.project_external_state
---

## ProjectExternalState Objects

```python
@dataclass_json

@dataclass(kw_only=True)
class ProjectExternalState()
```

A project&#x27;s external state.

**Attributes**:

- `external_state` - The state on the external service.
- `external_id` - The project ID within the external service.

## State Objects

```python
class State(StrEnum)
```

The external state of a project.

#### get\_last\_known\_external\_project\_state

```python
def get_last_known_external_project_state(
        project: Project,
        connector_instance: ConnectorInstanceID) -> ProjectExternalState
```

Retrieves the last known external state of a project consisting of its base upload state and external ID.

**Arguments**:

- `project` - The project.
- `connector_instance` - The connector instance ID.
  

**Returns**:

  The external state of the project.

#### check\_reuse\_external\_project

```python
def check_reuse_external_project(external_state: ProjectExternalState) -> bool
```

Checks whether an external project should be reused when uploading.

**Arguments**:

- `external_state` - The external project state.


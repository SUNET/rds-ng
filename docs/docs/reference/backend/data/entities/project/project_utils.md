---
sidebar_label: project_utils
title: data.entities.project.project_utils
---

#### find\_project\_by\_id

```python
def find_project_by_id(projects: typing.List[Project],
                       project_id: ProjectID) -> Project | None
```

Searches for a project by its ID within a list of projects.

**Arguments**:

- `projects` - The list of projects.
- `project_id` - The project to search for.
  

**Returns**:

  The found project or **None** otherwise.

#### apply\_project\_features\_update

```python
def apply_project_features_update(
        project: Project,
        updated_features: Project.Features,
        apply_to: typing.List[ProjectFeatureID] | None = None,
        *,
        shared_objects: MetadataObjects | None = None) -> None
```

Applies updates to project features.

**Arguments**:

- `project` - The project to apply the updates to.
- `updated_features` - The feature updates.
- `apply_to` - The features to update.
- `shared_objects` - Optionally updated project-wide shared objects.


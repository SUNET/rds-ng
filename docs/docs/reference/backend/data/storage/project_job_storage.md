---
sidebar_label: project_job_storage
title: data.storage.project_job_storage
---

## ProjectJobStorage Objects

```python
class ProjectJobStorage(Storage[ProjectJob, ProjectJobID], abc.ABC)
```

Storage for project jobs.

#### filter\_by\_user

```python
@abc.abstractmethod
def filter_by_user(user_id: UserID) -> typing.List[ProjectJob]
```

Returns all jobs belonging to the specified user.

**Arguments**:

- `user_id` - The user ID.
  

**Returns**:

  The matching project jobs list.

#### filter\_by\_project

```python
@abc.abstractmethod
def filter_by_project(project_id: ProjectID) -> typing.List[ProjectJob]
```

Returns all jobs belonging to the specified project.

**Arguments**:

- `project_id` - The project ID.
  

**Returns**:

  The matching project jobs list.


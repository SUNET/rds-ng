---
sidebar_label: project_storage
title: data.storage.project_storage
---

## ProjectStorage Objects

```python
class ProjectStorage(Storage[Project, ProjectID], abc.ABC)
```

Storage for projects.

#### filter\_by\_user

```python
@abc.abstractmethod
def filter_by_user(user_id: UserID) -> typing.List[Project]
```

Returns projects associated with the specified user.

**Arguments**:

- `user_id` - The user ID.
  

**Returns**:

  The matching projects list.


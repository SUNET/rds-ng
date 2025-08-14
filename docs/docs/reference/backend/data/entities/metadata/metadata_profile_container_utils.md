---
sidebar_label: metadata_profile_container_utils
title: data.entities.metadata.metadata_profile_container_utils
---

#### filter\_containers\_by\_category

```python
def filter_containers_by_category(
        containers: MetadataProfileContainerList,
        category: str) -> MetadataProfileContainerList
```

Gets all containers from a list matching the specified category.

**Arguments**:

- `containers` - The list of containers.
- `category` - The category to match.
  

**Returns**:

  List of all matching containers.

#### filter\_containers\_by\_roles

```python
def filter_containers_by_roles(
    containers: MetadataProfileContainerList,
    roles: typing.List[MetadataProfileContainer.Role]
) -> MetadataProfileContainerList
```

Gets all containers from a list matching the specified role.

**Arguments**:

- `containers` - The list of containers.
- `roles` - The roles to match.
  

**Returns**:

  List of all matching containers.

#### filter\_containers

```python
def filter_containers(
    containers: MetadataProfileContainerList, *, category: str,
    roles: typing.List[MetadataProfileContainer.Role]
) -> MetadataProfileContainerList
```

Gets all containers from a list matching the specified category and role.

**Arguments**:

- `containers` - The list of containers.
- `category` - The category to match.
- `roles` - The roles to match.
  

**Returns**:

  List of all matching containers.

#### containers\_from\_folder

```python
def containers_from_folder(
        folder: pathlib.PosixPath,
        *,
        default_category: str | None = None) -> MetadataProfileContainerList
```

Loads all profiles from the specified folder. The files are separated into distinct folders that
represent the various profile categories. Within each category folder, subfolders represent the
profile roles, and each role folder can hold an arbitrary number of profiles.

**Arguments**:

- `folder` - The folder to load.
- `default_category` - A default category for all profiles, skipping category directory parsing.
  

**Returns**:

  A list of all loaded profiles.


---
sidebar_label: resource_utils
title: data.entities.resource.resource_utils
---

#### resources\_list\_from\_syspath

```python
def resources_list_from_syspath(path: str,
                                *,
                                include_folders: bool = True,
                                include_files: bool = True,
                                recursive: bool = True) -> ResourcesList
```

Generates a *ResourcesList* from a system path.

**Arguments**:

- `path` - The root path.
- `include_folders` - Whether to list folders (if this is set to false, no recursion will occur independent of `recursive`).
- `include_files` - Whether to list files.
- `recursive` - Whether to recursively process all sub-folders as well.
  

**Returns**:

  A *ResourcesList* containing all contained files and folders.

#### search\_resources\_list

```python
def search_resources_list(resources: ResourcesList,
                          path: str) -> ResourcesList
```

Searches for a folder path within a resources list.

**Arguments**:

- `resources` - The resources list to search.
- `path` - The path to search for.
  

**Returns**:

  The found (nested) resources list, if any.
  

**Raises**:

- `ValueError` - If the path could not be found.

#### filter\_resources\_list

```python
def filter_resources_list(resources: ResourcesList,
                          *,
                          include_folders: bool = True,
                          include_files: bool = True) -> ResourcesList
```

Filters a resource list.

**Arguments**:

- `resources` - The list to filter.
- `include_folders` - Whether to include folders.
- `include_files` - Whether to include files.
  

**Returns**:

  The filtered list.

#### files\_list\_from\_resources\_list

```python
def files_list_from_resources_list(
        resources: ResourcesList) -> typing.List[Resource]
```

Converts a resources list into a flat list of all included files.

**Arguments**:

- `resources` - The resources list.
  

**Returns**:

  The flattened files list.


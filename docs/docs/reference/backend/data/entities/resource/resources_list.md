---
sidebar_label: resources_list
title: data.entities.resource.resources_list
---

## ResourcesList Objects

```python
@dataclass_json

@dataclass(kw_only=True)
class ResourcesList()
```

A recursive list of resources.

**Notes**:

  Resources are always given in absolute form.
  

**Attributes**:

- `resource` - The current resource path.
- `folders` - A list of all folders.
- `files` - A list of all files.


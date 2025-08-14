---
sidebar_label: resource
title: data.entities.resource.resource
---

## Resource Objects

```python
@dataclass_json

@dataclass(kw_only=True)
class Resource()
```

A single file or folder resource.

**Attributes**:

- `filename` - The complete name (path) of the resource.
- `basename` - The name (w/o path) of the resource.
- `type` - The type of the resource (folder or file).
- `size` - The size of the resource; for folders, this is the size of all its contents.
- `mime_type` - The MIME type of the resource.

## Type Objects

```python
class Type(StrEnum)
```

The resource type.


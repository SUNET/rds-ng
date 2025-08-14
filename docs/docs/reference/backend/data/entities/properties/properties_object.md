---
sidebar_label: properties_object
title: data.entities.properties.properties_object
---

## PropertyObject Objects

```python
@dataclass
class PropertyObject(DataClassJsonMixin)
```

A project object.

**Attributes**:

- `id` - The ID of the object.
- `value` - The values of the object.
- `refs` - The references that the object holds to other objects, by their id.


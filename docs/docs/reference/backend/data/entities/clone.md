---
sidebar_label: clone
title: data.entities.clone
---

#### EntityType

pylint: disable=invalid-name

#### clone\_entity

```python
def clone_entity(entity: typing.Generic[EntityType], **changes) -> EntityType
```

Creates a copy (clone) of the given entity, applying optional field changes.

**Arguments**:

- `entity` - The entity to clone.
- `**changes` - Any field changes to apply.
  

**Returns**:

  The cloned entity.


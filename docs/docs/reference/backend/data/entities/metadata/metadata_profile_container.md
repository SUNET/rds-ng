---
sidebar_label: metadata_profile_container
title: data.entities.metadata.metadata_profile_container
---

## MetadataProfileContainer Objects

```python
@dataclass_json

@dataclass(kw_only=True)
class MetadataProfileContainer()
```

A container that holds a metadata profile along with various descriptive information.

**Attributes**:

- `category` - The overall category of the profile.
- `role` - The role of the profile within its category.
- `profile` - The actual profile data.

## Role Objects

```python
class Role(StrEnum)
```

The role of a profile.

**Attributes**:

- `DEFAULT` - A default (fixed) profile that will always be used.
- `OPTIONAL` - An optional profile.


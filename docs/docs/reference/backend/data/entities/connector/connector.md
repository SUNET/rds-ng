---
sidebar_label: connector
title: data.entities.connector.connector
---

## Connector Objects

```python
@dataclass_json

@dataclass(kw_only=True)
class Connector()
```

Data for a single **Connector**.

**Attributes**:

- `connector_id` - The unique connector identifier.
- `connector_address` - The target address of the connector.
- `name` - The name of the connector.
- `description` - An optional connector description.
- `category` - The connector category.
- `authorization` - Authorization settings for the connector.
- `options` - The connector options.
- `logos` - Image data of the connector logos.
- `metadata_profiles` - The profiles for connector-specific data.
- `announce_timestamp` - The timestamp when the connector was last announced.

## Options Objects

```python
class Options(IntFlag)
```

Options of a connector.

**Attributes**:

- `UPLOAD_ONCE` - If set, the project may only be uploaded once.

## Logos Objects

```python
@dataclass_json

@dataclass
class Logos()
```

Base64-encoded image data of the connector logos.

**Attributes**:

- `default_logo` - The default logo.
- `horizontal_logo` - A logo with small height used specifically for horizontal display.


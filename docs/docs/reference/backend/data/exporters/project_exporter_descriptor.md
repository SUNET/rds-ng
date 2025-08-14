---
sidebar_label: project_exporter_descriptor
title: data.exporters.project_exporter_descriptor
---

## ProjectExporterDescriptor Objects

```python
@dataclass_json

@dataclass(frozen=True, kw_only=True)
class ProjectExporterDescriptor()
```

Describes a project exporter. This class is used to easily transfer information about an exporter.

**Attributes**:

- `exporter_id` - The global exporter ID.
- `name` - The display name.
- `description` - The exporter&#x27;s description.
- `extension` - The extension of exported files.
- `scope` - The scope where the exporter applies; if empty, it applies to the overall project.
- `capabilities` - Extended exporter capabilities.
- `default_scope` - A default scope when exporting if none is given.
- `default_filename` - A default filename used when none is given.

## Capabilities Objects

```python
class Capabilities(IntFlag)
```

Flags specifying extended capabilities of the exporter.


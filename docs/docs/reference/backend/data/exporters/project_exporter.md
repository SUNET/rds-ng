---
sidebar_label: project_exporter
title: data.exporters.project_exporter
---

## ProjectExporter Objects

```python
class ProjectExporter(abc.ABC)
```

Base class for project exporters.

#### \_\_init\_\_

```python
def __init__(exporter_id: ProjectExporterID,
             *,
             name: str,
             description: str,
             extension: str,
             scope: ProjectExporterScope,
             capabilities: ProjectExporterDescriptor.
             Capabilities = ProjectExporterDescriptor.Capabilities.NONE,
             default_scope: ProjectFeatureID | None = None,
             default_filename: str = "")
```

**Arguments**:

- `exporter_id` - The unique ID of the exporter.
- `name` - The name.
- `description` - The description.
- `extension` - The extension of exported files.
- `scope` - The scope the exporter applies to.
- `default_scope` - A default scope when exporting if none is given.
- `default_filename` - A default filename used when none is given.

#### descriptor

```python
@property
def descriptor() -> ProjectExporterDescriptor
```

The exporter descriptor.

#### exporter\_id

```python
@property
def exporter_id() -> ProjectExporterID
```

The ID of the exporter.

#### name

```python
@property
def name() -> str
```

The exporter name.

#### description

```python
@property
def description() -> str
```

The exporter description.

#### extension

```python
@property
def extension() -> str
```

The extension of exported files.

#### scope

```python
@property
def scope() -> ProjectExporterScope
```

The exporter&#x27;s scope.

#### capabilities

```python
@property
def capabilities() -> ProjectExporterDescriptor.Capabilities
```

The exporter&#x27;s capabilities.

#### default\_scope

```python
@property
def default_scope() -> ProjectFeatureID | None
```

The default scope when exporting if none is given.

#### default\_filename

```python
@property
def default_filename() -> str
```

The default filename used when none is given.


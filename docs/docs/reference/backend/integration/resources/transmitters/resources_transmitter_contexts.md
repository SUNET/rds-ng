---
sidebar_label: resources_transmitter_contexts
title: integration.resources.transmitters.resources_transmitter_contexts
---

## ResourcesTransmitterContext Objects

```python
@dataclass(kw_only=True)
class ResourcesTransmitterContext()
```

Internal data stored by the `ResourcesTransmitter`.

**Attributes**:

- `prepared` - Whether the context has been prepared.
- `resources` - List of all available resources.
- `download_list` - List of all resources to download.
- `download_index` - The currently active download as its index in `download_list`.

#### all\_downloads\_done

```python
@property
def all_downloads_done() -> bool
```

Checks if the entire list of downloads has been processed.

## ResourcesTransmitterDownloadContext Objects

```python
@dataclass(kw_only=True)
class ResourcesTransmitterDownloadContext()
```

Internal data stored by the `ResourcesTransmitter` for a single download.

**Attributes**:

- `resource` - The resource being downloaded.
- `tunnel` - The tunnel used to download the resource.


---
sidebar_label: webdav_types
title: integration.resources.brokers.webdav.webdav_types
---

## WebdavResource Objects

```python
@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclass(frozen=True, kw_only=True)
class WebdavResource()
```

A resource information object as returned by WebDAV.

#### size

Only filled for files

#### content\_type

Might not be provided by the underlying system


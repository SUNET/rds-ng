---
sidebar_label: webdav_utils
title: integration.resources.brokers.webdav.webdav_utils
---

#### parse\_webdav\_resource

```python
def parse_webdav_resource(resource: typing.Dict[str, typing.Any],
                          webdav_endpoint: str) -> WebdavResource | None
```

Transforms a WebDAV resource into a well-formatted object.

**Arguments**:

- `resource` - The WebDAV resource.
- `webdav_endpoint` - The endpoint that was used for resource retrieval (will be omitted from the result path).
  

**Returns**:

  A well-formatted resource object.


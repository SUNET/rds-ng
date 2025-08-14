---
sidebar_label: resources_broker_tunnel
title: integration.resources.brokers.resources_broker_tunnel
---

## ResourcesBrokerTunnel Objects

```python
class ResourcesBrokerTunnel(io.RawIOBase, metaclass=abc.ABCMeta)
```

Class used to &quot;tunnel&quot; the data when up-/downloading files through a broker.

Tunnels are file-like objects and need to be used as context managers (i.e., using *with*).

#### on

```python
def on(event: CallbackTypes, cb: CallbackType) -> typing.Self
```

Registers a new callback for they specified event.

**Arguments**:

- `event` - The event to react to.
- `cb` - The callback.


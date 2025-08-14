---
sidebar_label: client_service_context
title: services.client_service_context
---

## ClientServiceContext Objects

```python
class ClientServiceContext(ServiceContext)
```

A service context tailored towards working with a client connection.

#### set\_remote\_channel

```python
@staticmethod
def set_remote_channel(channel: Channel | None) -> None
```

Sets (or resets) the remote channel.

**Arguments**:

- `channel` - The remote or channel, or *None*.

#### remote\_channel

```python
@property
def remote_channel() -> Channel
```

The remote channel.

**Raises**:

- `RuntimeError` - If no connection exists.

#### is\_connected

```python
@property
def is_connected() -> bool
```

Whether the client is connected.


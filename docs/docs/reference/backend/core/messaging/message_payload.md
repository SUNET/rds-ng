---
sidebar_label: message_payload
title: core.messaging.message_payload
---

## MessagePayload Objects

```python
class MessagePayload()
```

Class holding arbitrary payload data (as key-value pairs) of a message.

#### set

```python
def set(key: str, data: PayloadData) -> None
```

Sets a payload item.

**Arguments**:

- `key` - The key of the item.
- `data` - The item data.

#### get

```python
def get(key: str) -> PayloadData | None
```

Retrieves a payload item.

**Arguments**:

- `key` - The key of the item.
  

**Returns**:

  The item data or *None* otherwise.

#### contains

```python
def contains(key: str) -> bool
```

Checks if an item exists.

**Arguments**:

- `key` - The key of the item.

#### clear

```python
def clear(key: str | None = None) -> None
```

Removes an item or clears the entire payload.

**Arguments**:

- `key` - The key of the item; if set to *None*, all items will be removed.

#### encode

```python
def encode() -> Payload
```

Encodes the payload for message passing.

**Returns**:

  The encoded data.

#### decode

```python
def decode(payload: Payload) -> None
```

Decodes the payload from message passing.

**Arguments**:

- `payload` - The incoming payload.


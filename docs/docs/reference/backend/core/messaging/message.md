---
sidebar_label: message
title: core.messaging.message
---

## Message Objects

```python
@dataclass_json

@dataclass(frozen=True, kw_only=True)
class Message(abc.ABC)
```

Base class for all messages.

A message, besides its actual data, consists mainly of information from where it came and where it should go.

This class also offers a useful decorator to easily declare new messages, like in the following example::

@Message.define(&quot;msg/command&quot;)
class MyCommand(Command):
some_number: int = 0

**Attributes**:

- `name` - The name of the message.
- `origin` - The initial source component of the message.
- `sender` - The component from where the message came from.
- `target` - Where the message should go to.
- `hops` - A list of components the message was sent through.
- `trace` - A unique trace identifying messages that logically belong together.
- `api_key` - An optional API key to access protected resources.

#### message\_name

```python
@staticmethod
def message_name() -> MessageName
```

Retrieves the name of the message type on a message class basis.

#### is\_protected

```python
@staticmethod
def is_protected() -> bool
```

Whether this message is protected and thus requires an API key.

#### define

```python
@staticmethod
def define(name: str, is_protected: bool = False)
```

Defines a new message.

The decorator takes care of wrapping the new class as a dataclass, passing the correct message
name to its constructor. It also registers the new message type in the global ``MessageTypesCatalog``.

Examples::

@Message.define(&quot;msg/command&quot;)
class MyCommand(Command):
some_number: int = 0

**Arguments**:

- `name` - The name of the message.
- `is_protected` - Whether the message requires an API key.

#### payload

```python
@property
def payload() -> MessagePayload
```

The message payload.


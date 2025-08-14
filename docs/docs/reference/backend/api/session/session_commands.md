---
sidebar_label: session_commands
title: api.session.session_commands
---

## GetSessionValueCommand Objects

```python
@Message.define("command/session/value/get")
class GetSessionValueCommand(Command)
```

Command to get a session value stored on the server.

**Arguments**:

- `key` - The value key.
  

**Notes**:

  Requires a ``GetSessionValueReply`` reply.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          *,
          key: str,
          chain: Message | None = None) -> CommandComposer
```

Helper function to easily build this message.

## GetSessionValueReply Objects

```python
@Message.define("command/session/value/get/reply")
class GetSessionValueReply(CommandReply)
```

Reply to ``GetSessionValueCommand``.

**Arguments**:

- `value` - The value or *None* if no such value was found.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          cmd: GetSessionValueCommand,
          *,
          value: typing.Any,
          success: bool = True,
          message: str = "") -> CommandReplyComposer
```

Helper function to easily build this message.

## SetSessionValueCommand Objects

```python
@Message.define("command/session/value/set")
class SetSessionValueCommand(Command)
```

Command to store a session value on the server.

**Arguments**:

- `key` - The value key.
- `value` - The value to store.
  

**Notes**:

  Requires a ``SetSessionValueReply`` reply.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          *,
          key: str,
          value: typing.Any,
          chain: Message | None = None) -> CommandComposer
```

Helper function to easily build this message.

## SetSessionValueReply Objects

```python
@Message.define("command/session/value/set/reply")
class SetSessionValueReply(CommandReply)
```

Reply to ``SetSessionValueCommand``.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          cmd: SetSessionValueCommand,
          *,
          success: bool = True,
          message: str = "") -> CommandReplyComposer
```

Helper function to easily build this message.


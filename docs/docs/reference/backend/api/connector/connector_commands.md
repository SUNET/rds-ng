---
sidebar_label: connector_commands
title: api.connector.connector_commands
---

## ListConnectorsCommand Objects

```python
@Message.define("command/connector/list")
class ListConnectorsCommand(Command)
```

Command to fetch all available connectors.

**Notes**:

  Requires a ``ListConnectorsReply`` reply.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          *,
          chain: Message | None = None) -> CommandComposer
```

Helper function to easily build this message.

## ListConnectorsReply Objects

```python
@Message.define("command/connector/list/reply")
class ListConnectorsReply(CommandReply)
```

Reply to ``ListConnectorsCommand``.

**Arguments**:

- `connectors` - List of all connectors.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          cmd: ListConnectorsCommand,
          *,
          connectors: typing.List[Connector],
          success: bool = True,
          message: str = "") -> CommandReplyComposer
```

Helper function to easily build this message.


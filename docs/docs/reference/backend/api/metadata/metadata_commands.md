---
sidebar_label: metadata_commands
title: api.metadata.metadata_commands
---

## GetMetadataProfilesCommand Objects

```python
@Message.define("command/metadata/profiles")
class GetMetadataProfilesCommand(Command)
```

Command to fetch all global metadata profiles.

**Notes**:

  Requires a ``GetMetadataProfilesReply`` reply.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          *,
          chain: Message | None = None) -> CommandComposer
```

Helper function to easily build this message.

## GetMetadataProfilesReply Objects

```python
@Message.define("command/metadata/profiles/reply")
class GetMetadataProfilesReply(CommandReply)
```

Reply to ``GetMetadataProfilesCommand``.

**Arguments**:

- `profiles` - List of all global profiles.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          cmd: GetMetadataProfilesCommand,
          *,
          profiles: MetadataProfileContainerList,
          success: bool = True,
          message: str = "") -> CommandReplyComposer
```

Helper function to easily build this message.


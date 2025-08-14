---
sidebar_label: resource_commands
title: api.resource.resource_commands
---

## AssignResourcesBrokerCommand Objects

```python
@Message.define("command/resource/assign-broker")
class AssignResourcesBrokerCommand(Command)
```

Command to assign a broker to access the user&#x27;s resources.

**Notes**:

  Requires a ``AssignResourcesBrokerReply`` reply.
  

**Arguments**:

- `broker` - The broker to use.
- `config` - The broker configuration.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          *,
          broker: str,
          config: typing.Dict[str, typing.Any],
          chain: Message | None = None) -> CommandComposer
```

Helper function to easily build this message.

## AssignResourcesBrokerReply Objects

```python
@Message.define("command/resource/assign-broker/reply")
class AssignResourcesBrokerReply(CommandReply)
```

Reply to ``AssignResourcesBrokerCommand``.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          cmd: AssignResourcesBrokerCommand,
          *,
          success: bool = True,
          message: str = "") -> CommandReplyComposer
```

Helper function to easily build this message.

## ListResourcesCommand Objects

```python
@Message.define("command/resource/list")
class ListResourcesCommand(Command)
```

Command to fetch all available resources.

**Notes**:

  Requires a ``ListResourcesReply`` reply.
  

**Arguments**:

- `root` - The root path (or empty if the system root should be used).
- `include_folders` - Whether to list folders (if this is set to false, no recursion will occur independent of `recursive`).
- `include_files` - Whether to list files.
- `recursive` - Whether to recursively process all sub-folders as well.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          *,
          root: str = "",
          include_folders: bool = True,
          include_files: bool = True,
          recursive: bool = True,
          chain: Message | None = None) -> CommandComposer
```

Helper function to easily build this message.

## ListResourcesReply Objects

```python
@Message.define("command/resource/list/reply")
class ListResourcesReply(CommandReply)
```

Reply to ``ListResourcesCommand``.

**Arguments**:

- `resources` - List of all resources.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          cmd: ListResourcesCommand,
          *,
          resources: ResourcesList,
          success: bool = True,
          message: str = "") -> CommandReplyComposer
```

Helper function to easily build this message.

## GetResourceCommand Objects

```python
@Message.define("command/resource/get")
class GetResourceCommand(Command)
```

Command to fetch a single resource.

**Notes**:

  Requires a ``GetResourceReply`` reply.
  

**Arguments**:

- `resource` - The resource.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          *,
          resource: Resource,
          chain: Message | None = None) -> CommandComposer
```

Helper function to easily build this message.

## GetResourceReply Objects

```python
@Message.define("command/resource/get/reply")
class GetResourceReply(CommandReply)
```

Reply to ``GetResourceCommand``.

**Arguments**:

- `resource` - The resource path.

#### data

```python
@property
def data() -> bytes | None
```

The data of the resource.

**Returns**:

  The binary data of the resource.

#### data

```python
@data.setter
def data(data: bytes) -> None
```

Sets the data of the resource.

**Arguments**:

- `data` - The resource data.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          cmd: GetResourceCommand,
          *,
          resource: Resource,
          data: bytes,
          success: bool = True,
          message: str = "") -> CommandReplyComposer
```

Helper function to easily build this message.


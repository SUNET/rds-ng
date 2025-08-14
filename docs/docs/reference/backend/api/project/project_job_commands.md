---
sidebar_label: project_job_commands
title: api.project.project_job_commands
---

## ListProjectJobsCommand Objects

```python
@Message.define("command/project-job/list")
class ListProjectJobsCommand(Command)
```

Command to fetch all project jobs of the current user.

**Notes**:

  Requires a ``ListProjectJobsReply`` reply.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          *,
          chain: Message | None = None) -> CommandComposer
```

Helper function to easily build this message.

## ListProjectJobsReply Objects

```python
@Message.define("command/project-job/list/reply")
class ListProjectJobsReply(CommandReply)
```

Reply to ``ListJobsCommand``.

**Arguments**:

- `jobs` - List of all project jobs.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          cmd: ListProjectJobsCommand,
          *,
          jobs: typing.List[ProjectJob],
          success: bool = True,
          message: str = "") -> CommandReplyComposer
```

Helper function to easily build this message.

## InitiateProjectJobCommand Objects

```python
@Message.define("command/project-job/initiate")
class InitiateProjectJobCommand(Command)
```

Command to initiate a project job.

**Arguments**:

- `project_id` - The project ID.
- `connector_instance` - The connector instance ID.
- `auto_exports` - List of enabled exporters for automatic file generation.
  

**Notes**:

  Requires a ``InitiateJobReply`` reply.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          *,
          project_id: ProjectID,
          connector_instance: ConnectorInstanceID,
          auto_exports: typing.List[ProjectExporterID] | None = None,
          chain: Message | None = None) -> CommandComposer
```

Helper function to easily build this message.

## InitiateProjectJobReply Objects

```python
@Message.define("command/project-job/initiate/reply")
class InitiateProjectJobReply(CommandReply)
```

Reply to ``InitiateProjectJobCommand``.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          cmd: InitiateProjectJobCommand,
          *,
          success: bool = True,
          message: str = "") -> CommandReplyComposer
```

Helper function to easily build this message.

## StartProjectJobCommand Objects

```python
@Message.define("command/project-job/start")
class StartProjectJobCommand(Command)
```

Command to start a project job in the target connector.

**Arguments**:

- `project` - The project to upload.
- `connector_instance` - The connector instance ID.
- `user_token` - The user token.
- `broker_token` - Token to create the resources broker.
  

**Notes**:

  Requires a ``StartProjectJobReply`` reply.

#### additional\_files

```python
@property
def additional_files() -> typing.Dict[str, bytes]
```

Any additional (auto-generated) files to be uploaded.

**Returns**:

  A dictionary mapping file names to their data.

#### additional\_files

```python
@additional_files.setter
def additional_files(files: typing.Dict[str, bytes]) -> None
```

Sets additional files to upload alongside the project files.

**Arguments**:

- `files` - A filename-&gt;data map containing the additional files.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          *,
          project: Project,
          connector_instance: ConnectorInstanceID,
          user_token: UserToken,
          broker_token: ResourcesBrokerToken,
          additional_files: typing.Dict[str, bytes] | None = None,
          chain: Message | None = None) -> CommandComposer
```

Helper function to easily build this message.

## StartProjectJobReply Objects

```python
@Message.define("command/project-job/start/reply")
class StartProjectJobReply(CommandReply)
```

Reply to ``StartProjectJobCommand``.

**Arguments**:

- `project_id` - The project ID.
- `connector_instance` - The connector instance ID.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          cmd: StartProjectJobCommand,
          *,
          project_id: ProjectID,
          connector_instance: ConnectorInstanceID,
          success: bool = True,
          message: str = "") -> CommandReplyComposer
```

Helper function to easily build this message.


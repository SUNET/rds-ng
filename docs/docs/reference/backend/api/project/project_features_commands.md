---
sidebar_label: project_features_commands
title: api.project.project_features_commands
---

## UpdateProjectFeaturesCommand Objects

```python
@Message.define("command/project/features/update")
class UpdateProjectFeaturesCommand(Command)
```

Command to update the features (data) of a project.

**Arguments**:

- `project_id` - The ID of the project to update.
- `updated_features` - List of all features (using their ID) to update.
- `features` - The new features data.
- `shared_objects` - Optionally updated project-wide shared objects.
  

**Notes**:

  Requires an ``UpdateProjectFeaturesReply`` reply.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          *,
          project_id: ProjectID,
          updated_features: typing.List[ProjectFeatureID],
          features: Project.Features,
          shared_objects: MetadataObjects | None = None,
          chain: Message | None = None) -> CommandComposer
```

Helper function to easily build this message.

## UpdateProjectFeaturesReply Objects

```python
@Message.define("command/project/features/update/reply")
class UpdateProjectFeaturesReply(CommandReply)
```

Reply to ``UpdateProjectFeaturesCommand``.

**Arguments**:

- `project_id` - The ID of the updated project.
- `updated_features` - List of all updated features (using their ID).

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          cmd: UpdateProjectFeaturesCommand,
          *,
          project_id: ProjectID,
          updated_features: typing.List[ProjectFeatureID],
          success: bool = True,
          message: str = "") -> CommandReplyComposer
```

Helper function to easily build this message.


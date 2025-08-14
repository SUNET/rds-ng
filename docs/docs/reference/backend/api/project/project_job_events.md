---
sidebar_label: project_job_events
title: api.project.project_job_events
---

## ProjectJobsListEvent Objects

```python
@Message.define("event/project-job/list")
class ProjectJobsListEvent(Event)
```

Emitted whenever the user&#x27;s project jobs list has been updated.

**Arguments**:

- `jobs` - List of all project jobs.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          *,
          jobs: typing.List[ProjectJob],
          chain: Message | None = None) -> EventComposer
```

Helper function to easily build this message.

## ProjectJobProgressEvent Objects

```python
@Message.define("event/project-job/progress")
class ProjectJobProgressEvent(Event)
```

Emitted to inform about the progression of a job.

**Arguments**:

- `project_id` - The project ID.
- `connector_instance` - The connector instance ID.
- `progress` - The total progress (0.0 - 1.0).
- `message` - The current activity message.

## Contents Objects

```python
class Contents(IntFlag)
```

Flags specifying which aspects of the job have been updated.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          *,
          project_id: ProjectID,
          connector_instance: ConnectorInstanceID,
          contents: Contents,
          progress: float,
          message: str,
          chain: Message | None = None) -> EventComposer
```

Helper function to easily build this message.

## ProjectJobCompletionEvent Objects

```python
@Message.define("event/project-job/completion")
class ProjectJobCompletionEvent(Event)
```

Emitted to inform about the completion (either succeeded or failed) of a job.

**Arguments**:

- `project_id` - The project ID.
- `connector_instance` - The connector instance ID.
- `success` - The success status (done or failed).
- `message` - An optional message (usually in case of an error).

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          *,
          project_id: ProjectID,
          connector_instance: ConnectorInstanceID,
          success: bool,
          message: str = "",
          ext_data: ProjectJobHistoryRecordExtData | None = None,
          chain: Message | None = None) -> EventComposer
```

Helper function to easily build this message.


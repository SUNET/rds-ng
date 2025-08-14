---
sidebar_label: project_events
title: api.project.project_events
---

## ProjectsListEvent Objects

```python
@Message.define("event/project/list")
class ProjectsListEvent(Event)
```

Emitted whenever the user&#x27;s projects list has been updated.

**Arguments**:

- `projects` - List of all projects.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          *,
          projects: typing.List[Project],
          chain: Message | None = None) -> EventComposer
```

Helper function to easily build this message.

## ProjectTouchEvent Objects

```python
@Message.define("event/project/touch")
class ProjectTouchEvent(Event)
```

Emitted whenever a project has been &quot;touched&quot; (i.e., selected/activated) by the user.

**Arguments**:

- `project_id` - The project ID.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          *,
          project_id: ProjectID,
          chain: Message | None = None) -> EventComposer
```

Helper function to easily build this message.

## ProjectLogbookEvent Objects

```python
@Message.define("event/project/logbook")
class ProjectLogbookEvent(Event)
```

Emitted whenever the project&#x27;s logbook has been updated.

**Arguments**:

- `project_id` - The project ID.
- `logbook` - The new project logbook.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          *,
          project_id: ProjectID,
          logbook: Project.Logbook,
          chain: Message | None = None) -> EventComposer
```

Helper function to easily build this message.

## ProjectExternalStateEvent Objects

```python
@Message.define("event/project/external-state")
class ProjectExternalStateEvent(Event)
```

Emitted whenever the external state of a project has been updated.

**Arguments**:

- `project_id` - The project ID.
- `user_id` - The user ID.
- `connector_instance` - The connector instance ID.
- `external_state` - The new project&#x27;s external state.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          *,
          project_id: ProjectID,
          user_id: UserID,
          connector_instance: ConnectorInstanceID,
          external_state: ProjectExternalState,
          chain: Message | None = None) -> EventComposer
```

Helper function to easily build this message.

## ProjectExternalStateRenewalEvent Objects

```python
@Message.define("event/project/external-state/renewal")
class ProjectExternalStateRenewalEvent(Event)
```

Emitted whenever the external state of a project needs to be updated.
Unlike `ProjectExternalStateEvent`, the entire project needs to be sent with this request, as more than the project ID will be needed.

**Arguments**:

- `project` - The project.
- `connector_instance` - The connector instance ID.
- `user_token` - The user token.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          *,
          project: Project,
          connector_instance: ConnectorInstanceID,
          user_token: UserToken,
          chain: Message | None = None) -> EventComposer
```

Helper function to easily build this message.


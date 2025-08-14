---
sidebar_label: connector_events
title: api.connector.connector_events
---

## ConnectorsListEvent Objects

```python
@Message.define("event/connector/list")
class ConnectorsListEvent(Event)
```

Emitted whenever the list of available connectors has been updated.

**Arguments**:

- `connectors` - List of all connectors.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          *,
          connectors: typing.List[Connector],
          chain: Message | None = None) -> EventComposer
```

Helper function to easily build this message.

## ConnectorAnnounceEvent Objects

```python
@Message.define("event/connector/announce")
class ConnectorAnnounceEvent(Event)
```

Emitted by a connector to let the server know about its existence.

#### build

```python
@staticmethod
def build(message_builder: MessageBuilder,
          *,
          connector_id: ConnectorID,
          name: str,
          description: str,
          category: ConnectorCategoryID,
          authorization_public: AuthorizationSettings,
          authorization_private: AuthorizationSettings,
          options: Connector.Options,
          logos: Connector.Logos,
          metadata_profiles: MetadataProfileContainerList,
          chain: Message | None = None) -> EventComposer
```

Helper function to easily build this message.


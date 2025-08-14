---
sidebar_label: connector_utils
title: data.entities.connector.connector_utils
---

#### find\_connector\_by\_id

```python
def find_connector_by_id(connectors: typing.List[Connector],
                         connector_id: ConnectorID) -> Connector | None
```

Searches for a connector by its ID within a list of connectors.

**Arguments**:

- `connectors` - The list of connectors.
- `connector_id` - The connector to search for.
  

**Returns**:

  The found connector or **None** otherwise.

#### apply\_connector\_update

```python
def apply_connector_update(connector: Connector,
                           updated_connector: Connector) -> None
```

Applies an update to a connector.

**Arguments**:

- `connector` - The connector to apply the update to.
- `updated_connector` - The updated connector.


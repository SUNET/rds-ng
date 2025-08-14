---
sidebar_label: connector_instance_utils
title: data.entities.connector.connector_instance_utils
---

#### find\_connector\_instance\_by\_id

```python
def find_connector_instance_by_id(
        connector_instances: typing.List[ConnectorInstance],
        instance_id: ConnectorInstanceID) -> ConnectorInstance | None
```

Searches for a connector instance by its ID within a list of connector instances.

**Arguments**:

- `connector_instances` - The list of connector instances.
- `instance_id` - The connector instance to search for.
  

**Returns**:

  The found connector instance or **None** otherwise.

#### find\_connector\_by\_instance\_id

```python
def find_connector_by_instance_id(
        connectors: typing.List[Connector],
        connector_instances: typing.List[ConnectorInstance],
        instance_id: ConnectorInstanceID) -> Connector | None
```

Retrieves the connector that is indirectly specified by a connector instance.

**Arguments**:

- `connectors` - The list of connectors.
- `connector_instances` - The list of connector instances.
- `instance_id` - The connector instance to search for.
  

**Returns**:

  The found connector or **None** otherwise.


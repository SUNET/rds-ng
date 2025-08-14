# Function: groupConnectorInstances()

> **groupConnectorInstances**(`connectorInstances`, `connectors?`): [`ConnectorInstancesGroup`](../interfaces/ConnectorInstancesGroup.md)[]

Defined in: [src/common/web/data/entities/connector/ConnectorInstanceUtils.ts:26](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/connector/ConnectorInstanceUtils.ts#L26)

Function to return all connector instances grouped by their used connectors. By default, the groups are sorted by their IDs; if a list of
connectors is given, the display name is used instead.

## Parameters

### connectorInstances

[`ConnectorInstance`](../../ConnectorInstance/classes/ConnectorInstance.md)[]

The connector instances.

### connectors?

[`Connector`](../../Connector/classes/Connector.md)[]

List of available connectors used to sort the groups by their display names.

## Returns

[`ConnectorInstancesGroup`](../interfaces/ConnectorInstancesGroup.md)[]

- The grouped connector instances.

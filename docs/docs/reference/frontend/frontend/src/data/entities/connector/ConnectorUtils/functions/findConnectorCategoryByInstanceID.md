# Function: findConnectorCategoryByInstanceID()

> **findConnectorCategoryByInstanceID**(`connectors`, `connectorInstances`, `instanceID`): `undefined` \| [`ConnectorCategory`](../../categories/ConnectorCategory/classes/ConnectorCategory.md)

Defined in: [src/frontend/src/data/entities/connector/ConnectorUtils.ts:24](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/data/entities/connector/ConnectorUtils.ts#L24)

Retrieves the category of a connector instance.

## Parameters

### connectors

[`Connector`](../../../../../../../common/web/data/entities/connector/Connector/classes/Connector.md)[]

The connectors.

### connectorInstances

[`ConnectorInstance`](../../../../../../../common/web/data/entities/connector/ConnectorInstance/classes/ConnectorInstance.md)[]

The connector instances.

### instanceID

`string`

The instance ID.

## Returns

`undefined` \| [`ConnectorCategory`](../../categories/ConnectorCategory/classes/ConnectorCategory.md)

- The connector category, if any.

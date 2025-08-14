# Function: findConnectorByInstanceID()

> **findConnectorByInstanceID**(`connectors`, `connectorInstances`, `instanceID`): `undefined` \| [`Connector`](../../Connector/classes/Connector.md)

Defined in: [src/common/web/data/entities/connector/ConnectorInstanceUtils.ts:64](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/connector/ConnectorInstanceUtils.ts#L64)

Searches for a connector using a connector instance ID.

## Parameters

### connectors

[`Connector`](../../Connector/classes/Connector.md)[]

The list of connectors.

### connectorInstances

[`ConnectorInstance`](../../ConnectorInstance/classes/ConnectorInstance.md)[]

The list of connector instances.

### instanceID

`string`

The connector instance ID.

## Returns

`undefined` \| [`Connector`](../../Connector/classes/Connector.md)

- The found connector or **undefined** otherwise.

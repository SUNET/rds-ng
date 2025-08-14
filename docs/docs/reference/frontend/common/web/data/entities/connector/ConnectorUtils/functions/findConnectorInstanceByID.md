# Function: findConnectorInstanceByID()

> **findConnectorInstanceByID**(`connectorInstances`, `instanceID`): `undefined` \| [`ConnectorInstance`](../../ConnectorInstance/classes/ConnectorInstance.md)

Defined in: [src/common/web/data/entities/connector/ConnectorUtils.ts:31](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/connector/ConnectorUtils.ts#L31)

Searches for a connector instance by its ID within a list of connector instances.

## Parameters

### connectorInstances

[`ConnectorInstance`](../../ConnectorInstance/classes/ConnectorInstance.md)[]

The list of connector instances.

### instanceID

`string`

The connector instance to search for.

## Returns

`undefined` \| [`ConnectorInstance`](../../ConnectorInstance/classes/ConnectorInstance.md)

- The found connector instance or **undefined** otherwise.

# Function: findConnectorByID()

> **findConnectorByID**(`connectors`, `connectorID`): `undefined` \| [`Connector`](../../Connector/classes/Connector.md)

Defined in: [src/common/web/data/entities/connector/ConnectorUtils.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/connector/ConnectorUtils.ts#L19)

Searches for a connector by its ID within a list of connectors.

## Parameters

### connectors

[`Connector`](../../Connector/classes/Connector.md)[]

The list of connectors.

### connectorID

`string`

The connector to search for.

## Returns

`undefined` \| [`Connector`](../../Connector/classes/Connector.md)

- The found connector or **undefined** otherwise.

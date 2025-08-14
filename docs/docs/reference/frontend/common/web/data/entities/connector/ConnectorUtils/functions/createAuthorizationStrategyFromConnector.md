# Function: createAuthorizationStrategyFromConnector()

> **createAuthorizationStrategyFromConnector**(`comp`, `svc`, `connector`): `undefined` \| [`AuthorizationStrategy`](../../../../../integration/authorization/strategies/AuthorizationStrategy/classes/AuthorizationStrategy.md)

Defined in: [src/common/web/data/entities/connector/ConnectorUtils.ts:74](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/connector/ConnectorUtils.ts#L74)

Creates the authorization strategy configured in a connector.

## Parameters

### comp

[`WebComponent`](../../../../../component/WebComponent/classes/WebComponent.md)

The global component.

### svc

[`Service`](../../../../../services/Service/classes/Service.md)

The service to use for message sending.

### connector

The connector.

`undefined` | [`Connector`](../../Connector/classes/Connector.md)

## Returns

`undefined` \| [`AuthorizationStrategy`](../../../../../integration/authorization/strategies/AuthorizationStrategy/classes/AuthorizationStrategy.md)

- The authorization strategy or **undefined** if none is required.

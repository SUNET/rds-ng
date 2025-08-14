# Function: createAuthorizationStrategyFromConnectorInstance()

> **createAuthorizationStrategyFromConnectorInstance**(`comp`, `svc`, `instance`, `connectors`): `undefined` \| [`AuthorizationStrategy`](../../../../../integration/authorization/strategies/AuthorizationStrategy/classes/AuthorizationStrategy.md)

Defined in: [src/common/web/data/entities/connector/ConnectorInstanceUtils.ts:83](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/connector/ConnectorInstanceUtils.ts#L83)

Creates the authorization strategy configured in a connector instance.

## Parameters

### comp

[`WebComponent`](../../../../../component/WebComponent/classes/WebComponent.md)

The global component.

### svc

[`Service`](../../../../../services/Service/classes/Service.md)

The service to use for message sending.

### instance

[`ConnectorInstance`](../../ConnectorInstance/classes/ConnectorInstance.md)

The connector instance.

### connectors

[`Connector`](../../Connector/classes/Connector.md)[]

List of all connectors.

## Returns

`undefined` \| [`AuthorizationStrategy`](../../../../../integration/authorization/strategies/AuthorizationStrategy/classes/AuthorizationStrategy.md)

- The authorization strategy or **undefined** if none is required.

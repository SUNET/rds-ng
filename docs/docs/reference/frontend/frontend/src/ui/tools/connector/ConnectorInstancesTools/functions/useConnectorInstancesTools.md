# Function: useConnectorInstancesTools()

> **useConnectorInstancesTools**(`comp`): `object`

Defined in: [src/frontend/src/ui/tools/connector/ConnectorInstancesTools.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/tools/connector/ConnectorInstancesTools.ts#L19)

Tools for working with connector instances.

## Parameters

### comp

[`FrontendComponent`](../../../../../component/FrontendComponent/classes/FrontendComponent.md)

## Returns

`object`

### deleteInstance()

> **deleteInstance**: (`instances`, `instance`) => `void`

#### Parameters

##### instances

[`ConnectorInstance`](../../../../../../../common/web/data/entities/connector/ConnectorInstance/classes/ConnectorInstance.md)[]

##### instance

[`ConnectorInstance`](../../../../../../../common/web/data/entities/connector/ConnectorInstance/classes/ConnectorInstance.md)

#### Returns

`void`

### editInstance()

> **editInstance**: (`instances`, `instance`, `connector?`) => `Promise`\<[`ConnectorInstance`](../../../../../../../common/web/data/entities/connector/ConnectorInstance/classes/ConnectorInstance.md)\>

#### Parameters

##### instances

[`ConnectorInstance`](../../../../../../../common/web/data/entities/connector/ConnectorInstance/classes/ConnectorInstance.md)[]

##### instance

[`ConnectorInstance`](../../../../../../../common/web/data/entities/connector/ConnectorInstance/classes/ConnectorInstance.md)

##### connector?

[`Connector`](../../../../../../../common/web/data/entities/connector/Connector/classes/Connector.md)

#### Returns

`Promise`\<[`ConnectorInstance`](../../../../../../../common/web/data/entities/connector/ConnectorInstance/classes/ConnectorInstance.md)\>

### newInstance()

> **newInstance**: (`instances`, `connector`) => `Promise`\<[`ConnectorInstance`](../../../../../../../common/web/data/entities/connector/ConnectorInstance/classes/ConnectorInstance.md)\>

#### Parameters

##### instances

[`ConnectorInstance`](../../../../../../../common/web/data/entities/connector/ConnectorInstance/classes/ConnectorInstance.md)[]

##### connector

[`Connector`](../../../../../../../common/web/data/entities/connector/Connector/classes/Connector.md)

#### Returns

`Promise`\<[`ConnectorInstance`](../../../../../../../common/web/data/entities/connector/ConnectorInstance/classes/ConnectorInstance.md)\>

### requestInstanceAuthorization()

> **requestInstanceAuthorization**: (`instance`, `connectors`, `authorizations`) => `void`

#### Parameters

##### instance

[`ConnectorInstance`](../../../../../../../common/web/data/entities/connector/ConnectorInstance/classes/ConnectorInstance.md)

##### connectors

[`Connector`](../../../../../../../common/web/data/entities/connector/Connector/classes/Connector.md)[]

##### authorizations

`string`[]

#### Returns

`void`

### revokeInstanceAuthorization()

> **revokeInstanceAuthorization**: (`instance`, `updateAuthState`) => `void`

#### Parameters

##### instance

[`ConnectorInstance`](../../../../../../../common/web/data/entities/connector/ConnectorInstance/classes/ConnectorInstance.md)

##### updateAuthState

`boolean` = `true`

#### Returns

`void`

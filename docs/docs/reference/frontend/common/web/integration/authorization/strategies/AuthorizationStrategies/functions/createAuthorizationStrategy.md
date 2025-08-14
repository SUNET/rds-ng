# Function: createAuthorizationStrategy()

> **createAuthorizationStrategy**(`comp`, `svc`, `strategy`, `config`): [`AuthorizationStrategy`](../../AuthorizationStrategy/classes/AuthorizationStrategy.md)

Defined in: [src/common/web/integration/authorization/strategies/AuthorizationStrategies.ts:32](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/strategies/AuthorizationStrategies.ts#L32)

Creates an authorization strategy using the specified identifier.

## Parameters

### comp

[`WebComponent`](../../../../../component/WebComponent/classes/WebComponent.md)

The global component.

### svc

[`Service`](../../../../../services/Service/classes/Service.md)

The service to use for message sending.

### strategy

`string`

The strategy identifier.

### config

`Record`\<`string`, `any`\>

The host strategy configuration as an arbitrary record.

## Returns

[`AuthorizationStrategy`](../../AuthorizationStrategy/classes/AuthorizationStrategy.md)

- The newly created strategy.

# Function: createOAuth2Strategy()

> **createOAuth2Strategy**(`comp`, `svc`, `config`): [`OAuth2Strategy`](../classes/OAuth2Strategy.md)

Defined in: [src/common/web/integration/authorization/strategies/oauth2/OAuth2Strategy.ts:89](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/strategies/oauth2/OAuth2Strategy.ts#L89)

Creates a new OAuth2 strategy instance, automatically configuring it.

## Parameters

### comp

[`WebComponent`](../../../../../../component/WebComponent/classes/WebComponent.md)

The main component.

### svc

[`Service`](../../../../../../services/Service/classes/Service.md)

The service to use for message sending.

### config

`Record`\<`string`, `any`\>

The strategy configuration.

## Returns

[`OAuth2Strategy`](../classes/OAuth2Strategy.md)

- The newly created strategy.

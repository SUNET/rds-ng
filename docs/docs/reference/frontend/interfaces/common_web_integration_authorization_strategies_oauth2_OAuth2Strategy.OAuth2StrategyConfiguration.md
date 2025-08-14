---
id: "common_web_integration_authorization_strategies_oauth2_OAuth2Strategy.OAuth2StrategyConfiguration"
title: "Interface: OAuth2StrategyConfiguration"
sidebar_label: "OAuth2StrategyConfiguration"
custom_edit_url: null
---

[common/web/integration/authorization/strategies/oauth2/OAuth2Strategy](../modules/common_web_integration_authorization_strategies_oauth2_OAuth2Strategy.md).OAuth2StrategyConfiguration

The OAuth2 strategy configuration.

## Properties

### client

• **client**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `client_id` | `string` |
| `redirect_target` | [`RedirectionTarget`](../enums/common_web_utils_HTMLUtils.RedirectionTarget.md) |
| `redirect_url` | `string` |

#### Defined in

[src/common/web/integration/authorization/strategies/oauth2/OAuth2Strategy.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/strategies/oauth2/OAuth2Strategy.ts#L19)

___

### server

• **server**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `authorization_endpoint` | `string` |
| `host` | `string` |
| `scope` | `string` |
| `token_endpoint` | `string` |

#### Defined in

[src/common/web/integration/authorization/strategies/oauth2/OAuth2Strategy.ts:13](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/strategies/oauth2/OAuth2Strategy.ts#L13)

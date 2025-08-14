---
id: "common_web_integration_authorization_strategies_oauth2_OAuth2Strategy"
title: "Module: common/web/integration/authorization/strategies/oauth2/OAuth2Strategy"
sidebar_label: "common/web/integration/authorization/strategies/oauth2/OAuth2Strategy"
sidebar_position: 0
custom_edit_url: null
---

## Classes

- [OAuth2Strategy](../classes/common_web_integration_authorization_strategies_oauth2_OAuth2Strategy.OAuth2Strategy.md)

## Interfaces

- [OAuth2StrategyConfiguration](../interfaces/common_web_integration_authorization_strategies_oauth2_OAuth2Strategy.OAuth2StrategyConfiguration.md)

## Functions

### createOAuth2Strategy

▸ **createOAuth2Strategy**(`comp`, `svc`, `config`): [`OAuth2Strategy`](../classes/common_web_integration_authorization_strategies_oauth2_OAuth2Strategy.OAuth2Strategy.md)

Creates a new OAuth2 strategy instance, automatically configuring it.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `comp` | [`WebComponent`](../classes/common_web_component_WebComponent.WebComponent.md)<[`UserInterface`](../classes/common_web_ui_UserInterface.UserInterface.md)\> | The main component. |
| `svc` | [`Service`](../classes/common_web_services_Service.Service.md)<[`ServiceContext`](../classes/common_web_services_ServiceContext.ServiceContext.md)\> | The service to use for message sending. |
| `config` | `Record`<`string`, `any`\> | The strategy configuration. |

#### Returns

[`OAuth2Strategy`](../classes/common_web_integration_authorization_strategies_oauth2_OAuth2Strategy.OAuth2Strategy.md)

- The newly created strategy.

#### Defined in

[src/common/web/integration/authorization/strategies/oauth2/OAuth2Strategy.ts:89](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/strategies/oauth2/OAuth2Strategy.ts#L89)

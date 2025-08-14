---
id: "common_web_integration_authorization_strategies_AuthorizationStrategies"
title: "Module: common/web/integration/authorization/strategies/AuthorizationStrategies"
sidebar_label: "common/web/integration/authorization/strategies/AuthorizationStrategies"
sidebar_position: 0
custom_edit_url: null
---

## Functions

### createAuthorizationStrategy

▸ **createAuthorizationStrategy**(`comp`, `svc`, `strategy`, `config`): [`AuthorizationStrategy`](../classes/common_web_integration_authorization_strategies_AuthorizationStrategy.AuthorizationStrategy.md)

Creates an authorization strategy using the specified identifier.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `comp` | [`WebComponent`](../classes/common_web_component_WebComponent.WebComponent.md)<[`UserInterface`](../classes/common_web_ui_UserInterface.UserInterface.md)\> | The global component. |
| `svc` | [`Service`](../classes/common_web_services_Service.Service.md)<[`ServiceContext`](../classes/common_web_services_ServiceContext.ServiceContext.md)\> | The service to use for message sending. |
| `strategy` | `string` | The strategy identifier. |
| `config` | `Record`<`string`, `any`\> | The host strategy configuration as an arbitrary record. |

#### Returns

[`AuthorizationStrategy`](../classes/common_web_integration_authorization_strategies_AuthorizationStrategy.AuthorizationStrategy.md)

- The newly created strategy.

#### Defined in

[src/common/web/integration/authorization/strategies/AuthorizationStrategies.ts:32](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/strategies/AuthorizationStrategies.ts#L32)

___

### registerAuthorizationStrategies

▸ **registerAuthorizationStrategies**(): `void`

Registers all available authorization strategies.

When adding a new strategy, always register it here.

#### Returns

`void`

#### Defined in

[src/common/web/integration/authorization/strategies/AuthorizationStrategies.ts:13](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/strategies/AuthorizationStrategies.ts#L13)

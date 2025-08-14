---
id: "frontend_src_integration_authorization_Authorizer.Authorizer"
title: "Class: Authorizer"
sidebar_label: "Authorizer"
custom_edit_url: null
---

[frontend/src/integration/authorization/Authorizer](../modules/frontend_src_integration_authorization_Authorizer.md).Authorizer

Base authorizer.

## Hierarchy

- [`IntegrationHandler`](frontend_src_integration_IntegrationHandler.IntegrationHandler.md)

  ↳ **`Authorizer`**

  ↳↳ [`BasicAuthorizer`](frontend_src_integration_authorization_BasicAuthorizer.BasicAuthorizer.md)

  ↳↳ [`HostAuthorizer`](frontend_src_integration_authorization_HostAuthorizer.HostAuthorizer.md)

## Constructors

### constructor

• **new Authorizer**(`comp`): [`Authorizer`](frontend_src_integration_authorization_Authorizer.Authorizer.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `comp` | [`FrontendComponent`](frontend_src_component_FrontendComponent.FrontendComponent.md) |

#### Returns

[`Authorizer`](frontend_src_integration_authorization_Authorizer.Authorizer.md)

#### Inherited from

[IntegrationHandler](frontend_src_integration_IntegrationHandler.IntegrationHandler.md).[constructor](frontend_src_integration_IntegrationHandler.IntegrationHandler.md#constructor)

#### Defined in

[src/frontend/src/integration/IntegrationHandler.ts:9](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/IntegrationHandler.ts#L9)

## Properties

### \_callbacks

• `Protected` `Readonly` **\_callbacks**: [`ExecutionCallbacks`](common_web_utils_ExecutionCallbacks.ExecutionCallbacks.md)<[`AuthorizerDoneCallback`](../modules/frontend_src_integration_authorization_Authorizer.md#authorizerdonecallback), [`AuthorizerFailCallback`](../modules/frontend_src_integration_authorization_Authorizer.md#authorizerfailcallback)\>

#### Defined in

[src/frontend/src/integration/authorization/Authorizer.ts:16](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/authorization/Authorizer.ts#L16)

___

### \_component

• `Protected` `Readonly` **\_component**: [`FrontendComponent`](frontend_src_component_FrontendComponent.FrontendComponent.md)

#### Inherited from

[IntegrationHandler](frontend_src_integration_IntegrationHandler.IntegrationHandler.md).[_component](frontend_src_integration_IntegrationHandler.IntegrationHandler.md#_component)

#### Defined in

[src/frontend/src/integration/IntegrationHandler.ts:7](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/IntegrationHandler.ts#L7)

## Methods

### authorize

▸ **authorize**(`authState`, `fingerprint`): `void`

Authorize the user/integration.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `authState` | [`AuthorizationState`](../enums/common_web_data_entities_authorization_AuthorizationState.AuthorizationState.md) | The current authorization state. |
| `fingerprint` | `string` | The user's fingerprint. |

#### Returns

`void`

#### Defined in

[src/frontend/src/integration/authorization/Authorizer.ts:24](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/authorization/Authorizer.ts#L24)

___

### done

▸ **done**(`cb`): [`Authorizer`](frontend_src_integration_authorization_Authorizer.Authorizer.md)

Adds a *Done* callback.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `cb` | [`AuthorizerDoneCallback`](../modules/frontend_src_integration_authorization_Authorizer.md#authorizerdonecallback) | The callback to add. |

#### Returns

[`Authorizer`](frontend_src_integration_authorization_Authorizer.Authorizer.md)

#### Defined in

[src/frontend/src/integration/authorization/Authorizer.ts:31](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/authorization/Authorizer.ts#L31)

___

### failed

▸ **failed**(`cb`): [`Authorizer`](frontend_src_integration_authorization_Authorizer.Authorizer.md)

Adds a *Fail* callback.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `cb` | [`AuthorizerFailCallback`](../modules/frontend_src_integration_authorization_Authorizer.md#authorizerfailcallback) | The callback to add. |

#### Returns

[`Authorizer`](frontend_src_integration_authorization_Authorizer.Authorizer.md)

#### Defined in

[src/frontend/src/integration/authorization/Authorizer.ts:41](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/authorization/Authorizer.ts#L41)

___

### setAuthorizationState

▸ **setAuthorizationState**(`authState`, `msg?`): `void`

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `authState` | [`AuthorizationState`](../enums/common_web_data_entities_authorization_AuthorizationState.AuthorizationState.md) | `undefined` |
| `msg` | `string` | `""` |

#### Returns

`void`

#### Defined in

[src/frontend/src/integration/authorization/Authorizer.ts:46](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/authorization/Authorizer.ts#L46)

---
id: "frontend_src_integration_authorization_BasicAuthorizer.BasicAuthorizer"
title: "Class: BasicAuthorizer"
sidebar_label: "BasicAuthorizer"
custom_edit_url: null
---

[frontend/src/integration/authorization/BasicAuthorizer](../modules/frontend_src_integration_authorization_BasicAuthorizer.md).BasicAuthorizer

Authorizer for basic integration.

## Hierarchy

- [`Authorizer`](frontend_src_integration_authorization_Authorizer.Authorizer.md)

  ↳ **`BasicAuthorizer`**

## Constructors

### constructor

• **new BasicAuthorizer**(`comp`): [`BasicAuthorizer`](frontend_src_integration_authorization_BasicAuthorizer.BasicAuthorizer.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `comp` | [`FrontendComponent`](frontend_src_component_FrontendComponent.FrontendComponent.md) |

#### Returns

[`BasicAuthorizer`](frontend_src_integration_authorization_BasicAuthorizer.BasicAuthorizer.md)

#### Overrides

[Authorizer](frontend_src_integration_authorization_Authorizer.Authorizer.md).[constructor](frontend_src_integration_authorization_Authorizer.Authorizer.md#constructor)

#### Defined in

[src/frontend/src/integration/authorization/BasicAuthorizer.ts:10](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/authorization/BasicAuthorizer.ts#L10)

## Properties

### \_callbacks

• `Protected` `Readonly` **\_callbacks**: [`ExecutionCallbacks`](common_web_utils_ExecutionCallbacks.ExecutionCallbacks.md)<[`AuthorizerDoneCallback`](../modules/frontend_src_integration_authorization_Authorizer.md#authorizerdonecallback), [`AuthorizerFailCallback`](../modules/frontend_src_integration_authorization_Authorizer.md#authorizerfailcallback)\>

#### Inherited from

[Authorizer](frontend_src_integration_authorization_Authorizer.Authorizer.md).[_callbacks](frontend_src_integration_authorization_Authorizer.Authorizer.md#_callbacks)

#### Defined in

[src/frontend/src/integration/authorization/Authorizer.ts:16](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/authorization/Authorizer.ts#L16)

___

### \_component

• `Protected` `Readonly` **\_component**: [`FrontendComponent`](frontend_src_component_FrontendComponent.FrontendComponent.md)

#### Inherited from

[Authorizer](frontend_src_integration_authorization_Authorizer.Authorizer.md).[_component](frontend_src_integration_authorization_Authorizer.Authorizer.md#_component)

#### Defined in

[src/frontend/src/integration/IntegrationHandler.ts:7](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/IntegrationHandler.ts#L7)

## Methods

### authorize

▸ **authorize**(`_`, `__`): `void`

Authorize the user/integration.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `_` | [`AuthorizationState`](../enums/common_web_data_entities_authorization_AuthorizationState.AuthorizationState.md) | The current authorization state. |
| `__` | `string` | The user's fingerprint. |

#### Returns

`void`

#### Overrides

[Authorizer](frontend_src_integration_authorization_Authorizer.Authorizer.md).[authorize](frontend_src_integration_authorization_Authorizer.Authorizer.md#authorize)

#### Defined in

[src/frontend/src/integration/authorization/BasicAuthorizer.ts:14](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/authorization/BasicAuthorizer.ts#L14)

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

#### Inherited from

[Authorizer](frontend_src_integration_authorization_Authorizer.Authorizer.md).[done](frontend_src_integration_authorization_Authorizer.Authorizer.md#done)

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

#### Inherited from

[Authorizer](frontend_src_integration_authorization_Authorizer.Authorizer.md).[failed](frontend_src_integration_authorization_Authorizer.Authorizer.md#failed)

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

#### Inherited from

[Authorizer](frontend_src_integration_authorization_Authorizer.Authorizer.md).[setAuthorizationState](frontend_src_integration_authorization_Authorizer.Authorizer.md#setauthorizationstate)

#### Defined in

[src/frontend/src/integration/authorization/Authorizer.ts:46](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/authorization/Authorizer.ts#L46)

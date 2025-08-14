---
id: "frontend_src_integration_authorization_HostAuthorizer.HostAuthorizer"
title: "Class: HostAuthorizer"
sidebar_label: "HostAuthorizer"
custom_edit_url: null
---

[frontend/src/integration/authorization/HostAuthorizer](../modules/frontend_src_integration_authorization_HostAuthorizer.md).HostAuthorizer

Authorizer for host integration.

## Hierarchy

- [`Authorizer`](frontend_src_integration_authorization_Authorizer.Authorizer.md)

  ↳ **`HostAuthorizer`**

## Constructors

### constructor

• **new HostAuthorizer**(`comp`, `hostAuth`): [`HostAuthorizer`](frontend_src_integration_authorization_HostAuthorizer.HostAuthorizer.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `comp` | [`FrontendComponent`](frontend_src_component_FrontendComponent.FrontendComponent.md) |
| `hostAuth` | [`AuthorizationSettings`](../interfaces/common_web_data_entities_authorization_AuthorizationSettings.AuthorizationSettings.md) |

#### Returns

[`HostAuthorizer`](frontend_src_integration_authorization_HostAuthorizer.HostAuthorizer.md)

#### Overrides

[Authorizer](frontend_src_integration_authorization_Authorizer.Authorizer.md).[constructor](frontend_src_integration_authorization_Authorizer.Authorizer.md#constructor)

#### Defined in

[src/frontend/src/integration/authorization/HostAuthorizer.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/authorization/HostAuthorizer.ts#L19)

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

___

### \_hostAuth

• `Private` `Readonly` **\_hostAuth**: [`AuthorizationSettings`](../interfaces/common_web_data_entities_authorization_AuthorizationSettings.AuthorizationSettings.md)

#### Defined in

[src/frontend/src/integration/authorization/HostAuthorizer.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/authorization/HostAuthorizer.ts#L17)

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

#### Overrides

[Authorizer](frontend_src_integration_authorization_Authorizer.Authorizer.md).[authorize](frontend_src_integration_authorization_Authorizer.Authorizer.md#authorize)

#### Defined in

[src/frontend/src/integration/authorization/HostAuthorizer.ts:25](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/authorization/HostAuthorizer.ts#L25)

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

### getStrategyConfiguration

▸ **getStrategyConfiguration**(`strategy`): `Record`<`string`, `any`\>

#### Parameters

| Name | Type |
| :------ | :------ |
| `strategy` | `string` |

#### Returns

`Record`<`string`, `any`\>

#### Defined in

[src/frontend/src/integration/authorization/HostAuthorizer.ts:56](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/authorization/HostAuthorizer.ts#L56)

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

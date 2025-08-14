---
id: "frontend_src_integration_authentication_Authenticator.Authenticator"
title: "Class: Authenticator"
sidebar_label: "Authenticator"
custom_edit_url: null
---

[frontend/src/integration/authentication/Authenticator](../modules/frontend_src_integration_authentication_Authenticator.md).Authenticator

Base authenticator.

## Hierarchy

- [`IntegrationHandler`](frontend_src_integration_IntegrationHandler.IntegrationHandler.md)

  ↳ **`Authenticator`**

  ↳↳ [`BasicAuthenticator`](frontend_src_integration_authentication_BasicAuthenticator.BasicAuthenticator.md)

  ↳↳ [`HostAuthenticator`](frontend_src_integration_authentication_HostAuthenticator.HostAuthenticator.md)

## Constructors

### constructor

• **new Authenticator**(`comp`, `token`): [`Authenticator`](frontend_src_integration_authentication_Authenticator.Authenticator.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `comp` | [`FrontendComponent`](frontend_src_component_FrontendComponent.FrontendComponent.md) |
| `token` | [`UserToken`](../interfaces/common_web_data_entities_user_UserToken.UserToken.md) |

#### Returns

[`Authenticator`](frontend_src_integration_authentication_Authenticator.Authenticator.md)

#### Overrides

[IntegrationHandler](frontend_src_integration_IntegrationHandler.IntegrationHandler.md).[constructor](frontend_src_integration_IntegrationHandler.IntegrationHandler.md#constructor)

#### Defined in

[src/frontend/src/integration/authentication/Authenticator.ts:24](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/authentication/Authenticator.ts#L24)

## Properties

### \_callbacks

• `Protected` `Readonly` **\_callbacks**: [`ExecutionCallbacks`](common_web_utils_ExecutionCallbacks.ExecutionCallbacks.md)<[`AuthenticatorDoneCallback`](../modules/frontend_src_integration_authentication_Authenticator.md#authenticatordonecallback), [`AuthenticatorFailCallback`](../modules/frontend_src_integration_authentication_Authenticator.md#authenticatorfailcallback)\>

#### Defined in

[src/frontend/src/integration/authentication/Authenticator.ts:22](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/authentication/Authenticator.ts#L22)

___

### \_component

• `Protected` `Readonly` **\_component**: [`FrontendComponent`](frontend_src_component_FrontendComponent.FrontendComponent.md)

#### Inherited from

[IntegrationHandler](frontend_src_integration_IntegrationHandler.IntegrationHandler.md).[_component](frontend_src_integration_IntegrationHandler.IntegrationHandler.md#_component)

#### Defined in

[src/frontend/src/integration/IntegrationHandler.ts:7](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/IntegrationHandler.ts#L7)

___

### \_userToken

• `Protected` `Readonly` **\_userToken**: [`UserToken`](../interfaces/common_web_data_entities_user_UserToken.UserToken.md)

#### Defined in

[src/frontend/src/integration/authentication/Authenticator.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/authentication/Authenticator.ts#L20)

## Methods

### authenticate

▸ **authenticate**(): `void`

Authenticate the user.

#### Returns

`void`

#### Defined in

[src/frontend/src/integration/authentication/Authenticator.ts:33](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/authentication/Authenticator.ts#L33)

___

### authenticateWithToken

▸ **authenticateWithToken**(): `void`

#### Returns

`void`

#### Defined in

[src/frontend/src/integration/authentication/Authenticator.ts:55](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/authentication/Authenticator.ts#L55)

___

### done

▸ **done**(`cb`): [`Authenticator`](frontend_src_integration_authentication_Authenticator.Authenticator.md)

Adds a *Done* callback.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `cb` | [`AuthenticatorDoneCallback`](../modules/frontend_src_integration_authentication_Authenticator.md#authenticatordonecallback) | The callback to add. |

#### Returns

[`Authenticator`](frontend_src_integration_authentication_Authenticator.Authenticator.md)

#### Defined in

[src/frontend/src/integration/authentication/Authenticator.ts:40](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/authentication/Authenticator.ts#L40)

___

### failed

▸ **failed**(`cb`): [`Authenticator`](frontend_src_integration_authentication_Authenticator.Authenticator.md)

Adds a *Fail* callback.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `cb` | [`AuthenticatorFailCallback`](../modules/frontend_src_integration_authentication_Authenticator.md#authenticatorfailcallback) | The callback to add. |

#### Returns

[`Authenticator`](frontend_src_integration_authentication_Authenticator.Authenticator.md)

#### Defined in

[src/frontend/src/integration/authentication/Authenticator.ts:50](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/authentication/Authenticator.ts#L50)

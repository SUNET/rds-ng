---
id: "frontend_src_integration_authentication_HostAuthenticator.HostAuthenticator"
title: "Class: HostAuthenticator"
sidebar_label: "HostAuthenticator"
custom_edit_url: null
---

[frontend/src/integration/authentication/HostAuthenticator](../modules/frontend_src_integration_authentication_HostAuthenticator.md).HostAuthenticator

Authenticator for host integration.

## Hierarchy

- [`Authenticator`](frontend_src_integration_authentication_Authenticator.Authenticator.md)

  ↳ **`HostAuthenticator`**

## Constructors

### constructor

• **new HostAuthenticator**(`comp`, `userToken`): [`HostAuthenticator`](frontend_src_integration_authentication_HostAuthenticator.HostAuthenticator.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `comp` | [`FrontendComponent`](frontend_src_component_FrontendComponent.FrontendComponent.md) |
| `userToken` | [`HostUserToken`](../interfaces/frontend_src_integration_HostTypes.HostUserToken.md) |

#### Returns

[`HostAuthenticator`](frontend_src_integration_authentication_HostAuthenticator.HostAuthenticator.md)

#### Overrides

[Authenticator](frontend_src_integration_authentication_Authenticator.Authenticator.md).[constructor](frontend_src_integration_authentication_Authenticator.Authenticator.md#constructor)

#### Defined in

[src/frontend/src/integration/authentication/HostAuthenticator.ts:11](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/authentication/HostAuthenticator.ts#L11)

## Properties

### \_callbacks

• `Protected` `Readonly` **\_callbacks**: [`ExecutionCallbacks`](common_web_utils_ExecutionCallbacks.ExecutionCallbacks.md)<[`AuthenticatorDoneCallback`](../modules/frontend_src_integration_authentication_Authenticator.md#authenticatordonecallback), [`AuthenticatorFailCallback`](../modules/frontend_src_integration_authentication_Authenticator.md#authenticatorfailcallback)\>

#### Inherited from

[Authenticator](frontend_src_integration_authentication_Authenticator.Authenticator.md).[_callbacks](frontend_src_integration_authentication_Authenticator.Authenticator.md#_callbacks)

#### Defined in

[src/frontend/src/integration/authentication/Authenticator.ts:22](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/authentication/Authenticator.ts#L22)

___

### \_component

• `Protected` `Readonly` **\_component**: [`FrontendComponent`](frontend_src_component_FrontendComponent.FrontendComponent.md)

#### Inherited from

[Authenticator](frontend_src_integration_authentication_Authenticator.Authenticator.md).[_component](frontend_src_integration_authentication_Authenticator.Authenticator.md#_component)

#### Defined in

[src/frontend/src/integration/IntegrationHandler.ts:7](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/IntegrationHandler.ts#L7)

___

### \_userToken

• `Protected` `Readonly` **\_userToken**: [`UserToken`](../interfaces/common_web_data_entities_user_UserToken.UserToken.md)

#### Inherited from

[Authenticator](frontend_src_integration_authentication_Authenticator.Authenticator.md).[_userToken](frontend_src_integration_authentication_Authenticator.Authenticator.md#_usertoken)

#### Defined in

[src/frontend/src/integration/authentication/Authenticator.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/authentication/Authenticator.ts#L20)

## Methods

### authenticate

▸ **authenticate**(): `void`

Authenticate the user.

#### Returns

`void`

#### Overrides

[Authenticator](frontend_src_integration_authentication_Authenticator.Authenticator.md).[authenticate](frontend_src_integration_authentication_Authenticator.Authenticator.md#authenticate)

#### Defined in

[src/frontend/src/integration/authentication/HostAuthenticator.ts:15](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/authentication/HostAuthenticator.ts#L15)

___

### authenticateWithToken

▸ **authenticateWithToken**(): `void`

#### Returns

`void`

#### Inherited from

[Authenticator](frontend_src_integration_authentication_Authenticator.Authenticator.md).[authenticateWithToken](frontend_src_integration_authentication_Authenticator.Authenticator.md#authenticatewithtoken)

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

#### Inherited from

[Authenticator](frontend_src_integration_authentication_Authenticator.Authenticator.md).[done](frontend_src_integration_authentication_Authenticator.Authenticator.md#done)

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

#### Inherited from

[Authenticator](frontend_src_integration_authentication_Authenticator.Authenticator.md).[failed](frontend_src_integration_authentication_Authenticator.Authenticator.md#failed)

#### Defined in

[src/frontend/src/integration/authentication/Authenticator.ts:50](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/authentication/Authenticator.ts#L50)

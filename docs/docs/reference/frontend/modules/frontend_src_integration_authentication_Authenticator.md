---
id: "frontend_src_integration_authentication_Authenticator"
title: "Module: frontend/src/integration/authentication/Authenticator"
sidebar_label: "frontend/src/integration/authentication/Authenticator"
sidebar_position: 0
custom_edit_url: null
---

## Classes

- [Authenticator](../classes/frontend_src_integration_authentication_Authenticator.Authenticator.md)

## Type Aliases

### AuthenticatorDoneCallback

Ƭ **AuthenticatorDoneCallback**: (`authState`: [`AuthorizationState`](../enums/common_web_data_entities_authorization_AuthorizationState.AuthorizationState.md), `fingerprint`: `string`) => `void`

#### Type declaration

▸ (`authState`, `fingerprint`): `void`

##### Parameters

| Name | Type |
| :------ | :------ |
| `authState` | [`AuthorizationState`](../enums/common_web_data_entities_authorization_AuthorizationState.AuthorizationState.md) |
| `fingerprint` | `string` |

##### Returns

`void`

#### Defined in

[src/frontend/src/integration/authentication/Authenticator.ts:13](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/authentication/Authenticator.ts#L13)

___

### AuthenticatorFailCallback

Ƭ **AuthenticatorFailCallback**: (`msg`: `string`) => `void`

#### Type declaration

▸ (`msg`): `void`

##### Parameters

| Name | Type |
| :------ | :------ |
| `msg` | `string` |

##### Returns

`void`

#### Defined in

[src/frontend/src/integration/authentication/Authenticator.ts:14](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/authentication/Authenticator.ts#L14)

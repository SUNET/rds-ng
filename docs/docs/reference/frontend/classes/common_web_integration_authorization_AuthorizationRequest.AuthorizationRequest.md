---
id: "common_web_integration_authorization_AuthorizationRequest.AuthorizationRequest"
title: "Class: AuthorizationRequest"
sidebar_label: "AuthorizationRequest"
custom_edit_url: null
---

[common/web/integration/authorization/AuthorizationRequest](../modules/common_web_integration_authorization_AuthorizationRequest.md).AuthorizationRequest

Helper class to deal with authorization requests and their payload.

## Constructors

### constructor

• **new AuthorizationRequest**(): [`AuthorizationRequest`](common_web_integration_authorization_AuthorizationRequest.AuthorizationRequest.md)

#### Returns

[`AuthorizationRequest`](common_web_integration_authorization_AuthorizationRequest.AuthorizationRequest.md)

#### Defined in

[src/common/web/integration/authorization/AuthorizationRequest.ts:26](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/AuthorizationRequest.ts#L26)

## Properties

### \_payload

• `Private` **\_payload**: [`AuthorizationRequestPayload`](../interfaces/common_web_integration_authorization_AuthorizationRequest.AuthorizationRequestPayload.md)

#### Defined in

[src/common/web/integration/authorization/AuthorizationRequest.ts:24](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/AuthorizationRequest.ts#L24)

## Accessors

### encodedPayload

• `get` **encodedPayload**(): `string`

The request payload, encoded as a base64 string.

#### Returns

`string`

#### Defined in

[src/common/web/integration/authorization/AuthorizationRequest.ts:114](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/AuthorizationRequest.ts#L114)

___

### payload

• `get` **payload**(): [`AuthorizationRequestPayload`](../interfaces/common_web_integration_authorization_AuthorizationRequest.AuthorizationRequestPayload.md)

The request payload.

#### Returns

[`AuthorizationRequestPayload`](../interfaces/common_web_integration_authorization_AuthorizationRequest.AuthorizationRequestPayload.md)

#### Defined in

[src/common/web/integration/authorization/AuthorizationRequest.ts:107](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/AuthorizationRequest.ts#L107)

## Methods

### decodeRequestPayload

▸ **decodeRequestPayload**(): [`AuthorizationRequestPayload`](../interfaces/common_web_integration_authorization_AuthorizationRequest.AuthorizationRequestPayload.md)

#### Returns

[`AuthorizationRequestPayload`](../interfaces/common_web_integration_authorization_AuthorizationRequest.AuthorizationRequestPayload.md)

#### Defined in

[src/common/web/integration/authorization/AuthorizationRequest.ts:126](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/AuthorizationRequest.ts#L126)

___

### encodeRequestPayload

▸ **encodeRequestPayload**(): `string`

#### Returns

`string`

#### Defined in

[src/common/web/integration/authorization/AuthorizationRequest.ts:122](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/AuthorizationRequest.ts#L122)

___

### payloadFromURLParameters

▸ **payloadFromURLParameters**(): `void`

#### Returns

`void`

#### Defined in

[src/common/web/integration/authorization/AuthorizationRequest.ts:118](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/AuthorizationRequest.ts#L118)

___

### verify

▸ **verify**(`other`): `void`

Compares this request to another one, throwing an error in case of any mismatch.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `other` | [`AuthorizationRequest`](common_web_integration_authorization_AuthorizationRequest.AuthorizationRequest.md) | The authorization request to compare to. |

#### Returns

`void`

#### Defined in

[src/common/web/integration/authorization/AuthorizationRequest.ts:91](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/AuthorizationRequest.ts#L91)

___

### fromURLParameters

▸ **fromURLParameters**(): [`AuthorizationRequest`](common_web_integration_authorization_AuthorizationRequest.AuthorizationRequest.md)

#### Returns

[`AuthorizationRequest`](common_web_integration_authorization_AuthorizationRequest.AuthorizationRequest.md)

#### Defined in

[src/common/web/integration/authorization/AuthorizationRequest.ts:63](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/AuthorizationRequest.ts#L63)

___

### fromValues

▸ **fromValues**(`authID`, `authType`, `authIssuer`, `authBearer`, `fingerprint`): [`AuthorizationRequest`](common_web_integration_authorization_AuthorizationRequest.AuthorizationRequest.md)

Creates a new authorization request based on values.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `authID` | `string` | The authorization ID. |
| `authType` | [`AuthorizationTokenType`](../enums/common_web_data_entities_authorization_AuthorizationToken.AuthorizationTokenType.md) | The authorization type. |
| `authIssuer` | `string` | The issuer of the authorization. |
| `authBearer` | `string` | The bearer of the authorization. |
| `fingerprint` | `string` | The user's fingerprint. |

#### Returns

[`AuthorizationRequest`](common_web_integration_authorization_AuthorizationRequest.AuthorizationRequest.md)

#### Defined in

[src/common/web/integration/authorization/AuthorizationRequest.ts:45](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/AuthorizationRequest.ts#L45)

___

### requestIssued

▸ **requestIssued**(`authTypes?`): `boolean`

Whether an authorization request has been issued and should be handled now.

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `authTypes` | [`AuthorizationTokenType`](../enums/common_web_data_entities_authorization_AuthorizationToken.AuthorizationTokenType.md)[] | `[]` | The authorization types to check for. |

#### Returns

`boolean`

#### Defined in

[src/common/web/integration/authorization/AuthorizationRequest.ts:74](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/integration/authorization/AuthorizationRequest.ts#L74)

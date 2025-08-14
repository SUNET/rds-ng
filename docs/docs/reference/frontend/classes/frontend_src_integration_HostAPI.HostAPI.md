---
id: "frontend_src_integration_HostAPI.HostAPI"
title: "Class: HostAPI"
sidebar_label: "HostAPI"
custom_edit_url: null
---

[frontend/src/integration/HostAPI](../modules/frontend_src_integration_HostAPI.md).HostAPI

The host integration API.

## Constructors

### constructor

• **new HostAPI**(`comp`): [`HostAPI`](frontend_src_integration_HostAPI.HostAPI.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `comp` | [`FrontendComponent`](frontend_src_component_FrontendComponent.FrontendComponent.md) |

#### Returns

[`HostAPI`](frontend_src_integration_HostAPI.HostAPI.md)

#### Defined in

[src/frontend/src/integration/HostAPI.ts:27](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/HostAPI.ts#L27)

## Properties

### \_apiURL

• `Private` `Readonly` **\_apiURL**: `string`

#### Defined in

[src/frontend/src/integration/HostAPI.ts:25](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/HostAPI.ts#L25)

## Methods

### getAuthorizationSettings

▸ **getAuthorizationSettings**(): `Promise`<[`AuthorizationSettings`](../interfaces/common_web_data_entities_authorization_AuthorizationSettings.AuthorizationSettings.md)\>

#### Returns

`Promise`<[`AuthorizationSettings`](../interfaces/common_web_data_entities_authorization_AuthorizationSettings.AuthorizationSettings.md)\>

#### Defined in

[src/frontend/src/integration/HostAPI.ts:39](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/HostAPI.ts#L39)

___

### getEndpointData

▸ **getEndpointData**<`DataType`\>(`endpoint`, `dataName`, `decodeData?`): `Promise`<`DataType`\>

#### Type parameters

| Name |
| :------ |
| `DataType` |

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `endpoint` | `string` | `undefined` |
| `dataName` | `string` | `undefined` |
| `decodeData` | `boolean` | `false` |

#### Returns

`Promise`<`DataType`\>

#### Defined in

[src/frontend/src/integration/HostAPI.ts:51](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/HostAPI.ts#L51)

___

### getPublicKey

▸ **getPublicKey**(): `Promise`<`JWK`\>

#### Returns

`Promise`<`JWK`\>

#### Defined in

[src/frontend/src/integration/HostAPI.ts:35](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/HostAPI.ts#L35)

___

### getResources

▸ **getResources**(): `Promise`<[`HostResources`](../interfaces/frontend_src_integration_HostTypes.HostResources.md)\>

#### Returns

`Promise`<[`HostResources`](../interfaces/frontend_src_integration_HostTypes.HostResources.md)\>

#### Defined in

[src/frontend/src/integration/HostAPI.ts:43](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/HostAPI.ts#L43)

___

### resolveAPIEndpoint

▸ **resolveAPIEndpoint**(`endpoint`): `string`

#### Parameters

| Name | Type |
| :------ | :------ |
| `endpoint` | `string` |

#### Returns

`string`

#### Defined in

[src/frontend/src/integration/HostAPI.ts:47](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/HostAPI.ts#L47)

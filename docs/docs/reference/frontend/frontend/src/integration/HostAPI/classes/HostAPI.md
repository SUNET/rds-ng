# Class: HostAPI

Defined in: [src/frontend/src/integration/HostAPI.ts:24](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/HostAPI.ts#L24)

The host integration API.

## Constructors

### Constructor

> **new HostAPI**(`comp`): `HostAPI`

Defined in: [src/frontend/src/integration/HostAPI.ts:27](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/HostAPI.ts#L27)

#### Parameters

##### comp

[`FrontendComponent`](../../../component/FrontendComponent/classes/FrontendComponent.md)

#### Returns

`HostAPI`

## Methods

### getAuthorizationSettings()

> **getAuthorizationSettings**(): `Promise`\<[`AuthorizationSettings`](../../../../../common/web/data/entities/authorization/AuthorizationSettings/interfaces/AuthorizationSettings.md)\>

Defined in: [src/frontend/src/integration/HostAPI.ts:39](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/HostAPI.ts#L39)

#### Returns

`Promise`\<[`AuthorizationSettings`](../../../../../common/web/data/entities/authorization/AuthorizationSettings/interfaces/AuthorizationSettings.md)\>

***

### getPublicKey()

> **getPublicKey**(): `Promise`\<`JWK`\>

Defined in: [src/frontend/src/integration/HostAPI.ts:35](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/HostAPI.ts#L35)

#### Returns

`Promise`\<`JWK`\>

***

### getResources()

> **getResources**(): `Promise`\<[`HostResources`](../../HostTypes/interfaces/HostResources.md)\>

Defined in: [src/frontend/src/integration/HostAPI.ts:43](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/HostAPI.ts#L43)

#### Returns

`Promise`\<[`HostResources`](../../HostTypes/interfaces/HostResources.md)\>

# Class: AuthorizationRequest

Defined in: [src/common/web/integration/authorization/AuthorizationRequest.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/AuthorizationRequest.ts#L23)

Helper class to deal with authorization requests and their payload.

## Accessors

### encodedPayload

#### Get Signature

> **get** **encodedPayload**(): `string`

Defined in: [src/common/web/integration/authorization/AuthorizationRequest.ts:114](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/AuthorizationRequest.ts#L114)

The request payload, encoded as a base64 string.

##### Returns

`string`

***

### payload

#### Get Signature

> **get** **payload**(): [`AuthorizationRequestPayload`](../interfaces/AuthorizationRequestPayload.md)

Defined in: [src/common/web/integration/authorization/AuthorizationRequest.ts:107](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/AuthorizationRequest.ts#L107)

The request payload.

##### Returns

[`AuthorizationRequestPayload`](../interfaces/AuthorizationRequestPayload.md)

## Methods

### verify()

> **verify**(`other`): `void`

Defined in: [src/common/web/integration/authorization/AuthorizationRequest.ts:91](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/AuthorizationRequest.ts#L91)

Compares this request to another one, throwing an error in case of any mismatch.

#### Parameters

##### other

`AuthorizationRequest`

The authorization request to compare to.

#### Returns

`void`

***

### fromURLParameters()

> `static` **fromURLParameters**(): `AuthorizationRequest`

Defined in: [src/common/web/integration/authorization/AuthorizationRequest.ts:63](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/AuthorizationRequest.ts#L63)

#### Returns

`AuthorizationRequest`

***

### fromValues()

> `static` **fromValues**(`authID`, `authType`, `authIssuer`, `authBearer`, `fingerprint`): `AuthorizationRequest`

Defined in: [src/common/web/integration/authorization/AuthorizationRequest.ts:45](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/AuthorizationRequest.ts#L45)

Creates a new authorization request based on values.

#### Parameters

##### authID

`string`

The authorization ID.

##### authType

[`AuthorizationTokenType`](../../../../data/entities/authorization/AuthorizationToken/enumerations/AuthorizationTokenType.md)

The authorization type.

##### authIssuer

`string`

The issuer of the authorization.

##### authBearer

`string`

The bearer of the authorization.

##### fingerprint

`string`

The user's fingerprint.

#### Returns

`AuthorizationRequest`

***

### requestIssued()

> `static` **requestIssued**(`authTypes`): `boolean`

Defined in: [src/common/web/integration/authorization/AuthorizationRequest.ts:74](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/AuthorizationRequest.ts#L74)

Whether an authorization request has been issued and should be handled now.

#### Parameters

##### authTypes

[`AuthorizationTokenType`](../../../../data/entities/authorization/AuthorizationToken/enumerations/AuthorizationTokenType.md)[] = `[]`

The authorization types to check for.

#### Returns

`boolean`

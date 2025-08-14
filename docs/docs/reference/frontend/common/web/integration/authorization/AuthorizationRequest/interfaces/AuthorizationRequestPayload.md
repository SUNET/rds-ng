# Interface: AuthorizationRequestPayload

Defined in: [src/common/web/integration/authorization/AuthorizationRequest.ts:7](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/AuthorizationRequest.ts#L7)

The payload that is sent with authorization requests.

## Properties

### auth\_bearer

> **auth\_bearer**: `string`

Defined in: [src/common/web/integration/authorization/AuthorizationRequest.ts:15](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/AuthorizationRequest.ts#L15)

The entity that will be authorized against.

***

### auth\_id

> **auth\_id**: `string`

Defined in: [src/common/web/integration/authorization/AuthorizationRequest.ts:9](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/AuthorizationRequest.ts#L9)

The authorization ID.

***

### auth\_issuer

> **auth\_issuer**: `string`

Defined in: [src/common/web/integration/authorization/AuthorizationRequest.ts:13](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/AuthorizationRequest.ts#L13)

The entity that requires the authorization.

***

### auth\_type

> **auth\_type**: [`AuthorizationTokenType`](../../../../data/entities/authorization/AuthorizationToken/enumerations/AuthorizationTokenType.md)

Defined in: [src/common/web/integration/authorization/AuthorizationRequest.ts:11](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/AuthorizationRequest.ts#L11)

The authorization type.

***

### fingerprint

> **fingerprint**: `string`

Defined in: [src/common/web/integration/authorization/AuthorizationRequest.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/AuthorizationRequest.ts#L17)

The user's fingerprint.

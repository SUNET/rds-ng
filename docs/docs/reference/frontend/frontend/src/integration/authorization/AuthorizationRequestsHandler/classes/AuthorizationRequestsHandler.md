# Class: AuthorizationRequestsHandler

Defined in: [src/frontend/src/integration/authorization/AuthorizationRequestsHandler.ts:16](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/authorization/AuthorizationRequestsHandler.ts#L16)

Class to handle pending authorization requests (except for host authorization).

## Constructors

### Constructor

> **new AuthorizationRequestsHandler**(`comp`, `svc`): `AuthorizationRequestsHandler`

Defined in: [src/frontend/src/integration/authorization/AuthorizationRequestsHandler.ts:24](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/authorization/AuthorizationRequestsHandler.ts#L24)

#### Parameters

##### comp

[`WebComponent`](../../../../../../common/web/component/WebComponent/classes/WebComponent.md)

The global component.

##### svc

[`Service`](../../../../../../common/web/services/Service/classes/Service.md)

The service used for message sending.

#### Returns

`AuthorizationRequestsHandler`

## Methods

### handlePendingRequests()

> **handlePendingRequests**(): `Promise`\<`void`\>

Defined in: [src/frontend/src/integration/authorization/AuthorizationRequestsHandler.ts:29](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/authorization/AuthorizationRequestsHandler.ts#L29)

#### Returns

`Promise`\<`void`\>

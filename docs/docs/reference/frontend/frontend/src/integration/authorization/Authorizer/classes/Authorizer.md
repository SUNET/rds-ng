# Abstract Class: Authorizer

Defined in: [src/frontend/src/integration/authorization/Authorizer.ts:15](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/authorization/Authorizer.ts#L15)

Base authorizer.

## Extends

- [`IntegrationHandler`](../../../IntegrationHandler/classes/IntegrationHandler.md)

## Extended by

- [`BasicAuthorizer`](../../BasicAuthorizer/classes/BasicAuthorizer.md)
- [`HostAuthorizer`](../../HostAuthorizer/classes/HostAuthorizer.md)

## Constructors

### Constructor

> `protected` **new Authorizer**(`comp`): `Authorizer`

Defined in: [src/frontend/src/integration/IntegrationHandler.ts:9](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/IntegrationHandler.ts#L9)

#### Parameters

##### comp

[`FrontendComponent`](../../../../component/FrontendComponent/classes/FrontendComponent.md)

#### Returns

`Authorizer`

#### Inherited from

[`IntegrationHandler`](../../../IntegrationHandler/classes/IntegrationHandler.md).[`constructor`](../../../IntegrationHandler/classes/IntegrationHandler.md#constructor)

## Properties

### \_callbacks

> `protected` `readonly` **\_callbacks**: [`ExecutionCallbacks`](../../../../../../common/web/utils/ExecutionCallbacks/classes/ExecutionCallbacks.md)\<[`AuthorizerDoneCallback`](../type-aliases/AuthorizerDoneCallback.md), [`AuthorizerFailCallback`](../type-aliases/AuthorizerFailCallback.md)\>

Defined in: [src/frontend/src/integration/authorization/Authorizer.ts:16](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/authorization/Authorizer.ts#L16)

***

### \_component

> `protected` `readonly` **\_component**: [`FrontendComponent`](../../../../component/FrontendComponent/classes/FrontendComponent.md)

Defined in: [src/frontend/src/integration/IntegrationHandler.ts:7](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/IntegrationHandler.ts#L7)

#### Inherited from

[`IntegrationHandler`](../../../IntegrationHandler/classes/IntegrationHandler.md).[`_component`](../../../IntegrationHandler/classes/IntegrationHandler.md#_component)

## Methods

### authorize()

> `abstract` **authorize**(`authState`, `fingerprint`): `void`

Defined in: [src/frontend/src/integration/authorization/Authorizer.ts:24](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/authorization/Authorizer.ts#L24)

Authorize the user/integration.

#### Parameters

##### authState

[`AuthorizationState`](../../../../../../common/web/data/entities/authorization/AuthorizationState/enumerations/AuthorizationState.md)

The current authorization state.

##### fingerprint

`string`

The user's fingerprint.

#### Returns

`void`

***

### done()

> **done**(`cb`): `Authorizer`

Defined in: [src/frontend/src/integration/authorization/Authorizer.ts:31](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/authorization/Authorizer.ts#L31)

Adds a *Done* callback.

#### Parameters

##### cb

[`AuthorizerDoneCallback`](../type-aliases/AuthorizerDoneCallback.md)

The callback to add.

#### Returns

`Authorizer`

***

### failed()

> **failed**(`cb`): `Authorizer`

Defined in: [src/frontend/src/integration/authorization/Authorizer.ts:41](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/authorization/Authorizer.ts#L41)

Adds a *Fail* callback.

#### Parameters

##### cb

[`AuthorizerFailCallback`](../type-aliases/AuthorizerFailCallback.md)

The callback to add.

#### Returns

`Authorizer`

***

### setAuthorizationState()

> `protected` **setAuthorizationState**(`authState`, `msg`): `void`

Defined in: [src/frontend/src/integration/authorization/Authorizer.ts:46](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/authorization/Authorizer.ts#L46)

#### Parameters

##### authState

[`AuthorizationState`](../../../../../../common/web/data/entities/authorization/AuthorizationState/enumerations/AuthorizationState.md)

##### msg

`string` = `""`

#### Returns

`void`

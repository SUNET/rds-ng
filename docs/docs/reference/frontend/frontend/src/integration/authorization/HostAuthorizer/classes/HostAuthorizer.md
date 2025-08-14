# Class: HostAuthorizer

Defined in: [src/frontend/src/integration/authorization/HostAuthorizer.ts:16](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/authorization/HostAuthorizer.ts#L16)

Authorizer for host integration.

## Extends

- [`Authorizer`](../../Authorizer/classes/Authorizer.md)

## Constructors

### Constructor

> **new HostAuthorizer**(`comp`, `hostAuth`): `HostAuthorizer`

Defined in: [src/frontend/src/integration/authorization/HostAuthorizer.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/authorization/HostAuthorizer.ts#L19)

#### Parameters

##### comp

[`FrontendComponent`](../../../../component/FrontendComponent/classes/FrontendComponent.md)

##### hostAuth

[`AuthorizationSettings`](../../../../../../common/web/data/entities/authorization/AuthorizationSettings/interfaces/AuthorizationSettings.md)

#### Returns

`HostAuthorizer`

#### Overrides

[`Authorizer`](../../Authorizer/classes/Authorizer.md).[`constructor`](../../Authorizer/classes/Authorizer.md#constructor)

## Properties

### \_callbacks

> `protected` `readonly` **\_callbacks**: [`ExecutionCallbacks`](../../../../../../common/web/utils/ExecutionCallbacks/classes/ExecutionCallbacks.md)\<[`AuthorizerDoneCallback`](../../Authorizer/type-aliases/AuthorizerDoneCallback.md), [`AuthorizerFailCallback`](../../Authorizer/type-aliases/AuthorizerFailCallback.md)\>

Defined in: [src/frontend/src/integration/authorization/Authorizer.ts:16](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/authorization/Authorizer.ts#L16)

#### Inherited from

[`Authorizer`](../../Authorizer/classes/Authorizer.md).[`_callbacks`](../../Authorizer/classes/Authorizer.md#_callbacks)

***

### \_component

> `protected` `readonly` **\_component**: [`FrontendComponent`](../../../../component/FrontendComponent/classes/FrontendComponent.md)

Defined in: [src/frontend/src/integration/IntegrationHandler.ts:7](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/IntegrationHandler.ts#L7)

#### Inherited from

[`Authorizer`](../../Authorizer/classes/Authorizer.md).[`_component`](../../Authorizer/classes/Authorizer.md#_component)

## Methods

### authorize()

> **authorize**(`authState`, `fingerprint`): `void`

Defined in: [src/frontend/src/integration/authorization/HostAuthorizer.ts:25](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/authorization/HostAuthorizer.ts#L25)

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

#### Overrides

[`Authorizer`](../../Authorizer/classes/Authorizer.md).[`authorize`](../../Authorizer/classes/Authorizer.md#authorize)

***

### done()

> **done**(`cb`): [`Authorizer`](../../Authorizer/classes/Authorizer.md)

Defined in: [src/frontend/src/integration/authorization/Authorizer.ts:31](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/authorization/Authorizer.ts#L31)

Adds a *Done* callback.

#### Parameters

##### cb

[`AuthorizerDoneCallback`](../../Authorizer/type-aliases/AuthorizerDoneCallback.md)

The callback to add.

#### Returns

[`Authorizer`](../../Authorizer/classes/Authorizer.md)

#### Inherited from

[`Authorizer`](../../Authorizer/classes/Authorizer.md).[`done`](../../Authorizer/classes/Authorizer.md#done)

***

### failed()

> **failed**(`cb`): [`Authorizer`](../../Authorizer/classes/Authorizer.md)

Defined in: [src/frontend/src/integration/authorization/Authorizer.ts:41](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/authorization/Authorizer.ts#L41)

Adds a *Fail* callback.

#### Parameters

##### cb

[`AuthorizerFailCallback`](../../Authorizer/type-aliases/AuthorizerFailCallback.md)

The callback to add.

#### Returns

[`Authorizer`](../../Authorizer/classes/Authorizer.md)

#### Inherited from

[`Authorizer`](../../Authorizer/classes/Authorizer.md).[`failed`](../../Authorizer/classes/Authorizer.md#failed)

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

#### Inherited from

[`Authorizer`](../../Authorizer/classes/Authorizer.md).[`setAuthorizationState`](../../Authorizer/classes/Authorizer.md#setauthorizationstate)

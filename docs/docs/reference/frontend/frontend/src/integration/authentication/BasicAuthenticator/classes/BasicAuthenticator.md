# Class: BasicAuthenticator

Defined in: [src/frontend/src/integration/authentication/BasicAuthenticator.ts:9](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/authentication/BasicAuthenticator.ts#L9)

Authenticator for basic integration.

## Extends

- [`Authenticator`](../../Authenticator/classes/Authenticator.md)

## Constructors

### Constructor

> **new BasicAuthenticator**(`comp`, `userName`): `BasicAuthenticator`

Defined in: [src/frontend/src/integration/authentication/BasicAuthenticator.ts:10](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/authentication/BasicAuthenticator.ts#L10)

#### Parameters

##### comp

[`FrontendComponent`](../../../../component/FrontendComponent/classes/FrontendComponent.md)

##### userName

`string`

#### Returns

`BasicAuthenticator`

#### Overrides

[`Authenticator`](../../Authenticator/classes/Authenticator.md).[`constructor`](../../Authenticator/classes/Authenticator.md#constructor)

## Properties

### \_callbacks

> `protected` `readonly` **\_callbacks**: [`ExecutionCallbacks`](../../../../../../common/web/utils/ExecutionCallbacks/classes/ExecutionCallbacks.md)\<[`AuthenticatorDoneCallback`](../../Authenticator/type-aliases/AuthenticatorDoneCallback.md), [`AuthenticatorFailCallback`](../../Authenticator/type-aliases/AuthenticatorFailCallback.md)\>

Defined in: [src/frontend/src/integration/authentication/Authenticator.ts:22](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/authentication/Authenticator.ts#L22)

#### Inherited from

[`Authenticator`](../../Authenticator/classes/Authenticator.md).[`_callbacks`](../../Authenticator/classes/Authenticator.md#_callbacks)

***

### \_component

> `protected` `readonly` **\_component**: [`FrontendComponent`](../../../../component/FrontendComponent/classes/FrontendComponent.md)

Defined in: [src/frontend/src/integration/IntegrationHandler.ts:7](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/IntegrationHandler.ts#L7)

#### Inherited from

[`Authenticator`](../../Authenticator/classes/Authenticator.md).[`_component`](../../Authenticator/classes/Authenticator.md#_component)

***

### \_userToken

> `protected` `readonly` **\_userToken**: [`UserToken`](../../../../../../common/web/data/entities/user/UserToken/interfaces/UserToken.md)

Defined in: [src/frontend/src/integration/authentication/Authenticator.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/authentication/Authenticator.ts#L20)

#### Inherited from

[`Authenticator`](../../Authenticator/classes/Authenticator.md).[`_userToken`](../../Authenticator/classes/Authenticator.md#_usertoken)

## Methods

### authenticate()

> **authenticate**(): `void`

Defined in: [src/frontend/src/integration/authentication/BasicAuthenticator.ts:14](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/authentication/BasicAuthenticator.ts#L14)

Authenticate the user.

#### Returns

`void`

#### Overrides

[`Authenticator`](../../Authenticator/classes/Authenticator.md).[`authenticate`](../../Authenticator/classes/Authenticator.md#authenticate)

***

### authenticateWithToken()

> `protected` **authenticateWithToken**(): `void`

Defined in: [src/frontend/src/integration/authentication/Authenticator.ts:55](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/authentication/Authenticator.ts#L55)

#### Returns

`void`

#### Inherited from

[`Authenticator`](../../Authenticator/classes/Authenticator.md).[`authenticateWithToken`](../../Authenticator/classes/Authenticator.md#authenticatewithtoken)

***

### done()

> **done**(`cb`): [`Authenticator`](../../Authenticator/classes/Authenticator.md)

Defined in: [src/frontend/src/integration/authentication/Authenticator.ts:40](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/authentication/Authenticator.ts#L40)

Adds a *Done* callback.

#### Parameters

##### cb

[`AuthenticatorDoneCallback`](../../Authenticator/type-aliases/AuthenticatorDoneCallback.md)

The callback to add.

#### Returns

[`Authenticator`](../../Authenticator/classes/Authenticator.md)

#### Inherited from

[`Authenticator`](../../Authenticator/classes/Authenticator.md).[`done`](../../Authenticator/classes/Authenticator.md#done)

***

### failed()

> **failed**(`cb`): [`Authenticator`](../../Authenticator/classes/Authenticator.md)

Defined in: [src/frontend/src/integration/authentication/Authenticator.ts:50](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/authentication/Authenticator.ts#L50)

Adds a *Fail* callback.

#### Parameters

##### cb

[`AuthenticatorFailCallback`](../../Authenticator/type-aliases/AuthenticatorFailCallback.md)

The callback to add.

#### Returns

[`Authenticator`](../../Authenticator/classes/Authenticator.md)

#### Inherited from

[`Authenticator`](../../Authenticator/classes/Authenticator.md).[`failed`](../../Authenticator/classes/Authenticator.md#failed)

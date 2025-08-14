# Abstract Class: Authenticator

Defined in: [src/frontend/src/integration/authentication/Authenticator.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/authentication/Authenticator.ts#L19)

Base authenticator.

## Extends

- [`IntegrationHandler`](../../../IntegrationHandler/classes/IntegrationHandler.md)

## Extended by

- [`BasicAuthenticator`](../../BasicAuthenticator/classes/BasicAuthenticator.md)
- [`HostAuthenticator`](../../HostAuthenticator/classes/HostAuthenticator.md)

## Constructors

### Constructor

> `protected` **new Authenticator**(`comp`, `token`): `Authenticator`

Defined in: [src/frontend/src/integration/authentication/Authenticator.ts:24](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/authentication/Authenticator.ts#L24)

#### Parameters

##### comp

[`FrontendComponent`](../../../../component/FrontendComponent/classes/FrontendComponent.md)

##### token

[`UserToken`](../../../../../../common/web/data/entities/user/UserToken/interfaces/UserToken.md)

#### Returns

`Authenticator`

#### Overrides

[`IntegrationHandler`](../../../IntegrationHandler/classes/IntegrationHandler.md).[`constructor`](../../../IntegrationHandler/classes/IntegrationHandler.md#constructor)

## Properties

### \_callbacks

> `protected` `readonly` **\_callbacks**: [`ExecutionCallbacks`](../../../../../../common/web/utils/ExecutionCallbacks/classes/ExecutionCallbacks.md)\<[`AuthenticatorDoneCallback`](../type-aliases/AuthenticatorDoneCallback.md), [`AuthenticatorFailCallback`](../type-aliases/AuthenticatorFailCallback.md)\>

Defined in: [src/frontend/src/integration/authentication/Authenticator.ts:22](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/authentication/Authenticator.ts#L22)

***

### \_component

> `protected` `readonly` **\_component**: [`FrontendComponent`](../../../../component/FrontendComponent/classes/FrontendComponent.md)

Defined in: [src/frontend/src/integration/IntegrationHandler.ts:7](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/IntegrationHandler.ts#L7)

#### Inherited from

[`IntegrationHandler`](../../../IntegrationHandler/classes/IntegrationHandler.md).[`_component`](../../../IntegrationHandler/classes/IntegrationHandler.md#_component)

***

### \_userToken

> `protected` `readonly` **\_userToken**: [`UserToken`](../../../../../../common/web/data/entities/user/UserToken/interfaces/UserToken.md)

Defined in: [src/frontend/src/integration/authentication/Authenticator.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/authentication/Authenticator.ts#L20)

## Methods

### authenticate()

> `abstract` **authenticate**(): `void`

Defined in: [src/frontend/src/integration/authentication/Authenticator.ts:33](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/authentication/Authenticator.ts#L33)

Authenticate the user.

#### Returns

`void`

***

### authenticateWithToken()

> `protected` **authenticateWithToken**(): `void`

Defined in: [src/frontend/src/integration/authentication/Authenticator.ts:55](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/authentication/Authenticator.ts#L55)

#### Returns

`void`

***

### done()

> **done**(`cb`): `Authenticator`

Defined in: [src/frontend/src/integration/authentication/Authenticator.ts:40](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/authentication/Authenticator.ts#L40)

Adds a *Done* callback.

#### Parameters

##### cb

[`AuthenticatorDoneCallback`](../type-aliases/AuthenticatorDoneCallback.md)

The callback to add.

#### Returns

`Authenticator`

***

### failed()

> **failed**(`cb`): `Authenticator`

Defined in: [src/frontend/src/integration/authentication/Authenticator.ts:50](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/authentication/Authenticator.ts#L50)

Adds a *Fail* callback.

#### Parameters

##### cb

[`AuthenticatorFailCallback`](../type-aliases/AuthenticatorFailCallback.md)

The callback to add.

#### Returns

`Authenticator`

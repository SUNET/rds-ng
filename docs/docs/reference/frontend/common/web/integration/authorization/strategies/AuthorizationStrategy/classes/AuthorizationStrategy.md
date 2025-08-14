# Abstract Class: AuthorizationStrategy

Defined in: [src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L19)

Base class for all authorization strategies.

## Extended by

- [`OAuth2Strategy`](../../oauth2/OAuth2Strategy/classes/OAuth2Strategy.md)

## Constructors

### Constructor

> `protected` **new AuthorizationStrategy**(`comp`, `svc`, `strategy`, `redirectionTarget`): `AuthorizationStrategy`

Defined in: [src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:29](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L29)

#### Parameters

##### comp

[`WebComponent`](../../../../../component/WebComponent/classes/WebComponent.md)

##### svc

[`Service`](../../../../../services/Service/classes/Service.md)

##### strategy

`string`

##### redirectionTarget

[`RedirectionTarget`](../../../../../utils/HTMLUtils/enumerations/RedirectionTarget.md) = `RedirectionTarget.Current`

#### Returns

`AuthorizationStrategy`

## Properties

### \_component

> `protected` `readonly` **\_component**: [`WebComponent`](../../../../../component/WebComponent/classes/WebComponent.md)

Defined in: [src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L20)

***

### \_redirectionTarget

> `protected` `readonly` **\_redirectionTarget**: [`RedirectionTarget`](../../../../../utils/HTMLUtils/enumerations/RedirectionTarget.md)

Defined in: [src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L23)

***

### \_service

> `protected` `readonly` **\_service**: [`Service`](../../../../../services/Service/classes/Service.md)

Defined in: [src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L21)

## Accessors

### strategy

#### Get Signature

> **get** **strategy**(): `string`

Defined in: [src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:159](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L159)

The strategy identifier.

##### Returns

`string`

## Methods

### executeAuthorizationRequest()

> **executeAuthorizationRequest**(`authRequest`): `Promise`\<[`AuthorizationState`](../../../../../data/entities/authorization/AuthorizationState/enumerations/AuthorizationState.md)\>

Defined in: [src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:52](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L52)

Executes an authorization requests (requires a preceding initiation).

#### Parameters

##### authRequest

[`AuthorizationRequest`](../../../AuthorizationRequest/classes/AuthorizationRequest.md)

The authorization request.

#### Returns

`Promise`\<[`AuthorizationState`](../../../../../data/entities/authorization/AuthorizationState/enumerations/AuthorizationState.md)\>

***

### finishRequest()

> `protected` **finishRequest**(): `void`

Defined in: [src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:115](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L115)

#### Returns

`void`

***

### getRequestData()

> `abstract` `protected` **getRequestData**(`authRequest`): `any`

Defined in: [src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:113](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L113)

#### Parameters

##### authRequest

[`AuthorizationRequest`](../../../AuthorizationRequest/classes/AuthorizationRequest.md)

#### Returns

`any`

***

### initiateAuthorizationRequest()

> **initiateAuthorizationRequest**(`authRequest`): `void`

Defined in: [src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:43](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L43)

Initiates an authorization request.

#### Parameters

##### authRequest

[`AuthorizationRequest`](../../../AuthorizationRequest/classes/AuthorizationRequest.md)

The authorization request.

#### Returns

`void`

***

### initiateRequest()

> `abstract` `protected` **initiateRequest**(`authRequest`): `void`

Defined in: [src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:111](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L111)

#### Parameters

##### authRequest

[`AuthorizationRequest`](../../../AuthorizationRequest/classes/AuthorizationRequest.md)

#### Returns

`void`

***

### redirect()

> `protected` **redirect**(`url`): `void`

Defined in: [src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:117](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L117)

#### Parameters

##### url

`string`

#### Returns

`void`

***

### requestAuthorization()

> **requestAuthorization**(`authState`, `authRequest`): `Promise`\<[`AuthorizationState`](../../../../../data/entities/authorization/AuthorizationState/enumerations/AuthorizationState.md)\>

Defined in: [src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:84](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L84)

Requests user authorization, handling all steps automatically.

#### Parameters

##### authState

[`AuthorizationState`](../../../../../data/entities/authorization/AuthorizationState/enumerations/AuthorizationState.md)

The current authorization state.

##### authRequest

[`AuthorizationRequest`](../../../AuthorizationRequest/classes/AuthorizationRequest.md)

The authorization request.

#### Returns

`Promise`\<[`AuthorizationState`](../../../../../data/entities/authorization/AuthorizationState/enumerations/AuthorizationState.md)\>

***

### requestCompleted()

> **requestCompleted**(`cb`): `this`

Defined in: [src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:106](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L106)

Adds a callback for completed requests.

#### Parameters

##### cb

[`AuthorizationRequestCallback`](../type-aliases/AuthorizationRequestCallback.md)

The callback to add.

#### Returns

`this`

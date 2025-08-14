# Class: OAuth2Strategy

Defined in: [src/common/web/integration/authorization/strategies/oauth2/OAuth2Strategy.ts:29](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/strategies/oauth2/OAuth2Strategy.ts#L29)

OAuth2 authorization strategy.

## Extends

- [`AuthorizationStrategy`](../../../AuthorizationStrategy/classes/AuthorizationStrategy.md)

## Constructors

### Constructor

> **new OAuth2Strategy**(`comp`, `svc`, `config`): `OAuth2Strategy`

Defined in: [src/common/web/integration/authorization/strategies/oauth2/OAuth2Strategy.ts:34](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/strategies/oauth2/OAuth2Strategy.ts#L34)

#### Parameters

##### comp

[`WebComponent`](../../../../../../component/WebComponent/classes/WebComponent.md)

##### svc

[`Service`](../../../../../../services/Service/classes/Service.md)

##### config

[`OAuth2StrategyConfiguration`](../interfaces/OAuth2StrategyConfiguration.md)

#### Returns

`OAuth2Strategy`

#### Overrides

[`AuthorizationStrategy`](../../../AuthorizationStrategy/classes/AuthorizationStrategy.md).[`constructor`](../../../AuthorizationStrategy/classes/AuthorizationStrategy.md#constructor)

## Properties

### \_component

> `protected` `readonly` **\_component**: [`WebComponent`](../../../../../../component/WebComponent/classes/WebComponent.md)

Defined in: [src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L20)

#### Inherited from

[`AuthorizationStrategy`](../../../AuthorizationStrategy/classes/AuthorizationStrategy.md).[`_component`](../../../AuthorizationStrategy/classes/AuthorizationStrategy.md#_component)

***

### \_redirectionTarget

> `protected` `readonly` **\_redirectionTarget**: [`RedirectionTarget`](../../../../../../utils/HTMLUtils/enumerations/RedirectionTarget.md)

Defined in: [src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L23)

#### Inherited from

[`AuthorizationStrategy`](../../../AuthorizationStrategy/classes/AuthorizationStrategy.md).[`_redirectionTarget`](../../../AuthorizationStrategy/classes/AuthorizationStrategy.md#_redirectiontarget)

***

### \_service

> `protected` `readonly` **\_service**: [`Service`](../../../../../../services/Service/classes/Service.md)

Defined in: [src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L21)

#### Inherited from

[`AuthorizationStrategy`](../../../AuthorizationStrategy/classes/AuthorizationStrategy.md).[`_service`](../../../AuthorizationStrategy/classes/AuthorizationStrategy.md#_service)

***

### Strategy

> `readonly` `static` **Strategy**: `"oauth2"` = `"oauth2"`

Defined in: [src/common/web/integration/authorization/strategies/oauth2/OAuth2Strategy.ts:30](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/strategies/oauth2/OAuth2Strategy.ts#L30)

## Accessors

### strategy

#### Get Signature

> **get** **strategy**(): `string`

Defined in: [src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:159](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L159)

The strategy identifier.

##### Returns

`string`

#### Inherited from

[`AuthorizationStrategy`](../../../AuthorizationStrategy/classes/AuthorizationStrategy.md).[`strategy`](../../../AuthorizationStrategy/classes/AuthorizationStrategy.md#strategy)

## Methods

### executeAuthorizationRequest()

> **executeAuthorizationRequest**(`authRequest`): `Promise`\<[`AuthorizationState`](../../../../../../data/entities/authorization/AuthorizationState/enumerations/AuthorizationState.md)\>

Defined in: [src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:52](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L52)

Executes an authorization requests (requires a preceding initiation).

#### Parameters

##### authRequest

[`AuthorizationRequest`](../../../../AuthorizationRequest/classes/AuthorizationRequest.md)

The authorization request.

#### Returns

`Promise`\<[`AuthorizationState`](../../../../../../data/entities/authorization/AuthorizationState/enumerations/AuthorizationState.md)\>

#### Inherited from

[`AuthorizationStrategy`](../../../AuthorizationStrategy/classes/AuthorizationStrategy.md).[`executeAuthorizationRequest`](../../../AuthorizationStrategy/classes/AuthorizationStrategy.md#executeauthorizationrequest)

***

### finishRequest()

> `protected` **finishRequest**(): `void`

Defined in: [src/common/web/integration/authorization/strategies/oauth2/OAuth2Strategy.ts:70](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/strategies/oauth2/OAuth2Strategy.ts#L70)

#### Returns

`void`

#### Overrides

[`AuthorizationStrategy`](../../../AuthorizationStrategy/classes/AuthorizationStrategy.md).[`finishRequest`](../../../AuthorizationStrategy/classes/AuthorizationStrategy.md#finishrequest)

***

### getRequestData()

> `protected` **getRequestData**(`_`): `any`

Defined in: [src/common/web/integration/authorization/strategies/oauth2/OAuth2Strategy.ts:52](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/strategies/oauth2/OAuth2Strategy.ts#L52)

#### Parameters

##### \_

[`AuthorizationRequest`](../../../../AuthorizationRequest/classes/AuthorizationRequest.md)

#### Returns

`any`

#### Overrides

[`AuthorizationStrategy`](../../../AuthorizationStrategy/classes/AuthorizationStrategy.md).[`getRequestData`](../../../AuthorizationStrategy/classes/AuthorizationStrategy.md#getrequestdata)

***

### initiateAuthorizationRequest()

> **initiateAuthorizationRequest**(`authRequest`): `void`

Defined in: [src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:43](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L43)

Initiates an authorization request.

#### Parameters

##### authRequest

[`AuthorizationRequest`](../../../../AuthorizationRequest/classes/AuthorizationRequest.md)

The authorization request.

#### Returns

`void`

#### Inherited from

[`AuthorizationStrategy`](../../../AuthorizationStrategy/classes/AuthorizationStrategy.md).[`initiateAuthorizationRequest`](../../../AuthorizationStrategy/classes/AuthorizationStrategy.md#initiateauthorizationrequest)

***

### initiateRequest()

> `protected` **initiateRequest**(`authRequest`): `void`

Defined in: [src/common/web/integration/authorization/strategies/oauth2/OAuth2Strategy.ts:40](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/strategies/oauth2/OAuth2Strategy.ts#L40)

#### Parameters

##### authRequest

[`AuthorizationRequest`](../../../../AuthorizationRequest/classes/AuthorizationRequest.md)

#### Returns

`void`

#### Overrides

[`AuthorizationStrategy`](../../../AuthorizationStrategy/classes/AuthorizationStrategy.md).[`initiateRequest`](../../../AuthorizationStrategy/classes/AuthorizationStrategy.md#initiaterequest)

***

### redirect()

> `protected` **redirect**(`url`): `void`

Defined in: [src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:117](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L117)

#### Parameters

##### url

`string`

#### Returns

`void`

#### Inherited from

[`AuthorizationStrategy`](../../../AuthorizationStrategy/classes/AuthorizationStrategy.md).[`redirect`](../../../AuthorizationStrategy/classes/AuthorizationStrategy.md#redirect)

***

### requestAuthorization()

> **requestAuthorization**(`authState`, `authRequest`): `Promise`\<[`AuthorizationState`](../../../../../../data/entities/authorization/AuthorizationState/enumerations/AuthorizationState.md)\>

Defined in: [src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:84](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L84)

Requests user authorization, handling all steps automatically.

#### Parameters

##### authState

[`AuthorizationState`](../../../../../../data/entities/authorization/AuthorizationState/enumerations/AuthorizationState.md)

The current authorization state.

##### authRequest

[`AuthorizationRequest`](../../../../AuthorizationRequest/classes/AuthorizationRequest.md)

The authorization request.

#### Returns

`Promise`\<[`AuthorizationState`](../../../../../../data/entities/authorization/AuthorizationState/enumerations/AuthorizationState.md)\>

#### Inherited from

[`AuthorizationStrategy`](../../../AuthorizationStrategy/classes/AuthorizationStrategy.md).[`requestAuthorization`](../../../AuthorizationStrategy/classes/AuthorizationStrategy.md#requestauthorization)

***

### requestCompleted()

> **requestCompleted**(`cb`): `this`

Defined in: [src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts:106](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/strategies/AuthorizationStrategy.ts#L106)

Adds a callback for completed requests.

#### Parameters

##### cb

[`AuthorizationRequestCallback`](../../../AuthorizationStrategy/type-aliases/AuthorizationRequestCallback.md)

The callback to add.

#### Returns

`this`

#### Inherited from

[`AuthorizationStrategy`](../../../AuthorizationStrategy/classes/AuthorizationStrategy.md).[`requestCompleted`](../../../AuthorizationStrategy/classes/AuthorizationStrategy.md#requestcompleted)

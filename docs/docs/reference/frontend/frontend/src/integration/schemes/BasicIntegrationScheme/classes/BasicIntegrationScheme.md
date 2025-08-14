# Class: BasicIntegrationScheme

Defined in: [src/frontend/src/integration/schemes/BasicIntegrationScheme.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/schemes/BasicIntegrationScheme.ts#L19)

Basic authentication using a simple username.

## Extends

- [`IntegrationScheme`](../../../IntegrationScheme/classes/IntegrationScheme.md)

## Constructors

### Constructor

> **new BasicIntegrationScheme**(`comp`): `BasicIntegrationScheme`

Defined in: [src/frontend/src/integration/schemes/BasicIntegrationScheme.ts:22](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/schemes/BasicIntegrationScheme.ts#L22)

#### Parameters

##### comp

[`FrontendComponent`](../../../../component/FrontendComponent/classes/FrontendComponent.md)

#### Returns

`BasicIntegrationScheme`

#### Overrides

[`IntegrationScheme`](../../../IntegrationScheme/classes/IntegrationScheme.md).[`constructor`](../../../IntegrationScheme/classes/IntegrationScheme.md#constructor)

## Properties

### \_component

> `protected` `readonly` **\_component**: [`FrontendComponent`](../../../../component/FrontendComponent/classes/FrontendComponent.md)

Defined in: [src/frontend/src/integration/IntegrationScheme.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/IntegrationScheme.ts#L19)

#### Inherited from

[`IntegrationScheme`](../../../IntegrationScheme/classes/IntegrationScheme.md).[`_component`](../../../IntegrationScheme/classes/IntegrationScheme.md#_component)

***

### Scheme

> `readonly` `static` **Scheme**: `"basic"` = `"basic"`

Defined in: [src/frontend/src/integration/schemes/BasicIntegrationScheme.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/schemes/BasicIntegrationScheme.ts#L20)

## Accessors

### integrationComponent

#### Get Signature

> **get** **integrationComponent**(): [`VueComponent`](../../../../../../common/web/component/WebComponent/type-aliases/VueComponent.md)

Defined in: [src/frontend/src/integration/IntegrationScheme.ts:101](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/IntegrationScheme.ts#L101)

The integration component used during the login process.

##### Returns

[`VueComponent`](../../../../../../common/web/component/WebComponent/type-aliases/VueComponent.md)

#### Inherited from

[`IntegrationScheme`](../../../IntegrationScheme/classes/IntegrationScheme.md).[`integrationComponent`](../../../IntegrationScheme/classes/IntegrationScheme.md#integrationcomponent)

***

### isIntegrated

#### Get Signature

> **get** **isIntegrated**(): `boolean`

Defined in: [src/frontend/src/integration/IntegrationScheme.ts:51](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/IntegrationScheme.ts#L51)

Checks whether the integration has completed.

##### Returns

`boolean`

#### Inherited from

[`IntegrationScheme`](../../../IntegrationScheme/classes/IntegrationScheme.md).[`isIntegrated`](../../../IntegrationScheme/classes/IntegrationScheme.md#isintegrated)

***

### scheme

#### Get Signature

> **get** **scheme**(): `string`

Defined in: [src/frontend/src/integration/IntegrationScheme.ts:94](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/IntegrationScheme.ts#L94)

The scheme identifier.

##### Returns

`string`

#### Inherited from

[`IntegrationScheme`](../../../IntegrationScheme/classes/IntegrationScheme.md).[`scheme`](../../../IntegrationScheme/classes/IntegrationScheme.md#scheme)

## Methods

### authenticator()

> **authenticator**(`userName`): [`Authenticator`](../../../authentication/Authenticator/classes/Authenticator.md)

Defined in: [src/frontend/src/integration/schemes/BasicIntegrationScheme.ts:30](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/schemes/BasicIntegrationScheme.ts#L30)

Creates a new authenticator.

#### Parameters

##### userName

`string`

#### Returns

[`Authenticator`](../../../authentication/Authenticator/classes/Authenticator.md)

#### Overrides

[`IntegrationScheme`](../../../IntegrationScheme/classes/IntegrationScheme.md).[`authenticator`](../../../IntegrationScheme/classes/IntegrationScheme.md#authenticator)

***

### authorizer()

> **authorizer**(): [`Authorizer`](../../../authorization/Authorizer/classes/Authorizer.md)

Defined in: [src/frontend/src/integration/schemes/BasicIntegrationScheme.ts:34](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/schemes/BasicIntegrationScheme.ts#L34)

Creates a new authorizer.

#### Returns

[`Authorizer`](../../../authorization/Authorizer/classes/Authorizer.md)

#### Overrides

[`IntegrationScheme`](../../../IntegrationScheme/classes/IntegrationScheme.md).[`authorizer`](../../../IntegrationScheme/classes/IntegrationScheme.md#authorizer)

***

### endSession()

> **endSession**(): `void`

Defined in: [src/frontend/src/integration/IntegrationScheme.ts:89](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/IntegrationScheme.ts#L89)

Called when the user leaves the main view.

#### Returns

`void`

#### Inherited from

[`IntegrationScheme`](../../../IntegrationScheme/classes/IntegrationScheme.md).[`endSession`](../../../IntegrationScheme/classes/IntegrationScheme.md#endsession)

***

### enter()

> **enter**(): `void`

Defined in: [src/frontend/src/integration/schemes/BasicIntegrationScheme.ts:42](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/schemes/BasicIntegrationScheme.ts#L42)

Called when the user enters the app.

#### Returns

`void`

#### Overrides

[`IntegrationScheme`](../../../IntegrationScheme/classes/IntegrationScheme.md).[`enter`](../../../IntegrationScheme/classes/IntegrationScheme.md#enter)

***

### leave()

> **leave**(): `void`

Defined in: [src/frontend/src/integration/IntegrationScheme.ts:65](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/IntegrationScheme.ts#L65)

Called when the user leaves the app (e.g., by closing or refreshing it).

#### Returns

`void`

#### Inherited from

[`IntegrationScheme`](../../../IntegrationScheme/classes/IntegrationScheme.md).[`leave`](../../../IntegrationScheme/classes/IntegrationScheme.md#leave)

***

### resourcesBroker()

> **resourcesBroker**(): [`ResourcesBroker`](../../../resources/brokers/ResourcesBroker/classes/ResourcesBroker.md)

Defined in: [src/frontend/src/integration/schemes/BasicIntegrationScheme.ts:38](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/schemes/BasicIntegrationScheme.ts#L38)

Creates a new resources broker.

#### Returns

[`ResourcesBroker`](../../../resources/brokers/ResourcesBroker/classes/ResourcesBroker.md)

#### Overrides

[`IntegrationScheme`](../../../IntegrationScheme/classes/IntegrationScheme.md).[`resourcesBroker`](../../../IntegrationScheme/classes/IntegrationScheme.md#resourcesbroker)

***

### startSession()

> **startSession**(): `Promise`\<`void`\>

Defined in: [src/frontend/src/integration/IntegrationScheme.ts:72](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/IntegrationScheme.ts#L72)

Called when the app has launched after completed integration.

#### Returns

`Promise`\<`void`\>

- A promise that can be used to perform tasks after post-initialization.

#### Inherited from

[`IntegrationScheme`](../../../IntegrationScheme/classes/IntegrationScheme.md).[`startSession`](../../../IntegrationScheme/classes/IntegrationScheme.md#startsession)

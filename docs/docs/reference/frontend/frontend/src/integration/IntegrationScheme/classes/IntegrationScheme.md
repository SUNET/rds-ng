# Abstract Class: IntegrationScheme

Defined in: [src/frontend/src/integration/IntegrationScheme.ts:18](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/IntegrationScheme.ts#L18)

Base class for integration schemes.

## Extended by

- [`BasicIntegrationScheme`](../../schemes/BasicIntegrationScheme/classes/BasicIntegrationScheme.md)
- [`HostIntegrationScheme`](../../schemes/HostIntegrationScheme/classes/HostIntegrationScheme.md)

## Constructors

### Constructor

> `protected` **new IntegrationScheme**(`comp`, `scheme`, `integrationComponent`): `IntegrationScheme`

Defined in: [src/frontend/src/integration/IntegrationScheme.ts:25](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/IntegrationScheme.ts#L25)

#### Parameters

##### comp

[`FrontendComponent`](../../../component/FrontendComponent/classes/FrontendComponent.md)

##### scheme

`string`

##### integrationComponent

[`VueComponent`](../../../../../common/web/component/WebComponent/type-aliases/VueComponent.md)

#### Returns

`IntegrationScheme`

## Properties

### \_component

> `protected` `readonly` **\_component**: [`FrontendComponent`](../../../component/FrontendComponent/classes/FrontendComponent.md)

Defined in: [src/frontend/src/integration/IntegrationScheme.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/IntegrationScheme.ts#L19)

## Accessors

### integrationComponent

#### Get Signature

> **get** **integrationComponent**(): [`VueComponent`](../../../../../common/web/component/WebComponent/type-aliases/VueComponent.md)

Defined in: [src/frontend/src/integration/IntegrationScheme.ts:101](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/IntegrationScheme.ts#L101)

The integration component used during the login process.

##### Returns

[`VueComponent`](../../../../../common/web/component/WebComponent/type-aliases/VueComponent.md)

***

### isIntegrated

#### Get Signature

> **get** **isIntegrated**(): `boolean`

Defined in: [src/frontend/src/integration/IntegrationScheme.ts:51](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/IntegrationScheme.ts#L51)

Checks whether the integration has completed.

##### Returns

`boolean`

***

### scheme

#### Get Signature

> **get** **scheme**(): `string`

Defined in: [src/frontend/src/integration/IntegrationScheme.ts:94](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/IntegrationScheme.ts#L94)

The scheme identifier.

##### Returns

`string`

## Methods

### authenticator()

> `abstract` **authenticator**(...`args`): [`Authenticator`](../../authentication/Authenticator/classes/Authenticator.md)

Defined in: [src/frontend/src/integration/IntegrationScheme.ts:36](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/IntegrationScheme.ts#L36)

Creates a new authenticator.

#### Parameters

##### args

...`any`[]

#### Returns

[`Authenticator`](../../authentication/Authenticator/classes/Authenticator.md)

***

### authorizer()

> `abstract` **authorizer**(...`args`): [`Authorizer`](../../authorization/Authorizer/classes/Authorizer.md)

Defined in: [src/frontend/src/integration/IntegrationScheme.ts:41](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/IntegrationScheme.ts#L41)

Creates a new authorizer.

#### Parameters

##### args

...`any`[]

#### Returns

[`Authorizer`](../../authorization/Authorizer/classes/Authorizer.md)

***

### endSession()

> **endSession**(): `void`

Defined in: [src/frontend/src/integration/IntegrationScheme.ts:89](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/IntegrationScheme.ts#L89)

Called when the user leaves the main view.

#### Returns

`void`

***

### enter()

> **enter**(): `void`

Defined in: [src/frontend/src/integration/IntegrationScheme.ts:60](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/IntegrationScheme.ts#L60)

Called when the user enters the app.

#### Returns

`void`

***

### leave()

> **leave**(): `void`

Defined in: [src/frontend/src/integration/IntegrationScheme.ts:65](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/IntegrationScheme.ts#L65)

Called when the user leaves the app (e.g., by closing or refreshing it).

#### Returns

`void`

***

### resourcesBroker()

> `abstract` **resourcesBroker**(...`args`): [`ResourcesBroker`](../../resources/brokers/ResourcesBroker/classes/ResourcesBroker.md)

Defined in: [src/frontend/src/integration/IntegrationScheme.ts:46](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/IntegrationScheme.ts#L46)

Creates a new resources broker.

#### Parameters

##### args

...`any`[]

#### Returns

[`ResourcesBroker`](../../resources/brokers/ResourcesBroker/classes/ResourcesBroker.md)

***

### startSession()

> **startSession**(): `Promise`\<`void`\>

Defined in: [src/frontend/src/integration/IntegrationScheme.ts:72](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/IntegrationScheme.ts#L72)

Called when the app has launched after completed integration.

#### Returns

`Promise`\<`void`\>

- A promise that can be used to perform tasks after post-initialization.

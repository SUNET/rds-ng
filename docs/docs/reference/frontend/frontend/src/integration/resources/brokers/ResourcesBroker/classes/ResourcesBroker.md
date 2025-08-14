# Abstract Class: ResourcesBroker

Defined in: [src/frontend/src/integration/resources/brokers/ResourcesBroker.ts:18](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/resources/brokers/ResourcesBroker.ts#L18)

Base resources broker.

## Extends

- [`IntegrationHandler`](../../../../IntegrationHandler/classes/IntegrationHandler.md)

## Extended by

- [`BasicResourcesBroker`](../../BasicResourcesBroker/classes/BasicResourcesBroker.md)
- [`HostResourcesBroker`](../../HostResourcesBroker/classes/HostResourcesBroker.md)

## Constructors

### Constructor

> `protected` **new ResourcesBroker**(`comp`, `hostResources`): `ResourcesBroker`

Defined in: [src/frontend/src/integration/resources/brokers/ResourcesBroker.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/resources/brokers/ResourcesBroker.ts#L23)

#### Parameters

##### comp

[`FrontendComponent`](../../../../../component/FrontendComponent/classes/FrontendComponent.md)

##### hostResources

[`HostResources`](../../../../HostTypes/interfaces/HostResources.md)

#### Returns

`ResourcesBroker`

#### Overrides

[`IntegrationHandler`](../../../../IntegrationHandler/classes/IntegrationHandler.md).[`constructor`](../../../../IntegrationHandler/classes/IntegrationHandler.md#constructor)

## Properties

### \_callbacks

> `protected` `readonly` **\_callbacks**: [`ExecutionCallbacks`](../../../../../../../common/web/utils/ExecutionCallbacks/classes/ExecutionCallbacks.md)\<[`ResourcesBrokerDoneCallback`](../type-aliases/ResourcesBrokerDoneCallback.md), [`ResourcesBrokerFailCallback`](../type-aliases/ResourcesBrokerFailCallback.md)\>

Defined in: [src/frontend/src/integration/resources/brokers/ResourcesBroker.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/resources/brokers/ResourcesBroker.ts#L21)

***

### \_component

> `protected` `readonly` **\_component**: [`FrontendComponent`](../../../../../component/FrontendComponent/classes/FrontendComponent.md)

Defined in: [src/frontend/src/integration/IntegrationHandler.ts:7](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/IntegrationHandler.ts#L7)

#### Inherited from

[`IntegrationHandler`](../../../../IntegrationHandler/classes/IntegrationHandler.md).[`_component`](../../../../IntegrationHandler/classes/IntegrationHandler.md#_component)

***

### \_hostResources

> `protected` `readonly` **\_hostResources**: [`HostResources`](../../../../HostTypes/interfaces/HostResources.md)

Defined in: [src/frontend/src/integration/resources/brokers/ResourcesBroker.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/resources/brokers/ResourcesBroker.ts#L19)

## Methods

### assign()

> `abstract` **assign**(): `void`

Defined in: [src/frontend/src/integration/resources/brokers/ResourcesBroker.ts:32](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/resources/brokers/ResourcesBroker.ts#L32)

Assigns a broker using the provided host resources.

#### Returns

`void`

***

### assignBrokerWithHostResources()

> `protected` **assignBrokerWithHostResources**(): `void`

Defined in: [src/frontend/src/integration/resources/brokers/ResourcesBroker.ts:54](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/resources/brokers/ResourcesBroker.ts#L54)

#### Returns

`void`

***

### done()

> **done**(`cb`): `ResourcesBroker`

Defined in: [src/frontend/src/integration/resources/brokers/ResourcesBroker.ts:39](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/resources/brokers/ResourcesBroker.ts#L39)

Adds a *Done* callback.

#### Parameters

##### cb

[`ResourcesBrokerDoneCallback`](../type-aliases/ResourcesBrokerDoneCallback.md)

The callback to add.

#### Returns

`ResourcesBroker`

***

### failed()

> **failed**(`cb`): `ResourcesBroker`

Defined in: [src/frontend/src/integration/resources/brokers/ResourcesBroker.ts:49](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/resources/brokers/ResourcesBroker.ts#L49)

Adds a *Fail* callback.

#### Parameters

##### cb

[`ResourcesBrokerFailCallback`](../type-aliases/ResourcesBrokerFailCallback.md)

The callback to add.

#### Returns

`ResourcesBroker`

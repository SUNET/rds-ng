# Class: BasicResourcesBroker

Defined in: [src/frontend/src/integration/resources/brokers/BasicResourcesBroker.ts:8](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/resources/brokers/BasicResourcesBroker.ts#L8)

Resources broker for basic integration.

## Extends

- [`ResourcesBroker`](../../ResourcesBroker/classes/ResourcesBroker.md)

## Constructors

### Constructor

> **new BasicResourcesBroker**(`comp`): `BasicResourcesBroker`

Defined in: [src/frontend/src/integration/resources/brokers/BasicResourcesBroker.ts:9](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/resources/brokers/BasicResourcesBroker.ts#L9)

#### Parameters

##### comp

[`FrontendComponent`](../../../../../component/FrontendComponent/classes/FrontendComponent.md)

#### Returns

`BasicResourcesBroker`

#### Overrides

[`ResourcesBroker`](../../ResourcesBroker/classes/ResourcesBroker.md).[`constructor`](../../ResourcesBroker/classes/ResourcesBroker.md#constructor)

## Properties

### \_callbacks

> `protected` `readonly` **\_callbacks**: [`ExecutionCallbacks`](../../../../../../../common/web/utils/ExecutionCallbacks/classes/ExecutionCallbacks.md)\<[`ResourcesBrokerDoneCallback`](../../ResourcesBroker/type-aliases/ResourcesBrokerDoneCallback.md), [`ResourcesBrokerFailCallback`](../../ResourcesBroker/type-aliases/ResourcesBrokerFailCallback.md)\>

Defined in: [src/frontend/src/integration/resources/brokers/ResourcesBroker.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/resources/brokers/ResourcesBroker.ts#L21)

#### Inherited from

[`ResourcesBroker`](../../ResourcesBroker/classes/ResourcesBroker.md).[`_callbacks`](../../ResourcesBroker/classes/ResourcesBroker.md#_callbacks)

***

### \_component

> `protected` `readonly` **\_component**: [`FrontendComponent`](../../../../../component/FrontendComponent/classes/FrontendComponent.md)

Defined in: [src/frontend/src/integration/IntegrationHandler.ts:7](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/IntegrationHandler.ts#L7)

#### Inherited from

[`ResourcesBroker`](../../ResourcesBroker/classes/ResourcesBroker.md).[`_component`](../../ResourcesBroker/classes/ResourcesBroker.md#_component)

***

### \_hostResources

> `protected` `readonly` **\_hostResources**: [`HostResources`](../../../../HostTypes/interfaces/HostResources.md)

Defined in: [src/frontend/src/integration/resources/brokers/ResourcesBroker.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/resources/brokers/ResourcesBroker.ts#L19)

#### Inherited from

[`ResourcesBroker`](../../ResourcesBroker/classes/ResourcesBroker.md).[`_hostResources`](../../ResourcesBroker/classes/ResourcesBroker.md#_hostresources)

## Methods

### assign()

> **assign**(): `void`

Defined in: [src/frontend/src/integration/resources/brokers/BasicResourcesBroker.ts:13](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/resources/brokers/BasicResourcesBroker.ts#L13)

Assigns a broker using the provided host resources.

#### Returns

`void`

#### Overrides

[`ResourcesBroker`](../../ResourcesBroker/classes/ResourcesBroker.md).[`assign`](../../ResourcesBroker/classes/ResourcesBroker.md#assign)

***

### assignBrokerWithHostResources()

> `protected` **assignBrokerWithHostResources**(): `void`

Defined in: [src/frontend/src/integration/resources/brokers/ResourcesBroker.ts:54](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/resources/brokers/ResourcesBroker.ts#L54)

#### Returns

`void`

#### Inherited from

[`ResourcesBroker`](../../ResourcesBroker/classes/ResourcesBroker.md).[`assignBrokerWithHostResources`](../../ResourcesBroker/classes/ResourcesBroker.md#assignbrokerwithhostresources)

***

### done()

> **done**(`cb`): [`ResourcesBroker`](../../ResourcesBroker/classes/ResourcesBroker.md)

Defined in: [src/frontend/src/integration/resources/brokers/ResourcesBroker.ts:39](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/resources/brokers/ResourcesBroker.ts#L39)

Adds a *Done* callback.

#### Parameters

##### cb

[`ResourcesBrokerDoneCallback`](../../ResourcesBroker/type-aliases/ResourcesBrokerDoneCallback.md)

The callback to add.

#### Returns

[`ResourcesBroker`](../../ResourcesBroker/classes/ResourcesBroker.md)

#### Inherited from

[`ResourcesBroker`](../../ResourcesBroker/classes/ResourcesBroker.md).[`done`](../../ResourcesBroker/classes/ResourcesBroker.md#done)

***

### failed()

> **failed**(`cb`): [`ResourcesBroker`](../../ResourcesBroker/classes/ResourcesBroker.md)

Defined in: [src/frontend/src/integration/resources/brokers/ResourcesBroker.ts:49](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/integration/resources/brokers/ResourcesBroker.ts#L49)

Adds a *Fail* callback.

#### Parameters

##### cb

[`ResourcesBrokerFailCallback`](../../ResourcesBroker/type-aliases/ResourcesBrokerFailCallback.md)

The callback to add.

#### Returns

[`ResourcesBroker`](../../ResourcesBroker/classes/ResourcesBroker.md)

#### Inherited from

[`ResourcesBroker`](../../ResourcesBroker/classes/ResourcesBroker.md).[`failed`](../../ResourcesBroker/classes/ResourcesBroker.md#failed)

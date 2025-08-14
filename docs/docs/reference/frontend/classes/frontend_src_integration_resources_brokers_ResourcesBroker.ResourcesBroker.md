---
id: "frontend_src_integration_resources_brokers_ResourcesBroker.ResourcesBroker"
title: "Class: ResourcesBroker"
sidebar_label: "ResourcesBroker"
custom_edit_url: null
---

[frontend/src/integration/resources/brokers/ResourcesBroker](../modules/frontend_src_integration_resources_brokers_ResourcesBroker.md).ResourcesBroker

Base resources broker.

## Hierarchy

- [`IntegrationHandler`](frontend_src_integration_IntegrationHandler.IntegrationHandler.md)

  ↳ **`ResourcesBroker`**

  ↳↳ [`BasicResourcesBroker`](frontend_src_integration_resources_brokers_BasicResourcesBroker.BasicResourcesBroker.md)

  ↳↳ [`HostResourcesBroker`](frontend_src_integration_resources_brokers_HostResourcesBroker.HostResourcesBroker.md)

## Constructors

### constructor

• **new ResourcesBroker**(`comp`, `hostResources`): [`ResourcesBroker`](frontend_src_integration_resources_brokers_ResourcesBroker.ResourcesBroker.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `comp` | [`FrontendComponent`](frontend_src_component_FrontendComponent.FrontendComponent.md) |
| `hostResources` | [`HostResources`](../interfaces/frontend_src_integration_HostTypes.HostResources.md) |

#### Returns

[`ResourcesBroker`](frontend_src_integration_resources_brokers_ResourcesBroker.ResourcesBroker.md)

#### Overrides

[IntegrationHandler](frontend_src_integration_IntegrationHandler.IntegrationHandler.md).[constructor](frontend_src_integration_IntegrationHandler.IntegrationHandler.md#constructor)

#### Defined in

[src/frontend/src/integration/resources/brokers/ResourcesBroker.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/resources/brokers/ResourcesBroker.ts#L23)

## Properties

### \_callbacks

• `Protected` `Readonly` **\_callbacks**: [`ExecutionCallbacks`](common_web_utils_ExecutionCallbacks.ExecutionCallbacks.md)<[`ResourcesBrokerDoneCallback`](../modules/frontend_src_integration_resources_brokers_ResourcesBroker.md#resourcesbrokerdonecallback), [`ResourcesBrokerFailCallback`](../modules/frontend_src_integration_resources_brokers_ResourcesBroker.md#resourcesbrokerfailcallback)\>

#### Defined in

[src/frontend/src/integration/resources/brokers/ResourcesBroker.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/resources/brokers/ResourcesBroker.ts#L21)

___

### \_component

• `Protected` `Readonly` **\_component**: [`FrontendComponent`](frontend_src_component_FrontendComponent.FrontendComponent.md)

#### Inherited from

[IntegrationHandler](frontend_src_integration_IntegrationHandler.IntegrationHandler.md).[_component](frontend_src_integration_IntegrationHandler.IntegrationHandler.md#_component)

#### Defined in

[src/frontend/src/integration/IntegrationHandler.ts:7](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/IntegrationHandler.ts#L7)

___

### \_hostResources

• `Protected` `Readonly` **\_hostResources**: [`HostResources`](../interfaces/frontend_src_integration_HostTypes.HostResources.md)

#### Defined in

[src/frontend/src/integration/resources/brokers/ResourcesBroker.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/resources/brokers/ResourcesBroker.ts#L19)

## Methods

### assign

▸ **assign**(): `void`

Assigns a broker using the provided host resources.

#### Returns

`void`

#### Defined in

[src/frontend/src/integration/resources/brokers/ResourcesBroker.ts:32](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/resources/brokers/ResourcesBroker.ts#L32)

___

### assignBrokerWithHostResources

▸ **assignBrokerWithHostResources**(): `void`

#### Returns

`void`

#### Defined in

[src/frontend/src/integration/resources/brokers/ResourcesBroker.ts:54](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/resources/brokers/ResourcesBroker.ts#L54)

___

### done

▸ **done**(`cb`): [`ResourcesBroker`](frontend_src_integration_resources_brokers_ResourcesBroker.ResourcesBroker.md)

Adds a *Done* callback.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `cb` | [`ResourcesBrokerDoneCallback`](../modules/frontend_src_integration_resources_brokers_ResourcesBroker.md#resourcesbrokerdonecallback) | The callback to add. |

#### Returns

[`ResourcesBroker`](frontend_src_integration_resources_brokers_ResourcesBroker.ResourcesBroker.md)

#### Defined in

[src/frontend/src/integration/resources/brokers/ResourcesBroker.ts:39](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/resources/brokers/ResourcesBroker.ts#L39)

___

### failed

▸ **failed**(`cb`): [`ResourcesBroker`](frontend_src_integration_resources_brokers_ResourcesBroker.ResourcesBroker.md)

Adds a *Fail* callback.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `cb` | [`ResourcesBrokerFailCallback`](../modules/frontend_src_integration_resources_brokers_ResourcesBroker.md#resourcesbrokerfailcallback) | The callback to add. |

#### Returns

[`ResourcesBroker`](frontend_src_integration_resources_brokers_ResourcesBroker.ResourcesBroker.md)

#### Defined in

[src/frontend/src/integration/resources/brokers/ResourcesBroker.ts:49](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/resources/brokers/ResourcesBroker.ts#L49)

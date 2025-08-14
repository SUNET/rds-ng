---
id: "frontend_src_integration_resources_brokers_BasicResourcesBroker.BasicResourcesBroker"
title: "Class: BasicResourcesBroker"
sidebar_label: "BasicResourcesBroker"
custom_edit_url: null
---

[frontend/src/integration/resources/brokers/BasicResourcesBroker](../modules/frontend_src_integration_resources_brokers_BasicResourcesBroker.md).BasicResourcesBroker

Resources broker for basic integration.

## Hierarchy

- [`ResourcesBroker`](frontend_src_integration_resources_brokers_ResourcesBroker.ResourcesBroker.md)

  ↳ **`BasicResourcesBroker`**

## Constructors

### constructor

• **new BasicResourcesBroker**(`comp`): [`BasicResourcesBroker`](frontend_src_integration_resources_brokers_BasicResourcesBroker.BasicResourcesBroker.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `comp` | [`FrontendComponent`](frontend_src_component_FrontendComponent.FrontendComponent.md) |

#### Returns

[`BasicResourcesBroker`](frontend_src_integration_resources_brokers_BasicResourcesBroker.BasicResourcesBroker.md)

#### Overrides

[ResourcesBroker](frontend_src_integration_resources_brokers_ResourcesBroker.ResourcesBroker.md).[constructor](frontend_src_integration_resources_brokers_ResourcesBroker.ResourcesBroker.md#constructor)

#### Defined in

[src/frontend/src/integration/resources/brokers/BasicResourcesBroker.ts:9](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/resources/brokers/BasicResourcesBroker.ts#L9)

## Properties

### \_callbacks

• `Protected` `Readonly` **\_callbacks**: [`ExecutionCallbacks`](common_web_utils_ExecutionCallbacks.ExecutionCallbacks.md)<[`ResourcesBrokerDoneCallback`](../modules/frontend_src_integration_resources_brokers_ResourcesBroker.md#resourcesbrokerdonecallback), [`ResourcesBrokerFailCallback`](../modules/frontend_src_integration_resources_brokers_ResourcesBroker.md#resourcesbrokerfailcallback)\>

#### Inherited from

[ResourcesBroker](frontend_src_integration_resources_brokers_ResourcesBroker.ResourcesBroker.md).[_callbacks](frontend_src_integration_resources_brokers_ResourcesBroker.ResourcesBroker.md#_callbacks)

#### Defined in

[src/frontend/src/integration/resources/brokers/ResourcesBroker.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/resources/brokers/ResourcesBroker.ts#L21)

___

### \_component

• `Protected` `Readonly` **\_component**: [`FrontendComponent`](frontend_src_component_FrontendComponent.FrontendComponent.md)

#### Inherited from

[ResourcesBroker](frontend_src_integration_resources_brokers_ResourcesBroker.ResourcesBroker.md).[_component](frontend_src_integration_resources_brokers_ResourcesBroker.ResourcesBroker.md#_component)

#### Defined in

[src/frontend/src/integration/IntegrationHandler.ts:7](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/IntegrationHandler.ts#L7)

___

### \_hostResources

• `Protected` `Readonly` **\_hostResources**: [`HostResources`](../interfaces/frontend_src_integration_HostTypes.HostResources.md)

#### Inherited from

[ResourcesBroker](frontend_src_integration_resources_brokers_ResourcesBroker.ResourcesBroker.md).[_hostResources](frontend_src_integration_resources_brokers_ResourcesBroker.ResourcesBroker.md#_hostresources)

#### Defined in

[src/frontend/src/integration/resources/brokers/ResourcesBroker.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/resources/brokers/ResourcesBroker.ts#L19)

## Methods

### assign

▸ **assign**(): `void`

Assigns a broker using the provided host resources.

#### Returns

`void`

#### Overrides

[ResourcesBroker](frontend_src_integration_resources_brokers_ResourcesBroker.ResourcesBroker.md).[assign](frontend_src_integration_resources_brokers_ResourcesBroker.ResourcesBroker.md#assign)

#### Defined in

[src/frontend/src/integration/resources/brokers/BasicResourcesBroker.ts:13](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/resources/brokers/BasicResourcesBroker.ts#L13)

___

### assignBrokerWithHostResources

▸ **assignBrokerWithHostResources**(): `void`

#### Returns

`void`

#### Inherited from

[ResourcesBroker](frontend_src_integration_resources_brokers_ResourcesBroker.ResourcesBroker.md).[assignBrokerWithHostResources](frontend_src_integration_resources_brokers_ResourcesBroker.ResourcesBroker.md#assignbrokerwithhostresources)

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

#### Inherited from

[ResourcesBroker](frontend_src_integration_resources_brokers_ResourcesBroker.ResourcesBroker.md).[done](frontend_src_integration_resources_brokers_ResourcesBroker.ResourcesBroker.md#done)

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

#### Inherited from

[ResourcesBroker](frontend_src_integration_resources_brokers_ResourcesBroker.ResourcesBroker.md).[failed](frontend_src_integration_resources_brokers_ResourcesBroker.ResourcesBroker.md#failed)

#### Defined in

[src/frontend/src/integration/resources/brokers/ResourcesBroker.ts:49](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/integration/resources/brokers/ResourcesBroker.ts#L49)

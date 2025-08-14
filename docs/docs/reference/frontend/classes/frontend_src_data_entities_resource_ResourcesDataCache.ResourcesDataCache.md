---
id: "frontend_src_data_entities_resource_ResourcesDataCache.ResourcesDataCache"
title: "Class: ResourcesDataCache"
sidebar_label: "ResourcesDataCache"
custom_edit_url: null
---

[frontend/src/data/entities/resource/ResourcesDataCache](../modules/frontend_src_data_entities_resource_ResourcesDataCache.md).ResourcesDataCache

Cache to store the data of resources.

The cache has space for a certain number of items, removing old elements when necessary.

## Constructors

### constructor

• **new ResourcesDataCache**(`capacity?`): [`ResourcesDataCache`](frontend_src_data_entities_resource_ResourcesDataCache.ResourcesDataCache.md)

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `capacity` | `number` | `100` |

#### Returns

[`ResourcesDataCache`](frontend_src_data_entities_resource_ResourcesDataCache.ResourcesDataCache.md)

#### Defined in

[src/frontend/src/data/entities/resource/ResourcesDataCache.ts:30](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/data/entities/resource/ResourcesDataCache.ts#L30)

## Properties

### \_cache

• `Private` `Readonly` **\_cache**: `ResourcesDataCacheEntry`[] = `[]`

#### Defined in

[src/frontend/src/data/entities/resource/ResourcesDataCache.ts:27](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/data/entities/resource/ResourcesDataCache.ts#L27)

___

### \_capacity

• `Private` `Readonly` **\_capacity**: `number`

#### Defined in

[src/frontend/src/data/entities/resource/ResourcesDataCache.ts:28](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/data/entities/resource/ResourcesDataCache.ts#L28)

## Methods

### bump

▸ **bump**(`resource`): `void`

Moves a resource to the end of the cache to mark it as "new."

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `resource` | [`Resource`](common_web_data_entities_resource_Resource.Resource.md) | The resource to bump. |

#### Returns

`void`

#### Defined in

[src/frontend/src/data/entities/resource/ResourcesDataCache.ts:82](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/data/entities/resource/ResourcesDataCache.ts#L82)

___

### findEntry

▸ **findEntry**(`resource`): ``null`` \| `ResourcesDataCacheEntry`

#### Parameters

| Name | Type |
| :------ | :------ |
| `resource` | [`Resource`](common_web_data_entities_resource_Resource.Resource.md) |

#### Returns

``null`` \| `ResourcesDataCacheEntry`

#### Defined in

[src/frontend/src/data/entities/resource/ResourcesDataCache.ts:91](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/data/entities/resource/ResourcesDataCache.ts#L91)

___

### getData

▸ **getData**(`resource`): `ArrayBuffer`

Gets the data stored for a given resource.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `resource` | [`Resource`](common_web_data_entities_resource_Resource.Resource.md) | The resource. |

#### Returns

`ArrayBuffer`

- The resource data.

**`Throws`**

Error - If no data exists for the resource.

#### Defined in

[src/frontend/src/data/entities/resource/ResourcesDataCache.ts:69](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/data/entities/resource/ResourcesDataCache.ts#L69)

___

### hasData

▸ **hasData**(`resource`): `boolean`

Checks if data is available for a given resource.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `resource` | [`Resource`](common_web_data_entities_resource_Resource.Resource.md) | The resource. |

#### Returns

`boolean`

#### Defined in

[src/frontend/src/data/entities/resource/ResourcesDataCache.ts:57](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/data/entities/resource/ResourcesDataCache.ts#L57)

___

### push

▸ **push**(`resource`, `data`): `void`

Add a new element to the cache.

If an entry for the resource already exists, it will simply be moved to the end of the cache. Otherwise,
a new element will be added, potentially removing old ones to stay within its capacity.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `resource` | [`Resource`](common_web_data_entities_resource_Resource.Resource.md) | The resource to add. |
| `data` | `ArrayBuffer` | The resource data. |

#### Returns

`void`

#### Defined in

[src/frontend/src/data/entities/resource/ResourcesDataCache.ts:43](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/data/entities/resource/ResourcesDataCache.ts#L43)

___

### reduce

▸ **reduce**(): `void`

#### Returns

`void`

#### Defined in

[src/frontend/src/data/entities/resource/ResourcesDataCache.ts:100](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/data/entities/resource/ResourcesDataCache.ts#L100)

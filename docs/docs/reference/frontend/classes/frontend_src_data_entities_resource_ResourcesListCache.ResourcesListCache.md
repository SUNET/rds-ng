---
id: "frontend_src_data_entities_resource_ResourcesListCache.ResourcesListCache"
title: "Class: ResourcesListCache"
sidebar_label: "ResourcesListCache"
custom_edit_url: null
---

[frontend/src/data/entities/resource/ResourcesListCache](../modules/frontend_src_data_entities_resource_ResourcesListCache.md).ResourcesListCache

Cache to store resources lists based on their root path.

This is used to store resources lists incrementally, i.d., the existing lists can be extended on demand.

## Constructors

### constructor

• **new ResourcesListCache**(): [`ResourcesListCache`](frontend_src_data_entities_resource_ResourcesListCache.ResourcesListCache.md)

#### Returns

[`ResourcesListCache`](frontend_src_data_entities_resource_ResourcesListCache.ResourcesListCache.md)

## Properties

### \_cacheEntries

• `Private` **\_cacheEntries**: `Record`<`string`, `ResourcesListCacheEntry`\> = `{}`

#### Defined in

[src/frontend/src/data/entities/resource/ResourcesListCache.ts:152](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/data/entities/resource/ResourcesListCache.ts#L152)

## Methods

### clear

▸ **clear**(): `void`

Removes all cached lists.

#### Returns

`void`

#### Defined in

[src/frontend/src/data/entities/resource/ResourcesListCache.ts:169](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/data/entities/resource/ResourcesListCache.ts#L169)

___

### root

▸ **root**(`root`): `ResourcesListCacheEntry`

Retrieves the cache for a specific root, creating one if necessary.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `root` | `string` | The root path. |

#### Returns

`ResourcesListCacheEntry`

#### Defined in

[src/frontend/src/data/entities/resource/ResourcesListCache.ts:159](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/data/entities/resource/ResourcesListCache.ts#L159)

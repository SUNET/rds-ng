# Class: ResourcesListCache

Defined in: [src/frontend/src/data/entities/resource/ResourcesListCache.ts:151](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/data/entities/resource/ResourcesListCache.ts#L151)

Cache to store resources lists based on their root path.

This is used to store resources lists incrementally, i.d., the existing lists can be extended on demand.

## Constructors

### Constructor

> **new ResourcesListCache**(): `ResourcesListCache`

#### Returns

`ResourcesListCache`

## Methods

### clear()

> **clear**(): `void`

Defined in: [src/frontend/src/data/entities/resource/ResourcesListCache.ts:169](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/data/entities/resource/ResourcesListCache.ts#L169)

Removes all cached lists.

#### Returns

`void`

***

### root()

> **root**(`root`): `ResourcesListCacheEntry`

Defined in: [src/frontend/src/data/entities/resource/ResourcesListCache.ts:159](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/data/entities/resource/ResourcesListCache.ts#L159)

Retrieves the cache for a specific root, creating one if necessary.

#### Parameters

##### root

`string`

The root path.

#### Returns

`ResourcesListCacheEntry`

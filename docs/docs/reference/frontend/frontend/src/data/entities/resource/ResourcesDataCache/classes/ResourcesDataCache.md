# Class: ResourcesDataCache

Defined in: [src/frontend/src/data/entities/resource/ResourcesDataCache.ts:26](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/data/entities/resource/ResourcesDataCache.ts#L26)

Cache to store the data of resources.

The cache has space for a certain number of items, removing old elements when necessary.

## Constructors

### Constructor

> **new ResourcesDataCache**(`capacity`): `ResourcesDataCache`

Defined in: [src/frontend/src/data/entities/resource/ResourcesDataCache.ts:30](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/data/entities/resource/ResourcesDataCache.ts#L30)

#### Parameters

##### capacity

`number` = `100`

#### Returns

`ResourcesDataCache`

## Methods

### bump()

> **bump**(`resource`): `void`

Defined in: [src/frontend/src/data/entities/resource/ResourcesDataCache.ts:82](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/data/entities/resource/ResourcesDataCache.ts#L82)

Moves a resource to the end of the cache to mark it as "new."

#### Parameters

##### resource

[`Resource`](../../../../../../../common/web/data/entities/resource/Resource/classes/Resource.md)

The resource to bump.

#### Returns

`void`

***

### getData()

> **getData**(`resource`): `ArrayBuffer`

Defined in: [src/frontend/src/data/entities/resource/ResourcesDataCache.ts:69](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/data/entities/resource/ResourcesDataCache.ts#L69)

Gets the data stored for a given resource.

#### Parameters

##### resource

[`Resource`](../../../../../../../common/web/data/entities/resource/Resource/classes/Resource.md)

The resource.

#### Returns

`ArrayBuffer`

- The resource data.

#### Throws

Error - If no data exists for the resource.

***

### hasData()

> **hasData**(`resource`): `boolean`

Defined in: [src/frontend/src/data/entities/resource/ResourcesDataCache.ts:57](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/data/entities/resource/ResourcesDataCache.ts#L57)

Checks if data is available for a given resource.

#### Parameters

##### resource

[`Resource`](../../../../../../../common/web/data/entities/resource/Resource/classes/Resource.md)

The resource.

#### Returns

`boolean`

***

### push()

> **push**(`resource`, `data`): `void`

Defined in: [src/frontend/src/data/entities/resource/ResourcesDataCache.ts:43](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/data/entities/resource/ResourcesDataCache.ts#L43)

Add a new element to the cache.

If an entry for the resource already exists, it will simply be moved to the end of the cache. Otherwise,
a new element will be added, potentially removing old ones to stay within its capacity.

#### Parameters

##### resource

[`Resource`](../../../../../../../common/web/data/entities/resource/Resource/classes/Resource.md)

The resource to add.

##### data

`ArrayBuffer`

The resource data.

#### Returns

`void`

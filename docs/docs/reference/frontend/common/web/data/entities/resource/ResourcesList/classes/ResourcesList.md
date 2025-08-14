# Class: ResourcesList

Defined in: [src/common/web/data/entities/resource/ResourcesList.ts:24](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/resource/ResourcesList.ts#L24)

A recursive list of resources.

Resources are always given in absolute form.

## Param

The current resource path.

## Param

A list of all folders.

## Param

A list of all files.

## Constructors

### Constructor

> **new ResourcesList**(`resource`, `folders`, `files`): `ResourcesList`

Defined in: [src/common/web/data/entities/resource/ResourcesList.ts:34](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/resource/ResourcesList.ts#L34)

#### Parameters

##### resource

[`Resource`](../../Resource/classes/Resource.md)

##### folders

[`ResourceFolders`](../type-aliases/ResourceFolders.md) = `[]`

##### files

[`ResourceFiles`](../type-aliases/ResourceFiles.md) = `[]`

#### Returns

`ResourcesList`

## Properties

### files

> `readonly` **files**: [`ResourceFiles`](../type-aliases/ResourceFiles.md)

Defined in: [src/common/web/data/entities/resource/ResourcesList.ts:32](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/resource/ResourcesList.ts#L32)

***

### folders

> `readonly` **folders**: [`ResourceFolders`](../type-aliases/ResourceFolders.md)

Defined in: [src/common/web/data/entities/resource/ResourcesList.ts:29](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/resource/ResourcesList.ts#L29)

***

### resource

> `readonly` **resource**: [`Resource`](../../Resource/classes/Resource.md)

Defined in: [src/common/web/data/entities/resource/ResourcesList.ts:25](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/resource/ResourcesList.ts#L25)

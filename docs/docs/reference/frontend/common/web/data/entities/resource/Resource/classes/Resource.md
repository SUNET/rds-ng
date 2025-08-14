# Class: Resource

Defined in: [src/common/web/data/entities/resource/Resource.ts:18](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/resource/Resource.ts#L18)

A single file or folder resource.

## Param

The complete name (path) of the resource.

## Param

The name (w/o path) of the resource.

## Param

The type of the resource (folder or file).

## Param

The size of the resource; for folders, this is the size of all its contents.

## Param

The MIME type of the resource.

## Constructors

### Constructor

> **new Resource**(`filename`, `basename`, `type`, `size`, `mimeType`): `Resource`

Defined in: [src/common/web/data/entities/resource/Resource.ts:26](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/resource/Resource.ts#L26)

#### Parameters

##### filename

`string`

##### basename

`string`

##### type

[`ResourceType`](../enumerations/ResourceType.md)

##### size

`number` = `0`

##### mimeType

`string` = `""`

#### Returns

`Resource`

## Properties

### basename

> `readonly` **basename**: `string`

Defined in: [src/common/web/data/entities/resource/Resource.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/resource/Resource.ts#L20)

***

### filename

> `readonly` **filename**: `string`

Defined in: [src/common/web/data/entities/resource/Resource.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/resource/Resource.ts#L19)

***

### mime\_type

> `readonly` **mime\_type**: `string`

Defined in: [src/common/web/data/entities/resource/Resource.ts:24](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/resource/Resource.ts#L24)

***

### size

> **size**: `number`

Defined in: [src/common/web/data/entities/resource/Resource.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/resource/Resource.ts#L23)

***

### type

> `readonly` **type**: [`ResourceType`](../enumerations/ResourceType.md)

Defined in: [src/common/web/data/entities/resource/Resource.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/resource/Resource.ts#L21)

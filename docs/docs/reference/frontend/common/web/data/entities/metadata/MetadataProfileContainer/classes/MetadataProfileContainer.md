# Class: MetadataProfileContainer

Defined in: [src/common/web/data/entities/metadata/MetadataProfileContainer.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/metadata/MetadataProfileContainer.ts#L23)

A container that holds a metadata profile along with various descriptive information.

## Param

The overall category of the profile.

## Param

The role of the profile within its category.

## Param

The actual profile data.

## Constructors

### Constructor

> **new MetadataProfileContainer**(`category`, `role`, `profile`): `MetadataProfileContainer`

Defined in: [src/common/web/data/entities/metadata/MetadataProfileContainer.ts:31](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/metadata/MetadataProfileContainer.ts#L31)

#### Parameters

##### category

`string`

##### role

[`MetadataProfileContainerRole`](../enumerations/MetadataProfileContainerRole.md)

##### profile

[`PropertyProfile`](../../../../../ui/components/propertyeditor/PropertyProfile/classes/PropertyProfile.md)

#### Returns

`MetadataProfileContainer`

## Properties

### category

> `readonly` **category**: `string`

Defined in: [src/common/web/data/entities/metadata/MetadataProfileContainer.ts:24](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/metadata/MetadataProfileContainer.ts#L24)

***

### profile

> `readonly` **profile**: [`PropertyProfile`](../../../../../ui/components/propertyeditor/PropertyProfile/classes/PropertyProfile.md)

Defined in: [src/common/web/data/entities/metadata/MetadataProfileContainer.ts:29](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/metadata/MetadataProfileContainer.ts#L29)

***

### role

> `readonly` **role**: [`MetadataProfileContainerRole`](../enumerations/MetadataProfileContainerRole.md)

Defined in: [src/common/web/data/entities/metadata/MetadataProfileContainer.ts:25](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/metadata/MetadataProfileContainer.ts#L25)

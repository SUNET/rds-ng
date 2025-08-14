# Class: ProjectFeatures

Defined in: [src/common/web/data/entities/project/features/ProjectFeatures.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/features/ProjectFeatures.ts#L17)

Superordinate data for all **Project** features.

## Param

The metadata project feature.

## Param

The resources metadata project feature.

## Param

The data management plan feature.

## Param

Project-wide shared metadata objects.

## Constructors

### Constructor

> **new ProjectFeatures**(`projectMetadata?`, `resourceMetadata?`, `dmp?`, `sharedPropertyObjects?`): `ProjectFeatures`

Defined in: [src/common/web/data/entities/project/features/ProjectFeatures.ts:32](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/features/ProjectFeatures.ts#L32)

#### Parameters

##### projectMetadata?

[`ProjectMetadataFeature`](../../ProjectMetadataFeature/classes/ProjectMetadataFeature.md)

##### resourceMetadata?

[`ResourcesMetadataFeature`](../../ResourcesMetadataFeature/classes/ResourcesMetadataFeature.md)

##### dmp?

[`DataManagementPlanFeature`](../../DataManagementPlanFeature/classes/DataManagementPlanFeature.md)

##### sharedPropertyObjects?

[`MetadataObjects`](../../../../metadata/Types/type-aliases/MetadataObjects.md)

#### Returns

`ProjectFeatures`

## Properties

### dmp

> `readonly` **dmp**: [`DataManagementPlanFeature`](../../DataManagementPlanFeature/classes/DataManagementPlanFeature.md)

Defined in: [src/common/web/data/entities/project/features/ProjectFeatures.ts:26](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/features/ProjectFeatures.ts#L26)

***

### project\_metadata

> `readonly` **project\_metadata**: [`ProjectMetadataFeature`](../../ProjectMetadataFeature/classes/ProjectMetadataFeature.md)

Defined in: [src/common/web/data/entities/project/features/ProjectFeatures.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/features/ProjectFeatures.ts#L20)

***

### resources\_metadata

> `readonly` **resources\_metadata**: [`ResourcesMetadataFeature`](../../ResourcesMetadataFeature/classes/ResourcesMetadataFeature.md)

Defined in: [src/common/web/data/entities/project/features/ProjectFeatures.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/features/ProjectFeatures.ts#L23)

***

### shared\_objects

> `readonly` **shared\_objects**: [`MetadataObjects`](../../../../metadata/Types/type-aliases/MetadataObjects.md)

Defined in: [src/common/web/data/entities/project/features/ProjectFeatures.ts:30](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/features/ProjectFeatures.ts#L30)

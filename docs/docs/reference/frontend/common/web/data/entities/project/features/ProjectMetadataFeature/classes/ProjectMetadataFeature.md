# Class: ProjectMetadataFeature

Defined in: [src/common/web/data/entities/project/features/ProjectMetadataFeature.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/features/ProjectMetadataFeature.ts#L17)

Data class for the metadata project feature.

## Extends

- [`ProjectFeature`](../../ProjectFeature/classes/ProjectFeature.md)

## Constructors

### Constructor

> **new ProjectMetadataFeature**(`metadata`, `enabledProfiles`): `ProjectMetadataFeature`

Defined in: [src/common/web/data/entities/project/features/ProjectMetadataFeature.ts:24](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/features/ProjectMetadataFeature.ts#L24)

#### Parameters

##### metadata

[`ProjectMetadata`](../type-aliases/ProjectMetadata.md) = `[]`

##### enabledProfiles

[`ProfileID`](../../../../../../ui/components/propertyeditor/PropertyProfile/type-aliases/ProfileID.md)[] = `[]`

#### Returns

`ProjectMetadataFeature`

#### Overrides

[`ProjectFeature`](../../ProjectFeature/classes/ProjectFeature.md).[`constructor`](../../ProjectFeature/classes/ProjectFeature.md#constructor)

## Properties

### enabled\_metadata\_profiles

> `readonly` **enabled\_metadata\_profiles**: [`ProfileID`](../../../../../../ui/components/propertyeditor/PropertyProfile/type-aliases/ProfileID.md)[] = `[]`

Defined in: [src/common/web/data/entities/project/features/ProjectFeature.ts:16](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/features/ProjectFeature.ts#L16)

#### Inherited from

[`ProjectFeature`](../../ProjectFeature/classes/ProjectFeature.md).[`enabled_metadata_profiles`](../../ProjectFeature/classes/ProjectFeature.md#enabled_metadata_profiles)

***

### metadata

> `readonly` **metadata**: [`ProjectMetadata`](../type-aliases/ProjectMetadata.md)

Defined in: [src/common/web/data/entities/project/features/ProjectMetadataFeature.ts:22](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/features/ProjectMetadataFeature.ts#L22)

***

### FeatureID

> `readonly` `static` **FeatureID**: `string` = `"project_metadata"`

Defined in: [src/common/web/data/entities/project/features/ProjectMetadataFeature.ts:18](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/features/ProjectMetadataFeature.ts#L18)

## Accessors

### featureID

#### Get Signature

> **get** **featureID**(): `string`

Defined in: [src/common/web/data/entities/project/features/ProjectMetadataFeature.ts:30](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/features/ProjectMetadataFeature.ts#L30)

The ID of this feature.

##### Returns

`string`

#### Overrides

[`ProjectFeature`](../../ProjectFeature/classes/ProjectFeature.md).[`featureID`](../../ProjectFeature/classes/ProjectFeature.md#featureid)

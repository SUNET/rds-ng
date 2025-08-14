# Class: ResourcesMetadataFeature

Defined in: [src/common/web/data/entities/project/features/ResourcesMetadataFeature.ts:32](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/features/ResourcesMetadataFeature.ts#L32)

Data class for the files project feature.

## Extends

- [`ProjectFeature`](../../ProjectFeature/classes/ProjectFeature.md)

## Constructors

### Constructor

> **new ResourcesMetadataFeature**(`resourcesMetadata`, `enabledProfiles`): `ResourcesMetadataFeature`

Defined in: [src/common/web/data/entities/project/features/ResourcesMetadataFeature.ts:41](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/features/ResourcesMetadataFeature.ts#L41)

#### Parameters

##### resourcesMetadata

[`ResourcesMetadata`](ResourcesMetadata.md) = `{}`

##### enabledProfiles

[`ProfileID`](../../../../../../ui/components/propertyeditor/PropertyProfile/type-aliases/ProfileID.md)[] = `[]`

#### Returns

`ResourcesMetadataFeature`

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

> `readonly` **metadata**: [`ResourcesMetadata`](ResourcesMetadata.md)

Defined in: [src/common/web/data/entities/project/features/ResourcesMetadataFeature.ts:39](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/features/ResourcesMetadataFeature.ts#L39)

***

### FeatureID

> `readonly` `static` **FeatureID**: `string` = `"resources_metadata"`

Defined in: [src/common/web/data/entities/project/features/ResourcesMetadataFeature.ts:33](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/features/ResourcesMetadataFeature.ts#L33)

## Accessors

### featureID

#### Get Signature

> **get** **featureID**(): `string`

Defined in: [src/common/web/data/entities/project/features/ResourcesMetadataFeature.ts:47](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/features/ResourcesMetadataFeature.ts#L47)

The ID of this feature.

##### Returns

`string`

#### Overrides

[`ProjectFeature`](../../ProjectFeature/classes/ProjectFeature.md).[`featureID`](../../ProjectFeature/classes/ProjectFeature.md#featureid)

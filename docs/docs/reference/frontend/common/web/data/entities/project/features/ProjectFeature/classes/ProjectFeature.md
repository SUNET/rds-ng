# Abstract Class: ProjectFeature

Defined in: [src/common/web/data/entities/project/features/ProjectFeature.ts:13](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/features/ProjectFeature.ts#L13)

Base data class for a project feature.

## Extended by

- [`DataManagementPlanFeature`](../../DataManagementPlanFeature/classes/DataManagementPlanFeature.md)
- [`ProjectMetadataFeature`](../../ProjectMetadataFeature/classes/ProjectMetadataFeature.md)
- [`ResourcesMetadataFeature`](../../ResourcesMetadataFeature/classes/ResourcesMetadataFeature.md)

## Constructors

### Constructor

> **new ProjectFeature**(`enabledProfiles`): `ProjectFeature`

Defined in: [src/common/web/data/entities/project/features/ProjectFeature.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/features/ProjectFeature.ts#L23)

#### Parameters

##### enabledProfiles

[`ProfileID`](../../../../../../ui/components/propertyeditor/PropertyProfile/type-aliases/ProfileID.md)[] = `[]`

#### Returns

`ProjectFeature`

## Properties

### enabled\_metadata\_profiles

> `readonly` **enabled\_metadata\_profiles**: [`ProfileID`](../../../../../../ui/components/propertyeditor/PropertyProfile/type-aliases/ProfileID.md)[] = `[]`

Defined in: [src/common/web/data/entities/project/features/ProjectFeature.ts:16](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/features/ProjectFeature.ts#L16)

## Accessors

### featureID

#### Get Signature

> **get** `abstract` **featureID**(): `string`

Defined in: [src/common/web/data/entities/project/features/ProjectFeature.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/features/ProjectFeature.ts#L21)

The ID of this feature.

##### Returns

`string`

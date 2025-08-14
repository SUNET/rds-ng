# Class: DataManagementPlanFeature

Defined in: [src/common/web/data/entities/project/features/DataManagementPlanFeature.ts:18](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/features/DataManagementPlanFeature.ts#L18)

Data class for the data management plan project feature.

## Extends

- [`ProjectFeature`](../../ProjectFeature/classes/ProjectFeature.md)

## Constructors

### Constructor

> **new DataManagementPlanFeature**(`plan`, `enabledProfiles`): `DataManagementPlanFeature`

Defined in: [src/common/web/data/entities/project/features/DataManagementPlanFeature.ts:25](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/features/DataManagementPlanFeature.ts#L25)

#### Parameters

##### plan

[`DataManagementPlan`](../type-aliases/DataManagementPlan.md) = `[]`

##### enabledProfiles

[`ProfileID`](../../../../../../ui/components/propertyeditor/PropertyProfile/type-aliases/ProfileID.md)[] = `[]`

#### Returns

`DataManagementPlanFeature`

#### Overrides

[`ProjectFeature`](../../ProjectFeature/classes/ProjectFeature.md).[`constructor`](../../ProjectFeature/classes/ProjectFeature.md#constructor)

## Properties

### enabled\_metadata\_profiles

> `readonly` **enabled\_metadata\_profiles**: [`ProfileID`](../../../../../../ui/components/propertyeditor/PropertyProfile/type-aliases/ProfileID.md)[] = `[]`

Defined in: [src/common/web/data/entities/project/features/ProjectFeature.ts:16](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/features/ProjectFeature.ts#L16)

#### Inherited from

[`ProjectFeature`](../../ProjectFeature/classes/ProjectFeature.md).[`enabled_metadata_profiles`](../../ProjectFeature/classes/ProjectFeature.md#enabled_metadata_profiles)

***

### plan

> `readonly` **plan**: [`DataManagementPlan`](../type-aliases/DataManagementPlan.md)

Defined in: [src/common/web/data/entities/project/features/DataManagementPlanFeature.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/features/DataManagementPlanFeature.ts#L23)

***

### FeatureID

> `readonly` `static` **FeatureID**: `string` = `"dmp"`

Defined in: [src/common/web/data/entities/project/features/DataManagementPlanFeature.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/features/DataManagementPlanFeature.ts#L19)

## Accessors

### featureID

#### Get Signature

> **get** **featureID**(): `string`

Defined in: [src/common/web/data/entities/project/features/DataManagementPlanFeature.ts:31](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/features/DataManagementPlanFeature.ts#L31)

The ID of this feature.

##### Returns

`string`

#### Overrides

[`ProjectFeature`](../../ProjectFeature/classes/ProjectFeature.md).[`featureID`](../../ProjectFeature/classes/ProjectFeature.md#featureid)

# Function: isContainerSelected()

> **isContainerSelected**(`container`, `enabledProfiles`): `boolean`

Defined in: [src/common/web/data/entities/metadata/MetadataProfileContainerUtils.ts:51](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/metadata/MetadataProfileContainerUtils.ts#L51)

Checks whether a profile (container) is selected - either since it is a default one or the user has enabled it.

## Parameters

### container

[`MetadataProfileContainer`](../../MetadataProfileContainer/classes/MetadataProfileContainer.md)

The container to check.

### enabledProfiles

[`ProfileID`](../../../../../ui/components/propertyeditor/PropertyProfile/type-aliases/ProfileID.md)[]

All user-enabled profiles.

## Returns

`boolean`

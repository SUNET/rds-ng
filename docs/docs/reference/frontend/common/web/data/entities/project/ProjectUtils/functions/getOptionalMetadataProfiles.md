# Function: getOptionalMetadataProfiles()

> **getOptionalMetadataProfiles**(`project`, `userSettings`, `connectors`, `profiles`, `featureID`): [`MetadataProfileContainerList`](../../../metadata/MetadataProfileContainer/type-aliases/MetadataProfileContainerList.md)

Defined in: [src/common/web/data/entities/project/ProjectUtils.ts:49](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/project/ProjectUtils.ts#L49)

Gets all optional profiles for a specific feature of a project.

## Parameters

### project

[`Project`](../../Project/classes/Project.md)

The project.

### userSettings

[`UserSettings`](../../../user/UserSettings/classes/UserSettings.md)

The user settings.

### connectors

[`Connector`](../../../connector/Connector/classes/Connector.md)[]

A list of all known connectors.

### profiles

[`MetadataProfileContainerList`](../../../metadata/MetadataProfileContainer/type-aliases/MetadataProfileContainerList.md)

A list of all metadata profiles.

### featureID

`string`

The project feature ID.

## Returns

[`MetadataProfileContainerList`](../../../metadata/MetadataProfileContainer/type-aliases/MetadataProfileContainerList.md)

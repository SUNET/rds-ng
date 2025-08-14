# Function: filterContainers()

> **filterContainers**(`containers`, `category`, `roles`): [`MetadataProfileContainerList`](../../MetadataProfileContainer/type-aliases/MetadataProfileContainerList.md)

Defined in: [src/common/web/data/entities/metadata/MetadataProfileContainerUtils.ts:37](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/metadata/MetadataProfileContainerUtils.ts#L37)

Gets all containers from a list matching the specified category and role.

## Parameters

### containers

[`MetadataProfileContainerList`](../../MetadataProfileContainer/type-aliases/MetadataProfileContainerList.md)

The list of containers.

### category

`string`

The category to match.

### roles

[`MetadataProfileContainerRole`](../../MetadataProfileContainer/enumerations/MetadataProfileContainerRole.md)[]

The roles to match.

## Returns

[`MetadataProfileContainerList`](../../MetadataProfileContainer/type-aliases/MetadataProfileContainerList.md)

- List of all matching containers.

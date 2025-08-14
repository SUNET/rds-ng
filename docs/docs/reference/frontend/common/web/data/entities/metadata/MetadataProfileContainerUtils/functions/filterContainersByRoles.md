# Function: filterContainersByRoles()

> **filterContainersByRoles**(`containers`, `roles`): [`MetadataProfileContainerList`](../../MetadataProfileContainer/type-aliases/MetadataProfileContainerList.md)

Defined in: [src/common/web/data/entities/metadata/MetadataProfileContainerUtils.ts:24](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/metadata/MetadataProfileContainerUtils.ts#L24)

Gets all containers from a list matching the specified role.

## Parameters

### containers

[`MetadataProfileContainerList`](../../MetadataProfileContainer/type-aliases/MetadataProfileContainerList.md)

The list of containers.

### roles

[`MetadataProfileContainerRole`](../../MetadataProfileContainer/enumerations/MetadataProfileContainerRole.md)[]

The roles to match.

## Returns

[`MetadataProfileContainerList`](../../MetadataProfileContainer/type-aliases/MetadataProfileContainerList.md)

- List of all matching containers.

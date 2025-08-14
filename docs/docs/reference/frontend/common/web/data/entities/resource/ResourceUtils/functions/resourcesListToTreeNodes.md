# Function: resourcesListToTreeNodes()

> **resourcesListToTreeNodes**(`resources`, `simpleData`, `includeFiles`): `TreeNode`[]

Defined in: [src/common/web/data/entities/resource/ResourceUtils.ts:15](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/resource/ResourceUtils.ts#L15)

Transforms a `ResourcesList` into a Vue *TreeNode*.

## Parameters

### resources

[`ResourcesList`](../../ResourcesList/classes/ResourcesList.md)

The resources list to transform.

### simpleData

`boolean` = `false`

Whether to use simple data.

### includeFiles

`boolean` = `true`

Whether to also include files.

## Returns

`TreeNode`[]

- The tree nodes list.

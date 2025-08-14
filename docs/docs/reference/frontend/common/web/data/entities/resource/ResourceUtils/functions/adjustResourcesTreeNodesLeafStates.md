# Function: adjustResourcesTreeNodesLeafStates()

> **adjustResourcesTreeNodesLeafStates**(`nodes`, `resources`, `predicate`, `includeFiles`): `TreeNode`[]

Defined in: [src/common/web/data/entities/resource/ResourceUtils.ts:106](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/data/entities/resource/ResourceUtils.ts#L106)

Adjust the `leaf` states of all children in the tree nodes, depending on their presence in the resources list and a predicate.

## Parameters

### nodes

`TreeNode`[]

The tree nodes to adjust.

### resources

[`ResourcesList`](../../ResourcesList/classes/ResourcesList.md)

The underlying resources list.

### predicate

(`path`) => `boolean`

A decider function whether to include a path.

### includeFiles

`boolean` = `true`

Whether to also take files into account.

## Returns

`TreeNode`[]

---
id: "common_web_data_entities_resource_ResourceUtils"
title: "Module: common/web/data/entities/resource/ResourceUtils"
sidebar_label: "common/web/data/entities/resource/ResourceUtils"
sidebar_position: 0
custom_edit_url: null
---

## Functions

### adjustResourcesTreeNodesLeafStates

▸ **adjustResourcesTreeNodesLeafStates**(`nodes`, `resources`, `predicate`, `includeFiles?`): `TreeNode`[]

Adjust the `leaf` states of all children in the tree nodes, depending on their presence in the resources list and a predicate.

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `nodes` | `TreeNode`[] | `undefined` | The tree nodes to adjust. |
| `resources` | [`ResourcesList`](../classes/common_web_data_entities_resource_ResourcesList.ResourcesList.md) | `undefined` | The underlying resources list. |
| `predicate` | (`path`: `string`) => `boolean` | `undefined` | A decider function whether to include a path. |
| `includeFiles` | `boolean` | `true` | Whether to also take files into account. |

#### Returns

`TreeNode`[]

#### Defined in

[src/common/web/data/entities/resource/ResourceUtils.ts:106](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/resource/ResourceUtils.ts#L106)

___

### filterResourcesTreeNodes

▸ **filterResourcesTreeNodes**(`nodes`, `keys`): `TreeNode`[]

Filters a list of resources tree nodes according to the provided keys.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `nodes` | `TreeNode`[] | The nodes to filter. |
| `keys` | `string`[] | The keys to keep. |

#### Returns

`TreeNode`[]

- A flat list of all matching nodes.

#### Defined in

[src/common/web/data/entities/resource/ResourceUtils.ts:79](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/resource/ResourceUtils.ts#L79)

___

### flattenResourcesTreeNodes

▸ **flattenResourcesTreeNodes**(`nodes`): `string`[]

Flattens resources tree nodes into a single, flat array.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `nodes` | `TreeNode`[] | The nodes to flatten. |

#### Returns

`string`[]

#### Defined in

[src/common/web/data/entities/resource/ResourceUtils.ts:55](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/resource/ResourceUtils.ts#L55)

___

### resourcesListContainsPath

▸ **resourcesListContainsPath**(`resources`, `path`): `boolean`

Checks if a given path exists in the resources list.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `resources` | [`ResourcesList`](../classes/common_web_data_entities_resource_ResourcesList.ResourcesList.md) | The resources list to check. |
| `path` | `string` | The path to search for. |

#### Returns

`boolean`

#### Defined in

[src/common/web/data/entities/resource/ResourceUtils.ts:160](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/resource/ResourceUtils.ts#L160)

___

### resourcesListFindPath

▸ **resourcesListFindPath**(`resources`, `path`): [`ResourcesList`](../classes/common_web_data_entities_resource_ResourcesList.ResourcesList.md) \| `undefined`

Search for a path within a resources list.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `resources` | [`ResourcesList`](../classes/common_web_data_entities_resource_ResourcesList.ResourcesList.md) | The resources list to search in. |
| `path` | `string` | The path to search for. |

#### Returns

[`ResourcesList`](../classes/common_web_data_entities_resource_ResourcesList.ResourcesList.md) \| `undefined`

- The found list or **undefined** otherwise.

#### Defined in

[src/common/web/data/entities/resource/ResourceUtils.ts:139](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/resource/ResourceUtils.ts#L139)

___

### resourcesListToTreeNodes

▸ **resourcesListToTreeNodes**(`resources`, `simpleData?`, `includeFiles?`): `TreeNode`[]

Transforms a `ResourcesList` into a Vue *TreeNode*.

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `resources` | [`ResourcesList`](../classes/common_web_data_entities_resource_ResourcesList.ResourcesList.md) | `undefined` | The resources list to transform. |
| `simpleData` | `boolean` | `false` | Whether to use simple data. |
| `includeFiles` | `boolean` | `true` | Whether to also include files. |

#### Returns

`TreeNode`[]

- The tree nodes list.

#### Defined in

[src/common/web/data/entities/resource/ResourceUtils.ts:15](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/resource/ResourceUtils.ts#L15)

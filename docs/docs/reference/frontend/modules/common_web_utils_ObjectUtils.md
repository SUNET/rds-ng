---
id: "common_web_utils_ObjectUtils"
title: "Module: common/web/utils/ObjectUtils"
sidebar_label: "common/web/utils/ObjectUtils"
sidebar_position: 0
custom_edit_url: null
---

## Functions

### deepClone

▸ **deepClone**<`ObjType`\>(`source?`, `defaultValue?`): `ObjType`

Deep-clones an object.

#### Type parameters

| Name | Type |
| :------ | :------ |
| `ObjType` | `object` |

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `source?` | `CloneObjectType` | The source object; if this is undefined, the default value is used. |
| `defaultValue?` | `CloneObjectType` | The default value if the source is undefined. |

#### Returns

`ObjType`

#### Defined in

[src/common/web/utils/ObjectUtils.ts:43](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/ObjectUtils.ts#L43)

___

### deepMerge

▸ **deepMerge**<`ObjType`\>(`target`, `...sources`): `ObjType`

Deep-merge two objects.

#### Type parameters

| Name | Type |
| :------ | :------ |
| `ObjType` | `object` |

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `target` | `CloneObjectType` | The target object. |
| `...sources` | `CloneObjectType`[] | The source objects to merge into the target. |

#### Returns

`ObjType`

#### Defined in

[src/common/web/utils/ObjectUtils.ts:15](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/ObjectUtils.ts#L15)

___

### intersectObjects

▸ **intersectObjects**<`ObjType`\>(`obj1`, `obj2`): `ObjType`

Intersects two objects, creating a new one containing only values shared by both objects.

#### Type parameters

| Name | Type |
| :------ | :------ |
| `ObjType` | extends `Record`<`any`, `any`\> = `object` |

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `obj1` | `ObjType` | The first object. |
| `obj2` | `ObjType` | The second object. |

#### Returns

`ObjType`

- The intersection object.

#### Defined in

[src/common/web/utils/ObjectUtils.ts:62](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/ObjectUtils.ts#L62)

___

### shortenDataStrings

▸ **shortenDataStrings**(`obj`): `any`

Shortens data strings in an object for better display.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `obj` | `any` | The object to clean up. |

#### Returns

`any`

#### Defined in

[src/common/web/utils/ObjectUtils.ts:91](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/ObjectUtils.ts#L91)

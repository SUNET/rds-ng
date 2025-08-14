---
id: "common_web_data_entities_resource_Resource.Resource"
title: "Class: Resource"
sidebar_label: "Resource"
custom_edit_url: null
---

[common/web/data/entities/resource/Resource](../modules/common_web_data_entities_resource_Resource.md).Resource

A single file or folder resource.

**`Param`**

The complete name (path) of the resource.

**`Param`**

The name (w/o path) of the resource.

**`Param`**

The type of the resource (folder or file).

**`Param`**

The size of the resource; for folders, this is the size of all its contents.

**`Param`**

The MIME type of the resource.

## Constructors

### constructor

• **new Resource**(`filename`, `basename`, `type`, `size?`, `mimeType?`): [`Resource`](common_web_data_entities_resource_Resource.Resource.md)

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `filename` | `string` | `undefined` |
| `basename` | `string` | `undefined` |
| `type` | [`ResourceType`](../enums/common_web_data_entities_resource_Resource.ResourceType.md) | `undefined` |
| `size` | `number` | `0` |
| `mimeType` | `string` | `""` |

#### Returns

[`Resource`](common_web_data_entities_resource_Resource.Resource.md)

#### Defined in

[src/common/web/data/entities/resource/Resource.ts:26](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/resource/Resource.ts#L26)

## Properties

### basename

• `Readonly` **basename**: `string`

#### Defined in

[src/common/web/data/entities/resource/Resource.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/resource/Resource.ts#L20)

___

### filename

• `Readonly` **filename**: `string`

#### Defined in

[src/common/web/data/entities/resource/Resource.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/resource/Resource.ts#L19)

___

### mime\_type

• `Readonly` **mime\_type**: `string`

#### Defined in

[src/common/web/data/entities/resource/Resource.ts:24](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/resource/Resource.ts#L24)

___

### size

• **size**: `number`

#### Defined in

[src/common/web/data/entities/resource/Resource.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/resource/Resource.ts#L23)

___

### type

• `Readonly` **type**: [`ResourceType`](../enums/common_web_data_entities_resource_Resource.ResourceType.md)

#### Defined in

[src/common/web/data/entities/resource/Resource.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/data/entities/resource/Resource.ts#L21)

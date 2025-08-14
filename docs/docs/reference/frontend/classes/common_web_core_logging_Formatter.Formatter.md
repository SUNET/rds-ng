---
id: "common_web_core_logging_Formatter.Formatter"
title: "Class: Formatter"
sidebar_label: "Formatter"
custom_edit_url: null
---

[common/web/core/logging/Formatter](../modules/common_web_core_logging_Formatter.md).Formatter

## Constructors

### constructor

• **new Formatter**(`record`): [`Formatter`](common_web_core_logging_Formatter.Formatter.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `record` | [`LogRecord`](common_web_core_logging_LogRecord.LogRecord.md) |

#### Returns

[`Formatter`](common_web_core_logging_Formatter.Formatter.md)

#### Defined in

[src/common/web/core/logging/Formatter.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/Formatter.ts#L23)

## Properties

### \_formattedText

• `Private` **\_formattedText**: `string` = `""`

#### Defined in

[src/common/web/core/logging/Formatter.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/Formatter.ts#L20)

___

### \_stylesStack

• `Private` **\_stylesStack**: `string`[] = `[]`

#### Defined in

[src/common/web/core/logging/Formatter.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/Formatter.ts#L21)

___

### \_colors

▪ `Static` `Private` **\_colors**: `Record`<`string`, `any`\>

#### Defined in

[src/common/web/core/logging/Formatter.ts:4](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/Formatter.ts#L4)

## Accessors

### formattedText

• `get` **formattedText**(): `string`

#### Returns

`string`

#### Defined in

[src/common/web/core/logging/Formatter.ts:42](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/Formatter.ts#L42)

___

### stylesStack

• `get` **stylesStack**(): `string`[]

#### Returns

`string`[]

#### Defined in

[src/common/web/core/logging/Formatter.ts:46](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/Formatter.ts#L46)

## Methods

### colorWrap

▸ **colorWrap**(`text`, `color`): `string`

#### Parameters

| Name | Type |
| :------ | :------ |
| `text` | `string` |
| `color` | `string` |

#### Returns

`string`

#### Defined in

[src/common/web/core/logging/Formatter.ts:50](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/Formatter.ts#L50)

___

### colorWrapEx

▸ **colorWrapEx**(`text`, `color`, `bold`, `italic`): `string`

#### Parameters

| Name | Type |
| :------ | :------ |
| `text` | `string` |
| `color` | `string` |
| `bold` | `boolean` |
| `italic` | `boolean` |

#### Returns

`string`

#### Defined in

[src/common/web/core/logging/Formatter.ts:54](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/Formatter.ts#L54)

___

### format

▸ **format**(`record`): `void`

#### Parameters

| Name | Type |
| :------ | :------ |
| `record` | [`LogRecord`](common_web_core_logging_LogRecord.LogRecord.md) |

#### Returns

`void`

#### Defined in

[src/common/web/core/logging/Formatter.ts:27](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/Formatter.ts#L27)

___

### getLevelColor

▸ **getLevelColor**(`levelName`): `string`

#### Parameters

| Name | Type |
| :------ | :------ |
| `levelName` | `string` |

#### Returns

`string`

#### Defined in

[src/common/web/core/logging/Formatter.ts:66](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/Formatter.ts#L66)

___

### getParametersList

▸ **getParametersList**(`record`): `string`

#### Parameters

| Name | Type |
| :------ | :------ |
| `record` | [`LogRecord`](common_web_core_logging_LogRecord.LogRecord.md) |

#### Returns

`string`

#### Defined in

[src/common/web/core/logging/Formatter.ts:73](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/Formatter.ts#L73)

___

### getTimestampString

▸ **getTimestampString**(`record`): `string`

#### Parameters

| Name | Type |
| :------ | :------ |
| `record` | [`LogRecord`](common_web_core_logging_LogRecord.LogRecord.md) |

#### Returns

`string`

#### Defined in

[src/common/web/core/logging/Formatter.ts:91](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/logging/Formatter.ts#L91)

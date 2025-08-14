---
id: "common_web_utils_Strings"
title: "Module: common/web/utils/Strings"
sidebar_label: "common/web/utils/Strings"
sidebar_position: 0
custom_edit_url: null
---

## Functions

### convertToStringArray

▸ **convertToStringArray**(`value`, `delimiter?`): `string`[]

Converts an arbitrary value or an array of such to a string array.

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `value` | `any` | `undefined` | The value to convert. |
| `delimiter` | `string` | `" "` | The delimiter to use for splitting a non-array value. |

#### Returns

`string`[]

#### Defined in

[src/common/web/utils/Strings.ts:7](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/Strings.ts#L7)

___

### encodeBase64

▸ **encodeBase64**(`buffer`): `string`

Encodes an ArrayBuffer to a base64 string.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `buffer` | `ArrayBuffer` | The array buffer to encode. |

#### Returns

`string`

#### Defined in

[src/common/web/utils/Strings.ts:101](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/Strings.ts#L101)

___

### finishSentence

▸ **finishSentence**(`sentence`): `string`

Adds a full stop to a string if necessary.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `sentence` | `string` | The sentence to complete. |

#### Returns

`string`

#### Defined in

[src/common/web/utils/Strings.ts:53](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/Strings.ts#L53)

___

### formatElapsedTime

▸ **formatElapsedTime**(`elapsed`): `string`

Formats a number of seconds into a readable form.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `elapsed` | `number` | The elapsed time in seconds. |

#### Returns

`string`

- The formatted string.

#### Defined in

[src/common/web/utils/Strings.ts:67](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/Strings.ts#L67)

___

### formatLocaleTimestamp

▸ **formatLocaleTimestamp**(`date`): `string`

Formats a UNIX timestamp to a string using the system locale.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `date` | `number` | The timestamp. |

#### Returns

`string`

- The formatted string.

#### Defined in

[src/common/web/utils/Strings.ts:44](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/Strings.ts#L44)

___

### humanReadableFileSize

▸ **humanReadableFileSize**(`size`): `string`

Converts a file size (in bytes) to a human-readable form.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `size` | `number` | The file size in bytes. |

#### Returns

`string`

- A string representation of the size.

#### Defined in

[src/common/web/utils/Strings.ts:28](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/Strings.ts#L28)

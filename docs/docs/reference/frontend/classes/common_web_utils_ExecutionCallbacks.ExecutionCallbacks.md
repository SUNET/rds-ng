---
id: "common_web_utils_ExecutionCallbacks.ExecutionCallbacks"
title: "Class: ExecutionCallbacks<DoneCallback, FailCallback>"
sidebar_label: "ExecutionCallbacks"
custom_edit_url: null
---

[common/web/utils/ExecutionCallbacks](../modules/common_web_utils_ExecutionCallbacks.md).ExecutionCallbacks

Helper class for running 'Done' and 'Failed' callbacks during arbitrary executions.

## Type parameters

| Name | Type |
| :------ | :------ |
| `DoneCallback` | extends `Function` |
| `FailCallback` | extends `Function` |

## Constructors

### constructor

• **new ExecutionCallbacks**<`DoneCallback`, `FailCallback`\>(): [`ExecutionCallbacks`](common_web_utils_ExecutionCallbacks.ExecutionCallbacks.md)<`DoneCallback`, `FailCallback`\>

#### Type parameters

| Name | Type |
| :------ | :------ |
| `DoneCallback` | extends `Function` |
| `FailCallback` | extends `Function` |

#### Returns

[`ExecutionCallbacks`](common_web_utils_ExecutionCallbacks.ExecutionCallbacks.md)<`DoneCallback`, `FailCallback`\>

#### Defined in

[src/common/web/utils/ExecutionCallbacks.ts:8](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/ExecutionCallbacks.ts#L8)

## Properties

### \_doneCallbacks

• `Private` **\_doneCallbacks**: `DoneCallback`[] = `[]`

#### Defined in

[src/common/web/utils/ExecutionCallbacks.ts:5](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/ExecutionCallbacks.ts#L5)

___

### \_failCallbacks

• `Private` **\_failCallbacks**: `FailCallback`[] = `[]`

#### Defined in

[src/common/web/utils/ExecutionCallbacks.ts:6](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/ExecutionCallbacks.ts#L6)

## Accessors

### doneCallbacks

• `get` **doneCallbacks**(): `DoneCallback`[]

All *Done* callbacks.

#### Returns

`DoneCallback`[]

#### Defined in

[src/common/web/utils/ExecutionCallbacks.ts:67](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/ExecutionCallbacks.ts#L67)

___

### failCallbacks

• `get` **failCallbacks**(): `FailCallback`[]

All *Fail* callbacks.

#### Returns

`FailCallback`[]

#### Defined in

[src/common/web/utils/ExecutionCallbacks.ts:74](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/ExecutionCallbacks.ts#L74)

## Methods

### done

▸ **done**(`cb`): [`ExecutionCallbacks`](common_web_utils_ExecutionCallbacks.ExecutionCallbacks.md)<`DoneCallback`, `FailCallback`\>

Adds a *Done* callback.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `cb` | `DoneCallback` | The callback to add. |

#### Returns

[`ExecutionCallbacks`](common_web_utils_ExecutionCallbacks.ExecutionCallbacks.md)<`DoneCallback`, `FailCallback`\>

- This instance to allow call chaining.

#### Defined in

[src/common/web/utils/ExecutionCallbacks.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/ExecutionCallbacks.ts#L17)

___

### failed

▸ **failed**(`cb`): [`ExecutionCallbacks`](common_web_utils_ExecutionCallbacks.ExecutionCallbacks.md)<`DoneCallback`, `FailCallback`\>

Adds a *Fail* callback.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `cb` | `FailCallback` | The callback to add. |

#### Returns

[`ExecutionCallbacks`](common_web_utils_ExecutionCallbacks.ExecutionCallbacks.md)<`DoneCallback`, `FailCallback`\>

- This instance to allow call chaining.

#### Defined in

[src/common/web/utils/ExecutionCallbacks.ts:29](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/ExecutionCallbacks.ts#L29)

___

### invokeDoneCallbacks

▸ **invokeDoneCallbacks**(`...args`): `void`

Invokes all *Done* callbacks.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `...args` | `any`[] | Arguments passed to the callbacks. |

#### Returns

`void`

#### Defined in

[src/common/web/utils/ExecutionCallbacks.ts:39](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/ExecutionCallbacks.ts#L39)

___

### invokeFailCallbacks

▸ **invokeFailCallbacks**(`...args`): `void`

Invokes all *Fail* callbacks.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `...args` | `any`[] | Arguments passed to the callbacks. |

#### Returns

`void`

#### Defined in

[src/common/web/utils/ExecutionCallbacks.ts:50](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/ExecutionCallbacks.ts#L50)

___

### reset

▸ **reset**(): `void`

Removecs all callbacks.

#### Returns

`void`

#### Defined in

[src/common/web/utils/ExecutionCallbacks.ts:59](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/utils/ExecutionCallbacks.ts#L59)

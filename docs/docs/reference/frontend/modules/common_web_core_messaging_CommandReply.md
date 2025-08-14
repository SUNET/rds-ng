---
id: "common_web_core_messaging_CommandReply"
title: "Module: common/web/core/messaging/CommandReply"
sidebar_label: "common/web/core/messaging/CommandReply"
sidebar_position: 0
custom_edit_url: null
---

## Enumerations

- [CommandFailType](../enums/common_web_core_messaging_CommandReply.CommandFailType.md)

## Classes

- [CommandReply](../classes/common_web_core_messaging_CommandReply.CommandReply.md)

## Type Aliases

### CommandDoneCallback

Ƭ **CommandDoneCallback**: (`reply`: [`CommandReply`](../classes/common_web_core_messaging_CommandReply.CommandReply.md), `success`: `boolean`, `msg`: `string`) => `void`

#### Type declaration

▸ (`reply`, `success`, `msg`): `void`

##### Parameters

| Name | Type |
| :------ | :------ |
| `reply` | [`CommandReply`](../classes/common_web_core_messaging_CommandReply.CommandReply.md) |
| `success` | `boolean` |
| `msg` | `string` |

##### Returns

`void`

#### Defined in

[src/common/web/core/messaging/CommandReply.ts:39](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/CommandReply.ts#L39)

___

### CommandFailCallback

Ƭ **CommandFailCallback**: (`failType`: [`CommandFailType`](../enums/common_web_core_messaging_CommandReply.CommandFailType.md), `msg`: `string`) => `void`

#### Type declaration

▸ (`failType`, `msg`): `void`

##### Parameters

| Name | Type |
| :------ | :------ |
| `failType` | [`CommandFailType`](../enums/common_web_core_messaging_CommandReply.CommandFailType.md) |
| `msg` | `string` |

##### Returns

`void`

#### Defined in

[src/common/web/core/messaging/CommandReply.ts:40](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/CommandReply.ts#L40)

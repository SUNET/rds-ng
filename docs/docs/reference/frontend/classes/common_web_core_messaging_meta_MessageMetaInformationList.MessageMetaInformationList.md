---
id: "common_web_core_messaging_meta_MessageMetaInformationList.MessageMetaInformationList"
title: "Class: MessageMetaInformationList"
sidebar_label: "MessageMetaInformationList"
custom_edit_url: null
---

[common/web/core/messaging/meta/MessageMetaInformationList](../modules/common_web_core_messaging_meta_MessageMetaInformationList.md).MessageMetaInformationList

List to store message meta information objects.

## Constructors

### constructor

• **new MessageMetaInformationList**(): [`MessageMetaInformationList`](common_web_core_messaging_meta_MessageMetaInformationList.MessageMetaInformationList.md)

#### Returns

[`MessageMetaInformationList`](common_web_core_messaging_meta_MessageMetaInformationList.MessageMetaInformationList.md)

## Properties

### \_list

• `Private` `Readonly` **\_list**: `MessageMetaInformationListType` = `{}`

#### Defined in

[src/common/web/core/messaging/meta/MessageMetaInformationList.ts:26](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/meta/MessageMetaInformationList.ts#L26)

## Methods

### add

▸ **add**(`unique`, `meta`, `timeout`): `void`

Adds a new entry to the list.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `unique` | `string` | The unique trace identifying the message. |
| `meta` | [`MessageMetaInformation`](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md) | The message meta information. |
| `timeout` | `number` | A timeout (in seconds) after which a message is deemed timed out. |

#### Returns

`void`

#### Defined in

[src/common/web/core/messaging/meta/MessageMetaInformationList.ts:35](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/meta/MessageMetaInformationList.ts#L35)

___

### find

▸ **find**(`unique`): ``null`` \| [`MessageMetaInformation`](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md)

Finds an entry associated with the given ``unique``.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `unique` | `string` | The unique trace identifying the message. |

#### Returns

``null`` \| [`MessageMetaInformation`](common_web_core_messaging_meta_MessageMetaInformation.MessageMetaInformation.md)

- The found meta information, if any.

#### Defined in

[src/common/web/core/messaging/meta/MessageMetaInformationList.ts:59](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/meta/MessageMetaInformationList.ts#L59)

___

### findTimedOutEntries

▸ **findTimedOutEntries**(): `string`[]

Finds all entries that have timed out already.

#### Returns

`string`[]

- A list of all timed out entries.

#### Defined in

[src/common/web/core/messaging/meta/MessageMetaInformationList.ts:72](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/meta/MessageMetaInformationList.ts#L72)

___

### remove

▸ **remove**(`unique`): `void`

Removes an entry from the list.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `unique` | `string` | The unique trace identifying the message. |

#### Returns

`void`

#### Defined in

[src/common/web/core/messaging/meta/MessageMetaInformationList.ts:46](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/core/messaging/meta/MessageMetaInformationList.ts#L46)

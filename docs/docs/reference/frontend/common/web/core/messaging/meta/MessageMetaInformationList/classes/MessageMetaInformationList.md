# Class: MessageMetaInformationList

Defined in: [src/common/web/core/messaging/meta/MessageMetaInformationList.ts:25](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/meta/MessageMetaInformationList.ts#L25)

List to store message meta information objects.

## Constructors

### Constructor

> **new MessageMetaInformationList**(): `MessageMetaInformationList`

#### Returns

`MessageMetaInformationList`

## Methods

### add()

> **add**(`unique`, `meta`, `timeout`): `void`

Defined in: [src/common/web/core/messaging/meta/MessageMetaInformationList.ts:35](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/meta/MessageMetaInformationList.ts#L35)

Adds a new entry to the list.

#### Parameters

##### unique

`string`

The unique trace identifying the message.

##### meta

[`MessageMetaInformation`](../../MessageMetaInformation/classes/MessageMetaInformation.md)

The message meta information.

##### timeout

`number`

A timeout (in seconds) after which a message is deemed timed out.

#### Returns

`void`

***

### find()

> **find**(`unique`): `null` \| [`MessageMetaInformation`](../../MessageMetaInformation/classes/MessageMetaInformation.md)

Defined in: [src/common/web/core/messaging/meta/MessageMetaInformationList.ts:59](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/meta/MessageMetaInformationList.ts#L59)

Finds an entry associated with the given ``unique``.

#### Parameters

##### unique

`string`

The unique trace identifying the message.

#### Returns

`null` \| [`MessageMetaInformation`](../../MessageMetaInformation/classes/MessageMetaInformation.md)

- The found meta information, if any.

***

### findTimedOutEntries()

> **findTimedOutEntries**(): `string`[]

Defined in: [src/common/web/core/messaging/meta/MessageMetaInformationList.ts:72](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/meta/MessageMetaInformationList.ts#L72)

Finds all entries that have timed out already.

#### Returns

`string`[]

- A list of all timed out entries.

***

### remove()

> **remove**(`unique`): `void`

Defined in: [src/common/web/core/messaging/meta/MessageMetaInformationList.ts:46](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/meta/MessageMetaInformationList.ts#L46)

Removes an entry from the list.

#### Parameters

##### unique

`string`

The unique trace identifying the message.

#### Returns

`void`

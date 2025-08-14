# Class: MessagePayload

Defined in: [src/common/web/core/messaging/MessagePayload.ts:9](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/MessagePayload.ts#L9)

Class holding arbitrary payload data (as key-value pairs) of a message.

## Constructors

### Constructor

> **new MessagePayload**(): `MessagePayload`

#### Returns

`MessagePayload`

## Methods

### clear()

> **clear**(`key`): `void`

Defined in: [src/common/web/core/messaging/MessagePayload.ts:46](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/MessagePayload.ts#L46)

Removes an item or clears the entire payload.

#### Parameters

##### key

The key of the item; if set to *None*, all items will be removed.

`undefined` | `string`

#### Returns

`void`

***

### contains()

> **contains**(`key`): `boolean`

Defined in: [src/common/web/core/messaging/MessagePayload.ts:37](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/MessagePayload.ts#L37)

Checks if an item exists.

#### Parameters

##### key

`string`

The key of the item.

#### Returns

`boolean`

***

### decode()

> **decode**(`payload`): `void`

Defined in: [src/common/web/core/messaging/MessagePayload.ts:70](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/MessagePayload.ts#L70)

Decodes the payload from message passing.

#### Parameters

##### payload

[`Payload`](../type-aliases/Payload.md)

The incoming payload.

#### Returns

`void`

***

### encode()

> **encode**(): [`Payload`](../type-aliases/Payload.md)

Defined in: [src/common/web/core/messaging/MessagePayload.ts:61](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/MessagePayload.ts#L61)

Encodes the payload for message passing.

#### Returns

[`Payload`](../type-aliases/Payload.md)

- The encoded data.

***

### get()

> **get**(`key`): `any`

Defined in: [src/common/web/core/messaging/MessagePayload.ts:28](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/MessagePayload.ts#L28)

Retrieves a payload item.

#### Parameters

##### key

`string`

The key of the item.

#### Returns

`any`

- The item data or *None* otherwise.

***

### set()

> **set**(`key`, `data`): `void`

Defined in: [src/common/web/core/messaging/MessagePayload.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/MessagePayload.ts#L17)

Sets a payload item.

#### Parameters

##### key

`string`

The key of the item.

##### data

`any`

The item data.

#### Returns

`void`

***

### toString()

> **toString**(): `string`

Defined in: [src/common/web/core/messaging/MessagePayload.ts:74](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/MessagePayload.ts#L74)

#### Returns

`string`

# Class: MessageHandlerMapping

Defined in: [src/common/web/core/messaging/handlers/MessageHandler.ts:10](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageHandler.ts#L10)

Mapping from a message name filter to a message handler.

## Constructors

### Constructor

> **new MessageHandlerMapping**(`filter`, `handler`, `messageType`): `MessageHandlerMapping`

Defined in: [src/common/web/core/messaging/handlers/MessageHandler.ts:16](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageHandler.ts#L16)

#### Parameters

##### filter

`string`

The message name filter.

##### handler

[`MessageHandler`](../type-aliases/MessageHandler.md)

The message handler.

##### messageType

[`Constructable`](../../../../../utils/Types/interfaces/Constructable.md)

The message type the handler expects.

#### Returns

`MessageHandlerMapping`

## Properties

### filter

> `readonly` **filter**: `string`

Defined in: [src/common/web/core/messaging/handlers/MessageHandler.ts:16](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageHandler.ts#L16)

The message name filter.

***

### handler

> `readonly` **handler**: [`MessageHandler`](../type-aliases/MessageHandler.md)

Defined in: [src/common/web/core/messaging/handlers/MessageHandler.ts:16](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageHandler.ts#L16)

The message handler.

***

### messageType

> `readonly` **messageType**: [`Constructable`](../../../../../utils/Types/interfaces/Constructable.md)

Defined in: [src/common/web/core/messaging/handlers/MessageHandler.ts:16](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageHandler.ts#L16)

The message type the handler expects.

## Methods

### toString()

> **toString**(): `string`

Defined in: [src/common/web/core/messaging/handlers/MessageHandler.ts:22](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageHandler.ts#L22)

Gets the string representation of the handler mapping.

#### Returns

`string`

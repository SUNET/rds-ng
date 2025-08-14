# Class: MessageHandlers

Defined in: [src/common/web/core/messaging/handlers/MessageHandlers.ts:10](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageHandlers.ts#L10)

Holds mappings for message handlers.

## Constructors

### Constructor

> **new MessageHandlers**(): `MessageHandlers`

#### Returns

`MessageHandlers`

## Methods

### addHandler()

> **addHandler**(`filter`, `handler`, `messageType`): `void`

Defined in: [src/common/web/core/messaging/handlers/MessageHandlers.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageHandlers.ts#L20)

Adds a new message handler mapping.

#### Parameters

##### filter

`string`

The message name filter.

##### handler

[`MessageHandler`](../../MessageHandler/type-aliases/MessageHandler.md)

The message handler.

##### messageType

[`Constructable`](../../../../../utils/Types/interfaces/Constructable.md)

The message type the handler expects.

#### Returns

`void`

***

### findHandlers()

> **findHandlers**(`msgName`): [`MessageHandlerMappings`](../../MessageHandler/type-aliases/MessageHandlerMappings.md)

Defined in: [src/common/web/core/messaging/handlers/MessageHandlers.ts:33](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageHandlers.ts#L33)

Finds all handlers that fit the given ``msg_name``.

The message name filter can be a complete message name, or a wildcard pattern using asterisks (*).

#### Parameters

##### msgName

`string`

The message name (pattern).

#### Returns

[`MessageHandlerMappings`](../../MessageHandler/type-aliases/MessageHandlerMappings.md)

- A list of all found message handlers.

***

### toString()

> **toString**(): `string`

Defined in: [src/common/web/core/messaging/handlers/MessageHandlers.ts:47](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageHandlers.ts#L47)

Gets the string representation of all mapped handlers.

#### Returns

`string`

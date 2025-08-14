# Class: MessageService\<CtxType\>

Defined in: [src/common/web/core/messaging/handlers/MessageService.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageService.ts#L17)

Base class for all message services.

A *message service* wraps message handlers and proper message context creation (i.e., using a flexible context type). It
is used by the message bus as an encapsulated layer for message dispatching.

## Extended by

- [`Service`](../../../../../services/Service/classes/Service.md)

## Type Parameters

### CtxType

`CtxType` *extends* [`MessageContext`](../../MessageContext/classes/MessageContext.md) = [`MessageContext`](../../MessageContext/classes/MessageContext.md)

## Constructors

### Constructor

> **new MessageService**\<`CtxType`\>(`compID`, `messageBus`, `contextType`): `MessageService`\<`CtxType`\>

Defined in: [src/common/web/core/messaging/handlers/MessageService.ts:29](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageService.ts#L29)

#### Parameters

##### compID

[`UnitID`](../../../../../utils/UnitID/classes/UnitID.md)

The global component identifier.

##### messageBus

[`MessageBusProtocol`](../../../MessageBusProtocol/interfaces/MessageBusProtocol.md)

The global message bus.

##### contextType

[`Constructable`](../../../../../utils/Types/interfaces/Constructable.md)\<`CtxType`\> = `...`

The type to use when creating a message context.

#### Returns

`MessageService`\<`CtxType`\>

## Accessors

### messageHandlers

#### Get Signature

> **get** **messageHandlers**(): [`MessageHandlers`](../../MessageHandlers/classes/MessageHandlers.md)

Defined in: [src/common/web/core/messaging/handlers/MessageService.ts:63](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageService.ts#L63)

The message handlers maintained by this message service.

##### Returns

[`MessageHandlers`](../../MessageHandlers/classes/MessageHandlers.md)

## Methods

### createContext()

> **createContext**(`msgMeta`, `msgOrigin`, `logger`, `config`): [`MessageContext`](../../MessageContext/classes/MessageContext.md)

Defined in: [src/common/web/core/messaging/handlers/MessageService.ts:47](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageService.ts#L47)

Creates a new service context.

#### Parameters

##### msgMeta

[`MessageMetaInformation`](../../../meta/MessageMetaInformation/classes/MessageMetaInformation.md)

The meta information of the message.

##### msgOrigin

[`UnitID`](../../../../../utils/UnitID/classes/UnitID.md)

The origin of the message.

##### logger

[`LoggerProxy`](../../../../logging/LoggerProxy/classes/LoggerProxy.md)

The logger to be used within the new context.

##### config

[`Configuration`](../../../../../utils/config/Configuration/classes/Configuration.md)

The global component configuration.

#### Returns

[`MessageContext`](../../MessageContext/classes/MessageContext.md)

- The newly created message context.

***

### createMessageBuilder()

> **createMessageBuilder**(): [`MessageBuilder`](../../../composers/MessageBuilder/classes/MessageBuilder.md)

Defined in: [src/common/web/core/messaging/handlers/MessageService.ts:56](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageService.ts#L56)

Creates a new message builder.

#### Returns

[`MessageBuilder`](../../../composers/MessageBuilder/classes/MessageBuilder.md)

- The newly created message builder.

# Class: Service\<CtxType\>

Defined in: [src/common/web/services/Service.ts:31](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/services/Service.ts#L31)

Base service class providing easy message handler mapping.

A service can be seen as the bridge between the inner workings of a component (represented by a ``Core``) and the
outside component domain.

Services register the various message handlers that are called when a certain message is received by the message bus and
dispatched locally. They also create instances of ``ServiceContext`` (or a subclass) that represent a single *unit of work*
when executing a message handler.

Message handlers are defined using the ``message_handler`` decorator, as can be seen in this example (``svc`` being a ``Service`` instance):
```
    @svc.messageHandler("msg/event", Event)
    function h(msg: Event, ctx: ServiceContext): void {
        ctx.logger.info("EVENT HANDLER CALLED");
    }
```

## Extends

- [`MessageService`](../../../core/messaging/handlers/MessageService/classes/MessageService.md)\<`CtxType`\>

## Type Parameters

### CtxType

`CtxType` *extends* [`ServiceContext`](../../ServiceContext/classes/ServiceContext.md) = [`ServiceContext`](../../ServiceContext/classes/ServiceContext.md)

## Constructors

### Constructor

> **new Service**\<`CtxType`\>(`compID`, `name`, `messageBus`, `contextType`): `Service`\<`CtxType`\>

Defined in: [src/common/web/services/Service.ts:40](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/services/Service.ts#L40)

#### Parameters

##### compID

[`UnitID`](../../../utils/UnitID/classes/UnitID.md)

The global component identifier.

##### name

`string`

The service name.

##### messageBus

[`MessageBusProtocol`](../../../core/messaging/MessageBusProtocol/interfaces/MessageBusProtocol.md)

The global message bus.

##### contextType

[`Constructable`](../../../utils/Types/interfaces/Constructable.md)\<`CtxType`\> = `...`

The type to use when creating a message context.

#### Returns

`Service`\<`CtxType`\>

#### Overrides

[`MessageService`](../../../core/messaging/handlers/MessageService/classes/MessageService.md).[`constructor`](../../../core/messaging/handlers/MessageService/classes/MessageService.md#constructor)

## Accessors

### messageBuilder

#### Get Signature

> **get** **messageBuilder**(): [`MessageBuilder`](../../../core/messaging/composers/MessageBuilder/classes/MessageBuilder.md)

Defined in: [src/common/web/services/Service.ts:82](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/services/Service.ts#L82)

The service's message builder.

##### Returns

[`MessageBuilder`](../../../core/messaging/composers/MessageBuilder/classes/MessageBuilder.md)

***

### messageHandlers

#### Get Signature

> **get** **messageHandlers**(): [`MessageHandlers`](../../../core/messaging/handlers/MessageHandlers/classes/MessageHandlers.md)

Defined in: [src/common/web/core/messaging/handlers/MessageService.ts:63](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageService.ts#L63)

The message handlers maintained by this message service.

##### Returns

[`MessageHandlers`](../../../core/messaging/handlers/MessageHandlers/classes/MessageHandlers.md)

#### Inherited from

[`MessageService`](../../../core/messaging/handlers/MessageService/classes/MessageService.md).[`messageHandlers`](../../../core/messaging/handlers/MessageService/classes/MessageService.md#messagehandlers)

***

### name

#### Get Signature

> **get** **name**(): `string`

Defined in: [src/common/web/services/Service.ts:75](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/services/Service.ts#L75)

The name of this service.

##### Returns

`string`

## Methods

### createContext()

> **createContext**(`msgMeta`, `msgOrigin`, `logger`, `config`): [`MessageContext`](../../../core/messaging/handlers/MessageContext/classes/MessageContext.md)

Defined in: [src/common/web/core/messaging/handlers/MessageService.ts:47](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageService.ts#L47)

Creates a new service context.

#### Parameters

##### msgMeta

[`MessageMetaInformation`](../../../core/messaging/meta/MessageMetaInformation/classes/MessageMetaInformation.md)

The meta information of the message.

##### msgOrigin

[`UnitID`](../../../utils/UnitID/classes/UnitID.md)

The origin of the message.

##### logger

[`LoggerProxy`](../../../core/logging/LoggerProxy/classes/LoggerProxy.md)

The logger to be used within the new context.

##### config

[`Configuration`](../../../utils/config/Configuration/classes/Configuration.md)

The global component configuration.

#### Returns

[`MessageContext`](../../../core/messaging/handlers/MessageContext/classes/MessageContext.md)

- The newly created message context.

#### Inherited from

[`MessageService`](../../../core/messaging/handlers/MessageService/classes/MessageService.md).[`createContext`](../../../core/messaging/handlers/MessageService/classes/MessageService.md#createcontext)

***

### createMessageBuilder()

> **createMessageBuilder**(): [`MessageBuilder`](../../../core/messaging/composers/MessageBuilder/classes/MessageBuilder.md)

Defined in: [src/common/web/core/messaging/handlers/MessageService.ts:56](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageService.ts#L56)

Creates a new message builder.

#### Returns

[`MessageBuilder`](../../../core/messaging/composers/MessageBuilder/classes/MessageBuilder.md)

- The newly created message builder.

#### Inherited from

[`MessageService`](../../../core/messaging/handlers/MessageService/classes/MessageService.md).[`createMessageBuilder`](../../../core/messaging/handlers/MessageService/classes/MessageService.md#createmessagebuilder)

***

### messageHandler()

> **messageHandler**\<`MsgType`, `CtxType`\>(`messageType`, `handler`, `nameFilter`): `void`

Defined in: [src/common/web/services/Service.ts:63](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/services/Service.ts#L63)

Declares a message handler.

To define a new message handler, use the following pattern:
```
    svc.messageHandler("msg/event", Event,
        (msg: Event, ctx: ServiceContext): void => {
             ctx.logger.info("EVENT HANDLER CALLED");
        }
    );
```

#### Type Parameters

##### MsgType

`MsgType` *extends* [`Message`](../../../core/messaging/Message/classes/Message.md)

##### CtxType

`CtxType` *extends* [`MessageContext`](../../../core/messaging/handlers/MessageContext/classes/MessageContext.md)

#### Parameters

##### messageType

[`ConstructableMessage`](../../../core/messaging/Message/interfaces/ConstructableMessage.md)\<`MsgType`\>

The type of the message.

##### handler

`ServiceHandler`\<`MsgType`, `CtxType`\>

The message handler callback.

##### nameFilter

`string` = `""`

A more generic message name filter to match against; wildcards (*) are supported as well.

#### Returns

`void`

***

### toString()

> **toString**(): `string`

Defined in: [src/common/web/services/Service.ts:89](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/services/Service.ts#L89)

Gets the string representation of this service.

#### Returns

`string`

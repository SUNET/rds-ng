# Class: Client

Defined in: [src/common/web/core/messaging/networking/Client.ts:18](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/networking/Client.ts#L18)

The client connection, based on ``socketio``.

## Constructors

### Constructor

> **new Client**(`compID`, `config`, `messageBuilder`): `Client`

Defined in: [src/common/web/core/messaging/networking/Client.ts:35](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/networking/Client.ts#L35)

#### Parameters

##### compID

[`UnitID`](../../../../../utils/UnitID/classes/UnitID.md)

The component identifier.

##### config

[`Configuration`](../../../../../utils/config/Configuration/classes/Configuration.md)

The global configuration.

##### messageBuilder

[`MessageBuilder`](../../../composers/MessageBuilder/classes/MessageBuilder.md)

A message builder instance.

#### Returns

`Client`

## Methods

### connectToServer()

> **connectToServer**(): `void`

Defined in: [src/common/web/core/messaging/networking/Client.ts:85](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/networking/Client.ts#L85)

Establishes the connection to the server.

#### Returns

`void`

***

### process()

> **process**(): `void`

Defined in: [src/common/web/core/messaging/networking/Client.ts:80](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/networking/Client.ts#L80)

Periodically performs certain tasks.

#### Returns

`void`

***

### run()

> **run**(): `void`

Defined in: [src/common/web/core/messaging/networking/Client.ts:73](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/networking/Client.ts#L73)

Automatically connects to a server.

#### Returns

`void`

***

### sendMessage()

> **sendMessage**(`msg`): `void`

Defined in: [src/common/web/core/messaging/networking/Client.ts:113](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/networking/Client.ts#L113)

Sends a message to the server (if connected).

For this, the message will be encoded as *JSON* first.

#### Parameters

##### msg

[`Message`](../../../Message/classes/Message.md)

The message to send.

#### Returns

`void`

***

### setMessageHandler()

> **setMessageHandler**(`msgHandler`): `void`

Defined in: [src/common/web/core/messaging/networking/Client.ts:102](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/networking/Client.ts#L102)

Sets a handler that gets called when a message arrives.

#### Parameters

##### msgHandler

`ClientMessageHandler`

The message handler to be called.

#### Returns

`void`

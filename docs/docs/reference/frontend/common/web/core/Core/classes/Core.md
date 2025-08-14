# Class: Core

Defined in: [src/common/web/core/Core.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/Core.ts#L19)

The main *underlying basis* of any component.

The ``Core`` brings together all portions and aspects that build the underlying foundation of every web component,
including the ``MessageBus``.

The core can be regarded as a facade to the *inner structure* of a component. It only offers a small number of public
methods and is accessed from the outside very rarely.

An instance of this class is always created when creating a ``WebComponent``; it should never be instantiated otherwise.

## Constructors

### Constructor

> **new Core**(`compData`): `Core`

Defined in: [src/common/web/core/Core.ts:27](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/Core.ts#L27)

#### Parameters

##### compData

[`WebComponentData`](../../../component/WebComponentData/classes/WebComponentData.md)

The component data used to access common component information.

#### Returns

`Core`

## Accessors

### isDebugMode

#### Get Signature

> **get** **isDebugMode**(): `boolean`

Defined in: [src/common/web/core/Core.ts:95](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/Core.ts#L95)

Whether we're running in Debug mode.

##### Returns

`boolean`

***

### messageBus

#### Get Signature

> **get** **messageBus**(): [`MessageBus`](../../messaging/MessageBus/classes/MessageBus.md)

Defined in: [src/common/web/core/Core.ts:88](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/Core.ts#L88)

The global ``MessageBus`` instance.

##### Returns

[`MessageBus`](../../messaging/MessageBus/classes/MessageBus.md)

## Methods

### registerService()

> **registerService**(`svc`): `void`

Defined in: [src/common/web/core/Core.ts:57](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/Core.ts#L57)

Registers a message service.

Services are always created and registered using ``create_service`` (in ``WebComponent``),
so you should rarely (if ever) need to call this method directly.

#### Parameters

##### svc

[`MessageService`](../../messaging/handlers/MessageService/classes/MessageService.md)

The message service to register.

#### Returns

`void`

***

### run()

> **run**(): `void`

Defined in: [src/common/web/core/Core.ts:81](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/Core.ts#L81)

Starts periodic background tasks.

#### Returns

`void`

***

### unregisterService()

> **unregisterService**(`svc`): `void`

Defined in: [src/common/web/core/Core.ts:70](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/Core.ts#L70)

Removes a message service.

#### Parameters

##### svc

[`MessageService`](../../messaging/handlers/MessageService/classes/MessageService.md)

The message service to remove.

#### Returns

`void`

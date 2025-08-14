# Class: WebComponent\<UserInterfaceType\>

Defined in: [src/common/web/component/WebComponent.ts:59](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponent.ts#L59)

Base class for all web components.

By default, an instance of ``UserInterfaceType`` is used to create the main UI handler. This can be overriden using the corresponding
template and constructor parameters.

Web applications are always based on this class. It mainly maintains an instance of the ``Core``, but also stores general information
about the application itself and the entire project.

## Extended by

- [`FrontendComponent`](../../../../../frontend/src/component/FrontendComponent/classes/FrontendComponent.md)

## Type Parameters

### UserInterfaceType

`UserInterfaceType` *extends* [`UserInterface`](../../../ui/UserInterface/classes/UserInterface.md) = [`UserInterface`](../../../ui/UserInterface/classes/UserInterface.md)

## Constructors

### Constructor

> **new WebComponent**\<`UserInterfaceType`\>(`env`, `compID`, `appRoot`, `userInterfaceType`): `WebComponent`\<`UserInterfaceType`\>

Defined in: [src/common/web/component/WebComponent.ts:78](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponent.ts#L78)

#### Parameters

##### env

[`SettingsContainer`](../../../utils/config/Configuration/type-aliases/SettingsContainer.md)

The global environment variables.

##### compID

[`UnitID`](../../../utils/UnitID/classes/UnitID.md)

The identifier of this component.

##### appRoot

[`VueComponent`](../type-aliases/VueComponent.md)

The root (main) application component.

##### userInterfaceType

[`Constructable`](../../../utils/Types/interfaces/Constructable.md)\<`UserInterfaceType`\> = `...`

The type of the user interface class.

#### Returns

`WebComponent`\<`UserInterfaceType`\>

## Properties

### \_core

> `protected` `readonly` **\_core**: [`Core`](../../../core/Core/classes/Core.md)

Defined in: [src/common/web/component/WebComponent.ts:66](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponent.ts#L66)

***

### \_data

> `protected` `readonly` **\_data**: [`WebComponentData`](../../WebComponentData/classes/WebComponentData.md)

Defined in: [src/common/web/component/WebComponent.ts:64](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponent.ts#L64)

***

### \_router

> `protected` `readonly` **\_router**: `Router`

Defined in: [src/common/web/component/WebComponent.ts:67](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponent.ts#L67)

***

### \_session

> `protected` `readonly` **\_session**: [`Session`](../../Session/classes/Session.md)

Defined in: [src/common/web/component/WebComponent.ts:63](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponent.ts#L63)

***

### \_userInterface

> `protected` `readonly` **\_userInterface**: `UserInterfaceType`

Defined in: [src/common/web/component/WebComponent.ts:69](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponent.ts#L69)

***

### \_vueApp

> `protected` `readonly` **\_vueApp**: `App`

Defined in: [src/common/web/component/WebComponent.ts:70](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponent.ts#L70)

## Accessors

### data

#### Get Signature

> **get** **data**(): [`WebComponentData`](../../WebComponentData/classes/WebComponentData.md)

Defined in: [src/common/web/component/WebComponent.ts:247](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponent.ts#L247)

A data helper object that stores useful component data and information.

##### Returns

[`WebComponentData`](../../WebComponentData/classes/WebComponentData.md)

***

### router

#### Get Signature

> **get** **router**(): `Router`

Defined in: [src/common/web/component/WebComponent.ts:254](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponent.ts#L254)

The global router.

##### Returns

`Router`

***

### session

#### Get Signature

> **get** **session**(): [`Session`](../../Session/classes/Session.md)

Defined in: [src/common/web/component/WebComponent.ts:240](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponent.ts#L240)

The client session.

##### Returns

[`Session`](../../Session/classes/Session.md)

***

### userInterface

#### Get Signature

> **get** **userInterface**(): `UserInterfaceType`

Defined in: [src/common/web/component/WebComponent.ts:261](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponent.ts#L261)

The global user interface.

##### Returns

`UserInterfaceType`

***

### vue

#### Get Signature

> **get** **vue**(): `App`

Defined in: [src/common/web/component/WebComponent.ts:268](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponent.ts#L268)

The global Vue application instance.

##### Returns

`App`

***

### instance

#### Get Signature

> **get** `static` **instance**(): `WebComponent`

Defined in: [src/common/web/component/WebComponent.ts:290](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponent.ts#L290)

The global ``WebComponent`` instance.

##### Throws

Error - If no instance has been created.

##### Returns

`WebComponent`

## Methods

### configureRoutes()

> `protected` **configureRoutes**(): `RouteRecordRaw`[]

Defined in: [src/common/web/component/WebComponent.ts:180](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponent.ts#L180)

Sets up routes for the Vue router.

#### Returns

`RouteRecordRaw`[]

- The routes as an array; return `null` if the router shouldn't be used.

***

### createService()

> **createService**\<`CtxType`\>(`name`, `initializer`, `contextType`): [`Service`](../../../services/Service/classes/Service.md)

Defined in: [src/common/web/component/WebComponent.ts:224](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponent.ts#L224)

Creates and registers a new service.

#### Type Parameters

##### CtxType

`CtxType` *extends* [`ServiceContext`](../../../services/ServiceContext/classes/ServiceContext.md)

#### Parameters

##### name

`string`

The name of the service.

##### initializer

A function called to registered message handlers etc. after the service has been created.

`null` | (`svc`) => `void`

##### contextType

[`Constructable`](../../../utils/Types/interfaces/Constructable.md)\<`CtxType`\> = `...`

Can be used to override the default ``ServiceContext`` type. All message handlers
     associated with the new service will then receive instances of this type for their service context.

#### Returns

[`Service`](../../../services/Service/classes/Service.md)

***

### mount()

> **mount**(`appElement`): `void`

Defined in: [src/common/web/component/WebComponent.ts:192](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponent.ts#L192)

Mounts the Vue application in the given element.

Notes:
    This method must be called immediately after creating the main component instance.

#### Parameters

##### appElement

`string` = `"#app"`

The HTML element ID used for mounting the root component.

#### Returns

`void`

***

### run()

> **run**(): `void`

Defined in: [src/common/web/component/WebComponent.ts:202](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponent.ts#L202)

Starts the component's execution cycles.

Notes:
    This method is automatically called by the framework.

#### Returns

`void`

***

### toString()

> **toString**(): `string`

Defined in: [src/common/web/component/WebComponent.ts:305](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponent.ts#L305)

#### Returns

`string`

- The string representation of this component.

***

### injectComponent()

> `static` **injectComponent**\<`CompType`\>(): `CompType`

Defined in: [src/common/web/component/WebComponent.ts:277](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponent.ts#L277)

The global ``WebComponent`` instance via Vue's injection mechanism.

#### Type Parameters

##### CompType

`CompType` *extends* `WebComponent`\<[`UserInterface`](../../../ui/UserInterface/classes/UserInterface.md)\> = `WebComponent`\<[`UserInterface`](../../../ui/UserInterface/classes/UserInterface.md)\>

#### Returns

`CompType`

#### Throws

Error - If no instance has been created.

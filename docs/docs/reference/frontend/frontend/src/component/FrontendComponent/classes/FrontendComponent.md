# Class: FrontendComponent

Defined in: [src/frontend/src/component/FrontendComponent.ts:33](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/component/FrontendComponent.ts#L33)

The main frontend component class.

## Extends

- [`WebComponent`](../../../../../common/web/component/WebComponent/classes/WebComponent.md)\<[`FrontendUserInterface`](../../../ui/FrontendUserInterface/classes/FrontendUserInterface.md)\>

## Constructors

### Constructor

> **new FrontendComponent**(): `FrontendComponent`

Defined in: [src/frontend/src/component/FrontendComponent.ts:44](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/component/FrontendComponent.ts#L44)

#### Returns

`FrontendComponent`

#### Overrides

[`WebComponent`](../../../../../common/web/component/WebComponent/classes/WebComponent.md).[`constructor`](../../../../../common/web/component/WebComponent/classes/WebComponent.md#constructor)

## Properties

### \_core

> `protected` `readonly` **\_core**: [`Core`](../../../../../common/web/core/Core/classes/Core.md)

Defined in: [src/common/web/component/WebComponent.ts:66](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponent.ts#L66)

#### Inherited from

[`WebComponent`](../../../../../common/web/component/WebComponent/classes/WebComponent.md).[`_core`](../../../../../common/web/component/WebComponent/classes/WebComponent.md#_core)

***

### \_data

> `protected` `readonly` **\_data**: [`WebComponentData`](../../../../../common/web/component/WebComponentData/classes/WebComponentData.md)

Defined in: [src/common/web/component/WebComponent.ts:64](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponent.ts#L64)

#### Inherited from

[`WebComponent`](../../../../../common/web/component/WebComponent/classes/WebComponent.md).[`_data`](../../../../../common/web/component/WebComponent/classes/WebComponent.md#_data)

***

### \_router

> `protected` `readonly` **\_router**: `Router`

Defined in: [src/common/web/component/WebComponent.ts:67](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponent.ts#L67)

#### Inherited from

[`WebComponent`](../../../../../common/web/component/WebComponent/classes/WebComponent.md).[`_router`](../../../../../common/web/component/WebComponent/classes/WebComponent.md#_router)

***

### \_session

> `protected` `readonly` **\_session**: [`Session`](../../../../../common/web/component/Session/classes/Session.md)

Defined in: [src/common/web/component/WebComponent.ts:63](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponent.ts#L63)

#### Inherited from

[`WebComponent`](../../../../../common/web/component/WebComponent/classes/WebComponent.md).[`_session`](../../../../../common/web/component/WebComponent/classes/WebComponent.md#_session)

***

### \_userInterface

> `protected` `readonly` **\_userInterface**: [`FrontendUserInterface`](../../../ui/FrontendUserInterface/classes/FrontendUserInterface.md)

Defined in: [src/common/web/component/WebComponent.ts:69](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponent.ts#L69)

#### Inherited from

[`WebComponent`](../../../../../common/web/component/WebComponent/classes/WebComponent.md).[`_userInterface`](../../../../../common/web/component/WebComponent/classes/WebComponent.md#_userinterface)

***

### \_vueApp

> `protected` `readonly` **\_vueApp**: `App`

Defined in: [src/common/web/component/WebComponent.ts:70](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponent.ts#L70)

#### Inherited from

[`WebComponent`](../../../../../common/web/component/WebComponent/classes/WebComponent.md).[`_vueApp`](../../../../../common/web/component/WebComponent/classes/WebComponent.md#_vueapp)

## Accessors

### connectorsService

#### Get Signature

> **get** **connectorsService**(): [`Service`](../../../../../common/web/services/Service/classes/Service.md)

Defined in: [src/frontend/src/component/FrontendComponent.ts:127](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/component/FrontendComponent.ts#L127)

The connectors service.

##### Returns

[`Service`](../../../../../common/web/services/Service/classes/Service.md)

***

### data

#### Get Signature

> **get** **data**(): [`WebComponentData`](../../../../../common/web/component/WebComponentData/classes/WebComponentData.md)

Defined in: [src/common/web/component/WebComponent.ts:247](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponent.ts#L247)

A data helper object that stores useful component data and information.

##### Returns

[`WebComponentData`](../../../../../common/web/component/WebComponentData/classes/WebComponentData.md)

#### Inherited from

[`WebComponent`](../../../../../common/web/component/WebComponent/classes/WebComponent.md).[`data`](../../../../../common/web/component/WebComponent/classes/WebComponent.md#data)

***

### frontendService

#### Get Signature

> **get** **frontendService**(): [`Service`](../../../../../common/web/services/Service/classes/Service.md)

Defined in: [src/frontend/src/component/FrontendComponent.ts:107](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/component/FrontendComponent.ts#L107)

The main frontend service.

##### Returns

[`Service`](../../../../../common/web/services/Service/classes/Service.md)

***

### integrationScheme

#### Get Signature

> **get** **integrationScheme**(): [`IntegrationScheme`](../../../integration/IntegrationScheme/classes/IntegrationScheme.md)

Defined in: [src/frontend/src/component/FrontendComponent.ts:97](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/component/FrontendComponent.ts#L97)

The active integration scheme.

##### Returns

[`IntegrationScheme`](../../../integration/IntegrationScheme/classes/IntegrationScheme.md)

***

### metadataService

#### Get Signature

> **get** **metadataService**(): [`Service`](../../../../../common/web/services/Service/classes/Service.md)

Defined in: [src/frontend/src/component/FrontendComponent.ts:137](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/component/FrontendComponent.ts#L137)

The metadata service.

##### Returns

[`Service`](../../../../../common/web/services/Service/classes/Service.md)

***

### projectExportersService

#### Get Signature

> **get** **projectExportersService**(): [`Service`](../../../../../common/web/services/Service/classes/Service.md)

Defined in: [src/frontend/src/component/FrontendComponent.ts:167](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/component/FrontendComponent.ts#L167)

The project exporters service.

##### Returns

[`Service`](../../../../../common/web/services/Service/classes/Service.md)

***

### projectJobsService

#### Get Signature

> **get** **projectJobsService**(): [`Service`](../../../../../common/web/services/Service/classes/Service.md)

Defined in: [src/frontend/src/component/FrontendComponent.ts:157](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/component/FrontendComponent.ts#L157)

The project jobs service.

##### Returns

[`Service`](../../../../../common/web/services/Service/classes/Service.md)

***

### projectsService

#### Get Signature

> **get** **projectsService**(): [`Service`](../../../../../common/web/services/Service/classes/Service.md)

Defined in: [src/frontend/src/component/FrontendComponent.ts:147](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/component/FrontendComponent.ts#L147)

The projects service.

##### Returns

[`Service`](../../../../../common/web/services/Service/classes/Service.md)

***

### router

#### Get Signature

> **get** **router**(): `Router`

Defined in: [src/common/web/component/WebComponent.ts:254](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponent.ts#L254)

The global router.

##### Returns

`Router`

#### Inherited from

[`WebComponent`](../../../../../common/web/component/WebComponent/classes/WebComponent.md).[`router`](../../../../../common/web/component/WebComponent/classes/WebComponent.md#router)

***

### session

#### Get Signature

> **get** **session**(): [`Session`](../../../../../common/web/component/Session/classes/Session.md)

Defined in: [src/common/web/component/WebComponent.ts:240](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponent.ts#L240)

The client session.

##### Returns

[`Session`](../../../../../common/web/component/Session/classes/Session.md)

#### Inherited from

[`WebComponent`](../../../../../common/web/component/WebComponent/classes/WebComponent.md).[`session`](../../../../../common/web/component/WebComponent/classes/WebComponent.md#session)

***

### userInterface

#### Get Signature

> **get** **userInterface**(): `UserInterfaceType`

Defined in: [src/common/web/component/WebComponent.ts:261](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponent.ts#L261)

The global user interface.

##### Returns

`UserInterfaceType`

#### Inherited from

[`WebComponent`](../../../../../common/web/component/WebComponent/classes/WebComponent.md).[`userInterface`](../../../../../common/web/component/WebComponent/classes/WebComponent.md#userinterface)

***

### userService

#### Get Signature

> **get** **userService**(): [`Service`](../../../../../common/web/services/Service/classes/Service.md)

Defined in: [src/frontend/src/component/FrontendComponent.ts:117](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/component/FrontendComponent.ts#L117)

The user service.

##### Returns

[`Service`](../../../../../common/web/services/Service/classes/Service.md)

***

### vue

#### Get Signature

> **get** **vue**(): `App`

Defined in: [src/common/web/component/WebComponent.ts:268](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponent.ts#L268)

The global Vue application instance.

##### Returns

`App`

#### Inherited from

[`WebComponent`](../../../../../common/web/component/WebComponent/classes/WebComponent.md).[`vue`](../../../../../common/web/component/WebComponent/classes/WebComponent.md#vue)

***

### instance

#### Get Signature

> **get** `static` **instance**(): [`WebComponent`](../../../../../common/web/component/WebComponent/classes/WebComponent.md)

Defined in: [src/common/web/component/WebComponent.ts:290](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponent.ts#L290)

The global ``WebComponent`` instance.

##### Throws

Error - If no instance has been created.

##### Returns

[`WebComponent`](../../../../../common/web/component/WebComponent/classes/WebComponent.md)

#### Inherited from

[`WebComponent`](../../../../../common/web/component/WebComponent/classes/WebComponent.md).[`instance`](../../../../../common/web/component/WebComponent/classes/WebComponent.md#instance)

## Methods

### configureRoutes()

> `protected` **configureRoutes**(): `RouteRecordRaw`[]

Defined in: [src/common/web/component/WebComponent.ts:180](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponent.ts#L180)

Sets up routes for the Vue router.

#### Returns

`RouteRecordRaw`[]

- The routes as an array; return `null` if the router shouldn't be used.

#### Inherited from

[`WebComponent`](../../../../../common/web/component/WebComponent/classes/WebComponent.md).[`configureRoutes`](../../../../../common/web/component/WebComponent/classes/WebComponent.md#configureroutes)

***

### createService()

> **createService**\<`CtxType`\>(`name`, `initializer`, `contextType`): [`Service`](../../../../../common/web/services/Service/classes/Service.md)

Defined in: [src/common/web/component/WebComponent.ts:224](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponent.ts#L224)

Creates and registers a new service.

#### Type Parameters

##### CtxType

`CtxType` *extends* [`ServiceContext`](../../../../../common/web/services/ServiceContext/classes/ServiceContext.md)

#### Parameters

##### name

`string`

The name of the service.

##### initializer

A function called to registered message handlers etc. after the service has been created.

`null` | (`svc`) => `void`

##### contextType

[`Constructable`](../../../../../common/web/utils/Types/interfaces/Constructable.md)\<`CtxType`\> = `...`

Can be used to override the default ``ServiceContext`` type. All message handlers
     associated with the new service will then receive instances of this type for their service context.

#### Returns

[`Service`](../../../../../common/web/services/Service/classes/Service.md)

#### Inherited from

[`WebComponent`](../../../../../common/web/component/WebComponent/classes/WebComponent.md).[`createService`](../../../../../common/web/component/WebComponent/classes/WebComponent.md#createservice)

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

#### Inherited from

[`WebComponent`](../../../../../common/web/component/WebComponent/classes/WebComponent.md).[`mount`](../../../../../common/web/component/WebComponent/classes/WebComponent.md#mount)

***

### run()

> **run**(): `void`

Defined in: [src/frontend/src/component/FrontendComponent.ts:50](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/component/FrontendComponent.ts#L50)

Starts the component's execution cycles.

Notes:
    This method is automatically called by the framework.

#### Returns

`void`

#### Overrides

[`WebComponent`](../../../../../common/web/component/WebComponent/classes/WebComponent.md).[`run`](../../../../../common/web/component/WebComponent/classes/WebComponent.md#run)

***

### toString()

> **toString**(): `string`

Defined in: [src/common/web/component/WebComponent.ts:305](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponent.ts#L305)

#### Returns

`string`

- The string representation of this component.

#### Inherited from

[`WebComponent`](../../../../../common/web/component/WebComponent/classes/WebComponent.md).[`toString`](../../../../../common/web/component/WebComponent/classes/WebComponent.md#tostring)

***

### inject()

> `static` **inject**(): `FrontendComponent`

Defined in: [src/frontend/src/component/FrontendComponent.ts:179](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/component/FrontendComponent.ts#L179)

The global ``FrontendComponent`` instance via Vue's injection mechanism.

#### Returns

`FrontendComponent`

#### Throws

Error - If no instance has been created.

***

### injectComponent()

> `static` **injectComponent**\<`CompType`\>(): `CompType`

Defined in: [src/common/web/component/WebComponent.ts:277](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/WebComponent.ts#L277)

The global ``WebComponent`` instance via Vue's injection mechanism.

#### Type Parameters

##### CompType

`CompType` *extends* [`WebComponent`](../../../../../common/web/component/WebComponent/classes/WebComponent.md)\<[`UserInterface`](../../../../../common/web/ui/UserInterface/classes/UserInterface.md)\> = [`WebComponent`](../../../../../common/web/component/WebComponent/classes/WebComponent.md)\<[`UserInterface`](../../../../../common/web/ui/UserInterface/classes/UserInterface.md)\>

#### Returns

`CompType`

#### Throws

Error - If no instance has been created.

#### Inherited from

[`WebComponent`](../../../../../common/web/component/WebComponent/classes/WebComponent.md).[`injectComponent`](../../../../../common/web/component/WebComponent/classes/WebComponent.md#injectcomponent)

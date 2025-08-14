---
id: "frontend_src_component_FrontendComponent.FrontendComponent"
title: "Class: FrontendComponent"
sidebar_label: "FrontendComponent"
custom_edit_url: null
---

[frontend/src/component/FrontendComponent](../modules/frontend_src_component_FrontendComponent.md).FrontendComponent

The main frontend component class.

## Hierarchy

- [`WebComponent`](common_web_component_WebComponent.WebComponent.md)<[`FrontendUserInterface`](frontend_src_ui_FrontendUserInterface.FrontendUserInterface.md)\>

  ↳ **`FrontendComponent`**

## Constructors

### constructor

• **new FrontendComponent**(): [`FrontendComponent`](frontend_src_component_FrontendComponent.FrontendComponent.md)

#### Returns

[`FrontendComponent`](frontend_src_component_FrontendComponent.FrontendComponent.md)

#### Overrides

[WebComponent](common_web_component_WebComponent.WebComponent.md).[constructor](common_web_component_WebComponent.WebComponent.md#constructor)

#### Defined in

[src/frontend/src/component/FrontendComponent.ts:44](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/component/FrontendComponent.ts#L44)

## Properties

### \_connectorsService

• `Private` **\_connectorsService**: ``null`` \| [`Service`](common_web_services_Service.Service.md)<[`ServiceContext`](common_web_services_ServiceContext.ServiceContext.md)\> = `null`

#### Defined in

[src/frontend/src/component/FrontendComponent.ts:38](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/component/FrontendComponent.ts#L38)

___

### \_core

• `Protected` `Readonly` **\_core**: [`Core`](common_web_core_Core.Core.md)

#### Inherited from

[WebComponent](common_web_component_WebComponent.WebComponent.md).[_core](common_web_component_WebComponent.WebComponent.md#_core)

#### Defined in

[src/common/web/component/WebComponent.ts:66](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L66)

___

### \_data

• `Protected` `Readonly` **\_data**: [`WebComponentData`](common_web_component_WebComponentData.WebComponentData.md)

#### Inherited from

[WebComponent](common_web_component_WebComponent.WebComponent.md).[_data](common_web_component_WebComponent.WebComponent.md#_data)

#### Defined in

[src/common/web/component/WebComponent.ts:64](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L64)

___

### \_frontendService

• `Private` **\_frontendService**: ``null`` \| [`Service`](common_web_services_Service.Service.md)<[`ServiceContext`](common_web_services_ServiceContext.ServiceContext.md)\> = `null`

#### Defined in

[src/frontend/src/component/FrontendComponent.ts:36](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/component/FrontendComponent.ts#L36)

___

### \_integrationScheme

• `Private` **\_integrationScheme**: ``null`` \| [`IntegrationScheme`](frontend_src_integration_IntegrationScheme.IntegrationScheme.md) = `null`

#### Defined in

[src/frontend/src/component/FrontendComponent.ts:34](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/component/FrontendComponent.ts#L34)

___

### \_metadataService

• `Private` **\_metadataService**: ``null`` \| [`Service`](common_web_services_Service.Service.md)<[`ServiceContext`](common_web_services_ServiceContext.ServiceContext.md)\> = `null`

#### Defined in

[src/frontend/src/component/FrontendComponent.ts:39](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/component/FrontendComponent.ts#L39)

___

### \_projectExportersService

• `Private` **\_projectExportersService**: ``null`` \| [`Service`](common_web_services_Service.Service.md)<[`ServiceContext`](common_web_services_ServiceContext.ServiceContext.md)\> = `null`

#### Defined in

[src/frontend/src/component/FrontendComponent.ts:42](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/component/FrontendComponent.ts#L42)

___

### \_projectJobsService

• `Private` **\_projectJobsService**: ``null`` \| [`Service`](common_web_services_Service.Service.md)<[`ServiceContext`](common_web_services_ServiceContext.ServiceContext.md)\> = `null`

#### Defined in

[src/frontend/src/component/FrontendComponent.ts:41](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/component/FrontendComponent.ts#L41)

___

### \_projectsService

• `Private` **\_projectsService**: ``null`` \| [`Service`](common_web_services_Service.Service.md)<[`ServiceContext`](common_web_services_ServiceContext.ServiceContext.md)\> = `null`

#### Defined in

[src/frontend/src/component/FrontendComponent.ts:40](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/component/FrontendComponent.ts#L40)

___

### \_router

• `Protected` `Readonly` **\_router**: `Router`

#### Inherited from

[WebComponent](common_web_component_WebComponent.WebComponent.md).[_router](common_web_component_WebComponent.WebComponent.md#_router)

#### Defined in

[src/common/web/component/WebComponent.ts:67](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L67)

___

### \_session

• `Protected` `Readonly` **\_session**: [`Session`](common_web_component_Session.Session.md)

#### Inherited from

[WebComponent](common_web_component_WebComponent.WebComponent.md).[_session](common_web_component_WebComponent.WebComponent.md#_session)

#### Defined in

[src/common/web/component/WebComponent.ts:63](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L63)

___

### \_userInterface

• `Protected` `Readonly` **\_userInterface**: [`FrontendUserInterface`](frontend_src_ui_FrontendUserInterface.FrontendUserInterface.md)

#### Inherited from

[WebComponent](common_web_component_WebComponent.WebComponent.md).[_userInterface](common_web_component_WebComponent.WebComponent.md#_userinterface)

#### Defined in

[src/common/web/component/WebComponent.ts:69](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L69)

___

### \_userService

• `Private` **\_userService**: ``null`` \| [`Service`](common_web_services_Service.Service.md)<[`ServiceContext`](common_web_services_ServiceContext.ServiceContext.md)\> = `null`

#### Defined in

[src/frontend/src/component/FrontendComponent.ts:37](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/component/FrontendComponent.ts#L37)

___

### \_vueApp

• `Protected` `Readonly` **\_vueApp**: `App`<`any`\>

#### Inherited from

[WebComponent](common_web_component_WebComponent.WebComponent.md).[_vueApp](common_web_component_WebComponent.WebComponent.md#_vueapp)

#### Defined in

[src/common/web/component/WebComponent.ts:70](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L70)

## Accessors

### connectorsService

• `get` **connectorsService**(): [`Service`](common_web_services_Service.Service.md)<[`ServiceContext`](common_web_services_ServiceContext.ServiceContext.md)\>

The connectors service.

#### Returns

[`Service`](common_web_services_Service.Service.md)<[`ServiceContext`](common_web_services_ServiceContext.ServiceContext.md)\>

#### Defined in

[src/frontend/src/component/FrontendComponent.ts:127](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/component/FrontendComponent.ts#L127)

___

### data

• `get` **data**(): [`WebComponentData`](common_web_component_WebComponentData.WebComponentData.md)

A data helper object that stores useful component data and information.

#### Returns

[`WebComponentData`](common_web_component_WebComponentData.WebComponentData.md)

#### Inherited from

WebComponent.data

#### Defined in

[src/common/web/component/WebComponent.ts:247](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L247)

___

### frontendService

• `get` **frontendService**(): [`Service`](common_web_services_Service.Service.md)<[`ServiceContext`](common_web_services_ServiceContext.ServiceContext.md)\>

The main frontend service.

#### Returns

[`Service`](common_web_services_Service.Service.md)<[`ServiceContext`](common_web_services_ServiceContext.ServiceContext.md)\>

#### Defined in

[src/frontend/src/component/FrontendComponent.ts:107](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/component/FrontendComponent.ts#L107)

___

### integrationScheme

• `get` **integrationScheme**(): [`IntegrationScheme`](frontend_src_integration_IntegrationScheme.IntegrationScheme.md)

The active integration scheme.

#### Returns

[`IntegrationScheme`](frontend_src_integration_IntegrationScheme.IntegrationScheme.md)

#### Defined in

[src/frontend/src/component/FrontendComponent.ts:97](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/component/FrontendComponent.ts#L97)

___

### metadataService

• `get` **metadataService**(): [`Service`](common_web_services_Service.Service.md)<[`ServiceContext`](common_web_services_ServiceContext.ServiceContext.md)\>

The metadata service.

#### Returns

[`Service`](common_web_services_Service.Service.md)<[`ServiceContext`](common_web_services_ServiceContext.ServiceContext.md)\>

#### Defined in

[src/frontend/src/component/FrontendComponent.ts:137](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/component/FrontendComponent.ts#L137)

___

### projectExportersService

• `get` **projectExportersService**(): [`Service`](common_web_services_Service.Service.md)<[`ServiceContext`](common_web_services_ServiceContext.ServiceContext.md)\>

The project exporters service.

#### Returns

[`Service`](common_web_services_Service.Service.md)<[`ServiceContext`](common_web_services_ServiceContext.ServiceContext.md)\>

#### Defined in

[src/frontend/src/component/FrontendComponent.ts:167](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/component/FrontendComponent.ts#L167)

___

### projectJobsService

• `get` **projectJobsService**(): [`Service`](common_web_services_Service.Service.md)<[`ServiceContext`](common_web_services_ServiceContext.ServiceContext.md)\>

The project jobs service.

#### Returns

[`Service`](common_web_services_Service.Service.md)<[`ServiceContext`](common_web_services_ServiceContext.ServiceContext.md)\>

#### Defined in

[src/frontend/src/component/FrontendComponent.ts:157](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/component/FrontendComponent.ts#L157)

___

### projectsService

• `get` **projectsService**(): [`Service`](common_web_services_Service.Service.md)<[`ServiceContext`](common_web_services_ServiceContext.ServiceContext.md)\>

The projects service.

#### Returns

[`Service`](common_web_services_Service.Service.md)<[`ServiceContext`](common_web_services_ServiceContext.ServiceContext.md)\>

#### Defined in

[src/frontend/src/component/FrontendComponent.ts:147](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/component/FrontendComponent.ts#L147)

___

### router

• `get` **router**(): `Router`

The global router.

#### Returns

`Router`

#### Inherited from

WebComponent.router

#### Defined in

[src/common/web/component/WebComponent.ts:254](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L254)

___

### session

• `get` **session**(): [`Session`](common_web_component_Session.Session.md)

The client session.

#### Returns

[`Session`](common_web_component_Session.Session.md)

#### Inherited from

WebComponent.session

#### Defined in

[src/common/web/component/WebComponent.ts:240](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L240)

___

### userInterface

• `get` **userInterface**(): `UserInterfaceType`

The global user interface.

#### Returns

`UserInterfaceType`

#### Inherited from

WebComponent.userInterface

#### Defined in

[src/common/web/component/WebComponent.ts:261](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L261)

___

### userService

• `get` **userService**(): [`Service`](common_web_services_Service.Service.md)<[`ServiceContext`](common_web_services_ServiceContext.ServiceContext.md)\>

The user service.

#### Returns

[`Service`](common_web_services_Service.Service.md)<[`ServiceContext`](common_web_services_ServiceContext.ServiceContext.md)\>

#### Defined in

[src/frontend/src/component/FrontendComponent.ts:117](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/component/FrontendComponent.ts#L117)

___

### vue

• `get` **vue**(): `App`<`any`\>

The global Vue application instance.

#### Returns

`App`<`any`\>

#### Inherited from

WebComponent.vue

#### Defined in

[src/common/web/component/WebComponent.ts:268](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L268)

___

### instance

• `get` **instance**(): [`WebComponent`](common_web_component_WebComponent.WebComponent.md)<[`UserInterface`](common_web_ui_UserInterface.UserInterface.md)\>

The global ``WebComponent`` instance.

#### Returns

[`WebComponent`](common_web_component_WebComponent.WebComponent.md)<[`UserInterface`](common_web_ui_UserInterface.UserInterface.md)\>

**`Throws`**

Error - If no instance has been created.

#### Inherited from

WebComponent.instance

#### Defined in

[src/common/web/component/WebComponent.ts:290](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L290)

## Methods

### addFrontendSettings

▸ **addFrontendSettings**(): `void`

#### Returns

`void`

#### Defined in

[src/frontend/src/component/FrontendComponent.ts:72](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/component/FrontendComponent.ts#L72)

___

### configureRoutes

▸ **configureRoutes**(): `RouteRecordRaw`[]

Sets up routes for the Vue router.

#### Returns

`RouteRecordRaw`[]

- The routes as an array; return `null` if the router shouldn't be used.

#### Inherited from

[WebComponent](common_web_component_WebComponent.WebComponent.md).[configureRoutes](common_web_component_WebComponent.WebComponent.md#configureroutes)

#### Defined in

[src/common/web/component/WebComponent.ts:180](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L180)

___

### createService

▸ **createService**<`CtxType`\>(`name`, `initializer?`, `contextType?`): [`Service`](common_web_services_Service.Service.md)<[`ServiceContext`](common_web_services_ServiceContext.ServiceContext.md)\>

Creates and registers a new service.

#### Type parameters

| Name | Type |
| :------ | :------ |
| `CtxType` | extends [`ServiceContext`](common_web_services_ServiceContext.ServiceContext.md) |

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `name` | `string` | `undefined` | The name of the service. |
| `initializer` | ``null`` \| (`svc`: [`Service`](common_web_services_Service.Service.md)<[`ServiceContext`](common_web_services_ServiceContext.ServiceContext.md)\>) => `void` | `null` | A function called to registered message handlers etc. after the service has been created. |
| `contextType` | [`Constructable`](../interfaces/common_web_utils_Types.Constructable.md)<`CtxType`\> | `undefined` | Can be used to override the default ``ServiceContext`` type. All message handlers associated with the new service will then receive instances of this type for their service context. |

#### Returns

[`Service`](common_web_services_Service.Service.md)<[`ServiceContext`](common_web_services_ServiceContext.ServiceContext.md)\>

#### Inherited from

[WebComponent](common_web_component_WebComponent.WebComponent.md).[createService](common_web_component_WebComponent.WebComponent.md#createservice)

#### Defined in

[src/common/web/component/WebComponent.ts:224](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L224)

___

### mount

▸ **mount**(`appElement?`): `void`

Mounts the Vue application in the given element.

Notes:
    This method must be called immediately after creating the main component instance.

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `appElement` | `string` | `"#app"` | The HTML element ID used for mounting the root component. |

#### Returns

`void`

#### Inherited from

[WebComponent](common_web_component_WebComponent.WebComponent.md).[mount](common_web_component_WebComponent.WebComponent.md#mount)

#### Defined in

[src/common/web/component/WebComponent.ts:192](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L192)

___

### mountIntegrationScheme

▸ **mountIntegrationScheme**(): `void`

#### Returns

`void`

#### Defined in

[src/frontend/src/component/FrontendComponent.ts:76](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/component/FrontendComponent.ts#L76)

___

### run

▸ **run**(): `void`

Starts the component's execution cycles.

Notes:
    This method is automatically called by the framework.

#### Returns

`void`

#### Overrides

[WebComponent](common_web_component_WebComponent.WebComponent.md).[run](common_web_component_WebComponent.WebComponent.md#run)

#### Defined in

[src/frontend/src/component/FrontendComponent.ts:50](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/component/FrontendComponent.ts#L50)

___

### toString

▸ **toString**(): `string`

#### Returns

`string`

- The string representation of this component.

#### Inherited from

[WebComponent](common_web_component_WebComponent.WebComponent.md).[toString](common_web_component_WebComponent.WebComponent.md#tostring)

#### Defined in

[src/common/web/component/WebComponent.ts:305](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L305)

___

### inject

▸ **inject**(): [`FrontendComponent`](frontend_src_component_FrontendComponent.FrontendComponent.md)

The global ``FrontendComponent`` instance via Vue's injection mechanism.

#### Returns

[`FrontendComponent`](frontend_src_component_FrontendComponent.FrontendComponent.md)

**`Throws`**

Error - If no instance has been created.

#### Defined in

[src/frontend/src/component/FrontendComponent.ts:179](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/component/FrontendComponent.ts#L179)

___

### injectComponent

▸ **injectComponent**<`CompType`\>(): `CompType`

The global ``WebComponent`` instance via Vue's injection mechanism.

#### Type parameters

| Name | Type |
| :------ | :------ |
| `CompType` | extends [`WebComponent`](common_web_component_WebComponent.WebComponent.md)<[`UserInterface`](common_web_ui_UserInterface.UserInterface.md)\> = [`WebComponent`](common_web_component_WebComponent.WebComponent.md)<[`UserInterface`](common_web_ui_UserInterface.UserInterface.md)\> |

#### Returns

`CompType`

**`Throws`**

Error - If no instance has been created.

#### Inherited from

[WebComponent](common_web_component_WebComponent.WebComponent.md).[injectComponent](common_web_component_WebComponent.WebComponent.md#injectcomponent)

#### Defined in

[src/common/web/component/WebComponent.ts:277](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L277)

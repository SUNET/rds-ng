---
id: "common_web_component_WebComponent.WebComponent"
title: "Class: WebComponent<UserInterfaceType>"
sidebar_label: "WebComponent"
custom_edit_url: null
---

[common/web/component/WebComponent](../modules/common_web_component_WebComponent.md).WebComponent

Base class for all web components.

By default, an instance of ``UserInterfaceType`` is used to create the main UI handler. This can be overriden using the corresponding
template and constructor parameters.

Web applications are always based on this class. It mainly maintains an instance of the ``Core``, but also stores general information
about the application itself and the entire project.

## Type parameters

| Name | Type |
| :------ | :------ |
| `UserInterfaceType` | extends [`UserInterface`](common_web_ui_UserInterface.UserInterface.md) = [`UserInterface`](common_web_ui_UserInterface.UserInterface.md) |

## Hierarchy

- **`WebComponent`**

  ↳ [`FrontendComponent`](frontend_src_component_FrontendComponent.FrontendComponent.md)

## Constructors

### constructor

• **new WebComponent**<`UserInterfaceType`\>(`env`, `compID`, `appRoot`, `userInterfaceType?`): [`WebComponent`](common_web_component_WebComponent.WebComponent.md)<`UserInterfaceType`\>

#### Type parameters

| Name | Type |
| :------ | :------ |
| `UserInterfaceType` | extends [`UserInterface`](common_web_ui_UserInterface.UserInterface.md) = [`UserInterface`](common_web_ui_UserInterface.UserInterface.md) |

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `env` | [`SettingsContainer`](../modules/common_web_utils_config_Configuration.md#settingscontainer) | The global environment variables. |
| `compID` | [`UnitID`](common_web_utils_UnitID.UnitID.md) | The identifier of this component. |
| `appRoot` | [`VueComponent`](../modules/common_web_component_WebComponent.md#vuecomponent) | The root (main) application component. |
| `userInterfaceType` | [`Constructable`](../interfaces/common_web_utils_Types.Constructable.md)<`UserInterfaceType`\> | The type of the user interface class. |

#### Returns

[`WebComponent`](common_web_component_WebComponent.WebComponent.md)<`UserInterfaceType`\>

#### Defined in

[src/common/web/component/WebComponent.ts:78](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L78)

## Properties

### \_core

• `Protected` `Readonly` **\_core**: [`Core`](common_web_core_Core.Core.md)

#### Defined in

[src/common/web/component/WebComponent.ts:66](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L66)

___

### \_data

• `Protected` `Readonly` **\_data**: [`WebComponentData`](common_web_component_WebComponentData.WebComponentData.md)

#### Defined in

[src/common/web/component/WebComponent.ts:64](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L64)

___

### \_router

• `Protected` `Readonly` **\_router**: `Router`

#### Defined in

[src/common/web/component/WebComponent.ts:67](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L67)

___

### \_session

• `Protected` `Readonly` **\_session**: [`Session`](common_web_component_Session.Session.md)

#### Defined in

[src/common/web/component/WebComponent.ts:63](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L63)

___

### \_userInterface

• `Protected` `Readonly` **\_userInterface**: `UserInterfaceType`

#### Defined in

[src/common/web/component/WebComponent.ts:69](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L69)

___

### \_vueApp

• `Protected` `Readonly` **\_vueApp**: `App`<`any`\>

#### Defined in

[src/common/web/component/WebComponent.ts:70](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L70)

___

### \_injectionKey

▪ `Static` `Private` `Readonly` **\_injectionKey**: typeof [`_injectionKey`](common_web_component_WebComponent.WebComponent.md#_injectionkey)

#### Defined in

[src/common/web/component/WebComponent.ts:61](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L61)

___

### \_instance

▪ `Static` `Private` **\_instance**: ``null`` \| [`WebComponent`](common_web_component_WebComponent.WebComponent.md)<`any`\> = `null`

#### Defined in

[src/common/web/component/WebComponent.ts:60](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L60)

## Accessors

### data

• `get` **data**(): [`WebComponentData`](common_web_component_WebComponentData.WebComponentData.md)

A data helper object that stores useful component data and information.

#### Returns

[`WebComponentData`](common_web_component_WebComponentData.WebComponentData.md)

#### Defined in

[src/common/web/component/WebComponent.ts:247](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L247)

___

### router

• `get` **router**(): `Router`

The global router.

#### Returns

`Router`

#### Defined in

[src/common/web/component/WebComponent.ts:254](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L254)

___

### session

• `get` **session**(): [`Session`](common_web_component_Session.Session.md)

The client session.

#### Returns

[`Session`](common_web_component_Session.Session.md)

#### Defined in

[src/common/web/component/WebComponent.ts:240](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L240)

___

### userInterface

• `get` **userInterface**(): `UserInterfaceType`

The global user interface.

#### Returns

`UserInterfaceType`

#### Defined in

[src/common/web/component/WebComponent.ts:261](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L261)

___

### vue

• `get` **vue**(): `App`<`any`\>

The global Vue application instance.

#### Returns

`App`<`any`\>

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

#### Defined in

[src/common/web/component/WebComponent.ts:290](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L290)

## Methods

### configureDefaultRoutes

▸ **configureDefaultRoutes**(): `RouteRecordRaw`[]

#### Returns

`RouteRecordRaw`[]

#### Defined in

[src/common/web/component/WebComponent.ts:171](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L171)

___

### configureRoutes

▸ **configureRoutes**(): `RouteRecordRaw`[]

Sets up routes for the Vue router.

#### Returns

`RouteRecordRaw`[]

- The routes as an array; return `null` if the router shouldn't be used.

#### Defined in

[src/common/web/component/WebComponent.ts:180](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L180)

___

### createConfig

▸ **createConfig**(`env`): [`Configuration`](common_web_utils_config_Configuration.Configuration.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `env` | [`SettingsContainer`](../modules/common_web_utils_config_Configuration.md#settingscontainer) |

#### Returns

[`Configuration`](common_web_utils_config_Configuration.Configuration.md)

#### Defined in

[src/common/web/component/WebComponent.ts:106](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L106)

___

### createRouter

▸ **createRouter**(): `Router`

#### Returns

`Router`

#### Defined in

[src/common/web/component/WebComponent.ts:119](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L119)

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

#### Defined in

[src/common/web/component/WebComponent.ts:224](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L224)

___

### createUserInterface

▸ **createUserInterface**(`userInterfaceType`, `appRoot`): `UserInterfaceType`

#### Parameters

| Name | Type |
| :------ | :------ |
| `userInterfaceType` | [`Constructable`](../interfaces/common_web_utils_Types.Constructable.md)<`UserInterfaceType`\> |
| `appRoot` | [`VueComponent`](../modules/common_web_component_WebComponent.md#vuecomponent) |

#### Returns

`UserInterfaceType`

#### Defined in

[src/common/web/component/WebComponent.ts:126](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L126)

___

### createVueApp

▸ **createVueApp**(): `App`<`any`\>

#### Returns

`App`<`any`\>

#### Defined in

[src/common/web/component/WebComponent.ts:130](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L130)

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

#### Defined in

[src/common/web/component/WebComponent.ts:192](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L192)

___

### run

▸ **run**(): `void`

Starts the component's execution cycles.

Notes:
    This method is automatically called by the framework.

#### Returns

`void`

#### Defined in

[src/common/web/component/WebComponent.ts:202](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L202)

___

### sanitizeComponentID

▸ **sanitizeComponentID**(`compID`): [`UnitID`](common_web_utils_UnitID.UnitID.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `compID` | [`UnitID`](common_web_utils_UnitID.UnitID.md) |

#### Returns

[`UnitID`](common_web_utils_UnitID.UnitID.md)

#### Defined in

[src/common/web/component/WebComponent.ts:297](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L297)

___

### toString

▸ **toString**(): `string`

#### Returns

`string`

- The string representation of this component.

#### Defined in

[src/common/web/component/WebComponent.ts:305](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L305)

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

#### Defined in

[src/common/web/component/WebComponent.ts:277](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponent.ts#L277)

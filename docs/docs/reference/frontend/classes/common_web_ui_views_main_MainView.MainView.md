---
id: "common_web_ui_views_main_MainView.MainView"
title: "Class: MainView"
sidebar_label: "MainView"
custom_edit_url: null
---

[common/web/ui/views/main/MainView](../modules/common_web_ui_views_main_MainView.md).MainView

The main view enclosing/containing the entire component.

## Hierarchy

- [`View`](common_web_ui_views_View.View.md)

  ↳ **`MainView`**

## Constructors

### constructor

• **new MainView**(`router`, `appRoot`, `routeOptions?`, `subViews?`): [`MainView`](common_web_ui_views_main_MainView.MainView.md)

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `router` | `Router` | The main Vue router. |
| `appRoot` | [`VueComponent`](../modules/common_web_component_WebComponent.md#vuecomponent) | The root (main) application component. |
| `routeOptions?` | `RouteRecordRaw` | Additional route options. |
| `subViews?` | [`View`](common_web_ui_views_View.View.md)[] | Optional sub-views. |

#### Returns

[`MainView`](common_web_ui_views_main_MainView.MainView.md)

#### Overrides

[View](common_web_ui_views_View.View.md).[constructor](common_web_ui_views_View.View.md#constructor)

#### Defined in

[src/common/web/ui/views/main/MainView.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/views/main/MainView.ts#L23)

## Properties

### \_appRoot

• `Private` `Readonly` **\_appRoot**: [`VueComponent`](../modules/common_web_component_WebComponent.md#vuecomponent)

#### Defined in

[src/common/web/ui/views/main/MainView.ts:15](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/views/main/MainView.ts#L15)

___

### \_routeName

• `Protected` `Readonly` **\_routeName**: `string`

#### Inherited from

[View](common_web_ui_views_View.View.md).[_routeName](common_web_ui_views_View.View.md#_routename)

#### Defined in

[src/common/web/ui/views/View.ts:11](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/views/View.ts#L11)

___

### \_routeOptions

• `Protected` `Readonly` **\_routeOptions**: `undefined` \| `RouteRecordRaw`

#### Inherited from

[View](common_web_ui_views_View.View.md).[_routeOptions](common_web_ui_views_View.View.md#_routeoptions)

#### Defined in

[src/common/web/ui/views/View.ts:12](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/views/View.ts#L12)

___

### \_router

• `Protected` `Readonly` **\_router**: `Router`

#### Inherited from

[View](common_web_ui_views_View.View.md).[_router](common_web_ui_views_View.View.md#_router)

#### Defined in

[src/common/web/ui/views/View.ts:10](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/views/View.ts#L10)

___

### \_subViews

• `Protected` `Readonly` **\_subViews**: `undefined` \| [`View`](common_web_ui_views_View.View.md)[]

#### Inherited from

[View](common_web_ui_views_View.View.md).[_subViews](common_web_ui_views_View.View.md#_subviews)

#### Defined in

[src/common/web/ui/views/View.ts:14](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/views/View.ts#L14)

## Accessors

### name

• `get` **name**(): `string`

The route name of this view.

#### Returns

`string`

#### Inherited from

View.name

#### Defined in

[src/common/web/ui/views/View.ts:72](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/views/View.ts#L72)

___

### subViews

• `get` **subViews**(): [`View`](common_web_ui_views_View.View.md)[]

The sub-views of the views.

#### Returns

[`View`](common_web_ui_views_View.View.md)[]

#### Inherited from

View.subViews

#### Defined in

[src/common/web/ui/views/View.ts:79](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/views/View.ts#L79)

## Methods

### defineRoute

▸ **defineRoute**(): `RouteRecordRaw`

Defines the route for this view.

#### Returns

`RouteRecordRaw`

#### Overrides

[View](common_web_ui_views_View.View.md).[defineRoute](common_web_ui_views_View.View.md#defineroute)

#### Defined in

[src/common/web/ui/views/main/MainView.ts:29](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/views/main/MainView.ts#L29)

___

### getStateComponent

▸ **getStateComponent**(`state`): [`VueComponent`](../modules/common_web_component_WebComponent.md#vuecomponent)

Get the Vue component for the specified global commponent state.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `state` | [`ComponentState`](../enums/common_web_data_stores_ComponentStore.ComponentState.md) | The global component state. |

#### Returns

[`VueComponent`](../modules/common_web_component_WebComponent.md#vuecomponent)

**`Throws`**

Error - If the component state is unknown.

#### Defined in

[src/common/web/ui/views/main/MainView.ts:44](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/views/main/MainView.ts#L44)

___

### mountRoute

▸ **mountRoute**(`router`): `void`

#### Parameters

| Name | Type |
| :------ | :------ |
| `router` | `Router` |

#### Returns

`void`

#### Inherited from

[View](common_web_ui_views_View.View.md).[mountRoute](common_web_ui_views_View.View.md#mountroute)

#### Defined in

[src/common/web/ui/views/View.ts:32](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/views/View.ts#L32)

___

### navigateTo

▸ **navigateTo**(`replace?`, `query?`, `params?`): `void`

Navigates to (= activates) this view.

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `replace` | `boolean` | `false` | Whether to replace the current browsing history entry. |
| `query?` | `LocationQueryRaw` | `undefined` | Additional query (URL) parameters. |
| `params?` | `RouteParamsRawGeneric` | `undefined` | Additional URL placeholder parameters. |

#### Returns

`void`

- A promise that can be used to react to page load events.

#### Inherited from

[View](common_web_ui_views_View.View.md).[navigateTo](common_web_ui_views_View.View.md#navigateto)

#### Defined in

[src/common/web/ui/views/View.ts:64](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/views/View.ts#L64)

___

### route

▸ **route**(): `RouteRecordRaw`

Gets the route of this view.

#### Returns

`RouteRecordRaw`

#### Inherited from

[View](common_web_ui_views_View.View.md).[route](common_web_ui_views_View.View.md#route)

#### Defined in

[src/common/web/ui/views/View.ts:39](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/views/View.ts#L39)

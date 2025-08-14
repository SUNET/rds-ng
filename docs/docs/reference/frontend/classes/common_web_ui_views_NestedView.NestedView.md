---
id: "common_web_ui_views_NestedView.NestedView"
title: "Class: NestedView"
sidebar_label: "NestedView"
custom_edit_url: null
---

[common/web/ui/views/NestedView](../modules/common_web_ui_views_NestedView.md).NestedView

A specialized nested view.

## Hierarchy

- [`View`](common_web_ui_views_View.View.md)

  ↳ **`NestedView`**

  ↳↳ [`FrontendView`](frontend_src_ui_views_frontend_FrontendView.FrontendView.md)

## Constructors

### constructor

• **new NestedView**(`router`, `name`, `routeOptions?`, `subViews?`): [`NestedView`](common_web_ui_views_NestedView.NestedView.md)

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `router` | `Router` | The Vue router. |
| `name` | `string` | The route name for this view. |
| `routeOptions?` | `RouteRecordRaw` | Additional route options. |
| `subViews?` | [`View`](common_web_ui_views_View.View.md)[] | Optional sub-views of this view. |

#### Returns

[`NestedView`](common_web_ui_views_NestedView.NestedView.md)

#### Inherited from

[View](common_web_ui_views_View.View.md).[constructor](common_web_ui_views_View.View.md#constructor)

#### Defined in

[src/common/web/ui/views/View.ts:22](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/views/View.ts#L22)

## Properties

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

#### Inherited from

[View](common_web_ui_views_View.View.md).[defineRoute](common_web_ui_views_View.View.md#defineroute)

#### Defined in

[src/common/web/ui/views/View.ts:53](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/views/View.ts#L53)

___

### mountRoute

▸ **mountRoute**(`router`): `void`

#### Parameters

| Name | Type |
| :------ | :------ |
| `router` | `Router` |

#### Returns

`void`

#### Overrides

[View](common_web_ui_views_View.View.md).[mountRoute](common_web_ui_views_View.View.md#mountroute)

#### Defined in

[src/common/web/ui/views/NestedView.ts:9](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/views/NestedView.ts#L9)

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

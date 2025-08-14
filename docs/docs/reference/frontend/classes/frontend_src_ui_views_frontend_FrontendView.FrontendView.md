---
id: "frontend_src_ui_views_frontend_FrontendView.FrontendView"
title: "Class: FrontendView"
sidebar_label: "FrontendView"
custom_edit_url: null
---

[frontend/src/ui/views/frontend/FrontendView](../modules/frontend_src_ui_views_frontend_FrontendView.md).FrontendView

The main view enclosing/containing the entire component.

## Hierarchy

- [`NestedView`](common_web_ui_views_NestedView.NestedView.md)

  ↳ **`FrontendView`**

## Constructors

### constructor

• **new FrontendView**(`router`): [`FrontendView`](frontend_src_ui_views_frontend_FrontendView.FrontendView.md)

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `router` | `Router` | The main Vue router. |

#### Returns

[`FrontendView`](frontend_src_ui_views_frontend_FrontendView.FrontendView.md)

#### Overrides

[NestedView](common_web_ui_views_NestedView.NestedView.md).[constructor](common_web_ui_views_NestedView.NestedView.md#constructor)

#### Defined in

[src/frontend/src/ui/views/frontend/FrontendView.ts:12](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/views/frontend/FrontendView.ts#L12)

## Properties

### \_routeName

• `Protected` `Readonly` **\_routeName**: `string`

#### Inherited from

[NestedView](common_web_ui_views_NestedView.NestedView.md).[_routeName](common_web_ui_views_NestedView.NestedView.md#_routename)

#### Defined in

[src/common/web/ui/views/View.ts:11](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/views/View.ts#L11)

___

### \_routeOptions

• `Protected` `Readonly` **\_routeOptions**: `undefined` \| `RouteRecordRaw`

#### Inherited from

[NestedView](common_web_ui_views_NestedView.NestedView.md).[_routeOptions](common_web_ui_views_NestedView.NestedView.md#_routeoptions)

#### Defined in

[src/common/web/ui/views/View.ts:12](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/views/View.ts#L12)

___

### \_router

• `Protected` `Readonly` **\_router**: `Router`

#### Inherited from

[NestedView](common_web_ui_views_NestedView.NestedView.md).[_router](common_web_ui_views_NestedView.NestedView.md#_router)

#### Defined in

[src/common/web/ui/views/View.ts:10](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/views/View.ts#L10)

___

### \_subViews

• `Protected` `Readonly` **\_subViews**: `undefined` \| [`View`](common_web_ui_views_View.View.md)[]

#### Inherited from

[NestedView](common_web_ui_views_NestedView.NestedView.md).[_subViews](common_web_ui_views_NestedView.NestedView.md#_subviews)

#### Defined in

[src/common/web/ui/views/View.ts:14](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/views/View.ts#L14)

## Accessors

### name

• `get` **name**(): `string`

The route name of this view.

#### Returns

`string`

#### Inherited from

NestedView.name

#### Defined in

[src/common/web/ui/views/View.ts:72](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/views/View.ts#L72)

___

### subViews

• `get` **subViews**(): [`View`](common_web_ui_views_View.View.md)[]

The sub-views of the views.

#### Returns

[`View`](common_web_ui_views_View.View.md)[]

#### Inherited from

NestedView.subViews

#### Defined in

[src/common/web/ui/views/View.ts:79](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/views/View.ts#L79)

___

### rootPath

• `get` **rootPath**(): `string`

The root path of the frontend.

#### Returns

`string`

#### Defined in

[src/frontend/src/ui/views/frontend/FrontendView.ts:30](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/views/frontend/FrontendView.ts#L30)

## Methods

### defineRoute

▸ **defineRoute**(): `RouteRecordRaw`

Defines the route for this view.

#### Returns

`RouteRecordRaw`

#### Overrides

[NestedView](common_web_ui_views_NestedView.NestedView.md).[defineRoute](common_web_ui_views_NestedView.NestedView.md#defineroute)

#### Defined in

[src/frontend/src/ui/views/frontend/FrontendView.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/views/frontend/FrontendView.ts#L19)

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

[NestedView](common_web_ui_views_NestedView.NestedView.md).[mountRoute](common_web_ui_views_NestedView.NestedView.md#mountroute)

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

[NestedView](common_web_ui_views_NestedView.NestedView.md).[navigateTo](common_web_ui_views_NestedView.NestedView.md#navigateto)

#### Defined in

[src/common/web/ui/views/View.ts:64](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/views/View.ts#L64)

___

### route

▸ **route**(): `RouteRecordRaw`

Gets the route of this view.

#### Returns

`RouteRecordRaw`

#### Inherited from

[NestedView](common_web_ui_views_NestedView.NestedView.md).[route](common_web_ui_views_NestedView.NestedView.md#route)

#### Defined in

[src/common/web/ui/views/View.ts:39](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/views/View.ts#L39)

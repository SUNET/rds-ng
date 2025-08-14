---
id: "common_web_ui_views_View.View"
title: "Class: View"
sidebar_label: "View"
custom_edit_url: null
---

[common/web/ui/views/View](../modules/common_web_ui_views_View.md).View

A class to help with routed views.

This class does not represent a view *per se*, it is only used to work with the corresponding view.
It is therefore safe to instantiate this class and use its functions, as this doesn't automatically create a new view.

## Hierarchy

- **`View`**

  ↳ [`NestedView`](common_web_ui_views_NestedView.NestedView.md)

  ↳ [`MainView`](common_web_ui_views_main_MainView.MainView.md)

## Constructors

### constructor

• **new View**(`router`, `name`, `routeOptions?`, `subViews?`): [`View`](common_web_ui_views_View.View.md)

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `router` | `Router` | The Vue router. |
| `name` | `string` | The route name for this view. |
| `routeOptions?` | `RouteRecordRaw` | Additional route options. |
| `subViews?` | [`View`](common_web_ui_views_View.View.md)[] | Optional sub-views of this view. |

#### Returns

[`View`](common_web_ui_views_View.View.md)

#### Defined in

[src/common/web/ui/views/View.ts:22](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/views/View.ts#L22)

## Properties

### \_routeName

• `Protected` `Readonly` **\_routeName**: `string`

#### Defined in

[src/common/web/ui/views/View.ts:11](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/views/View.ts#L11)

___

### \_routeOptions

• `Protected` `Readonly` **\_routeOptions**: `undefined` \| `RouteRecordRaw`

#### Defined in

[src/common/web/ui/views/View.ts:12](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/views/View.ts#L12)

___

### \_router

• `Protected` `Readonly` **\_router**: `Router`

#### Defined in

[src/common/web/ui/views/View.ts:10](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/views/View.ts#L10)

___

### \_subViews

• `Protected` `Readonly` **\_subViews**: `undefined` \| [`View`](common_web_ui_views_View.View.md)[]

#### Defined in

[src/common/web/ui/views/View.ts:14](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/views/View.ts#L14)

## Accessors

### name

• `get` **name**(): `string`

The route name of this view.

#### Returns

`string`

#### Defined in

[src/common/web/ui/views/View.ts:72](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/views/View.ts#L72)

___

### subViews

• `get` **subViews**(): [`View`](common_web_ui_views_View.View.md)[]

The sub-views of the views.

#### Returns

[`View`](common_web_ui_views_View.View.md)[]

#### Defined in

[src/common/web/ui/views/View.ts:79](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/views/View.ts#L79)

## Methods

### defineRoute

▸ **defineRoute**(): `RouteRecordRaw`

Defines the route for this view.

#### Returns

`RouteRecordRaw`

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

#### Defined in

[src/common/web/ui/views/View.ts:64](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/views/View.ts#L64)

___

### route

▸ **route**(): `RouteRecordRaw`

Gets the route of this view.

#### Returns

`RouteRecordRaw`

#### Defined in

[src/common/web/ui/views/View.ts:39](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/views/View.ts#L39)

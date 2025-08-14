---
id: "frontend_src_ui_FrontendUserInterface.FrontendUserInterface"
title: "Class: FrontendUserInterface"
sidebar_label: "FrontendUserInterface"
custom_edit_url: null
---

[frontend/src/ui/FrontendUserInterface](../modules/frontend_src_ui_FrontendUserInterface.md).FrontendUserInterface

Class for frontend-specific user interface handling.

## Hierarchy

- [`UserInterface`](common_web_ui_UserInterface.UserInterface.md)

  ↳ **`FrontendUserInterface`**

## Constructors

### constructor

• **new FrontendUserInterface**(`router`, `appRoot`): [`FrontendUserInterface`](frontend_src_ui_FrontendUserInterface.FrontendUserInterface.md)

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `router` | `Router` | The Vue router. |
| `appRoot` | [`VueComponent`](../modules/common_web_component_WebComponent.md#vuecomponent) | The root (main) application component. |

#### Returns

[`FrontendUserInterface`](frontend_src_ui_FrontendUserInterface.FrontendUserInterface.md)

#### Overrides

[UserInterface](common_web_ui_UserInterface.UserInterface.md).[constructor](common_web_ui_UserInterface.UserInterface.md#constructor)

#### Defined in

[src/frontend/src/ui/FrontendUserInterface.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/FrontendUserInterface.ts#L19)

## Properties

### \_frontendView

• `Private` `Readonly` **\_frontendView**: [`FrontendView`](frontend_src_ui_views_frontend_FrontendView.FrontendView.md)

#### Defined in

[src/frontend/src/ui/FrontendUserInterface.ts:13](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/FrontendUserInterface.ts#L13)

___

### \_mainView

• `Protected` `Readonly` **\_mainView**: [`MainView`](common_web_ui_views_main_MainView.MainView.md)

#### Inherited from

[UserInterface](common_web_ui_UserInterface.UserInterface.md).[_mainView](common_web_ui_UserInterface.UserInterface.md#_mainview)

#### Defined in

[src/common/web/ui/UserInterface.ts:12](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/UserInterface.ts#L12)

## Accessors

### frontendView

• `get` **frontendView**(): [`FrontendView`](frontend_src_ui_views_frontend_FrontendView.FrontendView.md)

The frontend view.

#### Returns

[`FrontendView`](frontend_src_ui_views_frontend_FrontendView.FrontendView.md)

#### Defined in

[src/frontend/src/ui/FrontendUserInterface.ts:39](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/FrontendUserInterface.ts#L39)

___

### mainView

• `get` **mainView**(): [`MainView`](common_web_ui_views_main_MainView.MainView.md)

The main view.

#### Returns

[`MainView`](common_web_ui_views_main_MainView.MainView.md)

#### Inherited from

UserInterface.mainView

#### Defined in

[src/common/web/ui/UserInterface.ts:43](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/UserInterface.ts#L43)

## Methods

### configureMainRoute

▸ **configureMainRoute**(): `undefined` \| `RouteRecordRaw`

Supply additional options for the main route.

#### Returns

`undefined` \| `RouteRecordRaw`

- Additional route options.

#### Overrides

[UserInterface](common_web_ui_UserInterface.UserInterface.md).[configureMainRoute](common_web_ui_UserInterface.UserInterface.md#configuremainroute)

#### Defined in

[src/frontend/src/ui/FrontendUserInterface.ts:26](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/FrontendUserInterface.ts#L26)

___

### createSubViews

▸ **createSubViews**(`router`): [`View`](common_web_ui_views_View.View.md)[]

Creates additional sub-views of the main view.

#### Parameters

| Name | Type |
| :------ | :------ |
| `router` | `Router` |

#### Returns

[`View`](common_web_ui_views_View.View.md)[]

- An array of all direct sub-views.

#### Overrides

[UserInterface](common_web_ui_UserInterface.UserInterface.md).[createSubViews](common_web_ui_UserInterface.UserInterface.md#createsubviews)

#### Defined in

[src/frontend/src/ui/FrontendUserInterface.ts:32](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/frontend/src/ui/FrontendUserInterface.ts#L32)

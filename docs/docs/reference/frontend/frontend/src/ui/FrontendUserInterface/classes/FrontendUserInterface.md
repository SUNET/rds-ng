# Class: FrontendUserInterface

Defined in: [src/frontend/src/ui/FrontendUserInterface.ts:12](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/FrontendUserInterface.ts#L12)

Class for frontend-specific user interface handling.

## Extends

- [`UserInterface`](../../../../../common/web/ui/UserInterface/classes/UserInterface.md)

## Constructors

### Constructor

> **new FrontendUserInterface**(`router`, `appRoot`): `FrontendUserInterface`

Defined in: [src/frontend/src/ui/FrontendUserInterface.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/FrontendUserInterface.ts#L19)

#### Parameters

##### router

`Router`

The Vue router.

##### appRoot

[`VueComponent`](../../../../../common/web/component/WebComponent/type-aliases/VueComponent.md)

The root (main) application component.

#### Returns

`FrontendUserInterface`

#### Overrides

[`UserInterface`](../../../../../common/web/ui/UserInterface/classes/UserInterface.md).[`constructor`](../../../../../common/web/ui/UserInterface/classes/UserInterface.md#constructor)

## Properties

### \_mainView

> `protected` `readonly` **\_mainView**: [`MainView`](../../../../../common/web/ui/views/main/MainView/classes/MainView.md)

Defined in: [src/common/web/ui/UserInterface.ts:12](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/UserInterface.ts#L12)

#### Inherited from

[`UserInterface`](../../../../../common/web/ui/UserInterface/classes/UserInterface.md).[`_mainView`](../../../../../common/web/ui/UserInterface/classes/UserInterface.md#_mainview)

## Accessors

### frontendView

#### Get Signature

> **get** **frontendView**(): [`FrontendView`](../../views/frontend/FrontendView/classes/FrontendView.md)

Defined in: [src/frontend/src/ui/FrontendUserInterface.ts:39](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/FrontendUserInterface.ts#L39)

The frontend view.

##### Returns

[`FrontendView`](../../views/frontend/FrontendView/classes/FrontendView.md)

***

### mainView

#### Get Signature

> **get** **mainView**(): [`MainView`](../../../../../common/web/ui/views/main/MainView/classes/MainView.md)

Defined in: [src/common/web/ui/UserInterface.ts:43](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/UserInterface.ts#L43)

The main view.

##### Returns

[`MainView`](../../../../../common/web/ui/views/main/MainView/classes/MainView.md)

#### Inherited from

[`UserInterface`](../../../../../common/web/ui/UserInterface/classes/UserInterface.md).[`mainView`](../../../../../common/web/ui/UserInterface/classes/UserInterface.md#mainview)

## Methods

### configureMainRoute()

> `protected` **configureMainRoute**(): `undefined` \| `RouteRecordRaw`

Defined in: [src/frontend/src/ui/FrontendUserInterface.ts:26](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/FrontendUserInterface.ts#L26)

Supply additional options for the main route.

#### Returns

`undefined` \| `RouteRecordRaw`

- Additional route options.

#### Overrides

[`UserInterface`](../../../../../common/web/ui/UserInterface/classes/UserInterface.md).[`configureMainRoute`](../../../../../common/web/ui/UserInterface/classes/UserInterface.md#configuremainroute)

***

### createSubViews()

> `protected` **createSubViews**(`router`): [`View`](../../../../../common/web/ui/views/View/classes/View.md)[]

Defined in: [src/frontend/src/ui/FrontendUserInterface.ts:32](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/FrontendUserInterface.ts#L32)

Creates additional sub-views of the main view.

#### Parameters

##### router

`Router`

#### Returns

[`View`](../../../../../common/web/ui/views/View/classes/View.md)[]

- An array of all direct sub-views.

#### Overrides

[`UserInterface`](../../../../../common/web/ui/UserInterface/classes/UserInterface.md).[`createSubViews`](../../../../../common/web/ui/UserInterface/classes/UserInterface.md#createsubviews)

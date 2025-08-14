# Class: UserInterface

Defined in: [src/common/web/ui/UserInterface.ts:11](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/UserInterface.ts#L11)

Class for overall user interface handling.

## Extended by

- [`FrontendUserInterface`](../../../../../frontend/src/ui/FrontendUserInterface/classes/FrontendUserInterface.md)

## Constructors

### Constructor

> **new UserInterface**(`router`, `appRoot`): `UserInterface`

Defined in: [src/common/web/ui/UserInterface.ts:18](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/UserInterface.ts#L18)

#### Parameters

##### router

`Router`

The Vue router.

##### appRoot

[`VueComponent`](../../../component/WebComponent/type-aliases/VueComponent.md)

The root (main) application component.

#### Returns

`UserInterface`

## Properties

### \_mainView

> `protected` `readonly` **\_mainView**: [`MainView`](../../views/main/MainView/classes/MainView.md)

Defined in: [src/common/web/ui/UserInterface.ts:12](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/UserInterface.ts#L12)

## Accessors

### mainView

#### Get Signature

> **get** **mainView**(): [`MainView`](../../views/main/MainView/classes/MainView.md)

Defined in: [src/common/web/ui/UserInterface.ts:43](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/UserInterface.ts#L43)

The main view.

##### Returns

[`MainView`](../../views/main/MainView/classes/MainView.md)

## Methods

### configureMainRoute()

> `protected` **configureMainRoute**(): `undefined` \| `RouteRecordRaw`

Defined in: [src/common/web/ui/UserInterface.ts:27](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/UserInterface.ts#L27)

Supply additional options for the main route.

#### Returns

`undefined` \| `RouteRecordRaw`

- Additional route options.

***

### createSubViews()

> `protected` **createSubViews**(`router`): [`View`](../../views/View/classes/View.md)[]

Defined in: [src/common/web/ui/UserInterface.ts:36](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/UserInterface.ts#L36)

Creates additional sub-views of the main view.

#### Parameters

##### router

`Router`

#### Returns

[`View`](../../views/View/classes/View.md)[]

- An array of all direct sub-views.

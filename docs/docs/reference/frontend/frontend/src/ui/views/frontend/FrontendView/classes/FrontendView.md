# Class: FrontendView

Defined in: [src/frontend/src/ui/views/frontend/FrontendView.ts:8](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/views/frontend/FrontendView.ts#L8)

The main view enclosing/containing the entire component.

## Extends

- [`NestedView`](../../../../../../../common/web/ui/views/NestedView/classes/NestedView.md)

## Constructors

### Constructor

> **new FrontendView**(`router`): `FrontendView`

Defined in: [src/frontend/src/ui/views/frontend/FrontendView.ts:12](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/views/frontend/FrontendView.ts#L12)

#### Parameters

##### router

`Router`

The main Vue router.

#### Returns

`FrontendView`

#### Overrides

[`NestedView`](../../../../../../../common/web/ui/views/NestedView/classes/NestedView.md).[`constructor`](../../../../../../../common/web/ui/views/NestedView/classes/NestedView.md#constructor)

## Properties

### \_routeName

> `protected` `readonly` **\_routeName**: `string`

Defined in: [src/common/web/ui/views/View.ts:11](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/views/View.ts#L11)

#### Inherited from

[`NestedView`](../../../../../../../common/web/ui/views/NestedView/classes/NestedView.md).[`_routeName`](../../../../../../../common/web/ui/views/NestedView/classes/NestedView.md#_routename)

***

### \_routeOptions

> `protected` `readonly` **\_routeOptions**: `undefined` \| `RouteRecordRaw`

Defined in: [src/common/web/ui/views/View.ts:12](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/views/View.ts#L12)

#### Inherited from

[`NestedView`](../../../../../../../common/web/ui/views/NestedView/classes/NestedView.md).[`_routeOptions`](../../../../../../../common/web/ui/views/NestedView/classes/NestedView.md#_routeoptions)

***

### \_router

> `protected` `readonly` **\_router**: `Router`

Defined in: [src/common/web/ui/views/View.ts:10](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/views/View.ts#L10)

#### Inherited from

[`NestedView`](../../../../../../../common/web/ui/views/NestedView/classes/NestedView.md).[`_router`](../../../../../../../common/web/ui/views/NestedView/classes/NestedView.md#_router)

***

### \_subViews

> `protected` `readonly` **\_subViews**: `undefined` \| [`View`](../../../../../../../common/web/ui/views/View/classes/View.md)[]

Defined in: [src/common/web/ui/views/View.ts:14](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/views/View.ts#L14)

#### Inherited from

[`NestedView`](../../../../../../../common/web/ui/views/NestedView/classes/NestedView.md).[`_subViews`](../../../../../../../common/web/ui/views/NestedView/classes/NestedView.md#_subviews)

## Accessors

### name

#### Get Signature

> **get** **name**(): `string`

Defined in: [src/common/web/ui/views/View.ts:72](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/views/View.ts#L72)

The route name of this view.

##### Returns

`string`

#### Inherited from

[`NestedView`](../../../../../../../common/web/ui/views/NestedView/classes/NestedView.md).[`name`](../../../../../../../common/web/ui/views/NestedView/classes/NestedView.md#name)

***

### subViews

#### Get Signature

> **get** **subViews**(): [`View`](../../../../../../../common/web/ui/views/View/classes/View.md)[]

Defined in: [src/common/web/ui/views/View.ts:79](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/views/View.ts#L79)

The sub-views of the views.

##### Returns

[`View`](../../../../../../../common/web/ui/views/View/classes/View.md)[]

#### Inherited from

[`NestedView`](../../../../../../../common/web/ui/views/NestedView/classes/NestedView.md).[`subViews`](../../../../../../../common/web/ui/views/NestedView/classes/NestedView.md#subviews)

***

### rootPath

#### Get Signature

> **get** `static` **rootPath**(): `string`

Defined in: [src/frontend/src/ui/views/frontend/FrontendView.ts:30](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/views/frontend/FrontendView.ts#L30)

The root path of the frontend.

##### Returns

`string`

## Methods

### defineRoute()

> `protected` **defineRoute**(): `RouteRecordRaw`

Defined in: [src/frontend/src/ui/views/frontend/FrontendView.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/views/frontend/FrontendView.ts#L19)

Defines the route for this view.

#### Returns

`RouteRecordRaw`

#### Overrides

[`NestedView`](../../../../../../../common/web/ui/views/NestedView/classes/NestedView.md).[`defineRoute`](../../../../../../../common/web/ui/views/NestedView/classes/NestedView.md#defineroute)

***

### mountRoute()

> `protected` **mountRoute**(`router`): `void`

Defined in: [src/common/web/ui/views/NestedView.ts:9](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/views/NestedView.ts#L9)

#### Parameters

##### router

`Router`

#### Returns

`void`

#### Inherited from

[`NestedView`](../../../../../../../common/web/ui/views/NestedView/classes/NestedView.md).[`mountRoute`](../../../../../../../common/web/ui/views/NestedView/classes/NestedView.md#mountroute)

***

### navigateTo()

> **navigateTo**(`replace`, `query?`, `params?`): `void`

Defined in: [src/common/web/ui/views/View.ts:64](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/views/View.ts#L64)

Navigates to (= activates) this view.

#### Parameters

##### replace

`boolean` = `false`

Whether to replace the current browsing history entry.

##### query?

`LocationQueryRaw`

Additional query (URL) parameters.

##### params?

`RouteParamsRawGeneric`

Additional URL placeholder parameters.

#### Returns

`void`

- A promise that can be used to react to page load events.

#### Inherited from

[`NestedView`](../../../../../../../common/web/ui/views/NestedView/classes/NestedView.md).[`navigateTo`](../../../../../../../common/web/ui/views/NestedView/classes/NestedView.md#navigateto)

***

### route()

> **route**(): `RouteRecordRaw`

Defined in: [src/common/web/ui/views/View.ts:39](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/views/View.ts#L39)

Gets the route of this view.

#### Returns

`RouteRecordRaw`

#### Inherited from

[`NestedView`](../../../../../../../common/web/ui/views/NestedView/classes/NestedView.md).[`route`](../../../../../../../common/web/ui/views/NestedView/classes/NestedView.md#route)

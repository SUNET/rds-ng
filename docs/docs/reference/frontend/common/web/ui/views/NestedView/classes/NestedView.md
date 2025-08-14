# Abstract Class: NestedView

Defined in: [src/common/web/ui/views/NestedView.ts:8](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/views/NestedView.ts#L8)

A specialized nested view.

## Extends

- [`View`](../../View/classes/View.md)

## Extended by

- [`FrontendView`](../../../../../../frontend/src/ui/views/frontend/FrontendView/classes/FrontendView.md)

## Constructors

### Constructor

> `protected` **new NestedView**(`router`, `name`, `routeOptions?`, `subViews?`): `NestedView`

Defined in: [src/common/web/ui/views/View.ts:22](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/views/View.ts#L22)

#### Parameters

##### router

`Router`

The Vue router.

##### name

`string`

The route name for this view.

##### routeOptions?

`RouteRecordRaw`

Additional route options.

##### subViews?

[`View`](../../View/classes/View.md)[]

Optional sub-views of this view.

#### Returns

`NestedView`

#### Inherited from

[`View`](../../View/classes/View.md).[`constructor`](../../View/classes/View.md#constructor)

## Properties

### \_routeName

> `protected` `readonly` **\_routeName**: `string`

Defined in: [src/common/web/ui/views/View.ts:11](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/views/View.ts#L11)

#### Inherited from

[`View`](../../View/classes/View.md).[`_routeName`](../../View/classes/View.md#_routename)

***

### \_routeOptions

> `protected` `readonly` **\_routeOptions**: `undefined` \| `RouteRecordRaw`

Defined in: [src/common/web/ui/views/View.ts:12](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/views/View.ts#L12)

#### Inherited from

[`View`](../../View/classes/View.md).[`_routeOptions`](../../View/classes/View.md#_routeoptions)

***

### \_router

> `protected` `readonly` **\_router**: `Router`

Defined in: [src/common/web/ui/views/View.ts:10](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/views/View.ts#L10)

#### Inherited from

[`View`](../../View/classes/View.md).[`_router`](../../View/classes/View.md#_router)

***

### \_subViews

> `protected` `readonly` **\_subViews**: `undefined` \| [`View`](../../View/classes/View.md)[]

Defined in: [src/common/web/ui/views/View.ts:14](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/views/View.ts#L14)

#### Inherited from

[`View`](../../View/classes/View.md).[`_subViews`](../../View/classes/View.md#_subviews)

## Accessors

### name

#### Get Signature

> **get** **name**(): `string`

Defined in: [src/common/web/ui/views/View.ts:72](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/views/View.ts#L72)

The route name of this view.

##### Returns

`string`

#### Inherited from

[`View`](../../View/classes/View.md).[`name`](../../View/classes/View.md#name)

***

### subViews

#### Get Signature

> **get** **subViews**(): [`View`](../../View/classes/View.md)[]

Defined in: [src/common/web/ui/views/View.ts:79](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/views/View.ts#L79)

The sub-views of the views.

##### Returns

[`View`](../../View/classes/View.md)[]

#### Inherited from

[`View`](../../View/classes/View.md).[`subViews`](../../View/classes/View.md#subviews)

## Methods

### defineRoute()

> `abstract` `protected` **defineRoute**(): `RouteRecordRaw`

Defined in: [src/common/web/ui/views/View.ts:53](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/views/View.ts#L53)

Defines the route for this view.

#### Returns

`RouteRecordRaw`

#### Inherited from

[`View`](../../View/classes/View.md).[`defineRoute`](../../View/classes/View.md#defineroute)

***

### mountRoute()

> `protected` **mountRoute**(`router`): `void`

Defined in: [src/common/web/ui/views/NestedView.ts:9](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/views/NestedView.ts#L9)

#### Parameters

##### router

`Router`

#### Returns

`void`

#### Overrides

[`View`](../../View/classes/View.md).[`mountRoute`](../../View/classes/View.md#mountroute)

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

[`View`](../../View/classes/View.md).[`navigateTo`](../../View/classes/View.md#navigateto)

***

### route()

> **route**(): `RouteRecordRaw`

Defined in: [src/common/web/ui/views/View.ts:39](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/views/View.ts#L39)

Gets the route of this view.

#### Returns

`RouteRecordRaw`

#### Inherited from

[`View`](../../View/classes/View.md).[`route`](../../View/classes/View.md#route)

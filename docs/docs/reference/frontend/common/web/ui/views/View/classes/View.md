# Abstract Class: View

Defined in: [src/common/web/ui/views/View.ts:9](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/views/View.ts#L9)

A class to help with routed views.

This class does not represent a view *per se*, it is only used to work with the corresponding view.
It is therefore safe to instantiate this class and use its functions, as this doesn't automatically create a new view.

## Extended by

- [`NestedView`](../../NestedView/classes/NestedView.md)
- [`MainView`](../../main/MainView/classes/MainView.md)

## Constructors

### Constructor

> `protected` **new View**(`router`, `name`, `routeOptions?`, `subViews?`): `View`

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

`View`[]

Optional sub-views of this view.

#### Returns

`View`

## Properties

### \_routeName

> `protected` `readonly` **\_routeName**: `string`

Defined in: [src/common/web/ui/views/View.ts:11](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/views/View.ts#L11)

***

### \_routeOptions

> `protected` `readonly` **\_routeOptions**: `undefined` \| `RouteRecordRaw`

Defined in: [src/common/web/ui/views/View.ts:12](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/views/View.ts#L12)

***

### \_router

> `protected` `readonly` **\_router**: `Router`

Defined in: [src/common/web/ui/views/View.ts:10](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/views/View.ts#L10)

***

### \_subViews

> `protected` `readonly` **\_subViews**: `undefined` \| `View`[]

Defined in: [src/common/web/ui/views/View.ts:14](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/views/View.ts#L14)

## Accessors

### name

#### Get Signature

> **get** **name**(): `string`

Defined in: [src/common/web/ui/views/View.ts:72](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/views/View.ts#L72)

The route name of this view.

##### Returns

`string`

***

### subViews

#### Get Signature

> **get** **subViews**(): `View`[]

Defined in: [src/common/web/ui/views/View.ts:79](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/views/View.ts#L79)

The sub-views of the views.

##### Returns

`View`[]

## Methods

### defineRoute()

> `abstract` `protected` **defineRoute**(): `RouteRecordRaw`

Defined in: [src/common/web/ui/views/View.ts:53](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/views/View.ts#L53)

Defines the route for this view.

#### Returns

`RouteRecordRaw`

***

### mountRoute()

> `protected` **mountRoute**(`router`): `void`

Defined in: [src/common/web/ui/views/View.ts:32](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/views/View.ts#L32)

#### Parameters

##### router

`Router`

#### Returns

`void`

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

***

### route()

> **route**(): `RouteRecordRaw`

Defined in: [src/common/web/ui/views/View.ts:39](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/views/View.ts#L39)

Gets the route of this view.

#### Returns

`RouteRecordRaw`

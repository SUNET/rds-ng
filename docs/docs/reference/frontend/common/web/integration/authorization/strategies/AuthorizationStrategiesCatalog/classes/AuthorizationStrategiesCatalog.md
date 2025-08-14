# Class: AuthorizationStrategiesCatalog

Defined in: [src/common/web/integration/authorization/strategies/AuthorizationStrategiesCatalog.ts:12](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/integration/authorization/strategies/AuthorizationStrategiesCatalog.ts#L12)

Global catalog of creator functions for all known authorization strategies.

## Extends

- [`ItemsCatalog`](../../../../../utils/ItemsCatalog/classes/ItemsCatalog.md)\<[`AuthorizationStrategyCreator`](../type-aliases/AuthorizationStrategyCreator.md)\>

## Constructors

### Constructor

> **new AuthorizationStrategiesCatalog**(): `AuthorizationStrategiesCatalog`

#### Returns

`AuthorizationStrategiesCatalog`

#### Inherited from

[`ItemsCatalog`](../../../../../utils/ItemsCatalog/classes/ItemsCatalog.md).[`constructor`](../../../../../utils/ItemsCatalog/classes/ItemsCatalog.md#constructor)

## Accessors

### items

#### Get Signature

> **get** `static` **items**(): `Record`\<`string`, `ItemType`\>

Defined in: [src/common/web/utils/ItemsCatalog.ts:60](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/utils/ItemsCatalog.ts#L60)

Retrieves all stored items.

##### Returns

`Record`\<`string`, `ItemType`\>

#### Inherited from

[`ItemsCatalog`](../../../../../utils/ItemsCatalog/classes/ItemsCatalog.md).[`items`](../../../../../utils/ItemsCatalog/classes/ItemsCatalog.md#items)

## Methods

### define()

> `static` **define**(): `Function`

Defined in: [src/common/web/utils/ItemsCatalog.ts:18](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/utils/ItemsCatalog.ts#L18)

A decorator to define a new item catalog.

Notes:
    This decorator must always be used for new item catalogs; otherwise, data corruption might occur.

#### Returns

`Function`

#### Inherited from

[`ItemsCatalog`](../../../../../utils/ItemsCatalog/classes/ItemsCatalog.md).[`define`](../../../../../utils/ItemsCatalog/classes/ItemsCatalog.md#define)

***

### findItem()

> `static` **findItem**(`name`): `any`

Defined in: [src/common/web/utils/ItemsCatalog.ts:52](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/utils/ItemsCatalog.ts#L52)

Finds the item associated with the given ``name``.

#### Parameters

##### name

`string`

The item name.

#### Returns

`any`

- The associated item, if any.

#### Inherited from

[`ItemsCatalog`](../../../../../utils/ItemsCatalog/classes/ItemsCatalog.md).[`findItem`](../../../../../utils/ItemsCatalog/classes/ItemsCatalog.md#finditem)

***

### registerItem()

> `static` **registerItem**(`name`, `item`): `void`

Defined in: [src/common/web/utils/ItemsCatalog.ts:34](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/utils/ItemsCatalog.ts#L34)

Registers a new item.

#### Parameters

##### name

`string`

The item name.

##### item

`ItemType`

The item.

#### Returns

`void`

#### Inherited from

[`ItemsCatalog`](../../../../../utils/ItemsCatalog/classes/ItemsCatalog.md).[`registerItem`](../../../../../utils/ItemsCatalog/classes/ItemsCatalog.md#registeritem)

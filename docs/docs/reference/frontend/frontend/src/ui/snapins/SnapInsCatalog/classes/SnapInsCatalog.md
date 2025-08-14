# Class: SnapInsCatalog

Defined in: [src/frontend/src/ui/snapins/SnapInsCatalog.ts:11](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/snapins/SnapInsCatalog.ts#L11)

Global catalog of all registered snap-ins.

This is a globally accessible list of all snap-ins, associated with their respective IDs.

## Extends

- [`ItemsCatalog`](../../../../../../common/web/utils/ItemsCatalog/classes/ItemsCatalog.md)\<[`SnapIn`](../../SnapIn/classes/SnapIn.md)\>

## Constructors

### Constructor

> **new SnapInsCatalog**(): `SnapInsCatalog`

#### Returns

`SnapInsCatalog`

#### Inherited from

[`ItemsCatalog`](../../../../../../common/web/utils/ItemsCatalog/classes/ItemsCatalog.md).[`constructor`](../../../../../../common/web/utils/ItemsCatalog/classes/ItemsCatalog.md#constructor)

## Accessors

### items

#### Get Signature

> **get** `static` **items**(): `Record`\<`string`, `ItemType`\>

Defined in: [src/common/web/utils/ItemsCatalog.ts:60](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/utils/ItemsCatalog.ts#L60)

Retrieves all stored items.

##### Returns

`Record`\<`string`, `ItemType`\>

#### Inherited from

[`ItemsCatalog`](../../../../../../common/web/utils/ItemsCatalog/classes/ItemsCatalog.md).[`items`](../../../../../../common/web/utils/ItemsCatalog/classes/ItemsCatalog.md#items)

## Methods

### allOptionals()

> `static` **allOptionals**(): [`SnapIn`](../../SnapIn/classes/SnapIn.md)[]

Defined in: [src/frontend/src/ui/snapins/SnapInsCatalog.ts:24](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/snapins/SnapInsCatalog.ts#L24)

Retrieve all optional snap-ins.

#### Returns

[`SnapIn`](../../SnapIn/classes/SnapIn.md)[]

***

### allWithTabPanel()

> `static` **allWithTabPanel**(): [`SnapIn`](../../SnapIn/classes/SnapIn.md)[]

Defined in: [src/frontend/src/ui/snapins/SnapInsCatalog.ts:31](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/snapins/SnapInsCatalog.ts#L31)

Retrieve all snap-ins with a tab panel.

#### Returns

[`SnapIn`](../../SnapIn/classes/SnapIn.md)[]

***

### define()

> `static` **define**(): `Function`

Defined in: [src/common/web/utils/ItemsCatalog.ts:18](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/utils/ItemsCatalog.ts#L18)

A decorator to define a new item catalog.

Notes:
    This decorator must always be used for new item catalogs; otherwise, data corruption might occur.

#### Returns

`Function`

#### Inherited from

[`ItemsCatalog`](../../../../../../common/web/utils/ItemsCatalog/classes/ItemsCatalog.md).[`define`](../../../../../../common/web/utils/ItemsCatalog/classes/ItemsCatalog.md#define)

***

### filter()

> `static` **filter**(`predicate`): [`SnapIn`](../../SnapIn/classes/SnapIn.md)[]

Defined in: [src/frontend/src/ui/snapins/SnapInsCatalog.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/snapins/SnapInsCatalog.ts#L17)

Select certain snap-ins that satisfy the given predicate.

#### Parameters

##### predicate

(`snapIn`) => `boolean`

The selection criterium.

#### Returns

[`SnapIn`](../../SnapIn/classes/SnapIn.md)[]

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

[`ItemsCatalog`](../../../../../../common/web/utils/ItemsCatalog/classes/ItemsCatalog.md).[`findItem`](../../../../../../common/web/utils/ItemsCatalog/classes/ItemsCatalog.md#finditem)

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

[`ItemsCatalog`](../../../../../../common/web/utils/ItemsCatalog/classes/ItemsCatalog.md).[`registerItem`](../../../../../../common/web/utils/ItemsCatalog/classes/ItemsCatalog.md#registeritem)

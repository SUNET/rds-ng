# Class: ItemsCatalog\<ItemType\>

Defined in: [src/common/web/utils/ItemsCatalog.ts:8](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/utils/ItemsCatalog.ts#L8)

Generic catalog to keep track of "registered" items (where the definition of "item" is completely context dependant).

This is a globally accessible list of these items, associated with their respective names.

## Extended by

- [`ConnectorCategoriesCatalog`](../../../../../frontend/src/data/entities/connector/categories/ConnectorCategoriesCatalog/classes/ConnectorCategoriesCatalog.md)
- [`IntegrationSchemesCatalog`](../../../../../frontend/src/integration/IntegrationSchemesCatalog/classes/IntegrationSchemesCatalog.md)
- [`ResourcePreviewersCatalog`](../../../../../frontend/src/ui/components/resource/ResourcePreviewersCatalog/classes/ResourcePreviewersCatalog.md)
- [`SnapInsCatalog`](../../../../../frontend/src/ui/snapins/SnapInsCatalog/classes/SnapInsCatalog.md)
- [`MessageTypesCatalog`](../../../core/messaging/MessageTypesCatalog/classes/MessageTypesCatalog.md)
- [`AuthorizationStrategiesCatalog`](../../../integration/authorization/strategies/AuthorizationStrategiesCatalog/classes/AuthorizationStrategiesCatalog.md)

## Type Parameters

### ItemType

`ItemType`

## Constructors

### Constructor

> **new ItemsCatalog**\<`ItemType`\>(): `ItemsCatalog`\<`ItemType`\>

#### Returns

`ItemsCatalog`\<`ItemType`\>

## Accessors

### items

#### Get Signature

> **get** `static` **items**(): `Record`\<`string`, `ItemType`\>

Defined in: [src/common/web/utils/ItemsCatalog.ts:60](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/utils/ItemsCatalog.ts#L60)

Retrieves all stored items.

##### Returns

`Record`\<`string`, `ItemType`\>

## Methods

### define()

> `static` **define**(): `Function`

Defined in: [src/common/web/utils/ItemsCatalog.ts:18](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/utils/ItemsCatalog.ts#L18)

A decorator to define a new item catalog.

Notes:
    This decorator must always be used for new item catalogs; otherwise, data corruption might occur.

#### Returns

`Function`

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

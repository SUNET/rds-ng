# Class: PropertyObjectStore

Defined in: [src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:116](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L116)

Represents a store for project objects.

## Constructors

### Constructor

> **new PropertyObjectStore**(): `PropertyObjectStore`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:122](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L122)

Constructs a new PropertyObjectStore instance.

#### Returns

`PropertyObjectStore`

## Properties

### \_objects

> **\_objects**: [`PropertyObject`](PropertyObject.md)[]

Defined in: [src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:117](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L117)

## Methods

### \_removeRefs()

> **\_removeRefs**(`id`): `void`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:180](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L180)

Removes references to a project object by its ID.

#### Parameters

##### id

The ID of the project object.

`string` | `string`[]

#### Returns

`void`

***

### add()

> **add**(`object`): [`PropertyObject`](PropertyObject.md)

Defined in: [src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:148](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L148)

Adds a project object to the store if no object with that ID exists.

#### Parameters

##### object

[`PropertyObject`](PropertyObject.md)

The project object to add.

#### Returns

[`PropertyObject`](PropertyObject.md)

The project object with that ID, either existing or newly created.

***

### addRef()

> **addRef**(`id`, `ref`): `undefined` \| [`PropertyObject`](PropertyObject.md)

Defined in: [src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:214](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L214)

Adds a reference to a project object.

#### Parameters

##### id

`string`

The ID of the project object.

##### ref

`string`

The reference ID to add.

#### Returns

`undefined` \| [`PropertyObject`](PropertyObject.md)

The updated project object, or undefined if the project object is not found.

***

### exportObjects()

> **exportObjects**(): [`PropertyObject`](PropertyObject.md)[]

Defined in: [src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:138](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L138)

Exports the objects from the store.

#### Returns

[`PropertyObject`](PropertyObject.md)[]

An array of project objects.

***

### get()

> **get**(`id`): `undefined` \| [`PropertyObject`](PropertyObject.md)

Defined in: [src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:163](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L163)

Retrieves a project object by its ID.

#### Parameters

##### id

`string`

The ID of the project object.

#### Returns

`undefined` \| [`PropertyObject`](PropertyObject.md)

The project object with the specified ID, or undefined if not found.

***

### getObjectsByType()

> **getObjectsByType**(`type`): [`SharedPropertyObject`](SharedPropertyObject.md)[]

Defined in: [src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:252](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L252)

Retrieves project objects of a specific type.

#### Parameters

##### type

`string`

The type of project objects to retrieve.

#### Returns

[`SharedPropertyObject`](SharedPropertyObject.md)[]

An array of project objects of the specified type.

***

### getReferencedObjects()

> **getReferencedObjects**(`id`): `string`[]

Defined in: [src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:241](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L241)

Retrieves the referenced objects of a project object.

#### Parameters

##### id

`string`

The ID of the project object.

#### Returns

`string`[]

An array of reference IDs of the referenced objects.

***

### remove()

> **remove**(`id`): `void`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:171](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L171)

Removes a project object from the store by its ID. Also removes all references to the object.

#### Parameters

##### id

`string`

The ID of the project object to remove.

#### Returns

`void`

***

### removeRef()

> **removeRef**(`id`, `ref`): `void`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:227](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L227)

Removes a reference from a project object.

#### Parameters

##### id

`string`

The ID of the project object.

##### ref

`string`

The reference ID to remove.

#### Returns

`void`

***

### setObjects()

> **setObjects**(`objects`): `void`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:130](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L130)

Sets the objects in the store.

#### Parameters

##### objects

[`PropertyObject`](PropertyObject.md)[]

An array of project objects.

#### Returns

`void`

***

### update()

> **update**(`inputId`, `id`, `value`): `void`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:198](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L198)

Updates the value of a project object.

#### Parameters

##### inputId

`string`

The input ID of the project object.

##### id

`string`

The ID of the project object.

##### value

`any`

The new value for the project object.

#### Returns

`void`

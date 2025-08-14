# Abstract Class: PropertyObject

Defined in: [src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:13](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L13)

Represents a project object with an ID, value, and references.

 PropertyObject

## Extended by

- [`LayoutPropertyObject`](LayoutPropertyObject.md)
- [`SharedPropertyObject`](SharedPropertyObject.md)

## Constructors

### Constructor

> `protected` **new PropertyObject**(`id?`, `value?`, `refs?`): `PropertyObject`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:24](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L24)

Creates a new instance of PropertyObject.

#### Parameters

##### id?

`string`

The object ID.

##### value?

`any` = `{}`

The object value.

##### refs?

`string`[] = `[]`

The object references.

#### Returns

`PropertyObject`

## Properties

### id

> **id**: `string`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:14](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L14)

***

### refs

> **refs**: `string`[]

Defined in: [src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:16](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L16)

***

### value

> **value**: `object`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:15](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L15)

#### Index Signature

\[`key`: `string`\]: `any`

## Methods

### getId()

> **getId**(): `string`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:35](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L35)

Retrieves the unique identifier of the project object.

#### Returns

`string`

The unique identifier of the project object.

***

### getReferences()

> **getReferences**(): `string`[]

Defined in: [src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:53](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L53)

Retrieves the list of the references that the object holds.

#### Returns

`string`[]

An array of reference strings.

***

### getValues()

> **getValues**(): `object`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:44](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L44)

Retrieves the current values stored in the PropertyObject.

#### Returns

`object`

An object where the keys are strings and the values can be of any type.

***

### isEmpty()

> **isEmpty**(): `boolean`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:75](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L75)

#### Returns

`boolean`

***

### pushReference()

> **pushReference**(`ref`): `void`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:71](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L71)

Adds a reference string to the list of references.

#### Parameters

##### ref

`string`

The reference string to be added.

#### Returns

`void`

***

### setReferences()

> **setReferences**(`refs`): `void`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:62](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L62)

Sets the references for the project object.

#### Parameters

##### refs

`string`[]

An array of reference strings to be set.

#### Returns

`void`

# Class: SharedPropertyObject

Defined in: [src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:95](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L95)

Represents a shared object that extends the `PropertyObject` class.

## Extends

- [`PropertyObject`](PropertyObject.md)

## Constructors

### Constructor

> **new SharedPropertyObject**(`type`, `id?`, `value?`, `refs?`): `SharedPropertyObject`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:98](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L98)

#### Parameters

##### type

`string`

##### id?

`string`

##### value?

`any` = `{}`

##### refs?

`string`[] = `[]`

#### Returns

`SharedPropertyObject`

#### Overrides

[`PropertyObject`](PropertyObject.md).[`constructor`](PropertyObject.md#constructor)

## Properties

### id

> **id**: `string`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:14](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L14)

#### Inherited from

[`PropertyObject`](PropertyObject.md).[`id`](PropertyObject.md#id)

***

### refs

> **refs**: `string`[]

Defined in: [src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:16](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L16)

#### Inherited from

[`PropertyObject`](PropertyObject.md).[`refs`](PropertyObject.md#refs)

***

### type

> **type**: `string`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:96](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L96)

***

### value

> **value**: `object`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:15](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L15)

#### Index Signature

\[`key`: `string`\]: `any`

#### Inherited from

[`PropertyObject`](PropertyObject.md).[`value`](PropertyObject.md#value)

## Methods

### getId()

> **getId**(): `string`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:35](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L35)

Retrieves the unique identifier of the project object.

#### Returns

`string`

The unique identifier of the project object.

#### Inherited from

[`PropertyObject`](PropertyObject.md).[`getId`](PropertyObject.md#getid)

***

### getReferences()

> **getReferences**(): `string`[]

Defined in: [src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:53](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L53)

Retrieves the list of the references that the object holds.

#### Returns

`string`[]

An array of reference strings.

#### Inherited from

[`PropertyObject`](PropertyObject.md).[`getReferences`](PropertyObject.md#getreferences)

***

### getType()

> **getType**(): `string`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:108](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L108)

Retrieves the type of the shared object.

#### Returns

`string`

The type of the shared object.

***

### getValues()

> **getValues**(): `object`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:44](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L44)

Retrieves the current values stored in the PropertyObject.

#### Returns

`object`

An object where the keys are strings and the values can be of any type.

#### Inherited from

[`PropertyObject`](PropertyObject.md).[`getValues`](PropertyObject.md#getvalues)

***

### isEmpty()

> **isEmpty**(): `boolean`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts:75](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyObjectStore.ts#L75)

#### Returns

`boolean`

#### Inherited from

[`PropertyObject`](PropertyObject.md).[`isEmpty`](PropertyObject.md#isempty)

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

#### Inherited from

[`PropertyObject`](PropertyObject.md).[`pushReference`](PropertyObject.md#pushreference)

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

#### Inherited from

[`PropertyObject`](PropertyObject.md).[`setReferences`](PropertyObject.md#setreferences)

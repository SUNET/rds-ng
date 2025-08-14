# Class: ProfileClassInput

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:61](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L61)

Represents an input for a profile class.

## Constructors

### Constructor

> **new ProfileClassInput**(`id`, `label`, `type`, `description?`, `example?`, `options?`, `required?`, `hints?`): `ProfileClassInput`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:83](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L83)

#### Parameters

##### id

`string`

##### label

`string`

##### type

`string`

##### description?

`string`

##### example?

`string`

##### options?

`string`[] = `[]`

##### required?

`boolean`

##### hints?

#### Returns

`ProfileClassInput`

## Properties

### description?

> `readonly` `optional` **description**: `string`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:77](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L77)

***

### example?

> `readonly` `optional` **example**: `string`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:78](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L78)

***

### hints?

> `optional` **hints**: `object`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:81](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L81)

#### Index Signature

\[`key`: `string`\]: `object`

***

### id

> `readonly` **id**: `string`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:74](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L74)

Creates an instance of `ProfileClassInput`.

#### Param

The ID of the input.

#### Param

The label of the input.

#### Param

The type of the input.

#### Param

The description of the input.

#### Param

An example of the input.

#### Param

The options of the input.

#### Param

Whether the input is required.

#### Param

Hints for certain inputs

***

### label

> `readonly` **label**: `string`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:75](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L75)

***

### options?

> `readonly` `optional` **options**: `string`[]

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:79](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L79)

***

### required?

> `optional` **required**: `boolean`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:80](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L80)

***

### type

> `readonly` **type**: `string`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:76](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L76)

## Methods

### getDescription()

> **getDescription**(): `undefined` \| `string`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:117](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L117)

Retrieves the description of the property input.

#### Returns

`undefined` \| `string`

The description of the property input.

***

### getExample()

> **getExample**(): `undefined` \| `string`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:126](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L126)

Retrieves the example of the property input.

#### Returns

`undefined` \| `string`

The example of the property input.

***

### getHint()

> **getHint**(`input`, `hintType`): `any`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:174](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L174)

Retrieves a hint based on the provided input and hint type.

#### Parameters

##### input

`string`

The key used to look up the hint.

##### hintType

[`HintType`](../enumerations/HintType.md)

The specific type of hint to retrieve.

#### Returns

`any`

An object representing the hint, or undefined if no hint is found.

***

### getId()

> **getId**(): `string`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:108](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L108)

Retrieves the unique identifier of the property input.

#### Returns

`string`

The identifier of the property input.

***

### getLabel()

> **getLabel**(): `string`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:135](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L135)

Retrieves the label of the property input.

#### Returns

`string`

The label of the property input.

***

### getOptions()

> **getOptions**(): `string`[]

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:153](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L153)

Retrieves the options of the input.

#### Returns

`string`[]

The options of the property input.

***

### getType()

> **getType**(): `string`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:144](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L144)

Retrieves the type of the property input.

#### Returns

`string`

The type of the property input.

***

### hasHints()

> **hasHints**(`input`): `boolean`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:163](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L163)

Determines whether hints exist for the given input key.

#### Parameters

##### input

`string`

The key to check for associated hints.

#### Returns

`boolean`

`true` if hints exist for the specified input key; otherwise, `false`.

# Class: ProfileClass

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:223](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L223)

Represents a profile with various properties and inputs.

## Extended by

- [`ProfileLayoutClass`](ProfileLayoutClass.md)

## Constructors

### Constructor

> **new ProfileClass**(`id`, `displayLabel`, `description?`, `labelTemplate?`, `required?`, `multiple?`, `example?`, `refs?`, `input?`): `ProfileClass`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:240](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L240)

#### Parameters

##### id

`string`

##### displayLabel

`string`

##### description?

`string`

##### labelTemplate?

`string`

##### required?

`boolean`

##### multiple?

`boolean`

##### example?

`string`

##### refs?

[`ProfileClassRef`](ProfileClassRef.md)[] = `[]`

##### input?

[`ProfileClassInput`](ProfileClassInput.md)[] = `[]`

#### Returns

`ProfileClass`

## Properties

### description?

> `readonly` `optional` **description**: `string`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:226](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L226)

***

### displayLabel

> `readonly` **displayLabel**: `string`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:225](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L225)

***

### example?

> `readonly` `optional` **example**: `string`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:230](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L230)

***

### id

> `readonly` **id**: `string`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:224](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L224)

***

### input

> `readonly` **input**: [`ProfileClassInput`](ProfileClassInput.md)[]

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:238](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L238)

***

### labelTemplate?

> `readonly` `optional` **labelTemplate**: `string`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:227](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L227)

***

### multiple?

> `readonly` `optional` **multiple**: `boolean`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:229](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L229)

***

### refs

> `readonly` **refs**: [`ProfileClassRef`](ProfileClassRef.md)[]

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:234](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L234)

***

### required?

> `optional` **required**: `boolean`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:228](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L228)

## Methods

### getDescription()

> **getDescription**(): `undefined` \| `string`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:303](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L303)

Retrieves the description of the property class.

#### Returns

`undefined` \| `string`

The description of the property class.

***

### getDisplayLabel()

> **getDisplayLabel**(): `string`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:294](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L294)

Retrieves the displayLabel of the ProfileClass.

#### Returns

`string`

The displayLabel of the ProfileClass.

***

### getExample()

> **getExample**(): `undefined` \| `string`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:312](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L312)

Retrieves an example for the property class.

#### Returns

`undefined` \| `string`

The current value of the example class.

***

### getId()

> **getId**(): `string`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:285](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L285)

Retrieves the unique identifier of the ProfileClass.

#### Returns

`string`

The unique identifier of the ProfileClass.

***

### getInputs()

> **getInputs**(): [`ProfileClassInput`](ProfileClassInput.md)[]

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:267](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L267)

Retrieves the inputs of the ProfileClass.

#### Returns

[`ProfileClassInput`](ProfileClassInput.md)[]

The input property.

***

### getRefTypes()

> **getRefTypes**(): [`ProfileClassRef`](ProfileClassRef.md)[]

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:276](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L276)

Retrieves the types that the ProfileClass can reference.

#### Returns

[`ProfileClassRef`](ProfileClassRef.md)[]

The types of the ProfileClass.

***

### isRequired()

> **isRequired**(): `undefined` \| `boolean`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:321](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L321)

Checks if the property is required.

#### Returns

`undefined` \| `boolean`

True if the property is required, otherwise false.

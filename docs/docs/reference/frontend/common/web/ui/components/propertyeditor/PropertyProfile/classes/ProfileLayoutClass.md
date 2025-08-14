# Class: ProfileLayoutClass

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:330](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L330)

Represents a layout class for profiles, extending the ProfileClass.
This class maintains an array of profile IDs.

## Extends

- [`ProfileClass`](ProfileClass.md)

## Constructors

### Constructor

> **new ProfileLayoutClass**(`id`, `displayLabel`, `description?`, `labelTemplate?`, `required?`, `multiple?`, `example?`, `refs?`, `input?`): `ProfileLayoutClass`

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

`ProfileLayoutClass`

#### Inherited from

[`ProfileClass`](ProfileClass.md).[`constructor`](ProfileClass.md#constructor)

## Properties

### description?

> `readonly` `optional` **description**: `string`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:226](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L226)

#### Inherited from

[`ProfileClass`](ProfileClass.md).[`description`](ProfileClass.md#description)

***

### displayLabel

> `readonly` **displayLabel**: `string`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:225](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L225)

#### Inherited from

[`ProfileClass`](ProfileClass.md).[`displayLabel`](ProfileClass.md#displaylabel)

***

### example?

> `readonly` `optional` **example**: `string`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:230](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L230)

#### Inherited from

[`ProfileClass`](ProfileClass.md).[`example`](ProfileClass.md#example)

***

### id

> `readonly` **id**: `string`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:224](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L224)

#### Inherited from

[`ProfileClass`](ProfileClass.md).[`id`](ProfileClass.md#id)

***

### input

> `readonly` **input**: [`ProfileClassInput`](ProfileClassInput.md)[]

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:238](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L238)

#### Inherited from

[`ProfileClass`](ProfileClass.md).[`input`](ProfileClass.md#input)

***

### labelTemplate?

> `readonly` `optional` **labelTemplate**: `string`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:227](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L227)

#### Inherited from

[`ProfileClass`](ProfileClass.md).[`labelTemplate`](ProfileClass.md#labeltemplate)

***

### multiple?

> `readonly` `optional` **multiple**: `boolean`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:229](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L229)

#### Inherited from

[`ProfileClass`](ProfileClass.md).[`multiple`](ProfileClass.md#multiple)

***

### profiles

> **profiles**: [`ProfileID`](../type-aliases/ProfileID.md)[] = `[]`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:331](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L331)

***

### refs

> `readonly` **refs**: [`ProfileClassRef`](ProfileClassRef.md)[]

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:234](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L234)

#### Inherited from

[`ProfileClass`](ProfileClass.md).[`refs`](ProfileClass.md#refs)

***

### required?

> `optional` **required**: `boolean`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:228](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L228)

#### Inherited from

[`ProfileClass`](ProfileClass.md).[`required`](ProfileClass.md#required)

## Methods

### addProfile()

> **addProfile**(`profile`): `void`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:338](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L338)

Adds a profile to the profiles array of the ProfileLayoutClass.

#### Parameters

##### profile

[`ProfileID`](../type-aliases/ProfileID.md)

The profile ID to be added.

#### Returns

`void`

***

### getDescription()

> **getDescription**(): `undefined` \| `string`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:303](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L303)

Retrieves the description of the property class.

#### Returns

`undefined` \| `string`

The description of the property class.

#### Inherited from

[`ProfileClass`](ProfileClass.md).[`getDescription`](ProfileClass.md#getdescription)

***

### getDisplayLabel()

> **getDisplayLabel**(): `string`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:294](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L294)

Retrieves the displayLabel of the ProfileClass.

#### Returns

`string`

The displayLabel of the ProfileClass.

#### Inherited from

[`ProfileClass`](ProfileClass.md).[`getDisplayLabel`](ProfileClass.md#getdisplaylabel)

***

### getExample()

> **getExample**(): `undefined` \| `string`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:312](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L312)

Retrieves an example for the property class.

#### Returns

`undefined` \| `string`

The current value of the example class.

#### Inherited from

[`ProfileClass`](ProfileClass.md).[`getExample`](ProfileClass.md#getexample)

***

### getId()

> **getId**(): `string`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:285](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L285)

Retrieves the unique identifier of the ProfileClass.

#### Returns

`string`

The unique identifier of the ProfileClass.

#### Inherited from

[`ProfileClass`](ProfileClass.md).[`getId`](ProfileClass.md#getid)

***

### getInputs()

> **getInputs**(): [`ProfileClassInput`](ProfileClassInput.md)[]

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:267](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L267)

Retrieves the inputs of the ProfileClass.

#### Returns

[`ProfileClassInput`](ProfileClassInput.md)[]

The input property.

#### Inherited from

[`ProfileClass`](ProfileClass.md).[`getInputs`](ProfileClass.md#getinputs)

***

### getProfiles()

> **getProfiles**(): [`ProfileID`](../type-aliases/ProfileID.md)[]

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:347](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L347)

Retrieves the list of profiles.

#### Returns

[`ProfileID`](../type-aliases/ProfileID.md)[]

An array of profiles.

***

### getRefTypes()

> **getRefTypes**(): [`ProfileClassRef`](ProfileClassRef.md)[]

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:276](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L276)

Retrieves the types that the ProfileClass can reference.

#### Returns

[`ProfileClassRef`](ProfileClassRef.md)[]

The types of the ProfileClass.

#### Inherited from

[`ProfileClass`](ProfileClass.md).[`getRefTypes`](ProfileClass.md#getreftypes)

***

### isRequired()

> **isRequired**(): `undefined` \| `boolean`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:321](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L321)

Checks if the property is required.

#### Returns

`undefined` \| `boolean`

True if the property is required, otherwise false.

#### Inherited from

[`ProfileClass`](ProfileClass.md).[`isRequired`](ProfileClass.md#isrequired)

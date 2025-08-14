# Class: PropertyProfile

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:369](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L369)

Represents a property profile with metadata, layout, and classes.

## Remarks

This class is used to encapsulate the profile metadata, layout, and class dictionary
for a property editor component.

## Constructors

### Constructor

> **new PropertyProfile**(`metadata`, `layout`, `classes?`): `PropertyProfile`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:382](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L382)

#### Parameters

##### metadata

`ProfileMetadata`

##### layout

[`ProfileLayoutClass`](ProfileLayoutClass.md)[]

##### classes?

`ProfileClassDictionary`

#### Returns

`PropertyProfile`

## Properties

### classes?

> `readonly` `optional` **classes**: `ProfileClassDictionary` = `{}`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:380](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L380)

***

### layout

> `readonly` **layout**: [`ProfileLayoutClass`](ProfileLayoutClass.md)[] = `[]`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:376](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L376)

***

### metadata

> `readonly` **metadata**: `ProfileMetadata`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:372](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L372)

## Methods

### getClasses()

> **getClasses**(): `undefined` \| `ProfileClassDictionary`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:400](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L400)

Gets the classes part of the profile

#### Returns

`undefined` \| `ProfileClassDictionary`

the profile classes

***

### getDescription()

> **getDescription**(): `string`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:440](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L440)

Retrieves the description from the metadata.

#### Returns

`string`

***

### getDisplayLabel()

> **getDisplayLabel**(): `string`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:433](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L433)

Retrieves the display label from the metadata.

#### Returns

`string`

The display label.

***

### getId()

> **getId**(): [`ProfileID`](../type-aliases/ProfileID.md)

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:408](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L408)

Gets the version part of the ProfileID

#### Returns

[`ProfileID`](../type-aliases/ProfileID.md)

the ProfileID version

***

### getLayout()

> **getLayout**(): [`ProfileLayoutClass`](ProfileLayoutClass.md)[]

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:392](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L392)

Gets the layout part of the profile

#### Returns

[`ProfileLayoutClass`](ProfileLayoutClass.md)[]

the profile layout

***

### getName()

> **getName**(): `string`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:416](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L416)

Gets the name part of the ProfileID

#### Returns

`string`

the ProfileID name

***

### getVersion()

> **getVersion**(): `string`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:424](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L424)

Gets the version part of the ProfileID

#### Returns

`string`

the ProfileID version

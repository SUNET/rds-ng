# Class: ProfileClassRef

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:179](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L179)

## Constructors

### Constructor

> **new ProfileClassRef**(`classId`, `required`, `inline`, `multiple`): `ProfileClassRef`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:185](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L185)

#### Parameters

##### classId

`string`

##### required

`Boolean` = `false`

##### inline

`Boolean` = `false`

##### multiple

`Boolean` = `true`

#### Returns

`ProfileClassRef`

## Properties

### classId

> `readonly` **classId**: `string`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:180](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L180)

***

### inline

> `readonly` **inline**: `Boolean`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:182](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L182)

***

### multiple

> `readonly` **multiple**: `Boolean`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:183](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L183)

***

### required

> `readonly` **required**: `Boolean`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:181](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L181)

## Methods

### allowsMultiple()

> **allowsMultiple**(): `Boolean`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:215](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L215)

Determines if multiple refs of this type are allowed.

#### Returns

`Boolean`

True if multiple refs are allowed, otherwise false.

***

### getClassId()

> **getClassId**(): `string`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:197](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L197)

Retrieves the class type identifier.

#### Returns

`string`

The class identifier.

***

### isInline()

> **isInline**(): `Boolean`

Defined in: [src/common/web/ui/components/propertyeditor/PropertyProfile.ts:206](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L206)

Checks if the ref property is set to inline mode.

#### Returns

`Boolean`

True if the property is inline, otherwise false.

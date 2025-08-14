---
id: "common_web_ui_components_propertyeditor_PropertyProfile.ProfileLayoutClass"
title: "Class: ProfileLayoutClass"
sidebar_label: "ProfileLayoutClass"
custom_edit_url: null
---

[common/web/ui/components/propertyeditor/PropertyProfile](../modules/common_web_ui_components_propertyeditor_PropertyProfile.md).ProfileLayoutClass

Represents a layout class for profiles, extending the ProfileClass.
This class maintains an array of profile IDs.

## Hierarchy

- [`ProfileClass`](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClass.md)

  ↳ **`ProfileLayoutClass`**

## Constructors

### constructor

• **new ProfileLayoutClass**(`id`, `displayLabel`, `description?`, `labelTemplate?`, `required?`, `multiple?`, `example?`, `refs?`, `input?`): [`ProfileLayoutClass`](common_web_ui_components_propertyeditor_PropertyProfile.ProfileLayoutClass.md)

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `id` | `string` | `undefined` |
| `displayLabel` | `string` | `undefined` |
| `description?` | `string` | `undefined` |
| `labelTemplate?` | `string` | `undefined` |
| `required?` | `boolean` | `undefined` |
| `multiple?` | `boolean` | `undefined` |
| `example?` | `string` | `undefined` |
| `refs` | [`ProfileClassRef`](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClassRef.md)[] | `[]` |
| `input` | [`ProfileClassInput`](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClassInput.md)[] | `[]` |

#### Returns

[`ProfileLayoutClass`](common_web_ui_components_propertyeditor_PropertyProfile.ProfileLayoutClass.md)

#### Inherited from

[ProfileClass](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClass.md).[constructor](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClass.md#constructor)

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:240](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L240)

## Properties

### description

• `Optional` `Readonly` **description**: `string`

#### Inherited from

[ProfileClass](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClass.md).[description](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClass.md#description)

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:226](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L226)

___

### displayLabel

• `Readonly` **displayLabel**: `string`

#### Inherited from

[ProfileClass](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClass.md).[displayLabel](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClass.md#displaylabel)

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:225](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L225)

___

### example

• `Optional` `Readonly` **example**: `string`

#### Inherited from

[ProfileClass](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClass.md).[example](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClass.md#example)

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:230](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L230)

___

### id

• `Readonly` **id**: `string`

#### Inherited from

[ProfileClass](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClass.md).[id](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClass.md#id)

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:224](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L224)

___

### input

• `Readonly` **input**: [`ProfileClassInput`](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClassInput.md)[]

#### Inherited from

[ProfileClass](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClass.md).[input](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClass.md#input)

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:238](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L238)

___

### labelTemplate

• `Optional` `Readonly` **labelTemplate**: `string`

#### Inherited from

[ProfileClass](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClass.md).[labelTemplate](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClass.md#labeltemplate)

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:227](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L227)

___

### multiple

• `Optional` `Readonly` **multiple**: `boolean`

#### Inherited from

[ProfileClass](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClass.md).[multiple](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClass.md#multiple)

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:229](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L229)

___

### profiles

• **profiles**: [`ProfileID`](../modules/common_web_ui_components_propertyeditor_PropertyProfile.md#profileid)[] = `[]`

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:331](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L331)

___

### refs

• `Readonly` **refs**: [`ProfileClassRef`](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClassRef.md)[]

#### Inherited from

[ProfileClass](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClass.md).[refs](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClass.md#refs)

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:234](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L234)

___

### required

• `Optional` **required**: `boolean`

#### Inherited from

[ProfileClass](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClass.md).[required](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClass.md#required)

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:228](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L228)

## Methods

### addProfile

▸ **addProfile**(`profile`): `void`

Adds a profile to the profiles array of the ProfileLayoutClass.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `profile` | [`ProfileID`](../modules/common_web_ui_components_propertyeditor_PropertyProfile.md#profileid) | The profile ID to be added. |

#### Returns

`void`

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:338](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L338)

___

### getDescription

▸ **getDescription**(): `undefined` \| `string`

Retrieves the description of the property class.

#### Returns

`undefined` \| `string`

The description of the property class.

#### Inherited from

[ProfileClass](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClass.md).[getDescription](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClass.md#getdescription)

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:303](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L303)

___

### getDisplayLabel

▸ **getDisplayLabel**(): `string`

Retrieves the displayLabel of the ProfileClass.

#### Returns

`string`

The displayLabel of the ProfileClass.

#### Inherited from

[ProfileClass](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClass.md).[getDisplayLabel](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClass.md#getdisplaylabel)

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:294](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L294)

___

### getExample

▸ **getExample**(): `undefined` \| `string`

Retrieves an example for the property class.

#### Returns

`undefined` \| `string`

The current value of the example class.

#### Inherited from

[ProfileClass](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClass.md).[getExample](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClass.md#getexample)

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:312](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L312)

___

### getId

▸ **getId**(): `string`

Retrieves the unique identifier of the ProfileClass.

#### Returns

`string`

The unique identifier of the ProfileClass.

#### Inherited from

[ProfileClass](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClass.md).[getId](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClass.md#getid)

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:285](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L285)

___

### getInputs

▸ **getInputs**(): [`ProfileClassInput`](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClassInput.md)[]

Retrieves the inputs of the ProfileClass.

#### Returns

[`ProfileClassInput`](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClassInput.md)[]

The input property.

#### Inherited from

[ProfileClass](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClass.md).[getInputs](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClass.md#getinputs)

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:267](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L267)

___

### getProfiles

▸ **getProfiles**(): [`ProfileID`](../modules/common_web_ui_components_propertyeditor_PropertyProfile.md#profileid)[]

Retrieves the list of profiles.

#### Returns

[`ProfileID`](../modules/common_web_ui_components_propertyeditor_PropertyProfile.md#profileid)[]

An array of profiles.

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:347](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L347)

___

### getRefTypes

▸ **getRefTypes**(): [`ProfileClassRef`](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClassRef.md)[]

Retrieves the types that the ProfileClass can reference.

#### Returns

[`ProfileClassRef`](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClassRef.md)[]

The types of the ProfileClass.

#### Inherited from

[ProfileClass](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClass.md).[getRefTypes](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClass.md#getreftypes)

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:276](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L276)

___

### isRequired

▸ **isRequired**(): `undefined` \| `boolean`

Checks if the property is required.

#### Returns

`undefined` \| `boolean`

True if the property is required, otherwise false.

#### Inherited from

[ProfileClass](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClass.md).[isRequired](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClass.md#isrequired)

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:321](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L321)

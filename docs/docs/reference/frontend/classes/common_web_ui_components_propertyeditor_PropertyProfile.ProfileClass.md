---
id: "common_web_ui_components_propertyeditor_PropertyProfile.ProfileClass"
title: "Class: ProfileClass"
sidebar_label: "ProfileClass"
custom_edit_url: null
---

[common/web/ui/components/propertyeditor/PropertyProfile](../modules/common_web_ui_components_propertyeditor_PropertyProfile.md).ProfileClass

Represents a profile with various properties and inputs.

## Hierarchy

- **`ProfileClass`**

  ↳ [`ProfileLayoutClass`](common_web_ui_components_propertyeditor_PropertyProfile.ProfileLayoutClass.md)

## Constructors

### constructor

• **new ProfileClass**(`id`, `displayLabel`, `description?`, `labelTemplate?`, `required?`, `multiple?`, `example?`, `refs?`, `input?`): [`ProfileClass`](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClass.md)

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

[`ProfileClass`](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClass.md)

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:240](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L240)

## Properties

### description

• `Optional` `Readonly` **description**: `string`

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:226](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L226)

___

### displayLabel

• `Readonly` **displayLabel**: `string`

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:225](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L225)

___

### example

• `Optional` `Readonly` **example**: `string`

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:230](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L230)

___

### id

• `Readonly` **id**: `string`

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:224](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L224)

___

### input

• `Readonly` **input**: [`ProfileClassInput`](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClassInput.md)[]

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:238](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L238)

___

### labelTemplate

• `Optional` `Readonly` **labelTemplate**: `string`

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:227](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L227)

___

### multiple

• `Optional` `Readonly` **multiple**: `boolean`

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:229](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L229)

___

### refs

• `Readonly` **refs**: [`ProfileClassRef`](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClassRef.md)[]

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:234](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L234)

___

### required

• `Optional` **required**: `boolean`

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:228](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L228)

## Methods

### getDescription

▸ **getDescription**(): `undefined` \| `string`

Retrieves the description of the property class.

#### Returns

`undefined` \| `string`

The description of the property class.

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:303](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L303)

___

### getDisplayLabel

▸ **getDisplayLabel**(): `string`

Retrieves the displayLabel of the ProfileClass.

#### Returns

`string`

The displayLabel of the ProfileClass.

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:294](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L294)

___

### getExample

▸ **getExample**(): `undefined` \| `string`

Retrieves an example for the property class.

#### Returns

`undefined` \| `string`

The current value of the example class.

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:312](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L312)

___

### getId

▸ **getId**(): `string`

Retrieves the unique identifier of the ProfileClass.

#### Returns

`string`

The unique identifier of the ProfileClass.

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:285](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L285)

___

### getInputs

▸ **getInputs**(): [`ProfileClassInput`](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClassInput.md)[]

Retrieves the inputs of the ProfileClass.

#### Returns

[`ProfileClassInput`](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClassInput.md)[]

The input property.

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:267](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L267)

___

### getRefTypes

▸ **getRefTypes**(): [`ProfileClassRef`](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClassRef.md)[]

Retrieves the types that the ProfileClass can reference.

#### Returns

[`ProfileClassRef`](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClassRef.md)[]

The types of the ProfileClass.

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:276](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L276)

___

### isRequired

▸ **isRequired**(): `undefined` \| `boolean`

Checks if the property is required.

#### Returns

`undefined` \| `boolean`

True if the property is required, otherwise false.

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:321](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L321)

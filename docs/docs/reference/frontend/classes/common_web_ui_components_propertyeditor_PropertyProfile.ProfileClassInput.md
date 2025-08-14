---
id: "common_web_ui_components_propertyeditor_PropertyProfile.ProfileClassInput"
title: "Class: ProfileClassInput"
sidebar_label: "ProfileClassInput"
custom_edit_url: null
---

[common/web/ui/components/propertyeditor/PropertyProfile](../modules/common_web_ui_components_propertyeditor_PropertyProfile.md).ProfileClassInput

Represents an input for a profile class.

## Constructors

### constructor

• **new ProfileClassInput**(`id`, `label`, `type`, `description?`, `example?`, `options?`, `required?`, `hints?`): [`ProfileClassInput`](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClassInput.md)

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `id` | `string` | `undefined` |
| `label` | `string` | `undefined` |
| `type` | `string` | `undefined` |
| `description?` | `string` | `undefined` |
| `example?` | `string` | `undefined` |
| `options` | `string`[] | `[]` |
| `required?` | `boolean` | `undefined` |
| `hints?` | `Object` | `undefined` |

#### Returns

[`ProfileClassInput`](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClassInput.md)

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:83](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L83)

## Properties

### description

• `Optional` `Readonly` **description**: `string`

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:77](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L77)

___

### example

• `Optional` `Readonly` **example**: `string`

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:78](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L78)

___

### hints

• `Optional` **hints**: `Object`

#### Index signature

▪ [key: `string`]: \{ `[key: string]`: `any`;  }

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:81](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L81)

___

### id

• `Readonly` **id**: `string`

Creates an instance of `ProfileClassInput`.

**`Param`**

The ID of the input.

**`Param`**

The label of the input.

**`Param`**

The type of the input.

**`Param`**

The description of the input.

**`Param`**

An example of the input.

**`Param`**

The options of the input.

**`Param`**

Whether the input is required.

**`Param`**

Hints for certain inputs

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:74](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L74)

___

### label

• `Readonly` **label**: `string`

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:75](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L75)

___

### options

• `Optional` `Readonly` **options**: `string`[]

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:79](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L79)

___

### required

• `Optional` **required**: `boolean`

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:80](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L80)

___

### type

• `Readonly` **type**: `string`

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:76](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L76)

## Methods

### getDescription

▸ **getDescription**(): `undefined` \| `string`

Retrieves the description of the property input.

#### Returns

`undefined` \| `string`

The description of the property input.

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:117](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L117)

___

### getExample

▸ **getExample**(): `undefined` \| `string`

Retrieves the example of the property input.

#### Returns

`undefined` \| `string`

The example of the property input.

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:126](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L126)

___

### getHint

▸ **getHint**(`input`, `hintType`): `any`

Retrieves a hint based on the provided input and hint type.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `input` | `string` | The key used to look up the hint. |
| `hintType` | [`HintType`](../enums/common_web_ui_components_propertyeditor_PropertyProfile.HintType.md) | The specific type of hint to retrieve. |

#### Returns

`any`

An object representing the hint, or undefined if no hint is found.

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:174](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L174)

___

### getId

▸ **getId**(): `string`

Retrieves the unique identifier of the property input.

#### Returns

`string`

The identifier of the property input.

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:108](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L108)

___

### getLabel

▸ **getLabel**(): `string`

Retrieves the label of the property input.

#### Returns

`string`

The label of the property input.

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:135](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L135)

___

### getOptions

▸ **getOptions**(): `string`[]

Retrieves the options of the input.

#### Returns

`string`[]

The options of the property input.

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:153](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L153)

___

### getType

▸ **getType**(): `string`

Retrieves the type of the property input.

#### Returns

`string`

The type of the property input.

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:144](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L144)

___

### hasHints

▸ **hasHints**(`input`): `boolean`

Determines whether hints exist for the given input key.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `input` | `string` | The key to check for associated hints. |

#### Returns

`boolean`

`true` if hints exist for the specified input key; otherwise, `false`.

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:163](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L163)

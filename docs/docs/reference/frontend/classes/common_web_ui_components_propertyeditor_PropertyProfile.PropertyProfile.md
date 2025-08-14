---
id: "common_web_ui_components_propertyeditor_PropertyProfile.PropertyProfile"
title: "Class: PropertyProfile"
sidebar_label: "PropertyProfile"
custom_edit_url: null
---

[common/web/ui/components/propertyeditor/PropertyProfile](../modules/common_web_ui_components_propertyeditor_PropertyProfile.md).PropertyProfile

Represents a property profile with metadata, layout, and classes.

**`Remarks`**

This class is used to encapsulate the profile metadata, layout, and class dictionary
for a property editor component.

## Constructors

### constructor

• **new PropertyProfile**(`metadata`, `layout`, `classes?`): [`PropertyProfile`](common_web_ui_components_propertyeditor_PropertyProfile.PropertyProfile.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `metadata` | `ProfileMetadata` |
| `layout` | [`ProfileLayoutClass`](common_web_ui_components_propertyeditor_PropertyProfile.ProfileLayoutClass.md)[] |
| `classes?` | `ProfileClassDictionary` |

#### Returns

[`PropertyProfile`](common_web_ui_components_propertyeditor_PropertyProfile.PropertyProfile.md)

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:382](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L382)

## Properties

### classes

• `Optional` `Readonly` **classes**: `ProfileClassDictionary` = `{}`

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:380](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L380)

___

### layout

• `Readonly` **layout**: [`ProfileLayoutClass`](common_web_ui_components_propertyeditor_PropertyProfile.ProfileLayoutClass.md)[] = `[]`

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:376](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L376)

___

### metadata

• `Readonly` **metadata**: `ProfileMetadata`

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:372](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L372)

## Methods

### getClasses

▸ **getClasses**(): `undefined` \| `ProfileClassDictionary`

Gets the classes part of the profile

#### Returns

`undefined` \| `ProfileClassDictionary`

the profile classes

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:400](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L400)

___

### getDescription

▸ **getDescription**(): `string`

Retrieves the description from the metadata.

#### Returns

`string`

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:440](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L440)

___

### getDisplayLabel

▸ **getDisplayLabel**(): `string`

Retrieves the display label from the metadata.

#### Returns

`string`

The display label.

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:433](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L433)

___

### getId

▸ **getId**(): [`ProfileID`](../modules/common_web_ui_components_propertyeditor_PropertyProfile.md#profileid)

Gets the version part of the ProfileID

#### Returns

[`ProfileID`](../modules/common_web_ui_components_propertyeditor_PropertyProfile.md#profileid)

the ProfileID version

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:408](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L408)

___

### getLayout

▸ **getLayout**(): [`ProfileLayoutClass`](common_web_ui_components_propertyeditor_PropertyProfile.ProfileLayoutClass.md)[]

Gets the layout part of the profile

#### Returns

[`ProfileLayoutClass`](common_web_ui_components_propertyeditor_PropertyProfile.ProfileLayoutClass.md)[]

the profile layout

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:392](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L392)

___

### getName

▸ **getName**(): `string`

Gets the name part of the ProfileID

#### Returns

`string`

the ProfileID name

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:416](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L416)

___

### getVersion

▸ **getVersion**(): `string`

Gets the version part of the ProfileID

#### Returns

`string`

the ProfileID version

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:424](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L424)

---
id: "common_web_ui_components_propertyeditor_PropertyProfile.ProfileClassRef"
title: "Class: ProfileClassRef"
sidebar_label: "ProfileClassRef"
custom_edit_url: null
---

[common/web/ui/components/propertyeditor/PropertyProfile](../modules/common_web_ui_components_propertyeditor_PropertyProfile.md).ProfileClassRef

## Constructors

### constructor

• **new ProfileClassRef**(`classId`, `required?`, `inline?`, `multiple?`): [`ProfileClassRef`](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClassRef.md)

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `classId` | `string` | `undefined` |
| `required` | `Boolean` | `false` |
| `inline` | `Boolean` | `false` |
| `multiple` | `Boolean` | `true` |

#### Returns

[`ProfileClassRef`](common_web_ui_components_propertyeditor_PropertyProfile.ProfileClassRef.md)

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:185](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L185)

## Properties

### classId

• `Readonly` **classId**: `string`

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:180](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L180)

___

### inline

• `Readonly` **inline**: `Boolean`

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:182](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L182)

___

### multiple

• `Readonly` **multiple**: `Boolean`

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:183](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L183)

___

### required

• `Readonly` **required**: `Boolean`

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:181](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L181)

## Methods

### allowsMultiple

▸ **allowsMultiple**(): `Boolean`

Determines if multiple refs of this type are allowed.

#### Returns

`Boolean`

True if multiple refs are allowed, otherwise false.

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:215](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L215)

___

### getClassId

▸ **getClassId**(): `string`

Retrieves the class type identifier.

#### Returns

`string`

The class identifier.

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:197](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L197)

___

### isInline

▸ **isInline**(): `Boolean`

Checks if the ref property is set to inline mode.

#### Returns

`Boolean`

True if the property is inline, otherwise false.

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:206](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L206)

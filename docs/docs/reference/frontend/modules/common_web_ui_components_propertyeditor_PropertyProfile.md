---
id: "common_web_ui_components_propertyeditor_PropertyProfile"
title: "Module: common/web/ui/components/propertyeditor/PropertyProfile"
sidebar_label: "common/web/ui/components/propertyeditor/PropertyProfile"
sidebar_position: 0
custom_edit_url: null
---

## Enumerations

- [HintType](../enums/common_web_ui_components_propertyeditor_PropertyProfile.HintType.md)
- [PropertyDataType](../enums/common_web_ui_components_propertyeditor_PropertyProfile.PropertyDataType.md)

## Classes

- [ProfileClass](../classes/common_web_ui_components_propertyeditor_PropertyProfile.ProfileClass.md)
- [ProfileClassInput](../classes/common_web_ui_components_propertyeditor_PropertyProfile.ProfileClassInput.md)
- [ProfileClassRef](../classes/common_web_ui_components_propertyeditor_PropertyProfile.ProfileClassRef.md)
- [ProfileLayoutClass](../classes/common_web_ui_components_propertyeditor_PropertyProfile.ProfileLayoutClass.md)
- [PropertyProfile](../classes/common_web_ui_components_propertyeditor_PropertyProfile.PropertyProfile.md)

## Type Aliases

### ProfileID

Ƭ **ProfileID**: [`string`, `string`]

Represents a profile ID. usually [profilename, profileversion]

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:18](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L18)

## Variables

### propertyDataForms

• `Const` **propertyDataForms**: \{ [key in PropertyDataType]?: Component }

A mapping of `PropertyDataType` to their corresponding form components.
This object is used to dynamically render the appropriate form component
based on the type of property data.

**`Type Param`**

The type of property data.

**`Type Param`**

The form component associated with the property data type.

#### Defined in

[src/common/web/ui/components/propertyeditor/PropertyProfile.ts:493](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/ui/components/propertyeditor/PropertyProfile.ts#L493)

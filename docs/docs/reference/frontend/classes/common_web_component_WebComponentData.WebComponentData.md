---
id: "common_web_component_WebComponentData.WebComponentData"
title: "Class: WebComponentData"
sidebar_label: "WebComponentData"
custom_edit_url: null
---

[common/web/component/WebComponentData](../modules/common_web_component_WebComponentData.md).WebComponentData

Holds general data and information about the component.

Objects of this class are passed to certain parts of the core for easy access to frequently
used component information and data.

## Constructors

### constructor

• **new WebComponentData**(`compID`, `config`, `title`, `name`, `version`): [`WebComponentData`](common_web_component_WebComponentData.WebComponentData.md)

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `compID` | [`UnitID`](common_web_utils_UnitID.UnitID.md) | The component identifier. |
| `config` | [`Configuration`](common_web_utils_config_Configuration.Configuration.md) | The configuration. |
| `title` | `string` | The project title. |
| `name` | `string` | The component name. |
| `version` | `SemVer` | The project version. |

#### Returns

[`WebComponentData`](common_web_component_WebComponentData.WebComponentData.md)

#### Defined in

[src/common/web/component/WebComponentData.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponentData.ts#L20)

## Properties

### compID

• `Readonly` **compID**: [`UnitID`](common_web_utils_UnitID.UnitID.md)

The component identifier.

#### Defined in

[src/common/web/component/WebComponentData.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponentData.ts#L20)

___

### config

• `Readonly` **config**: [`Configuration`](common_web_utils_config_Configuration.Configuration.md)

The configuration.

#### Defined in

[src/common/web/component/WebComponentData.ts:20](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponentData.ts#L20)

___

### name

• `Readonly` **name**: `string`

The component name.

#### Defined in

[src/common/web/component/WebComponentData.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponentData.ts#L21)

___

### title

• `Readonly` **title**: `string`

The project title.

#### Defined in

[src/common/web/component/WebComponentData.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponentData.ts#L21)

___

### version

• `Readonly` **version**: `SemVer`

The project version.

#### Defined in

[src/common/web/component/WebComponentData.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/WebComponentData.ts#L21)

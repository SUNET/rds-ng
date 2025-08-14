---
id: "common_web_component_MetaInformation.MetaInformation"
title: "Class: MetaInformation"
sidebar_label: "MetaInformation"
custom_edit_url: null
---

[common/web/component/MetaInformation](../modules/common_web_component_MetaInformation.md).MetaInformation

Accesses meta information about the entire project and its various component stored in a *JSON* file.

The JSON file needs to be structured like this:
```
{
    "global": {
        "title": "RDS-NG",
        "version": "0.0.1"
    },
    "components": {
        "web-frontend": {
            "name": "Web Frontend",
            "directory": "frontend",
            "tech": "web"
        },
        ...
    }
}
```

## Constructors

### constructor

• **new MetaInformation**(): [`MetaInformation`](common_web_component_MetaInformation.MetaInformation.md)

#### Returns

[`MetaInformation`](common_web_component_MetaInformation.MetaInformation.md)

## Properties

### \_data

• `Private` `Readonly` **\_data**: `MetaInformationType`

#### Defined in

[src/common/web/component/MetaInformation.ts:41](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/MetaInformation.ts#L41)

## Accessors

### title

• `get` **title**(): `string`

The project title.

#### Returns

`string`

#### Defined in

[src/common/web/component/MetaInformation.ts:46](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/MetaInformation.ts#L46)

___

### version

• `get` **version**(): `SemVer`

The project version (see https://semver.org).

#### Returns

`SemVer`

#### Defined in

[src/common/web/component/MetaInformation.ts:53](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/MetaInformation.ts#L53)

## Methods

### getComponent

▸ **getComponent**(`comp`): `ComponentInformationType`

Retrieves the meta information stored for a specific component.

This meta information includes the ``name`` of the component, as well as its ``directory`` within the code structure (rooted at ``/src``).

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `comp` | `string` | The name of the component. |

#### Returns

`ComponentInformationType`

- A dictionary containing the meta information.

#### Defined in

[src/common/web/component/MetaInformation.ts:66](https://github.com/Sciebo-RDS/rds-ng/blob/cd602ee64/src/common/web/component/MetaInformation.ts#L66)

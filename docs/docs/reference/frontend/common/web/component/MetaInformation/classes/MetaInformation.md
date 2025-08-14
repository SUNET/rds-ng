# Class: MetaInformation

Defined in: [src/common/web/component/MetaInformation.ts:40](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/MetaInformation.ts#L40)

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

### Constructor

> **new MetaInformation**(): `MetaInformation`

#### Returns

`MetaInformation`

## Accessors

### title

#### Get Signature

> **get** **title**(): `string`

Defined in: [src/common/web/component/MetaInformation.ts:46](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/MetaInformation.ts#L46)

The project title.

##### Returns

`string`

***

### version

#### Get Signature

> **get** **version**(): `SemVer`

Defined in: [src/common/web/component/MetaInformation.ts:53](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/MetaInformation.ts#L53)

The project version (see https://semver.org).

##### Returns

`SemVer`

## Methods

### getComponent()

> **getComponent**(`comp`): `ComponentInformationType`

Defined in: [src/common/web/component/MetaInformation.ts:66](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/component/MetaInformation.ts#L66)

Retrieves the meta information stored for a specific component.

This meta information includes the ``name`` of the component, as well as its ``directory`` within the code structure (rooted at ``/src``).

#### Parameters

##### comp

`string`

The name of the component.

#### Returns

`ComponentInformationType`

- A dictionary containing the meta information.

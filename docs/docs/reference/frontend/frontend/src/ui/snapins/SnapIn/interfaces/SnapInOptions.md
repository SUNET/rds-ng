# Interface: SnapInOptions

Defined in: [src/frontend/src/ui/snapins/SnapIn.ts:16](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/snapins/SnapIn.ts#L16)

Options to initialize a snap-in.

## Properties

### name

> **name**: `string`

Defined in: [src/frontend/src/ui/snapins/SnapIn.ts:18](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/snapins/SnapIn.ts#L18)

The general display name.

***

### optional?

> `optional` **optional**: `object`

Defined in: [src/frontend/src/ui/snapins/SnapIn.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/snapins/SnapIn.ts#L21)

Options specific to optional snap-ins (and their associated feature, if any).

#### description?

> `optional` **description**: `string`

A description of the feature.

#### feature?

> `optional` **feature**: `string`

The ID of a directly associated project feature. If set, the associated feature will be en-/disabled alongside the snap-in.

#### label

> **label**: `string`

The label name of the option (shown as a checkbox) for this snap-in.

***

### tabPanel?

> `optional` **tabPanel**: `object`

Defined in: [src/frontend/src/ui/snapins/SnapIn.ts:33](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/snapins/SnapIn.ts#L33)

Tab-panel options.

#### description

> **description**: `string`

Description of the panel.

#### label

> **label**: `string`

The tab panel label name (displayed as its header).

#### loader

> **loader**: [`SnapInPanelLoader`](../type-aliases/SnapInPanelLoader.md)

The panel loader.

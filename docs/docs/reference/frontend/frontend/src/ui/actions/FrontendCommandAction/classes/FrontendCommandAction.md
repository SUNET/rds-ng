# Abstract Class: FrontendCommandAction\<CmdType, CompType\>

Defined in: [src/frontend/src/ui/actions/FrontendCommandAction.ts:10](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/actions/FrontendCommandAction.ts#L10)

Command actions specific to the frontend.

## Extends

- [`CommandAction`](../../../../../../common/web/ui/actions/CommandAction/classes/CommandAction.md)\<`CmdType`, `CompType`\>

## Extended by

- [`ListUserAuthorizationsAction`](../../authorization/ListUserAuthorizationsAction/classes/ListUserAuthorizationsAction.md)
- [`RevokeAuthorizationAction`](../../authorization/RevokeAuthorizationAction/classes/RevokeAuthorizationAction.md)
- [`ListConnectorsAction`](../../connector/ListConnectorsAction/classes/ListConnectorsAction.md)
- [`GetMetadataProfilesAction`](../../metadata/GetMetadataProfilesAction/classes/GetMetadataProfilesAction.md)
- [`CreateProjectAction`](../../project/CreateProjectAction/classes/CreateProjectAction.md)
- [`DeleteProjectAction`](../../project/DeleteProjectAction/classes/DeleteProjectAction.md)
- [`ExportProjectAction`](../../project/ExportProjectAction/classes/ExportProjectAction.md)
- [`InitiateProjectJobAction`](../../project/InitiateProjectJobAction/classes/InitiateProjectJobAction.md)
- [`ListProjectJobsAction`](../../project/ListProjectJobsAction/classes/ListProjectJobsAction.md)
- [`ListProjectgExportersAction`](../../project/ListProjectgExportersAction/classes/ListProjectgExportersAction.md)
- [`ListProjectsAction`](../../project/ListProjectsAction/classes/ListProjectsAction.md)
- [`MarkProjectLogbookSeenAction`](../../project/MarkProjectLogbookSeenAction/classes/MarkProjectLogbookSeenAction.md)
- [`UpdateProjectAction`](../../project/UpdateProjectAction/classes/UpdateProjectAction.md)
- [`UpdateProjectFeaturesAction`](../../project/UpdateProjectFeaturesAction/classes/UpdateProjectFeaturesAction.md)
- [`GetResourceAction`](../../resource/GetResourceAction/classes/GetResourceAction.md)
- [`ListResourcesAction`](../../resource/ListResourcesAction/classes/ListResourcesAction.md)
- [`GetSessionValueAction`](../../session/GetSessionValueAction/classes/GetSessionValueAction.md)
- [`SetSessionValueAction`](../../session/SetSessionValueAction/classes/SetSessionValueAction.md)
- [`GetUserSettingsAction`](../../user/GetUserSettingsAction/classes/GetUserSettingsAction.md)
- [`SetUserSettingsAction`](../../user/SetUserSettingsAction/classes/SetUserSettingsAction.md)

## Type Parameters

### CmdType

`CmdType` *extends* [`Command`](../../../../../../common/web/core/messaging/Command/classes/Command.md)

### CompType

`CompType` *extends* [`CommandComposer`](../../../../../../common/web/core/messaging/composers/CommandComposer/classes/CommandComposer.md)\<`CmdType`\>

## Constructors

### Constructor

> **new FrontendCommandAction**\<`CmdType`, `CompType`\>(`comp`, `suppressDefaultNotifiers`): `FrontendCommandAction`\<`CmdType`, `CompType`\>

Defined in: [src/frontend/src/ui/actions/FrontendCommandAction.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/actions/FrontendCommandAction.ts#L17)

#### Parameters

##### comp

[`FrontendComponent`](../../../../component/FrontendComponent/classes/FrontendComponent.md)

The main frontend component.

##### suppressDefaultNotifiers

`boolean` = `false`

Suppress default notifiers.

#### Returns

`FrontendCommandAction`\<`CmdType`, `CompType`\>

#### Overrides

[`CommandAction`](../../../../../../common/web/ui/actions/CommandAction/classes/CommandAction.md).[`constructor`](../../../../../../common/web/ui/actions/CommandAction/classes/CommandAction.md#constructor)

## Properties

### \_component

> `protected` **\_component**: [`FrontendComponent`](../../../../component/FrontendComponent/classes/FrontendComponent.md)

Defined in: [src/frontend/src/ui/actions/FrontendCommandAction.ts:11](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/actions/FrontendCommandAction.ts#L11)

***

### \_composer

> `protected` **\_composer**: `null` \| `CompType` = `null`

Defined in: [src/common/web/ui/actions/Action.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/Action.ts#L19)

#### Inherited from

[`CommandAction`](../../../../../../common/web/ui/actions/CommandAction/classes/CommandAction.md).[`_composer`](../../../../../../common/web/ui/actions/CommandAction/classes/CommandAction.md#_composer)

***

### \_state

> `protected` **\_state**: [`ActionState`](../../../../../../common/web/ui/actions/ActionBase/enumerations/ActionState.md)

Defined in: [src/common/web/ui/actions/ActionBase.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L23)

#### Inherited from

[`CommandAction`](../../../../../../common/web/ui/actions/CommandAction/classes/CommandAction.md).[`_state`](../../../../../../common/web/ui/actions/CommandAction/classes/CommandAction.md#_state)

## Accessors

### messageBuilder

#### Get Signature

> **get** `protected` **messageBuilder**(): [`MessageBuilder`](../../../../../../common/web/core/messaging/composers/MessageBuilder/classes/MessageBuilder.md)

Defined in: [src/common/web/ui/actions/Action.ts:59](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/Action.ts#L59)

##### Returns

[`MessageBuilder`](../../../../../../common/web/core/messaging/composers/MessageBuilder/classes/MessageBuilder.md)

#### Inherited from

[`CommandAction`](../../../../../../common/web/ui/actions/CommandAction/classes/CommandAction.md).[`messageBuilder`](../../../../../../common/web/ui/actions/CommandAction/classes/CommandAction.md#messagebuilder)

***

### state

#### Get Signature

> **get** **state**(): [`ActionState`](../../../../../../common/web/ui/actions/ActionBase/enumerations/ActionState.md)

Defined in: [src/common/web/ui/actions/ActionBase.ts:143](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L143)

The current state of the action.

##### Returns

[`ActionState`](../../../../../../common/web/ui/actions/ActionBase/enumerations/ActionState.md)

#### Inherited from

[`CommandAction`](../../../../../../common/web/ui/actions/CommandAction/classes/CommandAction.md).[`state`](../../../../../../common/web/ui/actions/CommandAction/classes/CommandAction.md#state)

## Methods

### addDefaultNotifiers()

> `protected` **addDefaultNotifiers**(...`args`): `void`

Defined in: [src/common/web/ui/actions/ActionBase.ts:90](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L90)

#### Parameters

##### args

...`any`[]

#### Returns

`void`

#### Inherited from

[`CommandAction`](../../../../../../common/web/ui/actions/CommandAction/classes/CommandAction.md).[`addDefaultNotifiers`](../../../../../../common/web/ui/actions/CommandAction/classes/CommandAction.md#adddefaultnotifiers)

***

### addNotifier()

> **addNotifier**(`state`, `notifier`, `verboseOnly`): `void`

Defined in: [src/common/web/ui/actions/ActionBase.ts:66](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L66)

Adds a new notifier for the specified state.

#### Parameters

##### state

[`ActionState`](../../../../../../common/web/ui/actions/ActionBase/enumerations/ActionState.md)

The state the notifier should react to.

##### notifier

The notifier.

[`ActionNotifier`](../../../../../../common/web/ui/actions/notifiers/ActionNotifier/classes/ActionNotifier.md) | [`ActionNotifier`](../../../../../../common/web/ui/actions/notifiers/ActionNotifier/classes/ActionNotifier.md)[]

##### verboseOnly

`boolean` = `false`

If true, the notification will only be added in verbose mode.

#### Returns

`void`

#### Inherited from

[`CommandAction`](../../../../../../common/web/ui/actions/CommandAction/classes/CommandAction.md).[`addNotifier`](../../../../../../common/web/ui/actions/CommandAction/classes/CommandAction.md#addnotifier)

***

### completed()

> **completed**(`cb`): `this`

Defined in: [src/common/web/ui/actions/ActionBase.ts:44](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L44)

Adds a callback for action completion.

#### Parameters

##### cb

[`ActionDoneCallback`](../../../../../../common/web/ui/actions/ActionBase/type-aliases/ActionDoneCallback.md)

The callback to add.

#### Returns

`this`

#### Inherited from

[`CommandAction`](../../../../../../common/web/ui/actions/CommandAction/classes/CommandAction.md).[`completed`](../../../../../../common/web/ui/actions/CommandAction/classes/CommandAction.md#completed)

***

### execute()

> **execute**(): `void`

Defined in: [src/common/web/ui/actions/Action.ts:44](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/Action.ts#L44)

Executes the action (i.e., the message will be emitted).

#### Returns

`void`

#### Inherited from

[`CommandAction`](../../../../../../common/web/ui/actions/CommandAction/classes/CommandAction.md).[`execute`](../../../../../../common/web/ui/actions/CommandAction/classes/CommandAction.md#execute)

***

### failed()

> **failed**(`cb`): `this`

Defined in: [src/common/web/ui/actions/ActionBase.ts:54](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L54)

Adds a callback for action failure.

#### Parameters

##### cb

[`ActionFailCallback`](../../../../../../common/web/ui/actions/ActionBase/type-aliases/ActionFailCallback.md)

The callback to add.

#### Returns

`this`

#### Inherited from

[`CommandAction`](../../../../../../common/web/ui/actions/CommandAction/classes/CommandAction.md).[`failed`](../../../../../../common/web/ui/actions/CommandAction/classes/CommandAction.md#failed)

***

### onStateChanged()

> `protected` **onStateChanged**(`newState`, `oldState`): `void`

Defined in: [src/common/web/ui/actions/ActionBase.ts:134](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L134)

#### Parameters

##### newState

[`ActionState`](../../../../../../common/web/ui/actions/ActionBase/enumerations/ActionState.md)

##### oldState

[`ActionState`](../../../../../../common/web/ui/actions/ActionBase/enumerations/ActionState.md)

#### Returns

`void`

#### Inherited from

[`CommandAction`](../../../../../../common/web/ui/actions/CommandAction/classes/CommandAction.md).[`onStateChanged`](../../../../../../common/web/ui/actions/CommandAction/classes/CommandAction.md#onstatechanged)

***

### postExecution()

> `protected` **postExecution**(): `void`

Defined in: [src/common/web/ui/actions/ActionBase.ts:138](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L138)

#### Returns

`void`

#### Inherited from

[`CommandAction`](../../../../../../common/web/ui/actions/CommandAction/classes/CommandAction.md).[`postExecution`](../../../../../../common/web/ui/actions/CommandAction/classes/CommandAction.md#postexecution)

***

### preExecution()

> `protected` **preExecution**(): `void`

Defined in: [src/common/web/ui/actions/CommandAction.ts:11](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/CommandAction.ts#L11)

#### Returns

`void`

#### Inherited from

[`CommandAction`](../../../../../../common/web/ui/actions/CommandAction/classes/CommandAction.md).[`preExecution`](../../../../../../common/web/ui/actions/CommandAction/classes/CommandAction.md#preexecution)

***

### prepare()

> `abstract` **prepare**(...`args`): `CompType`

Defined in: [src/common/web/ui/actions/Action.ts:39](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/Action.ts#L39)

Prepares this action.

#### Parameters

##### args

...`any`[]

#### Returns

`CompType`

- A message composer that can be further modified.

#### Inherited from

[`CommandAction`](../../../../../../common/web/ui/actions/CommandAction/classes/CommandAction.md).[`prepare`](../../../../../../common/web/ui/actions/CommandAction/classes/CommandAction.md#prepare)

***

### prepareNotifiers()

> `protected` **prepareNotifiers**(...`args`): `void`

Defined in: [src/common/web/ui/actions/ActionBase.ts:84](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L84)

#### Parameters

##### args

...`any`[]

#### Returns

`void`

#### Inherited from

[`CommandAction`](../../../../../../common/web/ui/actions/CommandAction/classes/CommandAction.md).[`prepareNotifiers`](../../../../../../common/web/ui/actions/CommandAction/classes/CommandAction.md#preparenotifiers)

***

### setState()

> `protected` **setState**(`state`, `message`): `void`

Defined in: [src/common/web/ui/actions/ActionBase.ts:103](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L103)

Sets the active state of this action.

#### Parameters

##### state

[`ActionState`](../../../../../../common/web/ui/actions/ActionBase/enumerations/ActionState.md)

The state to apply

##### message

`string` = `""`

An optional notification message.

#### Returns

`void`

#### Inherited from

[`CommandAction`](../../../../../../common/web/ui/actions/CommandAction/classes/CommandAction.md).[`setState`](../../../../../../common/web/ui/actions/CommandAction/classes/CommandAction.md#setstate)

# Class: ListProjectJobsAction

Defined in: [src/frontend/src/ui/actions/project/ListProjectJobsAction.ts:13](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/actions/project/ListProjectJobsAction.ts#L13)

Action to retrieve all projects.

## Extends

- [`FrontendCommandAction`](../../../FrontendCommandAction/classes/FrontendCommandAction.md)\<[`ListProjectJobsCommand`](../../../../../../../common/web/api/project/ProjectJobCommands/classes/ListProjectJobsCommand.md), [`CommandComposer`](../../../../../../../common/web/core/messaging/composers/CommandComposer/classes/CommandComposer.md)\<[`ListProjectJobsCommand`](../../../../../../../common/web/api/project/ProjectJobCommands/classes/ListProjectJobsCommand.md)\>\>

## Constructors

### Constructor

> **new ListProjectJobsAction**(`comp`, `suppressDefaultNotifiers`): `ListProjectJobsAction`

Defined in: [src/frontend/src/ui/actions/FrontendCommandAction.ts:17](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/actions/FrontendCommandAction.ts#L17)

#### Parameters

##### comp

[`FrontendComponent`](../../../../../component/FrontendComponent/classes/FrontendComponent.md)

The main frontend component.

##### suppressDefaultNotifiers

`boolean` = `false`

Suppress default notifiers.

#### Returns

`ListProjectJobsAction`

#### Inherited from

[`FrontendCommandAction`](../../../FrontendCommandAction/classes/FrontendCommandAction.md).[`constructor`](../../../FrontendCommandAction/classes/FrontendCommandAction.md#constructor)

## Properties

### \_component

> `protected` **\_component**: [`FrontendComponent`](../../../../../component/FrontendComponent/classes/FrontendComponent.md)

Defined in: [src/frontend/src/ui/actions/FrontendCommandAction.ts:11](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/actions/FrontendCommandAction.ts#L11)

#### Inherited from

[`FrontendCommandAction`](../../../FrontendCommandAction/classes/FrontendCommandAction.md).[`_component`](../../../FrontendCommandAction/classes/FrontendCommandAction.md#_component)

***

### \_composer

> `protected` **\_composer**: `null` \| [`CommandComposer`](../../../../../../../common/web/core/messaging/composers/CommandComposer/classes/CommandComposer.md)\<[`ListProjectJobsCommand`](../../../../../../../common/web/api/project/ProjectJobCommands/classes/ListProjectJobsCommand.md)\> = `null`

Defined in: [src/common/web/ui/actions/Action.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/Action.ts#L19)

#### Inherited from

[`FrontendCommandAction`](../../../FrontendCommandAction/classes/FrontendCommandAction.md).[`_composer`](../../../FrontendCommandAction/classes/FrontendCommandAction.md#_composer)

***

### \_state

> `protected` **\_state**: [`ActionState`](../../../../../../../common/web/ui/actions/ActionBase/enumerations/ActionState.md)

Defined in: [src/common/web/ui/actions/ActionBase.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L23)

#### Inherited from

[`FrontendCommandAction`](../../../FrontendCommandAction/classes/FrontendCommandAction.md).[`_state`](../../../FrontendCommandAction/classes/FrontendCommandAction.md#_state)

## Accessors

### messageBuilder

#### Get Signature

> **get** `protected` **messageBuilder**(): [`MessageBuilder`](../../../../../../../common/web/core/messaging/composers/MessageBuilder/classes/MessageBuilder.md)

Defined in: [src/common/web/ui/actions/Action.ts:59](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/Action.ts#L59)

##### Returns

[`MessageBuilder`](../../../../../../../common/web/core/messaging/composers/MessageBuilder/classes/MessageBuilder.md)

#### Inherited from

[`FrontendCommandAction`](../../../FrontendCommandAction/classes/FrontendCommandAction.md).[`messageBuilder`](../../../FrontendCommandAction/classes/FrontendCommandAction.md#messagebuilder)

***

### state

#### Get Signature

> **get** **state**(): [`ActionState`](../../../../../../../common/web/ui/actions/ActionBase/enumerations/ActionState.md)

Defined in: [src/common/web/ui/actions/ActionBase.ts:143](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L143)

The current state of the action.

##### Returns

[`ActionState`](../../../../../../../common/web/ui/actions/ActionBase/enumerations/ActionState.md)

#### Inherited from

[`FrontendCommandAction`](../../../FrontendCommandAction/classes/FrontendCommandAction.md).[`state`](../../../FrontendCommandAction/classes/FrontendCommandAction.md#state)

## Methods

### addDefaultNotifiers()

> `protected` **addDefaultNotifiers**(): `void`

Defined in: [src/frontend/src/ui/actions/project/ListProjectJobsAction.ts:21](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/actions/project/ListProjectJobsAction.ts#L21)

#### Returns

`void`

#### Overrides

[`FrontendCommandAction`](../../../FrontendCommandAction/classes/FrontendCommandAction.md).[`addDefaultNotifiers`](../../../FrontendCommandAction/classes/FrontendCommandAction.md#adddefaultnotifiers)

***

### addNotifier()

> **addNotifier**(`state`, `notifier`, `verboseOnly`): `void`

Defined in: [src/common/web/ui/actions/ActionBase.ts:66](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L66)

Adds a new notifier for the specified state.

#### Parameters

##### state

[`ActionState`](../../../../../../../common/web/ui/actions/ActionBase/enumerations/ActionState.md)

The state the notifier should react to.

##### notifier

The notifier.

[`ActionNotifier`](../../../../../../../common/web/ui/actions/notifiers/ActionNotifier/classes/ActionNotifier.md) | [`ActionNotifier`](../../../../../../../common/web/ui/actions/notifiers/ActionNotifier/classes/ActionNotifier.md)[]

##### verboseOnly

`boolean` = `false`

If true, the notification will only be added in verbose mode.

#### Returns

`void`

#### Inherited from

[`FrontendCommandAction`](../../../FrontendCommandAction/classes/FrontendCommandAction.md).[`addNotifier`](../../../FrontendCommandAction/classes/FrontendCommandAction.md#addnotifier)

***

### completed()

> **completed**(`cb`): `this`

Defined in: [src/common/web/ui/actions/ActionBase.ts:44](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L44)

Adds a callback for action completion.

#### Parameters

##### cb

[`ActionDoneCallback`](../../../../../../../common/web/ui/actions/ActionBase/type-aliases/ActionDoneCallback.md)

The callback to add.

#### Returns

`this`

#### Inherited from

[`FrontendCommandAction`](../../../FrontendCommandAction/classes/FrontendCommandAction.md).[`completed`](../../../FrontendCommandAction/classes/FrontendCommandAction.md#completed)

***

### execute()

> **execute**(): `void`

Defined in: [src/common/web/ui/actions/Action.ts:44](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/Action.ts#L44)

Executes the action (i.e., the message will be emitted).

#### Returns

`void`

#### Inherited from

[`FrontendCommandAction`](../../../FrontendCommandAction/classes/FrontendCommandAction.md).[`execute`](../../../FrontendCommandAction/classes/FrontendCommandAction.md#execute)

***

### failed()

> **failed**(`cb`): `this`

Defined in: [src/common/web/ui/actions/ActionBase.ts:54](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L54)

Adds a callback for action failure.

#### Parameters

##### cb

[`ActionFailCallback`](../../../../../../../common/web/ui/actions/ActionBase/type-aliases/ActionFailCallback.md)

The callback to add.

#### Returns

`this`

#### Inherited from

[`FrontendCommandAction`](../../../FrontendCommandAction/classes/FrontendCommandAction.md).[`failed`](../../../FrontendCommandAction/classes/FrontendCommandAction.md#failed)

***

### onStateChanged()

> `protected` **onStateChanged**(`newState`, `oldState`): `void`

Defined in: [src/common/web/ui/actions/ActionBase.ts:134](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L134)

#### Parameters

##### newState

[`ActionState`](../../../../../../../common/web/ui/actions/ActionBase/enumerations/ActionState.md)

##### oldState

[`ActionState`](../../../../../../../common/web/ui/actions/ActionBase/enumerations/ActionState.md)

#### Returns

`void`

#### Inherited from

[`FrontendCommandAction`](../../../FrontendCommandAction/classes/FrontendCommandAction.md).[`onStateChanged`](../../../FrontendCommandAction/classes/FrontendCommandAction.md#onstatechanged)

***

### postExecution()

> `protected` **postExecution**(): `void`

Defined in: [src/common/web/ui/actions/ActionBase.ts:138](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L138)

#### Returns

`void`

#### Inherited from

[`FrontendCommandAction`](../../../FrontendCommandAction/classes/FrontendCommandAction.md).[`postExecution`](../../../FrontendCommandAction/classes/FrontendCommandAction.md#postexecution)

***

### preExecution()

> `protected` **preExecution**(): `void`

Defined in: [src/common/web/ui/actions/CommandAction.ts:11](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/CommandAction.ts#L11)

#### Returns

`void`

#### Inherited from

[`FrontendCommandAction`](../../../FrontendCommandAction/classes/FrontendCommandAction.md).[`preExecution`](../../../FrontendCommandAction/classes/FrontendCommandAction.md#preexecution)

***

### prepare()

> **prepare**(): [`CommandComposer`](../../../../../../../common/web/core/messaging/composers/CommandComposer/classes/CommandComposer.md)\<[`ListProjectJobsCommand`](../../../../../../../common/web/api/project/ProjectJobCommands/classes/ListProjectJobsCommand.md)\>

Defined in: [src/frontend/src/ui/actions/project/ListProjectJobsAction.ts:14](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/actions/project/ListProjectJobsAction.ts#L14)

Prepares this action.

#### Returns

[`CommandComposer`](../../../../../../../common/web/core/messaging/composers/CommandComposer/classes/CommandComposer.md)\<[`ListProjectJobsCommand`](../../../../../../../common/web/api/project/ProjectJobCommands/classes/ListProjectJobsCommand.md)\>

- A message composer that can be further modified.

#### Overrides

[`FrontendCommandAction`](../../../FrontendCommandAction/classes/FrontendCommandAction.md).[`prepare`](../../../FrontendCommandAction/classes/FrontendCommandAction.md#prepare)

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

[`FrontendCommandAction`](../../../FrontendCommandAction/classes/FrontendCommandAction.md).[`prepareNotifiers`](../../../FrontendCommandAction/classes/FrontendCommandAction.md#preparenotifiers)

***

### setState()

> `protected` **setState**(`state`, `message`): `void`

Defined in: [src/common/web/ui/actions/ActionBase.ts:103](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L103)

Sets the active state of this action.

#### Parameters

##### state

[`ActionState`](../../../../../../../common/web/ui/actions/ActionBase/enumerations/ActionState.md)

The state to apply

##### message

`string` = `""`

An optional notification message.

#### Returns

`void`

#### Inherited from

[`FrontendCommandAction`](../../../FrontendCommandAction/classes/FrontendCommandAction.md).[`setState`](../../../FrontendCommandAction/classes/FrontendCommandAction.md#setstate)

# Class: TouchProjectAction

Defined in: [src/frontend/src/ui/actions/project/TouchProjectAction.ts:10](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/actions/project/TouchProjectAction.ts#L10)

Action to touch a project.

## Extends

- [`FrontendEventAction`](../../../FrontendEventAction/classes/FrontendEventAction.md)\<[`ProjectTouchEvent`](../../../../../../../common/web/api/project/ProjectEvents/classes/ProjectTouchEvent.md), [`EventComposer`](../../../../../../../common/web/core/messaging/composers/EventComposer/classes/EventComposer.md)\<[`ProjectTouchEvent`](../../../../../../../common/web/api/project/ProjectEvents/classes/ProjectTouchEvent.md)\>\>

## Constructors

### Constructor

> **new TouchProjectAction**(`comp`, `suppressDefaultNotifiers`): `TouchProjectAction`

Defined in: [src/frontend/src/ui/actions/FrontendEventAction.ts:15](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/actions/FrontendEventAction.ts#L15)

#### Parameters

##### comp

[`FrontendComponent`](../../../../../component/FrontendComponent/classes/FrontendComponent.md)

The main frontend component.

##### suppressDefaultNotifiers

`boolean` = `false`

Suppress default notifiers.

#### Returns

`TouchProjectAction`

#### Inherited from

[`FrontendEventAction`](../../../FrontendEventAction/classes/FrontendEventAction.md).[`constructor`](../../../FrontendEventAction/classes/FrontendEventAction.md#constructor)

## Properties

### \_composer

> `protected` **\_composer**: `null` \| [`EventComposer`](../../../../../../../common/web/core/messaging/composers/EventComposer/classes/EventComposer.md)\<[`ProjectTouchEvent`](../../../../../../../common/web/api/project/ProjectEvents/classes/ProjectTouchEvent.md)\> = `null`

Defined in: [src/common/web/ui/actions/Action.ts:19](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/Action.ts#L19)

#### Inherited from

[`FrontendEventAction`](../../../FrontendEventAction/classes/FrontendEventAction.md).[`_composer`](../../../FrontendEventAction/classes/FrontendEventAction.md#_composer)

***

### \_state

> `protected` **\_state**: [`ActionState`](../../../../../../../common/web/ui/actions/ActionBase/enumerations/ActionState.md)

Defined in: [src/common/web/ui/actions/ActionBase.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L23)

#### Inherited from

[`FrontendEventAction`](../../../FrontendEventAction/classes/FrontendEventAction.md).[`_state`](../../../FrontendEventAction/classes/FrontendEventAction.md#_state)

## Accessors

### messageBuilder

#### Get Signature

> **get** `protected` **messageBuilder**(): [`MessageBuilder`](../../../../../../../common/web/core/messaging/composers/MessageBuilder/classes/MessageBuilder.md)

Defined in: [src/common/web/ui/actions/Action.ts:59](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/Action.ts#L59)

##### Returns

[`MessageBuilder`](../../../../../../../common/web/core/messaging/composers/MessageBuilder/classes/MessageBuilder.md)

#### Inherited from

[`FrontendEventAction`](../../../FrontendEventAction/classes/FrontendEventAction.md).[`messageBuilder`](../../../FrontendEventAction/classes/FrontendEventAction.md#messagebuilder)

***

### state

#### Get Signature

> **get** **state**(): [`ActionState`](../../../../../../../common/web/ui/actions/ActionBase/enumerations/ActionState.md)

Defined in: [src/common/web/ui/actions/ActionBase.ts:143](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L143)

The current state of the action.

##### Returns

[`ActionState`](../../../../../../../common/web/ui/actions/ActionBase/enumerations/ActionState.md)

#### Inherited from

[`FrontendEventAction`](../../../FrontendEventAction/classes/FrontendEventAction.md).[`state`](../../../FrontendEventAction/classes/FrontendEventAction.md#state)

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

[`FrontendEventAction`](../../../FrontendEventAction/classes/FrontendEventAction.md).[`addDefaultNotifiers`](../../../FrontendEventAction/classes/FrontendEventAction.md#adddefaultnotifiers)

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

[`FrontendEventAction`](../../../FrontendEventAction/classes/FrontendEventAction.md).[`addNotifier`](../../../FrontendEventAction/classes/FrontendEventAction.md#addnotifier)

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

[`FrontendEventAction`](../../../FrontendEventAction/classes/FrontendEventAction.md).[`completed`](../../../FrontendEventAction/classes/FrontendEventAction.md#completed)

***

### execute()

> **execute**(): `void`

Defined in: [src/common/web/ui/actions/Action.ts:44](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/Action.ts#L44)

Executes the action (i.e., the message will be emitted).

#### Returns

`void`

#### Inherited from

[`FrontendEventAction`](../../../FrontendEventAction/classes/FrontendEventAction.md).[`execute`](../../../FrontendEventAction/classes/FrontendEventAction.md#execute)

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

[`FrontendEventAction`](../../../FrontendEventAction/classes/FrontendEventAction.md).[`failed`](../../../FrontendEventAction/classes/FrontendEventAction.md#failed)

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

[`FrontendEventAction`](../../../FrontendEventAction/classes/FrontendEventAction.md).[`onStateChanged`](../../../FrontendEventAction/classes/FrontendEventAction.md#onstatechanged)

***

### postExecution()

> `protected` **postExecution**(): `void`

Defined in: [src/common/web/ui/actions/EventAction.ts:10](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/EventAction.ts#L10)

#### Returns

`void`

#### Inherited from

[`FrontendEventAction`](../../../FrontendEventAction/classes/FrontendEventAction.md).[`postExecution`](../../../FrontendEventAction/classes/FrontendEventAction.md#postexecution)

***

### preExecution()

> `protected` **preExecution**(): `void`

Defined in: [src/common/web/ui/actions/ActionBase.ts:136](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/ui/actions/ActionBase.ts#L136)

#### Returns

`void`

#### Inherited from

[`FrontendEventAction`](../../../FrontendEventAction/classes/FrontendEventAction.md).[`preExecution`](../../../FrontendEventAction/classes/FrontendEventAction.md#preexecution)

***

### prepare()

> **prepare**(`projectID`): [`EventComposer`](../../../../../../../common/web/core/messaging/composers/EventComposer/classes/EventComposer.md)\<[`ProjectTouchEvent`](../../../../../../../common/web/api/project/ProjectEvents/classes/ProjectTouchEvent.md)\>

Defined in: [src/frontend/src/ui/actions/project/TouchProjectAction.ts:11](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/ui/actions/project/TouchProjectAction.ts#L11)

Prepares this action.

#### Parameters

##### projectID

`number`

#### Returns

[`EventComposer`](../../../../../../../common/web/core/messaging/composers/EventComposer/classes/EventComposer.md)\<[`ProjectTouchEvent`](../../../../../../../common/web/api/project/ProjectEvents/classes/ProjectTouchEvent.md)\>

- A message composer that can be further modified.

#### Overrides

[`FrontendEventAction`](../../../FrontendEventAction/classes/FrontendEventAction.md).[`prepare`](../../../FrontendEventAction/classes/FrontendEventAction.md#prepare)

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

[`FrontendEventAction`](../../../FrontendEventAction/classes/FrontendEventAction.md).[`prepareNotifiers`](../../../FrontendEventAction/classes/FrontendEventAction.md#preparenotifiers)

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

[`FrontendEventAction`](../../../FrontendEventAction/classes/FrontendEventAction.md).[`setState`](../../../FrontendEventAction/classes/FrontendEventAction.md#setstate)

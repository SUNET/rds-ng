# Class: FrontendServiceContext

Defined in: [src/frontend/src/services/FrontendServiceContext.ts:15](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/services/FrontendServiceContext.ts#L15)

Service context for the frontend.

Note that the store type isn't explicitely defined due to Pinia's excessive type definitions.

## Extends

- [`ServiceContext`](../../../../../common/web/services/ServiceContext/classes/ServiceContext.md)

## Constructors

### Constructor

> **new FrontendServiceContext**(`msgMeta`, `msgOrigin`, `msgBuilder`, `logger`, `config`): `FrontendServiceContext`

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:38](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L38)

#### Parameters

##### msgMeta

[`MessageMetaInformation`](../../../../../common/web/core/messaging/meta/MessageMetaInformation/classes/MessageMetaInformation.md)

The meta information of the message.

##### msgOrigin

[`UnitID`](../../../../../common/web/utils/UnitID/classes/UnitID.md)

The origin of the message.

##### msgBuilder

[`MessageBuilder`](../../../../../common/web/core/messaging/composers/MessageBuilder/classes/MessageBuilder.md)

A ``MessageBuilder`` to be assigned to this context.

##### logger

[`LoggerProxy`](../../../../../common/web/core/logging/LoggerProxy/classes/LoggerProxy.md)

A logger that is configured to automatically print the trace belonging to the message that caused the handler to be executed.

##### config

[`Configuration`](../../../../../common/web/utils/config/Configuration/classes/Configuration.md)

The global component configuration.

#### Returns

`FrontendServiceContext`

#### Inherited from

[`ServiceContext`](../../../../../common/web/services/ServiceContext/classes/ServiceContext.md).[`constructor`](../../../../../common/web/services/ServiceContext/classes/ServiceContext.md#constructor)

## Properties

### \_config

> `protected` `readonly` **\_config**: [`Configuration`](../../../../../common/web/utils/config/Configuration/classes/Configuration.md)

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:27](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L27)

#### Inherited from

[`ServiceContext`](../../../../../common/web/services/ServiceContext/classes/ServiceContext.md).[`_config`](../../../../../common/web/services/ServiceContext/classes/ServiceContext.md#_config)

***

### \_logger

> `protected` `readonly` **\_logger**: [`LoggerProxy`](../../../../../common/web/core/logging/LoggerProxy/classes/LoggerProxy.md)

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:26](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L26)

#### Inherited from

[`ServiceContext`](../../../../../common/web/services/ServiceContext/classes/ServiceContext.md).[`_logger`](../../../../../common/web/services/ServiceContext/classes/ServiceContext.md#_logger)

***

### \_msgBuilder

> `protected` `readonly` **\_msgBuilder**: [`MessageBuilder`](../../../../../common/web/core/messaging/composers/MessageBuilder/classes/MessageBuilder.md)

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:24](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L24)

#### Inherited from

[`ServiceContext`](../../../../../common/web/services/ServiceContext/classes/ServiceContext.md).[`_msgBuilder`](../../../../../common/web/services/ServiceContext/classes/ServiceContext.md#_msgbuilder)

***

### \_msgMeta

> `protected` `readonly` **\_msgMeta**: [`MessageMetaInformation`](../../../../../common/web/core/messaging/meta/MessageMetaInformation/classes/MessageMetaInformation.md)

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:22](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L22)

#### Inherited from

[`ServiceContext`](../../../../../common/web/services/ServiceContext/classes/ServiceContext.md).[`_msgMeta`](../../../../../common/web/services/ServiceContext/classes/ServiceContext.md#_msgmeta)

***

### \_msgOrigin

> `protected` `readonly` **\_msgOrigin**: [`UnitID`](../../../../../common/web/utils/UnitID/classes/UnitID.md)

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:23](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L23)

#### Inherited from

[`ServiceContext`](../../../../../common/web/services/ServiceContext/classes/ServiceContext.md).[`_msgOrigin`](../../../../../common/web/services/ServiceContext/classes/ServiceContext.md#_msgorigin)

***

### \_requiresReply

> `protected` **\_requiresReply**: `boolean` = `false`

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:29](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L29)

#### Inherited from

[`ServiceContext`](../../../../../common/web/services/ServiceContext/classes/ServiceContext.md).[`_requiresReply`](../../../../../common/web/services/ServiceContext/classes/ServiceContext.md#_requiresreply)

## Accessors

### config

#### Get Signature

> **get** **config**(): [`Configuration`](../../../../../common/web/utils/config/Configuration/classes/Configuration.md)

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:123](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L123)

The global component configuration.

##### Returns

[`Configuration`](../../../../../common/web/utils/config/Configuration/classes/Configuration.md)

#### Inherited from

[`ServiceContext`](../../../../../common/web/services/ServiceContext/classes/ServiceContext.md).[`config`](../../../../../common/web/services/ServiceContext/classes/ServiceContext.md#config)

***

### connectorsStore

#### Get Signature

> **get** **connectorsStore**(): `Store`\<`"connectorsStore"`, `Pick`\<\{ `connectors`: `Ref`\<`object`[], [`Connector`](../../../../../common/web/data/entities/connector/Connector/classes/Connector.md)[] \| `object`[]\>; `reset`: () => `void`; \}, `"connectors"`\>, `Pick`\<\{ `connectors`: `Ref`\<`object`[], [`Connector`](../../../../../common/web/data/entities/connector/Connector/classes/Connector.md)[] \| `object`[]\>; `reset`: () => `void`; \}, `never`\>, `Pick`\<\{ `connectors`: `Ref`\<`object`[], [`Connector`](../../../../../common/web/data/entities/connector/Connector/classes/Connector.md)[] \| `object`[]\>; `reset`: () => `void`; \}, `"reset"`\>\>

Defined in: [src/frontend/src/services/FrontendServiceContext.ts:26](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/services/FrontendServiceContext.ts#L26)

The connectors store.

##### Returns

`Store`\<`"connectorsStore"`, `Pick`\<\{ `connectors`: `Ref`\<`object`[], [`Connector`](../../../../../common/web/data/entities/connector/Connector/classes/Connector.md)[] \| `object`[]\>; `reset`: () => `void`; \}, `"connectors"`\>, `Pick`\<\{ `connectors`: `Ref`\<`object`[], [`Connector`](../../../../../common/web/data/entities/connector/Connector/classes/Connector.md)[] \| `object`[]\>; `reset`: () => `void`; \}, `never`\>, `Pick`\<\{ `connectors`: `Ref`\<`object`[], [`Connector`](../../../../../common/web/data/entities/connector/Connector/classes/Connector.md)[] \| `object`[]\>; `reset`: () => `void`; \}, `"reset"`\>\>

***

### isEntrypointClient

#### Get Signature

> **get** **isEntrypointClient**(): `boolean`

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:95](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L95)

Whether the message entered through the client.

##### Returns

`boolean`

#### Inherited from

[`ServiceContext`](../../../../../common/web/services/ServiceContext/classes/ServiceContext.md).[`isEntrypointClient`](../../../../../common/web/services/ServiceContext/classes/ServiceContext.md#isentrypointclient)

***

### isEntrypointLocal

#### Get Signature

> **get** **isEntrypointLocal**(): `boolean`

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:81](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L81)

Whether the message entered locally.

##### Returns

`boolean`

#### Inherited from

[`ServiceContext`](../../../../../common/web/services/ServiceContext/classes/ServiceContext.md).[`isEntrypointLocal`](../../../../../common/web/services/ServiceContext/classes/ServiceContext.md#isentrypointlocal)

***

### isEntrypointServer

#### Get Signature

> **get** **isEntrypointServer**(): `boolean`

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:88](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L88)

Whether the message entered through the server.

##### Returns

`boolean`

#### Inherited from

[`ServiceContext`](../../../../../common/web/services/ServiceContext/classes/ServiceContext.md).[`isEntrypointServer`](../../../../../common/web/services/ServiceContext/classes/ServiceContext.md#isentrypointserver)

***

### logger

#### Get Signature

> **get** **logger**(): [`LoggerProxy`](../../../../../common/web/core/logging/LoggerProxy/classes/LoggerProxy.md)

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:116](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L116)

The logger to be used within this context.

##### Returns

[`LoggerProxy`](../../../../../common/web/core/logging/LoggerProxy/classes/LoggerProxy.md)

#### Inherited from

[`ServiceContext`](../../../../../common/web/services/ServiceContext/classes/ServiceContext.md).[`logger`](../../../../../common/web/services/ServiceContext/classes/ServiceContext.md#logger)

***

### messageBuilder

#### Get Signature

> **get** **messageBuilder**(): [`MessageBuilder`](../../../../../common/web/core/messaging/composers/MessageBuilder/classes/MessageBuilder.md)

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:109](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L109)

The message builder to be used within this context.

##### Returns

[`MessageBuilder`](../../../../../common/web/core/messaging/composers/MessageBuilder/classes/MessageBuilder.md)

#### Inherited from

[`ServiceContext`](../../../../../common/web/services/ServiceContext/classes/ServiceContext.md).[`messageBuilder`](../../../../../common/web/services/ServiceContext/classes/ServiceContext.md#messagebuilder)

***

### metadataStore

#### Get Signature

> **get** **metadataStore**(): `Store`\<`"metadataStore"`, `Pick`\<\{ `profiles`: `Ref`\<`object`[], [`MetadataProfileContainerList`](../../../../../common/web/data/entities/metadata/MetadataProfileContainer/type-aliases/MetadataProfileContainerList.md) \| `object`[]\>; `reset`: () => `void`; \}, `"profiles"`\>, `Pick`\<\{ `profiles`: `Ref`\<`object`[], [`MetadataProfileContainerList`](../../../../../common/web/data/entities/metadata/MetadataProfileContainer/type-aliases/MetadataProfileContainerList.md) \| `object`[]\>; `reset`: () => `void`; \}, `never`\>, `Pick`\<\{ `profiles`: `Ref`\<`object`[], [`MetadataProfileContainerList`](../../../../../common/web/data/entities/metadata/MetadataProfileContainer/type-aliases/MetadataProfileContainerList.md) \| `object`[]\>; `reset`: () => `void`; \}, `"reset"`\>\>

Defined in: [src/frontend/src/services/FrontendServiceContext.ts:33](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/services/FrontendServiceContext.ts#L33)

The metadata store.

##### Returns

`Store`\<`"metadataStore"`, `Pick`\<\{ `profiles`: `Ref`\<`object`[], [`MetadataProfileContainerList`](../../../../../common/web/data/entities/metadata/MetadataProfileContainer/type-aliases/MetadataProfileContainerList.md) \| `object`[]\>; `reset`: () => `void`; \}, `"profiles"`\>, `Pick`\<\{ `profiles`: `Ref`\<`object`[], [`MetadataProfileContainerList`](../../../../../common/web/data/entities/metadata/MetadataProfileContainer/type-aliases/MetadataProfileContainerList.md) \| `object`[]\>; `reset`: () => `void`; \}, `never`\>, `Pick`\<\{ `profiles`: `Ref`\<`object`[], [`MetadataProfileContainerList`](../../../../../common/web/data/entities/metadata/MetadataProfileContainer/type-aliases/MetadataProfileContainerList.md) \| `object`[]\>; `reset`: () => `void`; \}, `"reset"`\>\>

***

### origin

#### Get Signature

> **get** **origin**(): [`UnitID`](../../../../../common/web/utils/UnitID/classes/UnitID.md)

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:102](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L102)

The origin of the message.

##### Returns

[`UnitID`](../../../../../common/web/utils/UnitID/classes/UnitID.md)

#### Inherited from

[`ServiceContext`](../../../../../common/web/services/ServiceContext/classes/ServiceContext.md).[`origin`](../../../../../common/web/services/ServiceContext/classes/ServiceContext.md#origin)

***

### projectExportersStore

#### Get Signature

> **get** **projectExportersStore**(): `Store`\<`"projectExportersStore"`, `Pick`\<\{ `exporters`: `Ref`\<`object`[], [`ProjectExporterDescriptor`](../../../../../common/web/data/exporters/ProjectExporterDescriptor/classes/ProjectExporterDescriptor.md)[] \| `object`[]\>; `reset`: () => `void`; \}, `"exporters"`\>, `Pick`\<\{ `exporters`: `Ref`\<`object`[], [`ProjectExporterDescriptor`](../../../../../common/web/data/exporters/ProjectExporterDescriptor/classes/ProjectExporterDescriptor.md)[] \| `object`[]\>; `reset`: () => `void`; \}, `never`\>, `Pick`\<\{ `exporters`: `Ref`\<`object`[], [`ProjectExporterDescriptor`](../../../../../common/web/data/exporters/ProjectExporterDescriptor/classes/ProjectExporterDescriptor.md)[] \| `object`[]\>; `reset`: () => `void`; \}, `"reset"`\>\>

Defined in: [src/frontend/src/services/FrontendServiceContext.ts:61](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/services/FrontendServiceContext.ts#L61)

The project exporters store.

##### Returns

`Store`\<`"projectExportersStore"`, `Pick`\<\{ `exporters`: `Ref`\<`object`[], [`ProjectExporterDescriptor`](../../../../../common/web/data/exporters/ProjectExporterDescriptor/classes/ProjectExporterDescriptor.md)[] \| `object`[]\>; `reset`: () => `void`; \}, `"exporters"`\>, `Pick`\<\{ `exporters`: `Ref`\<`object`[], [`ProjectExporterDescriptor`](../../../../../common/web/data/exporters/ProjectExporterDescriptor/classes/ProjectExporterDescriptor.md)[] \| `object`[]\>; `reset`: () => `void`; \}, `never`\>, `Pick`\<\{ `exporters`: `Ref`\<`object`[], [`ProjectExporterDescriptor`](../../../../../common/web/data/exporters/ProjectExporterDescriptor/classes/ProjectExporterDescriptor.md)[] \| `object`[]\>; `reset`: () => `void`; \}, `"reset"`\>\>

***

### projectJobsStore

#### Get Signature

> **get** **projectJobsStore**(): `Store`\<`"projectJobsStore"`, `Pick`\<\{ `jobs`: `Ref`\<`object`[], [`ProjectJob`](../../../../../common/web/data/entities/project/ProjectJob/classes/ProjectJob.md)[] \| `object`[]\>; `reset`: () => `void`; \}, `"jobs"`\>, `Pick`\<\{ `jobs`: `Ref`\<`object`[], [`ProjectJob`](../../../../../common/web/data/entities/project/ProjectJob/classes/ProjectJob.md)[] \| `object`[]\>; `reset`: () => `void`; \}, `never`\>, `Pick`\<\{ `jobs`: `Ref`\<`object`[], [`ProjectJob`](../../../../../common/web/data/entities/project/ProjectJob/classes/ProjectJob.md)[] \| `object`[]\>; `reset`: () => `void`; \}, `"reset"`\>\>

Defined in: [src/frontend/src/services/FrontendServiceContext.ts:54](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/services/FrontendServiceContext.ts#L54)

The project jobs store.

##### Returns

`Store`\<`"projectJobsStore"`, `Pick`\<\{ `jobs`: `Ref`\<`object`[], [`ProjectJob`](../../../../../common/web/data/entities/project/ProjectJob/classes/ProjectJob.md)[] \| `object`[]\>; `reset`: () => `void`; \}, `"jobs"`\>, `Pick`\<\{ `jobs`: `Ref`\<`object`[], [`ProjectJob`](../../../../../common/web/data/entities/project/ProjectJob/classes/ProjectJob.md)[] \| `object`[]\>; `reset`: () => `void`; \}, `never`\>, `Pick`\<\{ `jobs`: `Ref`\<`object`[], [`ProjectJob`](../../../../../common/web/data/entities/project/ProjectJob/classes/ProjectJob.md)[] \| `object`[]\>; `reset`: () => `void`; \}, `"reset"`\>\>

***

### projectsStore

#### Get Signature

> **get** **projectsStore**(): `Store`\<`"projectsStore"`, `Pick`\<\{ `activeProject`: `Ref`\<`undefined` \| `null` \| `number`, `undefined` \| `null` \| `number`\>; `markForDeletion`: (`projectID`) => `void`; `pendingDeletions`: `Ref`\<`number`[], `number`[]\>; `projects`: `Ref`\<`object`[], [`Project`](../../../../../common/web/data/entities/project/Project/classes/Project.md)[] \| `object`[]\>; `reset`: () => `void`; `resetPendingDeletions`: () => `void`; `resolveActiveProject`: () => `undefined` \| [`Project`](../../../../../common/web/data/entities/project/Project/classes/Project.md); `unmarkForDeletion`: (`projectID`) => `void`; `volatileStates`: `Ref`\<\{ `addState`: `void`; `findState`: `undefined` \| [`ProjectVolatileState`](../../../data/entities/project/ProjectVolatileState/classes/ProjectVolatileState.md); \}, [`ProjectVolatileStates`](../../../data/entities/project/ProjectVolatileStates/classes/ProjectVolatileStates.md) \| \{ `addState`: `void`; `findState`: `undefined` \| [`ProjectVolatileState`](../../../data/entities/project/ProjectVolatileState/classes/ProjectVolatileState.md); \}\>; \}, `"projects"` \| `"activeProject"` \| `"pendingDeletions"` \| `"volatileStates"`\>, `Pick`\<\{ `activeProject`: `Ref`\<`undefined` \| `null` \| `number`, `undefined` \| `null` \| `number`\>; `markForDeletion`: (`projectID`) => `void`; `pendingDeletions`: `Ref`\<`number`[], `number`[]\>; `projects`: `Ref`\<`object`[], [`Project`](../../../../../common/web/data/entities/project/Project/classes/Project.md)[] \| `object`[]\>; `reset`: () => `void`; `resetPendingDeletions`: () => `void`; `resolveActiveProject`: () => `undefined` \| [`Project`](../../../../../common/web/data/entities/project/Project/classes/Project.md); `unmarkForDeletion`: (`projectID`) => `void`; `volatileStates`: `Ref`\<\{ `addState`: `void`; `findState`: `undefined` \| [`ProjectVolatileState`](../../../data/entities/project/ProjectVolatileState/classes/ProjectVolatileState.md); \}, [`ProjectVolatileStates`](../../../data/entities/project/ProjectVolatileStates/classes/ProjectVolatileStates.md) \| \{ `addState`: `void`; `findState`: `undefined` \| [`ProjectVolatileState`](../../../data/entities/project/ProjectVolatileState/classes/ProjectVolatileState.md); \}\>; \}, `never`\>, `Pick`\<\{ `activeProject`: `Ref`\<`undefined` \| `null` \| `number`, `undefined` \| `null` \| `number`\>; `markForDeletion`: (`projectID`) => `void`; `pendingDeletions`: `Ref`\<`number`[], `number`[]\>; `projects`: `Ref`\<`object`[], [`Project`](../../../../../common/web/data/entities/project/Project/classes/Project.md)[] \| `object`[]\>; `reset`: () => `void`; `resetPendingDeletions`: () => `void`; `resolveActiveProject`: () => `undefined` \| [`Project`](../../../../../common/web/data/entities/project/Project/classes/Project.md); `unmarkForDeletion`: (`projectID`) => `void`; `volatileStates`: `Ref`\<\{ `addState`: `void`; `findState`: `undefined` \| [`ProjectVolatileState`](../../../data/entities/project/ProjectVolatileState/classes/ProjectVolatileState.md); \}, [`ProjectVolatileStates`](../../../data/entities/project/ProjectVolatileStates/classes/ProjectVolatileStates.md) \| \{ `addState`: `void`; `findState`: `undefined` \| [`ProjectVolatileState`](../../../data/entities/project/ProjectVolatileState/classes/ProjectVolatileState.md); \}\>; \}, `"reset"` \| `"resolveActiveProject"` \| `"markForDeletion"` \| `"unmarkForDeletion"` \| `"resetPendingDeletions"`\>\>

Defined in: [src/frontend/src/services/FrontendServiceContext.ts:47](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/services/FrontendServiceContext.ts#L47)

The projects store.

##### Returns

`Store`\<`"projectsStore"`, `Pick`\<\{ `activeProject`: `Ref`\<`undefined` \| `null` \| `number`, `undefined` \| `null` \| `number`\>; `markForDeletion`: (`projectID`) => `void`; `pendingDeletions`: `Ref`\<`number`[], `number`[]\>; `projects`: `Ref`\<`object`[], [`Project`](../../../../../common/web/data/entities/project/Project/classes/Project.md)[] \| `object`[]\>; `reset`: () => `void`; `resetPendingDeletions`: () => `void`; `resolveActiveProject`: () => `undefined` \| [`Project`](../../../../../common/web/data/entities/project/Project/classes/Project.md); `unmarkForDeletion`: (`projectID`) => `void`; `volatileStates`: `Ref`\<\{ `addState`: `void`; `findState`: `undefined` \| [`ProjectVolatileState`](../../../data/entities/project/ProjectVolatileState/classes/ProjectVolatileState.md); \}, [`ProjectVolatileStates`](../../../data/entities/project/ProjectVolatileStates/classes/ProjectVolatileStates.md) \| \{ `addState`: `void`; `findState`: `undefined` \| [`ProjectVolatileState`](../../../data/entities/project/ProjectVolatileState/classes/ProjectVolatileState.md); \}\>; \}, `"projects"` \| `"activeProject"` \| `"pendingDeletions"` \| `"volatileStates"`\>, `Pick`\<\{ `activeProject`: `Ref`\<`undefined` \| `null` \| `number`, `undefined` \| `null` \| `number`\>; `markForDeletion`: (`projectID`) => `void`; `pendingDeletions`: `Ref`\<`number`[], `number`[]\>; `projects`: `Ref`\<`object`[], [`Project`](../../../../../common/web/data/entities/project/Project/classes/Project.md)[] \| `object`[]\>; `reset`: () => `void`; `resetPendingDeletions`: () => `void`; `resolveActiveProject`: () => `undefined` \| [`Project`](../../../../../common/web/data/entities/project/Project/classes/Project.md); `unmarkForDeletion`: (`projectID`) => `void`; `volatileStates`: `Ref`\<\{ `addState`: `void`; `findState`: `undefined` \| [`ProjectVolatileState`](../../../data/entities/project/ProjectVolatileState/classes/ProjectVolatileState.md); \}, [`ProjectVolatileStates`](../../../data/entities/project/ProjectVolatileStates/classes/ProjectVolatileStates.md) \| \{ `addState`: `void`; `findState`: `undefined` \| [`ProjectVolatileState`](../../../data/entities/project/ProjectVolatileState/classes/ProjectVolatileState.md); \}\>; \}, `never`\>, `Pick`\<\{ `activeProject`: `Ref`\<`undefined` \| `null` \| `number`, `undefined` \| `null` \| `number`\>; `markForDeletion`: (`projectID`) => `void`; `pendingDeletions`: `Ref`\<`number`[], `number`[]\>; `projects`: `Ref`\<`object`[], [`Project`](../../../../../common/web/data/entities/project/Project/classes/Project.md)[] \| `object`[]\>; `reset`: () => `void`; `resetPendingDeletions`: () => `void`; `resolveActiveProject`: () => `undefined` \| [`Project`](../../../../../common/web/data/entities/project/Project/classes/Project.md); `unmarkForDeletion`: (`projectID`) => `void`; `volatileStates`: `Ref`\<\{ `addState`: `void`; `findState`: `undefined` \| [`ProjectVolatileState`](../../../data/entities/project/ProjectVolatileState/classes/ProjectVolatileState.md); \}, [`ProjectVolatileStates`](../../../data/entities/project/ProjectVolatileStates/classes/ProjectVolatileStates.md) \| \{ `addState`: `void`; `findState`: `undefined` \| [`ProjectVolatileState`](../../../data/entities/project/ProjectVolatileState/classes/ProjectVolatileState.md); \}\>; \}, `"reset"` \| `"resolveActiveProject"` \| `"markForDeletion"` \| `"unmarkForDeletion"` \| `"resetPendingDeletions"`\>\>

***

### userStore

#### Get Signature

> **get** **userStore**(): `Store`\<`"userStore"`, `Pick`\<\{ `authorizationState`: `Ref`\<[`AuthorizationState`](../../../../../common/web/data/entities/authorization/AuthorizationState/enumerations/AuthorizationState.md), [`AuthorizationState`](../../../../../common/web/data/entities/authorization/AuthorizationState/enumerations/AuthorizationState.md)\>; `brokerAssigned`: `Ref`\<`boolean`, `boolean`\>; `reset`: () => `void`; `resetLogin`: () => `void`; `userAuthorizations`: `Ref`\<`string`[], `string`[]\>; `userFingerprint`: `Ref`\<`string`, `string`\>; `userSettings`: `Ref`\<\{ `connector_instances`: `object`[]; \}, [`UserSettings`](../../../../../common/web/data/entities/user/UserSettings/classes/UserSettings.md) \| \{ `connector_instances`: `object`[]; \}\>; `userToken`: `RemovableRef`\<[`UserToken`](../../../../../common/web/data/entities/user/UserToken/interfaces/UserToken.md)\>; \}, `"userToken"` \| `"userFingerprint"` \| `"userSettings"` \| `"userAuthorizations"` \| `"authorizationState"` \| `"brokerAssigned"`\>, `Pick`\<\{ `authorizationState`: `Ref`\<[`AuthorizationState`](../../../../../common/web/data/entities/authorization/AuthorizationState/enumerations/AuthorizationState.md), [`AuthorizationState`](../../../../../common/web/data/entities/authorization/AuthorizationState/enumerations/AuthorizationState.md)\>; `brokerAssigned`: `Ref`\<`boolean`, `boolean`\>; `reset`: () => `void`; `resetLogin`: () => `void`; `userAuthorizations`: `Ref`\<`string`[], `string`[]\>; `userFingerprint`: `Ref`\<`string`, `string`\>; `userSettings`: `Ref`\<\{ `connector_instances`: `object`[]; \}, [`UserSettings`](../../../../../common/web/data/entities/user/UserSettings/classes/UserSettings.md) \| \{ `connector_instances`: `object`[]; \}\>; `userToken`: `RemovableRef`\<[`UserToken`](../../../../../common/web/data/entities/user/UserToken/interfaces/UserToken.md)\>; \}, `never`\>, `Pick`\<\{ `authorizationState`: `Ref`\<[`AuthorizationState`](../../../../../common/web/data/entities/authorization/AuthorizationState/enumerations/AuthorizationState.md), [`AuthorizationState`](../../../../../common/web/data/entities/authorization/AuthorizationState/enumerations/AuthorizationState.md)\>; `brokerAssigned`: `Ref`\<`boolean`, `boolean`\>; `reset`: () => `void`; `resetLogin`: () => `void`; `userAuthorizations`: `Ref`\<`string`[], `string`[]\>; `userFingerprint`: `Ref`\<`string`, `string`\>; `userSettings`: `Ref`\<\{ `connector_instances`: `object`[]; \}, [`UserSettings`](../../../../../common/web/data/entities/user/UserSettings/classes/UserSettings.md) \| \{ `connector_instances`: `object`[]; \}\>; `userToken`: `RemovableRef`\<[`UserToken`](../../../../../common/web/data/entities/user/UserToken/interfaces/UserToken.md)\>; \}, `"reset"` \| `"resetLogin"`\>\>

Defined in: [src/frontend/src/services/FrontendServiceContext.ts:40](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/frontend/src/services/FrontendServiceContext.ts#L40)

The user store.

##### Returns

`Store`\<`"userStore"`, `Pick`\<\{ `authorizationState`: `Ref`\<[`AuthorizationState`](../../../../../common/web/data/entities/authorization/AuthorizationState/enumerations/AuthorizationState.md), [`AuthorizationState`](../../../../../common/web/data/entities/authorization/AuthorizationState/enumerations/AuthorizationState.md)\>; `brokerAssigned`: `Ref`\<`boolean`, `boolean`\>; `reset`: () => `void`; `resetLogin`: () => `void`; `userAuthorizations`: `Ref`\<`string`[], `string`[]\>; `userFingerprint`: `Ref`\<`string`, `string`\>; `userSettings`: `Ref`\<\{ `connector_instances`: `object`[]; \}, [`UserSettings`](../../../../../common/web/data/entities/user/UserSettings/classes/UserSettings.md) \| \{ `connector_instances`: `object`[]; \}\>; `userToken`: `RemovableRef`\<[`UserToken`](../../../../../common/web/data/entities/user/UserToken/interfaces/UserToken.md)\>; \}, `"userToken"` \| `"userFingerprint"` \| `"userSettings"` \| `"userAuthorizations"` \| `"authorizationState"` \| `"brokerAssigned"`\>, `Pick`\<\{ `authorizationState`: `Ref`\<[`AuthorizationState`](../../../../../common/web/data/entities/authorization/AuthorizationState/enumerations/AuthorizationState.md), [`AuthorizationState`](../../../../../common/web/data/entities/authorization/AuthorizationState/enumerations/AuthorizationState.md)\>; `brokerAssigned`: `Ref`\<`boolean`, `boolean`\>; `reset`: () => `void`; `resetLogin`: () => `void`; `userAuthorizations`: `Ref`\<`string`[], `string`[]\>; `userFingerprint`: `Ref`\<`string`, `string`\>; `userSettings`: `Ref`\<\{ `connector_instances`: `object`[]; \}, [`UserSettings`](../../../../../common/web/data/entities/user/UserSettings/classes/UserSettings.md) \| \{ `connector_instances`: `object`[]; \}\>; `userToken`: `RemovableRef`\<[`UserToken`](../../../../../common/web/data/entities/user/UserToken/interfaces/UserToken.md)\>; \}, `never`\>, `Pick`\<\{ `authorizationState`: `Ref`\<[`AuthorizationState`](../../../../../common/web/data/entities/authorization/AuthorizationState/enumerations/AuthorizationState.md), [`AuthorizationState`](../../../../../common/web/data/entities/authorization/AuthorizationState/enumerations/AuthorizationState.md)\>; `brokerAssigned`: `Ref`\<`boolean`, `boolean`\>; `reset`: () => `void`; `resetLogin`: () => `void`; `userAuthorizations`: `Ref`\<`string`[], `string`[]\>; `userFingerprint`: `Ref`\<`string`, `string`\>; `userSettings`: `Ref`\<\{ `connector_instances`: `object`[]; \}, [`UserSettings`](../../../../../common/web/data/entities/user/UserSettings/classes/UserSettings.md) \| \{ `connector_instances`: `object`[]; \}\>; `userToken`: `RemovableRef`\<[`UserToken`](../../../../../common/web/data/entities/user/UserToken/interfaces/UserToken.md)\>; \}, `"reset"` \| `"resetLogin"`\>\>

## Methods

### begin()

> **begin**(`requiresReply`): `void`

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:52](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L52)

Initiates execution within this context.

#### Parameters

##### requiresReply

`boolean`

Whether a reply is required.

#### Returns

`void`

#### Inherited from

[`ServiceContext`](../../../../../common/web/services/ServiceContext/classes/ServiceContext.md).[`begin`](../../../../../common/web/services/ServiceContext/classes/ServiceContext.md#begin)

***

### end()

> **end**(): `void`

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:59](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L59)

Finishes execution within this context.

#### Returns

`void`

#### Inherited from

[`ServiceContext`](../../../../../common/web/services/ServiceContext/classes/ServiceContext.md).[`end`](../../../../../common/web/services/ServiceContext/classes/ServiceContext.md#end)

***

### reportError()

> **reportError**(`err`): `void`

Defined in: [src/common/web/core/messaging/handlers/MessageContext.ts:68](https://github.com/Sciebo-RDS/rds-ng/blob/9b7c190cc4aaf42711ecc0fce854b1587c853586/src/common/web/core/messaging/handlers/MessageContext.ts#L68)

Reports an error occurred during context execution.

#### Parameters

##### err

`any`

The error to report.

#### Returns

`void`

#### Inherited from

[`ServiceContext`](../../../../../common/web/services/ServiceContext/classes/ServiceContext.md).[`reportError`](../../../../../common/web/services/ServiceContext/classes/ServiceContext.md#reporterror)

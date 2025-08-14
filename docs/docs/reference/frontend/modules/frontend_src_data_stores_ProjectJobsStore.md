---
id: "frontend_src_data_stores_ProjectJobsStore"
title: "Module: frontend/src/data/stores/ProjectJobsStore"
sidebar_label: "frontend/src/data/stores/ProjectJobsStore"
sidebar_position: 0
custom_edit_url: null
---

## Namespaces

- [useProjectJobsStore](../namespaces/frontend_src_data_stores_ProjectJobsStore.useProjectJobsStore.md)

## Functions

### useProjectJobsStore

▸ **useProjectJobsStore**(`pinia?`, `hot?`): `Store`<``"projectJobsStore"``, `Pick`<\{ `jobs`: `Ref`<\{ `connector_instance`: `string` ; `message`: `string` ; `progress`: `number` ; `project_id`: `number` ; `timestamp`: `number` ; `user_id`: `string`  }[], [`ProjectJob`](../classes/common_web_data_entities_project_ProjectJob.ProjectJob.md)[] \| \{ `connector_instance`: `string` ; `message`: `string` ; `progress`: `number` ; `project_id`: `number` ; `timestamp`: `number` ; `user_id`: `string`  }[]\> ; `reset`: () => `void`  }, ``"jobs"``\>, `Pick`<\{ `jobs`: `Ref`<\{ `connector_instance`: `string` ; `message`: `string` ; `progress`: `number` ; `project_id`: `number` ; `timestamp`: `number` ; `user_id`: `string`  }[], [`ProjectJob`](../classes/common_web_data_entities_project_ProjectJob.ProjectJob.md)[] \| \{ `connector_instance`: `string` ; `message`: `string` ; `progress`: `number` ; `project_id`: `number` ; `timestamp`: `number` ; `user_id`: `string`  }[]\> ; `reset`: () => `void`  }, `never`\>, `Pick`<\{ `jobs`: `Ref`<\{ `connector_instance`: `string` ; `message`: `string` ; `progress`: `number` ; `project_id`: `number` ; `timestamp`: `number` ; `user_id`: `string`  }[], [`ProjectJob`](../classes/common_web_data_entities_project_ProjectJob.ProjectJob.md)[] \| \{ `connector_instance`: `string` ; `message`: `string` ; `progress`: `number` ; `project_id`: `number` ; `timestamp`: `number` ; `user_id`: `string`  }[]\> ; `reset`: () => `void`  }, ``"reset"``\>\>

The project jobs store for all project job-specific data.

#### Parameters

| Name | Type |
| :------ | :------ |
| `pinia?` | ``null`` \| `Pinia` |
| `hot?` | `StoreGeneric` |

#### Returns

`Store`<``"projectJobsStore"``, `Pick`<\{ `jobs`: `Ref`<\{ `connector_instance`: `string` ; `message`: `string` ; `progress`: `number` ; `project_id`: `number` ; `timestamp`: `number` ; `user_id`: `string`  }[], [`ProjectJob`](../classes/common_web_data_entities_project_ProjectJob.ProjectJob.md)[] \| \{ `connector_instance`: `string` ; `message`: `string` ; `progress`: `number` ; `project_id`: `number` ; `timestamp`: `number` ; `user_id`: `string`  }[]\> ; `reset`: () => `void`  }, ``"jobs"``\>, `Pick`<\{ `jobs`: `Ref`<\{ `connector_instance`: `string` ; `message`: `string` ; `progress`: `number` ; `project_id`: `number` ; `timestamp`: `number` ; `user_id`: `string`  }[], [`ProjectJob`](../classes/common_web_data_entities_project_ProjectJob.ProjectJob.md)[] \| \{ `connector_instance`: `string` ; `message`: `string` ; `progress`: `number` ; `project_id`: `number` ; `timestamp`: `number` ; `user_id`: `string`  }[]\> ; `reset`: () => `void`  }, `never`\>, `Pick`<\{ `jobs`: `Ref`<\{ `connector_instance`: `string` ; `message`: `string` ; `progress`: `number` ; `project_id`: `number` ; `timestamp`: `number` ; `user_id`: `string`  }[], [`ProjectJob`](../classes/common_web_data_entities_project_ProjectJob.ProjectJob.md)[] \| \{ `connector_instance`: `string` ; `message`: `string` ; `progress`: `number` ; `project_id`: `number` ; `timestamp`: `number` ; `user_id`: `string`  }[]\> ; `reset`: () => `void`  }, ``"reset"``\>\>

#### Defined in

src/node_modules/pinia/dist/pinia.d.ts:686

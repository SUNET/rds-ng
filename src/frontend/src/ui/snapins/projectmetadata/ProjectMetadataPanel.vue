<script setup lang="ts">
import { storeToRefs } from "pinia";
import Message from "primevue/message";
import { type PropType, reactive, ref, toRefs, unref, watch } from "vue";

import { findConnectorByInstanceID } from "@common/data/entities/connector/ConnectorInstanceUtils";
import { type MetadataProfileContainerList, MetadataProfileContainerRole } from "@common/data/entities/metadata/MetadataProfileContainer";
import { filterContainers, filterContainersByRoles, isContainerSelected } from "@common/data/entities/metadata/MetadataProfileContainerUtils";
import { ProjectMetadataFeature } from "@common/data/entities/project/features/ProjectMetadataFeature";
import { Project } from "@common/data/entities/project/Project";
import { type ProfileID } from "@common/ui/components/propertyeditor/PropertyProfile.ts";
import { PropertyProfileStore } from "@common/ui/components/propertyeditor/PropertyProfileStore";
import { makeDebounce } from "@common/ui/components/propertyeditor/utils/PropertyEditorUtils";

import PropertyEditor from "@common/ui/components/propertyeditor/PropertyEditor.vue";

import { FrontendComponent } from "@/component/FrontendComponent";
import { useConnectorsStore } from "@/data/stores/ConnectorsStore";
import { useMetadataStore } from "@/data/stores/MetadataStore";
import { useUserStore } from "@/data/stores/UserStore";
import { UpdateProjectFeaturesAction } from "@/ui/actions/project/UpdateProjectFeaturesAction";

import MetadataProfilesSelector from "@/ui/components/metadata/MetadataProfilesSelector.vue";
import ProjectExportersBar from "@/ui/components/project/ProjectExportersBar.vue";

const comp = FrontendComponent.inject();
const props = defineProps({
    project: {
        type: Object as PropType<Project>,
        required: true
    }
});
const { project } = toRefs(props);
const metadataStore = useMetadataStore();
const consStore = useConnectorsStore();
const userStore = useUserStore();
const { connectors } = storeToRefs(consStore);
const { userSettings } = storeToRefs(userStore);
const projectProfiles = reactive(new PropertyProfileStore());

const optionalProfiles = ref<MetadataProfileContainerList>([]);
const enabledProfiles = ref<ProfileID[]>(unref(project)!.features.project_metadata.enabled_metadata_profiles);

const debounce = makeDebounce();

for (const profile of filterContainers(metadataStore.profiles, ProjectMetadataFeature.FeatureID, [
    MetadataProfileContainerRole.Default,
    MetadataProfileContainerRole.Optional
])) {
    if (isContainerSelected(profile, unref(enabledProfiles))) {
        projectProfiles.mountProfile(profile.profile);
    }

    if (profile.role == MetadataProfileContainerRole.Optional) {
        optionalProfiles.value.push(profile);
    }
}

// TODO fix auto merging connector profiles
connectors.value.forEach((connector) => {
    if (
        !userSettings.value.connector_instances.find((instance) => {
            if (project!.value.options.use_all_connector_instances) {
                return instance.connector_id == connector.connector_id;
            } else {
                return !!project!.value.options.active_connector_instances.find((instanceID) => {
                    const resolvedConnector = findConnectorByInstanceID(connectors.value, userSettings.value.connector_instances, instanceID);
                    return resolvedConnector && resolvedConnector.connector_id == connector.connector_id;
                });
            }
        })
    ) {
        return;
    }

    try {
        for (const profile of filterContainersByRoles(connector.metadata_profiles, [
            MetadataProfileContainerRole.Default,
            MetadataProfileContainerRole.Optional
        ])) {
            if (isContainerSelected(profile, unref(enabledProfiles))) {
                projectProfiles.mountProfile(profile.profile);
            }

            if (profile.role == MetadataProfileContainerRole.Optional) {
                optionalProfiles.value.push(profile);
            }
        }
    } catch (e) {
        console.error(e);
    }
});

function saveProject(): void {
    debounce(() => {
        const action = new UpdateProjectFeaturesAction(comp);
        action.prepare(project!.value, [new ProjectMetadataFeature(unref(project)!.features.project_metadata.metadata, unref(enabledProfiles))]);
        action.execute();
    });
}

watch(() => project!.value.features.project_metadata.metadata, saveProject, { deep: true });
watch(enabledProfiles, saveProject);
</script>

<template>
    <div v-if="userSettings.connector_instances.length == 0" class="p-2 px-6">
        <Message severity="warn" :closable="false" class="pb-1">
            <div>
                You haven't configured any connections to external services yet. In order to add metadata to your project, open your settings
                <span class="material-icons-outlined mi-settings relative top-1.5" />
                and add at least one connection.
            </div>
        </Message>
    </div>
    <div v-else>
        <div class="grid grid-cols-[1fr_max-content] gap-10 px-1 pt-1 h-min">
            <MetadataProfilesSelector
                v-if="optionalProfiles.length > 0"
                :profiles="optionalProfiles"
                v-model:selected-profiles="enabledProfiles"
                class="h-min"
            />
            <div v-else>&nbsp;</div>

            <ProjectExportersBar :project="project" :scope="ProjectMetadataFeature.FeatureID" class="p-2 justify-self-end" />
        </div>
        <PropertyEditor
            v-model="project!.features.project_metadata.metadata"
            v-model:shared-property-objects="project!.features.shared_objects"
            :projectProfiles="projectProfiles as PropertyProfileStore"
        />
    </div>
</template>

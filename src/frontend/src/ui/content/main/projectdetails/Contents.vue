<script setup lang="ts">
import Tabs from "primevue/tabs";
import TabList from "primevue/tablist";
import Tab from "primevue/tab";
import TabPanels from "primevue/tabpanels";
import TabPanel from "primevue/tabpanel";
import { computed, defineAsyncComponent, type PropType, reactive, ref, toRefs, unref, watch } from "vue";

import { Project } from "@common/data/entities/project/Project";
import { ProjectObjectStore } from "@common/ui/components/propertyeditor/ProjectObjectStore";
import { makeDebounce } from "@common/ui/components/propertyeditor/utils/PropertyEditorUtils";

import { FrontendComponent } from "@/component/FrontendComponent";
import { type UIOptions } from "@/data/entities/ui/UIOptions";
import { UpdateProjectFeaturesAction } from "@/ui/actions/project/UpdateProjectFeaturesAction";
import { SnapInsCatalog } from "@/ui/snapins/SnapInsCatalog";

const comp = FrontendComponent.inject();
const props = defineProps({
    project: {
        type: Object as PropType<Project>,
        required: true
    }
});
const { project } = toRefs(props);

const activePanelIndex = ref(0);
const panels = computed(() => {
    // Select all snap-ins that provide a tab panel and are either non-optional or turned on by the user
    const panelSnapIns = SnapInsCatalog.allWithTabPanel().filter((snapIn) => {
        const uiOptions = project!.value.options.ui as UIOptions;
        return !snapIn.isOptional() || uiOptions.optional_snapins?.includes(snapIn.snapInID);
    });

    if (unref(activePanelIndex) >= panelSnapIns.length) {
        activePanelIndex.value = panelSnapIns.length - 1;
    }

    return panelSnapIns.map((snapIn) => {
        return { title: snapIn.options.tabPanel!.label, component: defineAsyncComponent(snapIn.options.tabPanel!.loader) };
    });
});

const sharedObjectStore = reactive(new ProjectObjectStore());

const debounce = makeDebounce();
watch(
    () => project!.value.features.shared_objects,
    (shared_objects) => {
        debounce(() => {
            const action = new UpdateProjectFeaturesAction(comp);
            action.prepare(project!.value, [], shared_objects);
            action.execute();
        });
    },
    { deep: true }
);
</script>

<template>
    <div class="h-full">
        <Tabs :value="panels[0].title" class="h-full">
            <TabList :pt="{ tabList: 'tab-list', activeBar: 'tab-list-active-bar' }">
                <Tab v-for="panel in panels" :value="panel.title" class="tab">{{ panel.title }}</Tab>
            </TabList>
            <TabPanels class="overflow-y-auto max-h-[calc(100vh-8.0rem)] p-0 h-full">
                <TabPanel v-for="panel in panels" :value="panel.title" class="h-full">
                    <component :is="panel.component" :project="project" :sharedObjectStore="sharedObjectStore" />
                </TabPanel>
            </TabPanels>
        </Tabs>
        <!--
        <TabView
            v-model:active-index="activePanelIndex"
            class="h-full"
            :pt="{
                nav: 'tab-view',
                panelContainer: 'overflow-y-auto max-h-[calc(100vh-8.0rem)] p-0 h-full' // TODO: Hacky height
            }"
        >
            <TabPanel
                v-for="panel in panels"
                :key="panel.title"
                :header="panel.title"
                :pt="{
                    header: 'tab-view-panel',
                    headerAction: 'tab-view-panel-action',
                    content: 'h-full'
                }"
            >
                <component :is="panel.component" :project="project" :sharedObjectStore="sharedObjectStore" />
            </TabPanel>
        </TabView>
        -->
    </div>
</template>

<style scoped lang="scss">
:deep(.tab-list) {
    @apply grid grid-flow-col bg-surface-50;
}

:deep(.tab-list-active-bar) {
    @apply border border-[var(--p-button-warn-background)];
}

:deep(.tab) {
    @apply border-e border-inherit;
}
</style>

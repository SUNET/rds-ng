<script setup lang="ts">
import Button from "primevue/button";
import Chip from "primevue/chip";
import Dialog from "primevue/dialog";
import FloatLabel from "primevue/floatlabel";
import InputText from "primevue/inputtext";
import OrderList from "primevue/orderlist";

import { computed, ref, type Ref } from "vue";
import { useColorsStore } from "../../../data/stores/ColorsStore";
import { calculateLayout as makeLayout } from "./utils/PropertyEditorUtils";

import { ProjectObjectStore } from "./ProjectObjectStore";
import PropertyOneCol from "./PropertyOneCol.vue";
import { ProfileLayoutClass } from "./PropertyProfile";

const props = defineProps(["controller", "project", "projectProfiles", "projectObjects", "sharedObjectStore"]);
const colorsStore = useColorsStore();

var layout = makeLayout(props.projectProfiles);

const propsToShow = ref<ProfileLayoutClass[]>(
    layout
        .filter((e: ProfileLayoutClass) => e.required || props.projectObjects.get(e.id) !== undefined)
        .sort((a: ProfileLayoutClass, b: ProfileLayoutClass) => -a.profiles!.length - -b.profiles!.length)
);

const selectedProperties = ref([]) as Ref<ProfileLayoutClass[]>;
const unselectProperties = () => (selectedProperties.value = []);
const selectProperties = (selection: ProfileLayoutClass[]) => (selectedProperties.value = selection);

const hideProperty = (id: string) => {
    layout = layout.filter((e: ProfileLayoutClass) => e.getId() != id);
};

const showAddProperties = ref(false);
const hiddenPropertys = computed(() =>
    layout.filter((e: ProfileLayoutClass) => !propsToShow.value.map((e: ProfileLayoutClass) => e.getId()).includes(e.getId()))
);

const filteredProperties = computed(() =>
    hiddenPropertys.value.filter(
        (e: ProfileLayoutClass) =>
            e.label.toLowerCase().includes(searchString.value.toLowerCase()) || e.description?.toLowerCase().includes(searchString.value.toLowerCase())
    )
);

const searchString = ref("");
</script>

<template>
    <div class="w-full max-w-full">
        <PropertyOneCol
            v-for="(p, i) in propsToShow"
            :key="p.id"
            :index="i"
            class="my-5 w-full max-w-full"
            :propertyClass="p"
            :projectObjects="projectObjects"
            :sharedObjectStore="sharedObjectStore as ProjectObjectStore"
            :projectProfiles="projectProfiles"
            :layoutProfiles="layout"
            @hide="(id) => hideProperty(id)"
        />
    </div>
    <Button v-if="hiddenPropertys.length !== 0" class="fixed bottom-10 right-10" icon="pi pi-plus" size="large" rounded @click="showAddProperties = true" />

    <Dialog
        v-model:visible="showAddProperties"
        modal
        header="Add Properties"
        :pt="{ content: { class: 'h-full' } }"
        :style="{ width: '50vw', height: '80vh' }"
        @after-hide="
            unselectProperties();
            searchString = '';
        "
    >
        <template #default>
            <div class="h-full flex-col flex space-y-4">
                <FloatLabel>
                    <InputText type="text" v-model="searchString" id="searchString" class="w-full" />
                    <label for="searchString">Search...</label>
                </FloatLabel>
                <OrderList
                    v-model="filteredProperties"
                    @update:selection="(selection: ProfileLayoutClass[]) => selectProperties(selection)"
                    dataKey="id"
                    class="h-full"
                    :pt="{ list: { class: 'min-h-full' } }"
                    :stripedRows="true"
                >
                    <template #item="slotProps">
                        <div class="flex flex-col">
                            <span class="font-semibold flex gap-2" :title="slotProps.item.label">
                                <span class="grow"> {{ slotProps.item.label }} </span>
                                <Chip
                                    v-for="p in slotProps.item.profiles"
                                    :label="p[0]"
                                    size="small"
                                    :style="`background-color: ${colorsStore.color(p[0])}`"
                                    class="h-4 !rounded py-3 text-sm bg-opacity-40"
                            /></span>
                            <span class="text-gray-500 ellipsis line-clamp-1" :title="slotProps.item.description">{{ slotProps.item.description }}</span>
                        </div>
                    </template>
                </OrderList>
            </div>
        </template>
        <template #footer>
            <div class="flex justify-end gap-2 mt-5">
                <Button
                    :disabled="!selectedProperties.length"
                    @click="
                        propsToShow.push(...selectedProperties);
                        unselectProperties();
                        searchString = '';
                        showAddProperties = false;
                    "
                    >Add {{ selectedProperties.length ? "(" + selectedProperties.length + ")" : "" }}
                </Button>
                <Button
                    outlined
                    severity="secondary"
                    @click="
                        unselectProperties();
                        searchString = '';
                        showAddProperties = false;
                    "
                    >Cancel
                </Button>
            </div>
        </template>
    </Dialog>
</template>

<style scoped lang="scss">
:deep(.p-orderlist-controls) {
    display: none;
}

:deep(.p-orderlist-item) {
    @apply border-l-2 border-solid border-transparent;
}

:deep(.p-orderlist-item.p-highlight) {
    @apply bg-emerald-50  border-l-2 border-emerald-600 text-slate-700;
}
</style>

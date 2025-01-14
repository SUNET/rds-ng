<script setup lang="ts">
import Button from "primevue/button";
import Chip from "primevue/chip";
import Dialog from "primevue/dialog";
import FloatLabel from "primevue/floatlabel";
import IconField from "primevue/iconfield";
import InputIcon from "primevue/inputicon";
import InputSwitch from "primevue/inputswitch";
import InputText from "primevue/inputtext";
import OrderList from "primevue/orderlist";

import { computed, ref, type Ref } from "vue";
import { useColorsStore } from "../../../data/stores/ColorsStore";
import { calculateLayout as makeLayout } from "./utils/PropertyEditorUtils";

import { PropertyObjectStore } from "./PropertyObjectStore";
import PropertyOneCol from "./PropertyOneCol.vue";
import { type ProfileID, ProfileLayoutClass } from "./PropertyProfile";

const props = defineProps(["controller", "project", "projectProfiles", "propertyObjects", "sharedPropertyObjectStore"]);
const colorsStore = useColorsStore();

var layout = makeLayout(props.projectProfiles);

const profileFilter = ref<ProfileID[]>([]);
const requiredOnly = ref(false);
const addSearchString = ref("");
const searchString = ref("");

// TODO Comment and maybe refactor to have dynamic filters
const propsToShow = computed(() =>
    layout
        .filter((e: ProfileLayoutClass) => e.required || (requiredOnly.value ? false : props.propertyObjects.get(e.id) !== undefined))
        .filter(
            (e: ProfileLayoutClass) =>
                profileFilter.value.length === 0 || e.profiles.some((p: ProfileID) => profileFilter.value.map((i) => i[0]).includes(p[0]))
        )
        .filter(
            (e: ProfileLayoutClass) =>
                // search in label
                e.getDisplayLabel().toLowerCase().includes(searchString.value.toLowerCase()) ||
                // search in description
                e.description?.toLowerCase().includes(searchString.value.toLowerCase()) ||
                // search in simple property objects
                !Object.values(props.propertyObjects.get(e.id).getValues()).findIndex((v: string) =>
                    v.toLowerCase().includes(searchString.value.toLowerCase())
                ) ||
                // search in referenced property objects
                !props.propertyObjects
                    .getReferencedObjects(e.id)
                    .map((o: String) => props.sharedPropertyObjectStore.get(o).getValues())
                    .map((e: String[]) => Object.values(e))
                    .flat()
                    .findIndex((v: string) => v.toLowerCase().includes(searchString.value.toLowerCase()))
        )
        .sort((a: ProfileLayoutClass, b: ProfileLayoutClass) => -a.profiles!.length - -b.profiles!.length)
);

const selectedProperties = ref([]) as Ref<ProfileLayoutClass[]>;
const unselectProperties = () => (selectedProperties.value = []);
const selectProperties = (selection: ProfileLayoutClass[]) => (selectedProperties.value = selection);

const showAddProperties = ref(false);
const hiddenPropertys = computed(() =>
    layout.filter((e: ProfileLayoutClass) => !propsToShow.value.map((e: ProfileLayoutClass) => e.getId()).includes(e.getId()))
);

const filteredProperties = computed(() =>
    hiddenPropertys.value.filter(
        (e: ProfileLayoutClass) =>
            e.getDisplayLabel().toLowerCase().includes(addSearchString.value.toLowerCase()) ||
            e.description?.toLowerCase().includes(addSearchString.value.toLowerCase())
    )
);

const resetFilters = () => {
    profileFilter.value = [];
    searchString.value = "";
    requiredOnly.value = false;
};
</script>

<template>
    <div class="w-full max-w-full">
        <!-- TODO In eigene Komponente auslagern, auch zum "add Properties" Dialog hinzufuegen. -->
        <div class="m-5 mb-5 mr-0" :class="projectProfiles.list().length > 1 ? 'border-b' : ''">
            <IconField iconPosition="left">
                <InputIcon class="pi pi-search"> </InputIcon>
                <InputText type="text" v-model="searchString" id="searchString" class="w-full" placeholder="Search..." autocomplete="off" />
            </IconField>
            <div v-if="projectProfiles.list().length > 1" class="my-3 flex justify-between">
                <span class="flex align-center gap-2">
                    <Chip
                        :label="`All (${layout.filter((e: ProfileLayoutClass) => e.required || props.propertyObjects.get(e.id) !== undefined).length})`"
                        title="Show all properties"
                        class="h-4 !rounded py-3 text-sm border border-slate-700 cursor-pointer"
                        :class="profileFilter.length === 0 && !searchString && !requiredOnly ? 'text-emerald-100 bg-slate-700' : ''"
                        @click="resetFilters"
                    />
                    <Chip
                        v-for="profile in projectProfiles.list()"
                        :label="profile.getDisplayLabel()"
                        class="h-4 !rounded py-3 text-sm border cursor-pointer"
                        :class="profileFilter.includes(profile.getId()) ? 'bg-emerald-50 border-emerald-600 text-slate-700' : ''"
                        @click="
                            profileFilter.includes(profile.getId())
                                ? (profileFilter = profileFilter.filter((e) => e !== profile.getId()))
                                : profileFilter.push(profile.getId())
                        "
                    />
                </span>
                <span class="flex align-center gap-2" title="Hide optional properties." aria-label="Hide optional properties.">
                    <label for="required">Required only</label>
                    <InputSwitch v-model="requiredOnly" inputId="required" />
                </span>
            </div>
        </div>

        <!-- TODO: Put into its own component -->
        <div v-if="searchString && propsToShow.length == 0" class="w-full text-center">
            No matches for <span class="font-bold">{{ searchString }}</span
            >...
        </div>
        <div v-else-if="searchString">
            <div class="w-full text-center">
                <span class="font-bold">{{ propsToShow.length }}</span> match{{ propsToShow.length > 1 ? `es` : "" }} for
                <span class="font-bold">{{ searchString }}</span
                >...
            </div>
        </div>

        <PropertyOneCol
            v-for="(p, i) in propsToShow"
            :key="p.id"
            :index="i"
            class="my-5 w-full max-w-full"
            :propertyClass="p"
            :propertyObjects="propertyObjects"
            :sharedPropertyObjectStore="sharedPropertyObjectStore as PropertyObjectStore"
            :projectProfiles="projectProfiles"
            :layoutProfiles="layout"
        />
    </div>
    <Button
        v-if="hiddenPropertys.length !== 0"
        class="fixed bottom-10 right-10"
        icon="material-icons-outlined mi-add"
        size="large"
        rounded
        severity="primary"
        @click="showAddProperties = true"
        v-tooltip="{ value: 'Add more properties' }"
    />

    <Dialog
        v-model:visible="showAddProperties"
        modal
        header="Add properties"
        :pt="{ content: 'h-full' }"
        :style="{ width: '50vw', height: '80vh' }"
        @after-hide="
            unselectProperties();
            addSearchString = '';
        "
    >
        <template #default>
            <div class="h-full flex-col flex space-y-4">
                <FloatLabel>
                    <InputText type="text" v-model="addSearchString" id="searchString" class="w-full" />
                    <label for="searchString">Search...</label>
                </FloatLabel>
                <OrderList
                    v-model="filteredProperties"
                    @update:selection="(selection: ProfileLayoutClass[]) => selectProperties(selection)"
                    dataKey="id"
                    class="h-full"
                    :pt="{ pcListbox: { listContainer: 'min-h-full' } }"
                    :stripedRows="true"
                >
                    <template #option="slotProps">
                        <div class="flex flex-col w-full p-1">
                            <span class="font-semibold flex gap-2" :title="slotProps.option.label">
                                <span class="grow"> {{ slotProps.option.getDisplayLabel() }}</span>
                                <Chip
                                    v-for="p in slotProps.option.profiles"
                                    :label="p[0]"
                                    size="small"
                                    :style="`background-color: ${colorsStore.color(p[0])}`"
                                    class="h-4 !rounded py-3 text-sm bg-opacity-40"
                            /></span>
                            <span class="text-gray-500 ellipsis line-clamp-1" :title="slotProps.option.description">{{ slotProps.option.description }}</span>
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
                        addSearchString = '';
                        showAddProperties = false;
                    "
                    >Add {{ selectedProperties.length ? "(" + selectedProperties.length + ")" : "" }}
                </Button>
                <Button
                    outlined
                    severity="secondary"
                    @click="
                        unselectProperties();
                        addSearchString = '';
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

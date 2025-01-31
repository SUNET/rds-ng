<script setup lang="ts">
import { computed, type ComputedRef, inject, reactive, ref, type Ref } from "vue";

import Breadcrumb from "primevue/breadcrumb";
import Button from "primevue/button";
import Card from "primevue/card";
import type { MenuItem } from "primevue/menuitem";
import ScrollPanel from "primevue/scrollpanel";
import SplitButton from "primevue/splitbutton";

import Fieldset from "primevue/fieldset";

import { History } from "./Breadcrumbs";
import EntityColumnHeader from "./EntityColumn/EntityColumnHeader.vue";
import EntityColumnInputs from "./EntityColumn/EntityColumnInputs.vue";
import EntityColumnLinkedItems from "./EntityColumn/EntityColumnLinkedItems.vue";
import { PropertyObjectStore, SharedPropertyObject } from "./PropertyObjectStore";
import { ProfileClass, ProfileClassRef } from "./PropertyProfile";
import { PropertyProfileStore } from "./PropertyProfileStore";
import { calcObjLabel } from "./utils/ObjectUtils";

const dialogRef = inject("dialogRef") as any;
const {
    id,
    propertyObjects,
    sharedPropertyObjectStore,
    projectProfiles
}: { id: string; propertyObjects: PropertyObjectStore; sharedPropertyObjectStore: PropertyObjectStore; projectProfiles: PropertyProfileStore } =
    dialogRef.value.data;

// selected object
const object = ref(sharedPropertyObjectStore.get(id)!) as Ref<SharedPropertyObject>;
let propertyClass = reactive(projectProfiles.getClassById(object.value.getType())!) as ProfileClass;
const referencedObjects = computed(() => object.value.getReferences().map((e) => sharedPropertyObjectStore.get(e))) as ComputedRef<SharedPropertyObject[]>;

const displayableInputs = ref(propertyClass.getInputs());
const addableTypes = ref(propertyClass.getRefTypes()) as Ref<ProfileClassRef[]>;

const addableExlineTypes = computed(() => addableTypes.value.filter((t) => !t.isInline()));
const addableInlineTypes = computed(() => addableTypes.value.filter((t) => t.isInline()));

// History for Breadcrumbs
const history = new History();
const menuPath = ref();

function selectActiveObject(id: string) {
    object.value = sharedPropertyObjectStore.get(id) as SharedPropertyObject;
    propertyClass = projectProfiles.getClassById(object.value.getType())! as ProfileClass;
    addableTypes.value = propertyClass.getRefTypes();
    displayableInputs.value = propertyClass.getInputs();
    history.navigateTo(object.value);
    // TODO optimize by only updating necessary elements
    menuPath.value = history.list().map((item: SharedPropertyObject) => {
        const obj = sharedPropertyObjectStore.get(item.getId()) as SharedPropertyObject;

        return {
            label: `${projectProfiles.getClassLabelById(item.getType())}:  ${calcObjLabel(obj!, projectProfiles)}`,
            command: () => selectActiveObject(item.getId())
        };
    });
}

selectActiveObject(id);

function createObject(type: string) {
    const newObject = new SharedPropertyObject(type);
    sharedPropertyObjectStore.add(newObject);
    propertyObjects.addRef(object.value.getId(), newObject.getId()) || sharedPropertyObjectStore.addRef(object.value.getId(), newObject.getId());
}
</script>

<template>
    <ScrollPanel class="h-full pr-5">
        <Card :pt="{ root: 'shadow-none', body: 'pl-1 p-0 overflow-hidden' }">
            <template #header>
                <Breadcrumb
                    :model="menuPath as MenuItem[]"
                    class="max-w-full w-full grid grid-cols-1"
                    :pt="{
                        root: { class: 'px-0 pt-0' },
                        list: { class: ' flex flex-wrap ' },
                        separator: { class: 'mb-2' },
                        item: { class: 'max-w-full breadcrumbs-item' },
                        itemLabel: { class: 'text-red-900 opacity-80 hover:opacity-100 cursor-pointer truncate pb-2' }
                    }"
                />
            </template>
            <template #title>
                <!--  Header Row -->

                <EntityColumnHeader
                    :addableTypes="addableTypes"
                    :propertyClass="propertyClass"
                    :propertyObject="object"
                    :propertyObjects="propertyObjects"
                    :sharedPropertyObjectStore="sharedPropertyObjectStore"
                    :projectProfiles="projectProfiles"
                    :isDialog="true"
                    @loadObject="(id) => selectActiveObject(id)"
                />
            </template>
            <template #content>
                <div class="flex flex-row">
                    <div class="grow max-w-full space-y-4">
                        <!--  Linked Items Row -->

                        <EntityColumnLinkedItems
                            v-if="!!addableExlineTypes.length"
                            :propertyObjects="propertyObjects"
                            :propertyClass="object"
                            :sharedPropertyObjectStore="sharedPropertyObjectStore"
                            :projectProfiles="projectProfiles"
                            :addableTypes="addableExlineTypes"
                            :propertyObject="object"
                        />
                        <!-- Simple Input Row -->
                        <EntityColumnInputs
                            v-if="displayableInputs.length > 0"
                            :displayableInputs="displayableInputs"
                            :propertyObject="object"
                            :propertyObjects="sharedPropertyObjectStore"
                            :propertyClass="propertyClass"
                            :isDialog="true"
                        />

                        <Fieldset
                            v-for="t in addableInlineTypes"
                            class="p-0 border"
                            :class="{ 'border-0': referencedObjects.filter((e) => e.getType() === t.getClassId()).length === 0 }"
                        >
                            <template #legend>
                                <div class="right">
                                    <SplitButton
                                        @click="() => createObject(t.getClassId())"
                                        icon="pi pi-plus"
                                        dropdownIcon="pi pi-link"
                                        severity="primary"
                                        outlined
                                        :label="projectProfiles.getClassById(t.getClassId())?.getDisplayLabel()"
                                        :title="projectProfiles.getClassById(t.getClassId())?.getDescription()"
                                        :disabled="
                                            !t.allowsMultiple() &&
                                            referencedObjects.filter((e: SharedPropertyObject) => e.getType() === t.getClassId()).length > 0
                                        "
                                    />
                                </div>
                            </template>
                            <div class="space-y">
                                <div
                                    v-for="[i, refObject] of referencedObjects.filter((e: SharedPropertyObject) => e.getType() === t.getClassId()).entries()"
                                    class="row-span-1 space-y-1 my-2 last-fieldset-round mb-0 mt-1"
                                >
                                    <Fieldset class="bg-sky-50 rounded-none border-y my-0">
                                        <template #legend class="m-0 p-0">
                                            <div class="flex items-center space-x-3">
                                                <span> #{{ i + 1 }}</span>
                                                <Button
                                                    @click="sharedPropertyObjectStore.remove(refObject!.getId())"
                                                    class="[&:not(:hover)]:bg-white"
                                                    icon="pi pi-times"
                                                    severity="danger"
                                                    rounded
                                                    outlined
                                                    size="small"
                                                />
                                            </div>
                                        </template>

                                        <EntityColumnInputs
                                            v-if="!!projectProfiles.getClassById(t.getClassId())?.getInputs().length"
                                            class="mt-2"
                                            :displayableInputs="projectProfiles.getClassById(t.getClassId())?.getInputs()"
                                            :propertyObject="object"
                                            :propertyObjects="sharedPropertyObjectStore"
                                            :propertyClass="propertyClass"
                                            :isDialog="true"
                                        />
                                    </Fieldset>
                                </div>
                            </div>
                        </Fieldset>
                    </div>
                </div>
            </template>
        </Card>
    </ScrollPanel>
</template>

<style scoped lang="scss">
:deep(.breadcrumbs-item:last-child) {
    @apply font-bold;
}

:deep(.p-fieldset-legend) {
    @apply ml-auto m-0 p-0 rounded bg-transparent;
}

.last-fieldset-round:last-child > .p-fieldset {
    @apply rounded-b-md;
}
</style>

<script setup lang="ts">
import { computed, type ComputedRef, inject, reactive, ref, type Ref } from "vue";

import Breadcrumb from "primevue/breadcrumb";
import Button from "primevue/button";
import Card from "primevue/card";
import type { MenuItem } from "primevue/menuitem";
import ScrollPanel from "primevue/scrollpanel";
import SplitButton from "primevue/splitbutton";

import Fieldset from "primevue/fieldset";

import Popover from "primevue/popover";
import { History } from "./Breadcrumbs";
import LinkedItemButton from "./LinkedItemButton.vue";
import NewPropertyButton from "./NewPropertyButton.vue";
import { PropertyObjectStore, SharedPropertyObject } from "./PropertyObjectStore";
import { ProfileClass, ProfileClassRef, propertyDataForms, PropertyDataType } from "./PropertyProfile";
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
let objectClass = reactive(projectProfiles.getClassById(object.value.getType())!) as ProfileClass;
let referencedObjects = computed(() => object.value.getReferences().map((e) => sharedPropertyObjectStore.get(e))) as ComputedRef<SharedPropertyObject[]>;

const displayableInputs = ref(objectClass.getInputs());
const addableTypes = ref(objectClass.getRefTypes()) as Ref<ProfileClassRef[]>;

const addableExlineTypes = computed(() => addableTypes.value.filter((t) => !t.isInline()));
const addableInlineTypes = computed(() => addableTypes.value.filter((t) => t.isInline()));

const linkedObjects = computed(() => sharedPropertyObjectStore.getReferencedObjects(object.value.getId()));

// History for Breadcrumbs
const history = new History();
const menuPath = ref();

// Description Overlay
const op = ref();
const toggle = (event: Event) => {
    op.value.toggle(event);
};

function selectActiveObject(id: string) {
    object.value = sharedPropertyObjectStore.get(id) as SharedPropertyObject;
    objectClass = projectProfiles.getClassById(object.value.getType())! as ProfileClass;
    addableTypes.value = objectClass.getRefTypes();
    displayableInputs.value = objectClass.getInputs();
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
                <div class="row-span-1 text-gray-800 justify-between flex items-center">
                    <span :title="objectClass.getDisplayLabel()" class="flex-none">
                        <span class="text-2xl"> {{ objectClass.getDisplayLabel() }}</span>
                        <Button v-if="objectClass.getDescription()" unstyled @click="toggle" :title="objectClass.getDescription()">
                            <i class="pi pi-question-circle mx-2" style="font-size: 1rem" />
                        </Button>
                        <Popover ref="op" class="max-w-lg">
                            {{ objectClass.getDescription() }}
                            <span v-if="objectClass.getExample()" v-html="`<br/>Example: ${objectClass.getExample()}`" />
                        </Popover>
                    </span>

                    <span class="mr-auto ml-5 flex gap-1 flex-wrap">
                        <NewPropertyButton
                            v-for="t in addableExlineTypes"
                            :key="t.getClassId()"
                            :type="t.getClassId()"
                            :parentId="object.getId()"
                            :propertyObjects="propertyObjects"
                            :sharedPropertyObjectStore="sharedPropertyObjectStore as PropertyObjectStore"
                            :projectProfiles="projectProfiles"
                            mode="dialog"
                            @loadObject="(id) => selectActiveObject(id)"
                        />
                    </span>
                </div>
            </template>
            <template #content>
                <div class="flex flex-row">
                    <div class="grow max-w-full space-y-4">
                        <!--  Linked Items Row -->
                        <div
                            v-if="addableExlineTypes.length > 0"
                            class="row-span-1 flex mt-3 p-2 flex-wrap gap-0.5 rounded-md"
                            style="
                                box-shadow:
                                    0 0 #0000,
                                    0 0 #0000,
                                    0 1px 2px 0 rgba(18, 18, 23, 0.05);
                                transition:
                                    background-color 0.2s,
                                    color 0.2s,
                                    border-color 0.2s,
                                    box-shadow 0.2s,
                                    outline-color 0.2s;
                                border: 1px dashed #b6bfca;
                            "
                        >
                            <LinkedItemButton
                                v-if="linkedObjects.length > 0"
                                v-for="i in linkedObjects"
                                :key="i"
                                class="m-1 max-w-full"
                                :item-id="i"
                                :parentId="object.getId()"
                                :propertyObjects="propertyObjects"
                                :sharedPropertyObjectStore="sharedPropertyObjectStore as PropertyObjectStore"
                                :projectProfiles="projectProfiles"
                                mode="dialog"
                                @loadObject="(id) => selectActiveObject(id)"
                            />
                            <span v-else class="text-gray-500 m-1 my-3 place-self-center align-middle inline-block"
                                >No
                                <span class="italic">
                                    {{
                                        addableTypes
                                            .map((e: ProfileClassRef) => projectProfiles.getClassLabelById(e.getClassId()))
                                            .join(", ")
                                            .replace(/, ([^,]*)$/, " or $1")
                                    }}
                                </span>
                                linked</span
                            >
                        </div>
                        <!-- Simple Input Row -->
                        <div class="space-y-5">
                            <div v-for="input in displayableInputs" class="row-span-1 space-y-1">
                                <div v-if="input.getLabel() !== objectClass.getDisplayLabel()" class="font-bold mb-1 font">{{ input.getLabel() }}</div>
                                {{ input.getDescription() }}
                                <span v-if="input.getExample()" v-html="`<br/>Example: ${input.getExample()}`" />
                                <component
                                    :is="propertyDataForms[input.getType() as PropertyDataType]"
                                    class="w-full"
                                    :propertyObjectId="object.getId()"
                                    :propertyObjects="sharedPropertyObjectStore"
                                    :sharedPropertyObjectStore="sharedPropertyObjectStore as PropertyObjectStore"
                                    :inputId="input.getId()"
                                    :inputOptions="input.getOptions() ? input.getOptions() : []"
                                />
                            </div>
                        </div>

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
                                    class="row-span-1 space-y-1 my-2 some-elemente mb-0 mt-1"
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
                                        <div v-for="input in projectProfiles.getClassById(t.getClassId())?.getInputs()" class="py-2 first:mt-0 space-y-0.5">
                                            <div v-if="input.getLabel() !== objectClass.getDisplayLabel()" class="font-bold">
                                                {{ input.getLabel() }}
                                            </div>
                                            <div v-if="input.getLabel() !== objectClass.getDisplayLabel()" class="r-text-gray">
                                                {{ input.getDescription() }}
                                            </div>
                                            <div v-if="input.getExample()" v-html="`Example: ${input.getExample()}`" />
                                            <component
                                                :is="propertyDataForms[input.getType() as PropertyDataType]"
                                                class="w-full"
                                                :propertyObjectId="refObject?.getId()"
                                                :propertyObjects="sharedPropertyObjectStore"
                                                :sharedPropertyObjectStore="sharedPropertyObjectStore as PropertyObjectStore"
                                                :inputId="input.getId()"
                                                :inputOptions="input.getOptions() ? input.getOptions() : []"
                                            />
                                        </div>
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

.some-elemente:last-child > .p-fieldset {
    @apply rounded-b-md;
}
</style>

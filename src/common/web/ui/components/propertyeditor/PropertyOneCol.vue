<script setup lang="ts">
import { computed, ref, watch, type PropType, type Ref } from "vue";

import Button from "primevue/button";
import Chip from "primevue/chip";
import Popover from "primevue/popover";

import { useColorsStore } from "../../../data/stores/ColorsStore";
import IndexColumn from "./IndexColumn.vue";
import { LayoutPropertyObject, PropertyObject, PropertyObjectStore } from "./PropertyObjectStore";
import { ProfileClass, ProfileLayoutClass, PropertyDataType, propertyDataForms, type ProfileID } from "./PropertyProfile";
import { PropertyProfileStore } from "./PropertyProfileStore";

import MandatoryMark from "../misc/MandatoryMark.vue";
import LinkedItemButton from "./LinkedItemButton.vue";
import NewPropertyButton from "./NewPropertyButton.vue";

const { index, propertyClass, propertyObjects, projectProfiles, sharedPropertyObjectStore, layoutProfiles } = defineProps({
    index: {
        type: Number,
        required: true
    },
    propertyClass: {
        type: Object as PropType<ProfileClass & { profiles: ProfileID[] }>,
        required: true
    },
    propertyObjects: {
        type: Object as PropType<PropertyObjectStore>,
        required: true
    },
    projectProfiles: {
        type: PropertyProfileStore,
        required: true
    },
    sharedPropertyObjectStore: {
        type: Object as PropType<PropertyObjectStore>,
        required: true
    },
    layoutProfiles: {
        type: Object as PropType<Array<ProfileLayoutClass>>,
        required: true
    }
});
const colorsStore = useColorsStore();

propertyObjects.add(new LayoutPropertyObject(propertyClass.getId()));

const propertyObject = computed(
    () => propertyObjects.get(propertyClass.getId()) || propertyObjects.add(new LayoutPropertyObject(propertyClass.getId()))
) as Ref<PropertyObject>;

watch(
    () => propertyObjects.get(propertyClass.getId()),
    (obj) => {
        if (!obj) propertyObjects.add(new LayoutPropertyObject(propertyClass.getId()));
    }
);

const op = ref();
const toggleRemoveDeadLink = (event: Event) => {
    op.value.toggle(event);
};

const displayableInputs = propertyClass.getInputs();

const addableTypes = propertyClass.getRefTypes();

const linkedObjects = computed(() => propertyObjects.getReferencedObjects(propertyClass.getId()));

const profiles = computed(() => {
    const profileIDs = layoutProfiles?.find((e) => e.id == propertyObject.value.getId())!.getProfiles() as ProfileID[];
    const filteredProfileIDs: ProfileID[] = [];

    profileIDs.forEach((id) => {
        if (!filteredProfileIDs.find((e) => e[0] == id[0])) {
            filteredProfileIDs.push(id);
        }
    });
    return filteredProfileIDs;
});

const removeFromLayout = (pId: string) => {
    propertyObjects.remove(pId);
};
</script>

<template>
    <div class="flex flex-row hover:bg-gray-100 px-2 pl-0 rounded group max-w-full w-full">
        <!-- IndexColumn holds the index number and the remove button for the property, if it is not required. -->
        <IndexColumn class="grid w-16 justify-center shrink-0" @remove="(pId) => removeFromLayout(pId)" :propertyClass="propertyClass" :index="index + 1" />

        <div class="w-full grid grid-cols-1">
            <!--  Header Row -->
            <div class="row-span-1 text-gray-800 justify-between flex flex-wrap gap-4 max-w-full w-full items-center">
                <span :title="propertyClass.getDisplayLabel()" class="min-w-fit">
                    <span class="text-lg"> {{ propertyClass.getDisplayLabel() }} </span>
                    <MandatoryMark v-if="propertyClass.isRequired()" class="pl-1" color="red" />

                    <Button v-if="propertyClass.getDescription()" unstyled @click="toggleRemoveDeadLink" :title="propertyClass.getDescription()">
                        <i class="pi pi-question-circle mx-2" style="font-size: 1rem; color: gray" />
                    </Button>
                    <Popover ref="op" class="max-w-lg">
                        {{ propertyClass.description }}
                        <p v-if="propertyClass.getExample()" class="mt-2" v-html="`<b>Example</b>: ${propertyClass.getExample()}`" />
                    </Popover>
                </span>
                <span class="mr-auto ml-5 flex gap-1 flex-wrap">
                    <NewPropertyButton
                        v-for="t in addableTypes.filter((t) => !t.isInline())"
                        :key="t.getClassId()"
                        :type="t.getClassId()"
                        :parentId="propertyObject.getId()"
                        :propertyObjects="propertyObjects as PropertyObjectStore"
                        :sharedPropertyObjectStore="sharedPropertyObjectStore as PropertyObjectStore"
                        :projectProfiles="projectProfiles"
                    />
                </span>
                <span class="flex self-center gap-2">
                    <Chip
                        v-for="p in profiles.sort()"
                        :label="projectProfiles.getProfileLabelById(p)"
                        size="small"
                        class="h-4 !rounded py-3 text-sm bg-opacity-40"
                        :style="`background-color: ${colorsStore.color(p[0])}`"
                    />
                </span>
            </div>
            <!--  Linked Items Row -->
            <div
                v-if="addableTypes !== undefined && addableTypes.length > 0"
                class="row-span-1 flex mt-3 p-2 flex-wrap gap-0.5 rounded-md border"
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
                    :parentId="propertyClass.getId()"
                    :propertyObjects="propertyObjects"
                    :sharedPropertyObjectStore="sharedPropertyObjectStore as PropertyObjectStore"
                    :projectProfiles="projectProfiles"
                />
                <span v-else class="text-gray-500 m-1 my-3 place-self-center align-middle inline-block"
                    >No
                    <span class="italic">
                        {{
                            addableTypes
                                .map((e) => projectProfiles.getClassLabelById(e))
                                .join(", ")
                                .replace(/, ([^,]*)$/, " or $1")
                        }}
                    </span>
                    linked</span
                >
            </div>
            <!-- Simple Input Row -->
            <div v-if="displayableInputs.length > 0" class="space-y-2 mt-2">
                <div v-for="input in displayableInputs" class="row-span-1">
                    <span v-if="input.getLabel() !== propertyClass.getDisplayLabel()">{{ input.getLabel() }}</span>
                    <component
                        :is="propertyDataForms[input.getType() as PropertyDataType]"
                        class="w-full"
                        :propertyObjectId="propertyObject.getId()"
                        :propertyObjects="propertyObjects"
                        :inputId="input.getId()"
                        :inputOptions="input.getOptions() ? input.getOptions() : []"
                    />
                </div>
            </div>
        </div>
    </div>
</template>

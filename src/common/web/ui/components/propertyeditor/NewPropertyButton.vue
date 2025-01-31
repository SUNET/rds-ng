<script setup lang="ts">
import SplitButton from "primevue/splitbutton";
import { useDialog } from "primevue/usedialog";
import { computed } from "vue";
import PropertyDialog from "./PropertyDialog.vue";
import { SharedPropertyObject } from "./PropertyObjectStore";
import { injectTemplate } from "./utils/Templates";

const dialog = useDialog();
const props = defineProps(["type", "parentId", "propertyObjects", "sharedPropertyObjectStore", "projectProfiles", "isDialog"]);

const emit = defineEmits(["loadObject"]);
const label = props.projectProfiles.getClassLabelById(props.type);
const linkableItems = computed(() => {
    const linkedItems = [
        ...props.propertyObjects.getReferencedObjects(props.parentId),
        ...props.sharedPropertyObjectStore.getReferencedObjects(props.parentId)
    ].flat();
    const linkable = props.sharedPropertyObjectStore
        .getObjectsByType(props.type)
        .filter((item: SharedPropertyObject) => !linkedItems.includes(item.id))
        .filter((item: SharedPropertyObject) => item.id != props.parentId);
    return linkable.length > 0
        ? linkable.map((item: SharedPropertyObject) => ({
              label: injectTemplate(props.projectProfiles.getLabelTemplateById(item.type), props.sharedPropertyObjectStore.get(item.id)),
              command: () => {
                  props.propertyObjects.addRef(props.parentId, item.id) || props.sharedPropertyObjectStore.addRef(props.parentId, item.id);
              }
          }))
        : [];
});

function createObject() {
    const newObject = new SharedPropertyObject(props.type);
    props.sharedPropertyObjectStore.add(newObject);
    props.propertyObjects.addRef(props.parentId, newObject.getId()) || props.sharedPropertyObjectStore.addRef(props.parentId, newObject.getId());

    if (props.isDialog) {
        emit("loadObject", newObject.getId());
    } else {
        dialog.open(PropertyDialog, {
            props: {
                header: "New item",
                style: {
                    "min-width": "50vw",
                    "max-width": "50vw",
                    height: "80vh"
                },
                breakpoints: {
                    "960px": "75vw",
                    "640px": "90vw"
                },
                modal: true,
                dismissableMask: true
            },
            data: {
                id: newObject.getId(),
                propertyObjects: props.propertyObjects,
                sharedPropertyObjectStore: props.sharedPropertyObjectStore,
                projectProfiles: props.projectProfiles
            }
        });
    }
}
</script>

<template>
    <SplitButton
        @click="() => createObject()"
        @contextmenu="(e: Event) => e.preventDefault()"
        :model="
            linkableItems.length
                ? linkableItems.sort((a: any, b: any) => (a.label > b.label ? 1 : b.label > a.label ? -1 : 0))
                : [{ label: `No linkable ${label}(s) available`, disabled: true }]
        "
        :pt="{ root: 'splitbutton' }"
    >
        <span :title="'Add new ' + label" class="capitalize text-nowrap">
            <i class="pi pi-plus text-xs capitalize"> </i>
            {{ label }}
        </span>
        <template #dropdownicon>
            <i class="pi pi-link" :title="'Link existing ' + label" />
        </template>
    </SplitButton>
</template>

<style scoped lang="scss">
.splitbutton {
    @apply h-6 border border-[#608f00] text-gray-600;
}

.splitbutton > *:first-child {
    @apply bg-[#eaffbe] [&:not(:hover)]:bg-opacity-40 border-0 px-2 text-inherit;
}

.splitbutton > *:not(:first-child) {
    @apply bg-[#eaffbe] [&:not(:hover)]:bg-opacity-40 border-0 border-l border-[#608f00] text-inherit;
}
</style>

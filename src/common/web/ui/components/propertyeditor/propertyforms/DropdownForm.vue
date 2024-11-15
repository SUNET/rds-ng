<script setup lang="ts">
import Dropdown from "primevue/dropdown";
import { computed, type PropType } from "vue";

import { ProjectObjectStore } from "../ProjectObjectStore";

const props = defineProps({
    propertyObjectId: { type: String, required: true },
    inputId: { type: String, required: true },
    projectObjects: { type: ProjectObjectStore, required: true },
    inputOptions: { type: Array as PropType<string[]>, required: true }
});

const value = computed(() => props.projectObjects.get(props.propertyObjectId)?.getValues() as Record<string, any>);
</script>

<template>
    <div class="flex">
        <Dropdown
            :modelValue="value[inputId]"
            @update:modelValue="(val: String[]) => projectObjects.update(inputId, propertyObjectId, val)"
            :options="inputOptions"
            class="grow"
            placeholder="Select"
            filter
            :pt="{
                panel: {
                    class: 'w-0'
                }
            }"
        />
    </div>
</template>

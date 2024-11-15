<script setup lang="ts">
import MultiSelect from "primevue/multiselect";
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
    <div>
        <MultiSelect
            v-model="value[inputId]"
            :options="inputOptions"
            class="w-full relative"
            @update:modelValue="(val: String[]) => projectObjects.update(inputId, propertyObjectId, val)"
        />
    </div>
</template>

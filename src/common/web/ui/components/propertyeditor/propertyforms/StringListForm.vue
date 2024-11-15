<script setup lang="ts">
import Chips from "primevue/chips";
import { computed } from "vue";

import { ProjectObjectStore } from "../ProjectObjectStore";

const props = defineProps({
    propertyObjectId: { type: String, required: true },
    inputId: { type: String, required: true },
    projectObjects: { type: ProjectObjectStore, required: true }
});

const value = computed(() => props.projectObjects.get(props.propertyObjectId)?.getValues() as Record<string, any>);
</script>

<template>
    <Chips
        @update:modelValue="(val) => projectObjects.update(inputId, propertyObjectId, val)"
        v-model="value[inputId]"
        separator=","
        class="inline"
        :addOnBlur="true"
        placeholder="Separate by comma"
    />
</template>

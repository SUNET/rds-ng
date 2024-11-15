<script setup lang="ts">
import Textarea from "primevue/textarea";
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
    <div>
        <Textarea @update:modelValue="(val) => projectObjects.update(inputId, propertyObjectId, val)" v-model="value[inputId]" autoResize class="w-full" />
    </div>
</template>

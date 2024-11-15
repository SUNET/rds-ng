<script setup lang="ts">
import InputText from "primevue/inputtext";
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
        <InputText type="text" v-model="value[inputId]" class="w-full" @update:modelValue="(val) => projectObjects.update(inputId, propertyObjectId, val)" />
    </div>
</template>

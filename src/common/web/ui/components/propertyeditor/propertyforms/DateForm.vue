<script setup lang="ts">
import Calendar from "primevue/calendar";
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
        <Calendar
            @date-select="(date: Date) => projectObjects.update(inputId, propertyObjectId, date)"
            dateFormat="dd/mm/yy"
            v-model="value[inputId]"
            class="w-full"
        />
    </div>
</template>

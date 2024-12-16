<script setup lang="ts">
import DatePicker from "primevue/datepicker";
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
        <DatePicker
            @date-select="(date: Date) => projectObjects.update(profileId || [], inputId, propertyObjectId, date)"
            dateFormat="dd/mm/yy"
            v-model="value[inputId]"
            class="w-full"
        />
    </div>
</template>

<script setup lang="ts">
import InputNumber, { type InputNumberInputEvent } from "primevue/inputnumber";
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
        <!-- 
            @update:modelValue on InputNumber is weird: https://github.com/primefaces/primevue/issues/506
         -->
        <InputNumber
            v-model="value[inputId]"
            :useGrouping="false"
            class="w-full"
            @input="(e: InputNumberInputEvent) => projectObjects.update(inputId, propertyObjectId, e.value)"
        />
    </div>
</template>

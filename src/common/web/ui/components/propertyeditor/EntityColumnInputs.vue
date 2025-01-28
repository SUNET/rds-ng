<script setup lang="ts">
import { propertyDataForms, PropertyDataType } from "./PropertyProfile";

const props = defineProps(["displayableInputs", "propertyClass", "propertyObject", "propertyObjects"]);
</script>

<template>
    <div v-for="input in displayableInputs" class="row-span-1">
        <span v-if="input.getLabel() !== propertyClass.getDisplayLabel()">{{ input.getLabel() }}</span>
        <component
            :is="propertyDataForms[input.getType() as PropertyDataType]"
            class="w-full"
            :propertyObjectId="propertyObject.getId()"
            :propertyObjects="propertyObjects"
            :inputId="input.getId()"
            :inputOptions="input.getOptions()"
        />
    </div>
</template>

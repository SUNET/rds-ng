<script setup lang="ts">
import { propertyDataForms, PropertyDataType } from "../PropertyProfile";

const props = defineProps(["displayableInputs", "propertyClass", "propertyObject", "propertyObjects", "isDialog"]);
</script>

<template>
    <div class="space-y-3">
        <div v-for="input in displayableInputs" class="row-span-1 space-y-0.5">
            <span v-if="input.getLabel() !== propertyClass.getDisplayLabel()" :class="{ 'font-bold': isDialog }">
                {{ input.getLabel() }}
            </span>
            <div v-if="isDialog && input.getLabel() !== propertyClass.getDisplayLabel()" class="r-text-gray">
                {{ input.getDescription() }}
            </div>
            <div v-if="isDialog && input.getExample()" v-html="`Example: ${input.getExample()}`" />
            <component
                :is="propertyDataForms[input.getType() as PropertyDataType]"
                class="w-full"
                :propertyObjectId="propertyObject.getId()"
                :propertyObjects="propertyObjects"
                :inputId="input.getId()"
                :inputOptions="input.getOptions()"
            />
        </div>
    </div>
</template>

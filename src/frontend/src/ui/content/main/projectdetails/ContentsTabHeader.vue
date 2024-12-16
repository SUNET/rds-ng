<script setup lang="ts">
import Popover from "primevue/popover";
import { ref, toRefs } from "vue";

const props = defineProps({
    title: {
        type: String,
        required: true
    },
    description: {
        type: String
    }
});
const { title, description } = toRefs(props);

const descriptionPopover = ref();
</script>

<template>
    {{ title }}
    <span
        v-if="description"
        :title="description"
        class="opacity-65"
        @click="
            (e) => {
                descriptionPopover.toggle(e);
                e.stopPropagation();
            }
        "
    >
        <i class="pi pi-question-circle ml-2 text-lg" />
        <Popover ref="descriptionPopover">{{ description }}</Popover>
    </span>
</template>

<style scoped lang="scss"></style>

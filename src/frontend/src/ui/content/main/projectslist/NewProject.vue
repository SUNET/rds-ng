<script setup lang="ts">
import Button from "primevue/button";

import { FrontendComponent } from "@/component/FrontendComponent";
import { useProjectTools } from "@/ui/tools/project/ProjectTools";

const comp = FrontendComponent.inject();
const { newProject } = useProjectTools(comp);
</script>

<template>
    <div>
        <Button
            class="w-full h-full text-xl hover:bg-orange-100 grid grid-flow-col place-content-center"
            label="New Project"
            icon="material-icons-outlined mi-add-circle-outline"
            icon-class="!text-4xl mr-2"
            severity="warn"
            @click="newProject"
            :pt="{ label: 'mr-auto' }"
            text
        />
    </div>
</template>

<style scoped lang="scss"></style>

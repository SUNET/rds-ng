<script setup lang="ts">
import { toRefs } from "vue";

import { useProjectsStore } from "@/data/stores/ProjectsStore";
import LandingPage from "@/ui/content/main/projectdetails/LandingPage.vue";

const { projects } = toRefs(useProjectsStore());
</script>

<template>
    <div class="r-centered-grid content-center r-shade-text">
        <div v-if="projects.length > 0">Select a project in the list on the left or create a new one using the <em>New Project</em> button.</div>
        <div v-else>
            <LandingPage />
        </div>
    </div>
</template>

<style scoped lang="scss"></style>

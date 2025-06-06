<script setup lang="ts">
import NewProject from "@/ui/content/main/projectslist/NewProject.vue";
import ProjectsListbox from "@/ui/content/main/projectslist/ProjectsListbox.vue";
</script>

<template>
    <div class="grid grid-rows-[1fr_4.5rem] grid-cols-1 bg-surface-50">
        <ProjectsListbox />
        <NewProject />
    </div>
</template>

<style scoped lang="scss"></style>

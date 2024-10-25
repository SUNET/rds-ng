<script setup lang="ts">
import Card from "primevue/card";

import ExternalLink from "@common/ui/components/misc/ExternalLink.vue";
</script>

<template>
    <div class="r-centered-grid">
        <div class="w-2/3">
            <div class="text-xl">
                <strong class="text-2xl">Welcome to sciebo Research Data Services (sciebo RDS)</strong> – Your flexible solution for research data managing and
                publishing. The services are designed to make data management effortless and collaborative, so you can focus on what matters most: your
                research.
            </div>
            <div>Here's how we support you:</div>
            <div>
                <ul class="pl-6">
                    <li class="flex items-center gap-1">
                        <span class="material-icons-outlined mi-hdr-strong" />
                        <strong>Configure research processes -</strong> A research data tool in your cloud that flexibly adapts to your individual research
                        workflows.
                    </li>
                    <li class="flex items-center gap-1">
                        <span class="material-icons-outlined mi-hdr-strong" />
                        <strong>Project Workflow Integration -</strong> A research data tool that connects existing research data services according to your
                        needs
                    </li>
                    <li class="flex items-center gap-1">
                        <span class="material-icons-outlined mi-hdr-strong" />
                        <strong>User Control -</strong> Full control over your data, with clear options to manage access, set metadata and conditions for
                        sharing.
                    </li>
                    <li class="flex items-center gap-1">
                        <span class="material-icons-outlined mi-hdr-strong" />
                        <strong>Ease of Use -</strong> Intuitive services that integrate smoothly into your daily research activities, saving you time and
                        effort.
                    </li>
                </ul>
            </div>
            <div>
                Learn more:
                <ExternalLink link="https://github.com/Sciebo-RDS" text="GitHub repository" />
            </div>
            <div>To get started immediately: Click on <strong>New project</strong>!</div>
            <div class="flex items-center gap-4 pt-8 place-self-center">
                <Card :pt="{ root: 'bg-slate-100 text-center w-64 h-48', content: 'pt-1 place-self-center' }">
                    <template #title>Step 1</template>
                    <template #content>
                        <span class="!text-4xl material-icons-outlined mi-hub pb-2" />
                        <p class="flex items-center gap-1 r-text-gray">Add repository connections.</p>
                    </template>
                </Card>

                <Card :pt="{ root: 'bg-slate-100 text-center w-64 h-48', content: 'pt-1 place-self-center' }">
                    <template #title>Step 2</template>
                    <template #content>
                        <span class="!text-4xl material-icons-outlined mi-add-circle-outline pb-2" />
                        <p class="flex items-center gap-1 r-text-gray">Create a new project.</p>
                    </template>
                </Card>

                <Card :pt="{ root: 'bg-slate-100 text-center w-64 h-48', content: 'pt-1 place-self-center' }">
                    <template #title>Step 3</template>
                    <template #content>
                        <span class="!text-4xl material-icons-outlined mi-file-copy pb-2" />
                        <p class="flex items-center gap-1 r-text-gray">Collect and manage data.</p>
                    </template>
                </Card>

                <Card :pt="{ root: 'bg-slate-100 text-center w-64 h-48', content: 'pt-1 place-self-center' }">
                    <template #title>Step 4</template>
                    <template #content>
                        <span class="!text-4xl material-icons-outlined mi-edit pb-2" />
                        <p class="flex items-center gap-1 r-text-gray">Edit metadata and annotations.</p>
                    </template>
                </Card>

                <Card :pt="{ root: 'bg-slate-100 text-center w-64 h-48', content: 'pt-1 place-self-center' }">
                    <template #title>Step 5</template>
                    <template #content>
                        <span class="!text-4xl material-icons-outlined mi-move-down pb-2" />
                        <p class="flex items-center gap-1 r-text-gray">Finish project and transfer data to other services.</p>
                    </template>
                </Card>
            </div>
        </div>
    </div>
</template>

<style scoped lang="scss">
div {
    @apply pb-4;
}
</style>

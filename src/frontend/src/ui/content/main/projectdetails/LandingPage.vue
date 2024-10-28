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
            <div class="text-lg">Here's how we support you:</div>
            <div>
                <ul class="pl-6">
                    <li class="flex items-center gap-1">
                        &#x2022;
                        <strong>Configure research processes -</strong> A research data tool in your cloud that flexibly adapts to your individual research
                        workflows.
                    </li>
                    <li class="flex items-center gap-1">
                        &#x2022;
                        <strong>Project Workflow Integration -</strong> A research data tool that connects existing research data services according to your
                        needs
                    </li>
                    <li class="flex items-center gap-1">
                        &#x2022;
                        <strong>User Control -</strong> Full control over your data, with clear options to manage access, set metadata and conditions for
                        sharing.
                    </li>
                    <li class="flex items-center gap-1">
                        &#x2022;
                        <strong>Ease of Use -</strong> Intuitive services that integrate smoothly into your daily research activities, saving you time and
                        effort.
                    </li>
                </ul>
            </div>
            <div class="pl-6">
                Learn more:
                <ExternalLink link="https://github.com/Sciebo-RDS" text="GitHub repository" />
            </div>
            <div class="pt-4 text-lg">To get started, simply follow these steps:</div>
            <div>
                <div class="flex items-center gap-4 pt-8 place-self-center">
                    <Card :pt="{ root: 'bg-slate-100 text-center w-64 h-48', content: 'pt-1 place-self-center' }">
                        <template #title>Initial setup</template>
                        <template #content>
                            <span class="!text-4xl material-icons-outlined mi-settings pb-2" />
                            <p class="flex items-center gap-1 r-text-gray">Add repository connections</p>
                        </template>
                    </Card>
                </div>

                <div class="flex items-center gap-4 pt-2 place-self-center">
                    <Card :pt="{ root: 'bg-slate-200 text-center w-64 h-48', content: 'pt-1 place-self-center' }">
                        <template #title>Step 1</template>
                        <template #content>
                            <span class="!text-4xl material-icons-outlined mi-add-circle-outline pb-2" />
                            <p class="flex items-center gap-1 r-text-gray">Create new project</p>
                        </template>
                    </Card>

                    <Card :pt="{ root: 'bg-slate-200 text-center w-64 h-48', content: 'pt-1 place-self-center' }">
                        <template #title>Step 2</template>
                        <template #content>
                            <span class="!text-4xl material-icons-outlined mi-file-copy pb-2" />
                            <p class="flex items-center gap-1 r-text-gray">Collect &amp; manage data</p>
                        </template>
                    </Card>

                    <Card :pt="{ root: 'bg-slate-200 text-center w-64 h-48', content: 'pt-1 place-self-center' }">
                        <template #title>Step 3</template>
                        <template #content>
                            <span class="!text-4xl material-icons-outlined mi-edit pb-2" />
                            <p class="flex items-center gap-1 r-text-gray">Edit metadata &amp; annotations</p>
                        </template>
                    </Card>

                    <Card :pt="{ root: 'bg-slate-200 text-center w-64 h-48', content: 'pt-1 place-self-center' }">
                        <template #title>Step 4</template>
                        <template #content>
                            <span class="!text-4xl material-icons-outlined mi-rocket-launch pb-2" />
                            <p class="flex items-center gap-1 r-text-gray">Finish project &amp; submit data</p>
                        </template>
                    </Card>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped lang="scss">
div {
    @apply pb-4;
}
</style>

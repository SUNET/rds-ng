<script setup lang="ts">
import Card from "primevue/card";

import ExternalLink from "@common/ui/components/misc/ExternalLink.vue";
</script>

<template>
    <div>
        <div class="content-center r-shade-text m-10">
            <div class="grid grid-cols-2 min-w-full min-h-full place-content-start gap-24">
                <div class="space-y-8">
                    <div>
                        <div class="text font-light uppercase">Sciebo Research Data Services</div>
                        <div class="text-5xl font-black uppercase leading-none">Research data <span class="font-thin text-nowrap">made easy</span></div>
                    </div>
                    <div class="text-xl font-light mb-10">
                        Your flexible solution for research data managing and publishing. The services are designed to make data management effortless and
                        collaborative, so you can focus on what matters most: your research.
                        <div class="pt-2 text-lg">
                            Learn more:
                            <ExternalLink link="https://github.com/Sciebo-RDS" text="GitHub repository" />
                        </div>
                    </div>
                    <Card class="p-6">
                        <template #content>
                            <div class="grid justify-items-center">
                                <img src="@assets/img/rds-steps-web.png" class="w-full" alt="Steps"/>
                            </div>
                        </template>
                    </Card>
                </div>
                <!-- ... -->
                <div class="grid place-items-start space-y-7">
                    <img src="@assets/img/landing_image.png" class="w-[25rem]" alt="Image" />
                    <Card class="w-[30rem]">
                        <template #title>
                            <div class="">Here's how we support you</div>
                        </template>
                        <template #content>
                            <ul class="pl-6 list-outside list-disc">
                                <li class="">
                                    <strong>Configure research processes -</strong> A research data tool in your cloud that flexibly adapts to your individual
                                    research workflows.
                                </li>
                                <li class="">
                                    <strong>Project Workflow Integration -</strong> A research data tool that connects existing research data services according
                                    to your needs.
                                </li>
                                <li class="">
                                    <strong>User Control -</strong> Full control over your data, with clear options to manage access, set metadata and
                                    conditions for sharing.
                                </li>
                                <li class="">
                                    <strong>Ease of Use -</strong> Intuitive services that integrate smoothly into your daily research activities, saving you
                                    time and effort.
                                </li>
                            </ul>
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

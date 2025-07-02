<script setup lang="ts">
import Card from "primevue/card";

import ExternalLink from "@common/ui/components/misc/ExternalLink.vue";

import { FrontendComponent } from "@/component/FrontendComponent.ts";

const comp = FrontendComponent.inject();
</script>

<template>
    <div class="grid grid-cols-[auto_1fr] gap-20 r-shade-text pt-5">
        <div class="flex flex-col items-center gap-y-2 text-sm">
            <img src="@assets/img/rds_ng-octopus-blue.png" alt="logo" class="w-[30rem]" />
            <Card class="w-[22rem] bg-primary-100 text-primary !p-0" :pt="{ title: '!text-base', body: 'p-3 px-5' }">
                <template #title>
                    <div class="flex items-center gap-1">
                        <span class="material-icons-outlined mi-construction !text-xl" />
                        <span class="">This is a beta version!</span>
                    </div>
                </template>
                <template #content>
                    <span class="text-sm">
                        If you encounter any issues or have other kinds of feedback, feel free to
                        <ExternalLink link="mailto:sciebo.rds@uni-muenster.de" text="send us an email" />
                        !
                    </span>
                </template>
            </Card>
        </div>
        <div class="flex flex-col max-w-[35rem]">
            <div class="text-4xl font-bold mt-10">Hello, I'm {{ comp.data.title }}!</div>
            <div class="text-xl font-bold">Your assistent for easy and secure research data sharing.</div>
            <div>&nbsp;</div>
            <div>I'm here to help you manage, prepare, and share your research data - flexibly, securely, and in line with your workflows.</div>
            <div>My goal: making your data handling easier and safe, so you can stay focused on your research.</div>
            <div>&nbsp;</div>
            <div>
                <img src="@assets/img/landing-steps.png" class="w-full h-full pr-8" alt="Steps" />
            </div>
        </div>
    </div>
</template>

<style scoped lang="scss">
div {
    @apply pb-4;
}
</style>

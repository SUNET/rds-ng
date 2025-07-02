<script setup lang="ts">
import Card from "primevue/card";

import ExternalLink from "@common/ui/components/misc/ExternalLink.vue";

import { FrontendComponent } from "@/component/FrontendComponent.ts";

const comp = FrontendComponent.inject();
</script>

<template>
    <div class="grid grid-cols-[auto_1fr] gap-x-20 gap-y-0 r-shade-text px-5">
        <div class="flex flex-col items-center gap-y-2 text-sm">
            <img src="@assets/img/rds_ng-octopus-blue.png" alt="logo" class="w-[30rem]" />
        </div>
        <div class="flex flex-col">
            <div class="text-4xl font-bold mt-10">Hello, I'm {{ comp.data.title }}!</div>
            <div class="text-xl font-bold">Your assistent for easy and secure research data sharing.</div>
            <div>&nbsp;</div>
            <div>I'm here to help you manage, prepare, and share your research data - flexibly, securely, and in line with your workflows.</div>
            <div>My goal: making your data handling easier and safe, so you can stay focused on your research.</div>
            <Card class="bg-primary-100 text-primary !p-0 mt-4" :pt="{ title: '!text-base', caption: 'h-5', body: 'p-3 px-5' }">
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
        <div class="col-span-2">
            <img src="@assets/img/landing-steps.png" class="w-[100rem] h-full pr-2" alt="Steps" />
        </div>
    </div>
</template>

<style scoped lang="scss">
div {
    @apply pb-4;
}
</style>

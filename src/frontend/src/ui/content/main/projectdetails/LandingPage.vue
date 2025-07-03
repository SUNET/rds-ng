<script setup lang="ts">
import Card from "primevue/card";

import ExternalLink from "@common/ui/components/misc/ExternalLink.vue";

import { FrontendComponent } from "@/component/FrontendComponent.ts";

const comp = FrontendComponent.inject();
</script>

<template>
    <div class="grid grid-rows-2 r-shade-text mx-14 max-w-[85rem]">
        <div class="flex flex-row">
            <div class="flex flex-col ml-auto">
                <div class="text-3xl font-bold mt-12">Hello, I'm {{ comp.data.title }}!</div>
                <div class="text-lg font-bold">Your assistent for easy and secure research data sharing.</div>
                <div>&nbsp;</div>
                <div>I'm here to help you manage, prepare, and share your research data - flexibly, securely, and in line with your workflows.</div>
                <div>My goal: making your data handling easier and safe, so you can stay focused on your research.</div>
                <Card class="bg-amber-100 text-amber-700 !p-0 mt-4" :pt="{ title: '!text-base', caption: 'h-5', body: 'p-3 px-5' }">
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
            <div class="mr-auto">
                <img src="@assets/img/rds_ng-octopus-blue.png" alt="logo" class="w-[28rem]" />
            </div>
        </div>

        <div class="mr-6">
            <img src="@assets/img/landing-steps.svg" class="w-[92%] justify-self-center self-center" alt="First steps" />
        </div>
    </div>
</template>

<style scoped lang="scss">
div {
    @apply pb-4;
}
</style>

<script setup lang="ts">
import { storeToRefs } from "pinia";
import Message from "primevue/message";
import ScrollPanel from "primevue/scrollpanel";
import { ref } from "vue";

import { Project } from "@common/data/entities/project/Project";
import { useExtendedDialogTools } from "@common/ui/dialogs/ExtendedDialogTools";

import { useUserStore } from "@/data/stores/UserStore";

import UploadConnectionsList from "@/ui/dialogs/project/upload/UploadConnectionsList.vue";

const { dialogData } = useExtendedDialogTools();

const project = ref<Project>(dialogData.userData.project);
const userStore = useUserStore();
const { userSettings } = storeToRefs(userStore);
</script>

<template>
    <div class="grid grid-rows-[min-content_1fr] gap-1.5 w-full h-full">
        <Message v-if="userSettings.connector_instances.length == 0" severity="warn" :closable="false" class="pb-1">
            <div>
                To upload your project, add at least one connection to an external service in your settings
                <span class="material-icons-outlined mi-settings relative top-1.5" />.
            </div>
        </Message>
        <div v-else class="mb-2">To upload your project to an external service, click on its corresponding button.</div>

        <ScrollPanel class="h-[calc(60vh-3rem)] min-h-[33rem]">
            <UploadConnectionsList :project="project" :user-settings="userSettings" />
        </ScrollPanel>
    </div>
</template>

<style scoped lang="scss"></style>

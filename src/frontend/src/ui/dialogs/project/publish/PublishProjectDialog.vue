<script setup lang="ts">
import { storeToRefs } from "pinia";
import Message from "primevue/message";
import ScrollPanel from "primevue/scrollpanel";
import { ref } from "vue";

import { Project } from "@common/data/entities/project/Project";
import { useExtendedDialogTools } from "@common/ui/dialogs/ExtendedDialogTools";

import { useUserStore } from "@/data/stores/UserStore";

import PublishConnectionsList from "@/ui/dialogs/project/publish/PublishConnectionsList.vue";

const { dialogData } = useExtendedDialogTools();

const project = ref<Project>(dialogData.userData.project);
const userStore = useUserStore();
const { userSettings } = storeToRefs(userStore);
</script>

<template>
    <div class="grid grid-rows-[min-content_1fr] gap-1.5 w-full h-full">
        <Message v-if="userSettings.connector_instances.length == 0" severity="warn" :closable="false" class="pb-1">
            <div>
                To publish or export, add at least one connection to an external service in your settings
                <span class="material-icons-outlined mi-settings relative top-1.5" />.
            </div>
        </Message>
        <div v-else class="mb-2">To publish or export a project to a service, click on its corresponding button.</div>

        <ScrollPanel class="h-[61rem]">
            <PublishConnectionsList :project="project" :user-settings="userSettings" />
        </ScrollPanel>
    </div>
</template>

<style scoped lang="scss"></style>

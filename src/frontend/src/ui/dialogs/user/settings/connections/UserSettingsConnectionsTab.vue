<script setup lang="ts">
import { storeToRefs } from "pinia";
import ScrollPanel from "primevue/scrollpanel";
import { type PropType, toRefs, unref } from "vue";

import { FrontendComponent } from "@/component/FrontendComponent";
import { useConnectorsStore } from "@/data/stores/ConnectorsStore";
import { useUserStore } from "@/data/stores/UserStore";

import { useConnectorInstancesTools } from "@/ui/tools/connector/ConnectorInstancesTools";
import { useUserTools } from "@/ui/tools/user/UserTools";

import { ConnectorInstance } from "@common/data/entities/connector/ConnectorInstance";
import { findConnectorByID } from "@common/data/entities/connector/ConnectorUtils";
import { UserSettings } from "@common/data/entities/user/UserSettings";

import ConnectorInstancesList from "@/ui/components/connector/ConnectorInstancesList.vue";
import ConnectorInstancesListItem from "@/ui/dialogs/user/settings/connections/ConnectorInstancesListItem.vue";
import NewConnectorInstance from "@/ui/dialogs/user/settings/connections/NewConnectorInstance.vue";

const comp = FrontendComponent.inject();
const props = defineProps({
    tabData: {
        type: Object as PropType<UserSettings>,
        required: true
    }
});
const { tabData: userSettings } = toRefs(props);

const consStore = useConnectorsStore();
const userStore = useUserStore();
const { connectors } = storeToRefs(consStore);
const { userAuthorizations } = storeToRefs(userStore);

const { editInstance, deleteInstance, requestInstanceAuthorization, revokeInstanceAuthorization } = useConnectorInstancesTools(comp);
const { saveUserSettings } = useUserTools(comp);

function onCreateInstance(instance: ConnectorInstance): void {
    saveUserSettings(unref(userSettings)!);
}

function onEditInstance(instance: ConnectorInstance): void {
    editInstance(unref(userSettings)!.connector_instances, instance, findConnectorByID(unref(connectors), instance.connector_id)).then(() => {
        saveUserSettings(unref(userSettings)!);
    });
}

function onDeleteInstance(instance: ConnectorInstance) {
    deleteInstance(unref(userSettings)!.connector_instances, instance);
    saveUserSettings(unref(userSettings)!);
}
</script>

<template>
    <div class="grid grid-rows-[auto_auto_1fr_auto] grid-cols-1 gap-1.5 w-full h-full">
        <div class="r-text-title">Connections</div>
        <div>
            To publish your project or export its data to an external service, you need to set up <em>connections</em> to these services. To add a new
            connection, use the drop-down list at the bottom of the connections list.
        </div>

        <ScrollPanel class="h-[29rem]">
            <ConnectorInstancesList :instances="userSettings.connector_instances" :connectors="connectors">
                <template #instance="slotProps">
                    <ConnectorInstancesListItem
                        :instance="slotProps.instance"
                        @authorize-instance="requestInstanceAuthorization(slotProps.instance, connectors, userAuthorizations)"
                        @unauthorize-instance="revokeInstanceAuthorization(slotProps.instance)"
                        @dblclick="onEditInstance(slotProps.instance)"
                        @edit-instance="onEditInstance(slotProps.instance)"
                        @delete-instance="onDeleteInstance(slotProps.instance)"
                    />
                </template>
            </ConnectorInstancesList>
        </ScrollPanel>
        <NewConnectorInstance :user-settings="userSettings" @create-instance="onCreateInstance" />
    </div>
</template>

<style scoped lang="scss"></style>

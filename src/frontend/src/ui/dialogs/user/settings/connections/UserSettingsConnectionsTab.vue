<script setup lang="ts">
import { storeToRefs } from "pinia";
import { type PropType, ref, toRefs, unref } from "vue";

import { ConnectorInstance, type ConnectorInstanceID } from "@common/data/entities/connector/ConnectorInstance";
import { UserSettings } from "@common/data/entities/user/UserSettings";

import { FrontendComponent } from "@/component/FrontendComponent";
import { useUserTools } from "@/ui/tools/user/UserTools";

import { useConnectorsStore } from "@/data/stores/ConnectorsStore";

import ConnectorInstancesList from "@/ui/components/connector/ConnectorInstancesList.vue";
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
const { connectors } = storeToRefs(consStore);

const { saveUserSettings } = useUserTools(comp);

const selectedConnectorInstance = ref<ConnectorInstanceID | undefined>();

function onCreateInstance(instance: ConnectorInstance): void {
    saveUserSettings(unref(userSettings)!);

    selectedConnectorInstance.value = instance.instance_id;
}
</script>

<template>
    <div class="grid grid-rows-[auto_auto_1fr_auto] grid-cols-1 gap-1.5 w-full h-full">
        <div class="r-text-title">Connections</div>
        <div>
            To publish your project or export its data to an external service, you need to set up <em>connections</em> to these services. To add a new
            connection, use the drop-down list at the bottom of the connections list.
        </div>

        <ScrollPanel class="overflow-y-auto h-[27rem]">
            <ConnectorInstancesList :instances="userSettings.connector_instances" :connectors="connectors" />
        </ScrollPanel>
        <NewConnectorInstance :user-settings="userSettings" @create-instance="onCreateInstance" />
    </div>
</template>

<style scoped lang="scss"></style>

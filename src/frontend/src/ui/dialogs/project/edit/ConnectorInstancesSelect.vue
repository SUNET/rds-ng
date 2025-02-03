<script setup lang="ts">
import { storeToRefs } from "pinia";
import Checkbox from "primevue/checkbox";
import ScrollPanel from "primevue/scrollpanel";
import { computed, toRefs } from "vue";

import { groupConnectorInstances } from "@common/data/entities/connector/ConnectorInstanceUtils";

import { useConnectorsStore } from "@/data/stores/ConnectorsStore";
import { useUserStore } from "@/data/stores/UserStore";

import ConnectorInstancesHeader from "@/ui/components/connector/ConnectorInstancesHeader.vue";

const consStore = useConnectorsStore();
const userStore = useUserStore();
const props = defineProps({
    disabled: {
        type: Boolean,
        default: false
    }
});
const { connectors } = storeToRefs(consStore);
const { userSettings } = storeToRefs(userStore);
const { disabled } = toRefs(props);

const groupedInstances = computed(() => groupConnectorInstances(userSettings.value.connector_instances, connectors.value));
const model = defineModel({ default: [] });
</script>

<template>
    <ScrollPanel>
        <div v-for="group of groupedInstances" :class="{ 'p-disabled': disabled }">
            <ConnectorInstancesHeader :connector-id="group.connectorID" class="r-shade-dark rounded list-entry h-11" />

            <div v-for="instance of group.connectorInstances" :key="instance.instance_id" class="flex align-items-center list-entry !py-1">
                <Checkbox v-model="model" :inputId="instance.instance_id" :value="instance.instance_id" :disabled="disabled" size="large" class="self-center" />
                <label :for="instance.instance_id" class="pl-1.5">{{ instance.name }}</label>
            </div>
        </div>
    </ScrollPanel>
</template>

<style scoped lang="scss">
.list-entry {
    @apply p-0.5 pl-2;
}
</style>

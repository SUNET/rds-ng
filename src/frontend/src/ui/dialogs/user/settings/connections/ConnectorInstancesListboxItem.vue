<script setup lang="ts">
import { storeToRefs } from "pinia";
import Button from "primevue/button";
import Menu from "primevue/menu";
import Tag from "primevue/tag";
import { computed, type PropType, ref, toRefs, unref, watch } from "vue";

import { ConnectorInstance } from "@common/data/entities/connector/ConnectorInstance";
import { connectorInstanceIsAuthorized } from "@common/data/entities/connector/ConnectorInstanceUtils";
import { connectorRequiresAuthorization, findConnectorByID } from "@common/data/entities/connector/ConnectorUtils";

import { useConnectorsStore } from "@/data/stores/ConnectorsStore";
import { useUserStore } from "@/data/stores/UserStore";

const consStore = useConnectorsStore();
const userStore = useUserStore();
const props = defineProps({
    instance: {
        type: Object as PropType<ConnectorInstance>,
        required: true
    },
    isSelected: {
        type: Boolean,
        default: false
    }
});
const emits = defineEmits<{
    (e: "authorize-instance", instance: ConnectorInstance): void;
    (e: "unauthorize-instance", instance: ConnectorInstance): void;
    (e: "edit-instance", instance: ConnectorInstance): void;
    (e: "delete-instance", instance: ConnectorInstance): void;
}>();

const { instance, isSelected } = toRefs(props);
const { userAuthorizations } = storeToRefs(userStore);

const connector = computed(() => findConnectorByID(consStore.connectors, instance.value.connector_id));
const requiresAuthorization = computed(() => (!!unref(connector) ? connectorRequiresAuthorization(unref(connector)!) : false));
const isAuthorized = computed(() => connectorInstanceIsAuthorized(unref(instance)!, unref(userAuthorizations)));
const isUnAuthorizing = ref(false);

const editMenu = ref();
const editMenuItems = computed(() => {
    const menuItems = {
        label: "Edit connection",
        items: [] as Record<any, any>[]
    };

    if (unref(requiresAuthorization)) {
        if (unref(isAuthorized)) {
            menuItems.items.push({
                label: () => (unref(isUnAuthorizing) ? `Disconnecting from ${unref(instance).name}...` : `Disconnect from ${unref(instance).name}`),
                icon: "material-icons-outlined mi-link-off",
                disabled: () => unref(isUnAuthorizing),
                command: onUnauthorize
            });
        } else {
            menuItems.items.push({
                label: () => (unref(isUnAuthorizing) ? `Connecting to ${unref(instance).name}...` : `Connect to ${unref(instance).name}`),
                icon: "material-icons-outlined mi-link",
                disabled: () => unref(isUnAuthorizing),
                command: onAuthorize
            });
        }
    }

    menuItems.items.push(
        {
            label: "Connection settings",
            icon: "material-icons-outlined mi-settings",
            command: () => emits("edit-instance", unref(instance)!)
        },
        { separator: true },
        {
            label: "Delete connection",
            icon: "material-icons-outlined mi-delete-forever",
            class: "r-text-error",
            command: () => emits("delete-instance", unref(instance)!)
        }
    );

    return [menuItems];
});
const editMenuShown = ref(false);

function onAuthorize(): void {
    isUnAuthorizing.value = true;
    emits("authorize-instance", unref(instance)!);
}

function onUnauthorize(): void {
    isUnAuthorizing.value = true;
    emits("unauthorize-instance", unref(instance)!);
}

// Whenever any authorization state changes, any pending (un)authorizations have completed
watch(userAuthorizations, () => {
    isUnAuthorizing.value = false;
});
</script>

<template>
    <div class="grid grid-rows-auto grid-cols-[min-content_1fr_min-content] grid-flow-row gap-0 place-content-start group w-full">
        <div v-if="requiresAuthorization" class="row-span-3 pt-1 pr-2.5">
            <Tag :severity="isAuthorized ? 'success' : 'danger'" :title="isAuthorized ? 'Connected' : 'Not connected'" class="w-10 h-10 rounded-full">
                <span class="material-icons-outlined" :class="isAuthorized ? 'mi-power' : 'mi-power-off'" />
            </Tag>
        </div>
        <div v-else class="row-span-3" />

        <div :id="'connector-instance-' + instance!.instance_id" class="r-text-caption h-6 truncate" :title="instance!.name">{{ instance!.name }}</div>

        <div class="row-span-2 pl-1">
            <Button
                text
                rounded
                size="small"
                aria-label="Options"
                title="More options"
                :class="{ invisible: !editMenuShown, 'group-hover:visible': true }"
                @click="(event) => editMenu.toggle(event)"
            >
                <template #icon>
                    <span class="material-icons-outlined mi-more-vert" :class="[isSelected ? 'r-highlight-text' : 'r-text']" style="font-size: 32px" />
                </template>
            </Button>
            <Menu
                ref="editMenu"
                :model="editMenuItems"
                :base-z-index="Number.MAX_SAFE_INTEGER"
                popup
                @focus="editMenuShown = true"
                @blur="editMenuShown = false"
            />
        </div>

        <div class="truncate" :title="instance!.description">{{ instance!.description }}</div>

        <div v-if="requiresAuthorization" class="col-span-3 place-self-end mt-1">
            <Button
                v-if="isAuthorized"
                :label="isUnAuthorizing ? 'Disconnecting...' : 'Disconnect'"
                severity="warn"
                size="small"
                rounded
                icon="material-icons-outlined mi-link-off"
                class="r-button-small !min-h-10"
                :loading="isUnAuthorizing"
                @click="onUnauthorize"
            />
            <Button
                v-else
                :label="isUnAuthorizing ? 'Connecting...' : 'Connect'"
                severity="info"
                size="small"
                rounded
                icon="material-icons-outlined mi-link"
                class="r-button-small !min-h-10"
                :loading="isUnAuthorizing"
                @click="onAuthorize"
            />
        </div>
        <div v-else class="col-span-3 place-self-end">&nbsp;</div>
    </div>
</template>

<style scoped lang="scss"></style>

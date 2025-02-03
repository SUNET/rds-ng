<script setup lang="ts">
import Accordion from "primevue/accordion";
import AccordionContent from "primevue/accordioncontent";
import AccordionHeader from "primevue/accordionheader";
import AccordionPanel from "primevue/accordionpanel";
import { computed, type PropType, toRefs, unref } from "vue";

import { Connector } from "@common/data/entities/connector/Connector";
import { ConnectorInstance } from "@common/data/entities/connector/ConnectorInstance";
import { groupConnectorInstances } from "@common/data/entities/connector/ConnectorInstanceUtils";

import ConnectorInstancesHeader from "@/ui/components/connector/ConnectorInstancesHeader.vue";

const props = defineProps({
    connectors: {
        type: Object as PropType<Connector[]>,
        required: true
    },
    instances: {
        type: Object as PropType<ConnectorInstance[]>,
        required: true
    }
});
const { connectors, instances } = toRefs(props);

const groupedInstances = computed(() => groupConnectorInstances(unref(instances), unref(connectors)));
</script>

<template>
    <Accordion :value="groupedInstances.map((inst) => inst.connectorID)" multiple>
        <AccordionPanel v-for="group in groupedInstances" :key="group.connectorID" :value="group.connectorID">
            <AccordionHeader class="pl-0">
                <ConnectorInstancesHeader :connector-id="group.connectorID" />
            </AccordionHeader>
            <AccordionContent>
                <div v-for="instance in group.connectorInstances" class="pl-0">
                    <slot name="instance" :instance="instance" />
                </div>
            </AccordionContent>
        </AccordionPanel>
    </Accordion>
</template>

<style scoped lang="scss"></style>

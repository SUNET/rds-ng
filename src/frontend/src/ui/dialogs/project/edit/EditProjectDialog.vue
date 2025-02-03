<script setup lang="ts">
import { Form } from "@primevue/forms";
import Checkbox from "primevue/checkbox";
import Fieldset from "primevue/fieldset";
import IftaLabel from "primevue/iftalabel";
import InputText from "primevue/inputtext";
import ScrollPanel from "primevue/scrollpanel";
import Stepper from "primevue/stepper";
import StepList from "primevue/steplist";
import StepPanels from "primevue/steppanels";
import Step from "primevue/step";
import StepPanel from "primevue/steppanel";
import Textarea from "primevue/textarea";
import ToggleSwitch from "primevue/toggleswitch";
import { computed, onMounted, ref, unref, watch } from "vue";
import * as yup from "yup";

import { ListResourcesReply } from "@common/api/resource/ResourceCommands";
import { resourcesListToTreeNodes } from "@common/data/entities/resource/ResourceUtils";
import { useExtendedDialogTools } from "@common/ui/dialogs/ExtendedDialogTools";
import { useDirectives } from "@common/ui/Directives";

import MandatoryMark from "@common/ui/components/misc/MandatoryMark.vue";
import ResourcesTree from "@common/ui/components/resource/ResourcesTree.vue";
import StepIconHeader from "@common/ui/components/stepper/StepIconHeader.vue";

import { FrontendComponent } from "@/component/FrontendComponent";
import { type UIOptions } from "@/data/entities/ui/UIOptions";
import { ListResourcesAction } from "@/ui/actions/resource/ListResourcesAction";
import { SnapInsCatalog } from "@/ui/snapins/SnapInsCatalog";

import ConnectorInstancesSelect from "@/ui/dialogs/project/edit/ConnectorInstancesSelect.vue";
import EditProjectDialogFooter from "@/ui/dialogs/project/edit/EditProjectDialogFooter.vue";

const { dialogData, acceptDialog, useValidator } = useExtendedDialogTools();
const { vFocus } = useDirectives();

const comp = FrontendComponent.inject();
const optSnapIns = SnapInsCatalog.allOptionals();
const uiOptions = ref<UIOptions>(dialogData.userData.options.ui);
const showDataPathSelector = dialogData.options["showDataPathSelector"];
const newProject = dialogData.userData.newProject;

const stepIndices = {
    main: 0,
    datapath: 1,
    features: 2,
    connections: 3
};
const lastStepIndex = Object.entries(stepIndices).length - 1;
const activeStep = ref(stepIndices.main);

const form = ref();
const validator = useValidator(form, {
    title: yup.string().trim().required().label("Title").default(dialogData.userData.title),
    description: yup.string().label("Description").default(dialogData.userData.description),
    datapath: yup
        .string()
        .test("datapath-not-empty", "No data path selected", (_, ctx) => {
            if (dialogData.userData.datapath == "") {
                return ctx.createError({ path: "datapath" });
            }
            return true;
        })
        .label("Data path")
        .default(dialogData.userData.datapath)
});

const resourcesNodes = ref<Object[]>([]);
const resourcesError = ref("");
onMounted(() => {
    if (showDataPathSelector) {
        const action = new ListResourcesAction(comp, true);
        action
            .prepare("", true, false)
            .done((reply: ListResourcesReply, success, msg) => {
                if (success) {
                    resourcesNodes.value = resourcesListToTreeNodes(reply.resources, true);
                }
            })
            .failed((_, msg) => {
                resourcesError.value = "Unable to load resources";
            });
        action.execute();
    }
});

// Reflect selected features based on snap-ins with associated project features
watch(
    () => uiOptions.value.optional_snapins,
    (snapIns) => {
        dialogData.userData.options.optional_features = SnapInsCatalog.filter(
            (snapIn) => snapIns.includes(snapIn.snapInID) && !!snapIn.options.optional?.feature
        ).map((snapIn) => snapIn.options.optional!.feature);
    }
);

const prevCallback = computed(() => {
    if (unref(activeStep) == stepIndices.main) {
        return undefined;
    } else {
        return onPrevStep;
    }
});
const nextCallback = computed(() => {
    if (unref(activeStep) >= lastStepIndex) {
        return acceptDialog;
    } else {
        // Verify each step to prevent advancing to the next one
        if (unref(activeStep) == stepIndices.main) {
            if (validator.hasError("title")) {
                return undefined;
            }
        } else if (unref(activeStep) == stepIndices.datapath) {
            if (validator.hasError("datapath")) {
                return undefined;
            }
        }

        return onNextStep;
    }
});
const nextName = computed(() => {
    if (unref(activeStep) >= lastStepIndex) {
        return newProject ? "Create" : "Save";
    } else {
        return undefined;
    }
});

function onClickStep(event: Event, callback: (event: Event) => void) {
    validator
        .validate()
        .then(() => {
            if (callback) {
                callback(event);
            }
        })
        .catch(() => {});
}

function onPrevStep() {
    activeStep.value -= 1;
}

function onNextStep() {
    activeStep.value += 1;
}
</script>

<template>
    <Form
        ref="form"
        :resolver="validator.resolver"
        validate-on-mount
        @submit="!newProject ? acceptDialog : undefined"
        :class="[{ 'h-[calc(100%-4rem)]': newProject }, 'r-form']"
    >
        <Stepper v-model:value="activeStep" :linear="newProject" :dt="!newProject ? { 'separator.activeBackground': '{content.border.color}' } : {}">
            <StepList>
                <Step v-slot="{ activateCallback }" :value="stepIndices.main" :pt="{ number: 'hidden' }">
                    <StepIconHeader
                        :active="newProject ? stepIndices.main <= activeStep : stepIndices.main == activeStep"
                        :click-callback="(event: Event) => onClickStep(event, activateCallback)"
                        icon="mi-edit"
                        title="Main settings"
                    />
                </Step>

                <Step v-slot="{ activateCallback }" :value="stepIndices.datapath" :pt="{ number: 'hidden' }">
                    <StepIconHeader
                        :active="newProject ? stepIndices.datapath <= activeStep : stepIndices.datapath == activeStep"
                        :click-callback="(event: Event) => onClickStep(event, activateCallback)"
                        icon="mi-folder"
                        title="Data path"
                    />
                </Step>

                <Step v-slot="{ activateCallback }" :value="stepIndices.features" :pt="{ number: 'hidden' }">
                    <StepIconHeader
                        :active="newProject ? stepIndices.features <= activeStep : stepIndices.features == activeStep"
                        :click-callback="(event: Event) => onClickStep(event, activateCallback)"
                        icon="mi-checklist"
                        title="Features"
                    />
                </Step>

                <Step v-slot="{ activateCallback }" :value="stepIndices.connections" :pt="{ number: 'hidden' }">
                    <StepIconHeader
                        :active="newProject ? stepIndices.connections <= activeStep : stepIndices.connections == activeStep"
                        :click-callback="(event: Event) => onClickStep(event, activateCallback)"
                        icon="mi-hub"
                        title="Connections"
                    />
                </Step>
            </StepList>
            <StepPanels>
                <StepPanel :value="stepIndices.main">
                    <div class="mb-2">Set your main project settings, like its title, here. You can always change these later.</div>

                    <Fieldset legend="General settings" class="r-form-fieldset">
                        <span class="r-form-field">
                            <IftaLabel>
                                <label>Title <MandatoryMark /></label>
                                <InputText name="title" v-model="dialogData.userData.title" fluid v-focus />
                            </IftaLabel>
                            <small>The title of the project.</small>
                        </span>

                        <span class="r-form-field mt-5">
                            <IftaLabel class="mb-[-0.5rem]">
                                <label>Description</label>
                                <Textarea name="description" v-model="dialogData.userData.description" rows="3" fluid />
                            </IftaLabel>
                            <small>An (optional) project description.</small>
                        </span>
                    </Fieldset>
                </StepPanel>

                <StepPanel :value="stepIndices.datapath">
                    <div class="mb-2">
                        Select the root data path for your project here. Note that this path cannot be changed once the project has been created.
                    </div>

                    <Fieldset
                        legend="Data path"
                        class="h-fit r-form-fieldset"
                        :class="{ 'border-[var(--p-inputtext-invalid-border-color)]': validator.hasError('datapath') }"
                    >
                        <template #legend>
                            <span class="p-fieldset-legend-label">Data path <MandatoryMark /></span>
                        </template>

                        <div class="r-form-field">
                            <div v-if="showDataPathSelector" class="grid grid-flow-row">
                                <div v-if="!resourcesError" class="w-full">
                                    <small class="px-2 py-1.5 r-shade-gray rounded-lg truncated inline-block w-full">
                                        <b class="pr-1">Selected path:</b> {{ dialogData.userData.datapath || "(None)" }}
                                    </small>
                                    <ScrollPanel class="h-48">
                                        <ResourcesTree
                                            name="datapath"
                                            v-model="dialogData.userData.datapath"
                                            :options="resourcesNodes"
                                            loading
                                            class="w-full h-fit"
                                            @changed="validator.refresh()"
                                        />
                                    </ScrollPanel>
                                </div>
                                <div v-else class="h-fit"><b>Unable to load resources:</b> {{ resourcesError }}</div>
                            </div>
                            <div v-else class="grid grid-flow-row">
                                <span class="flex border border-solid rounded p-2">
                                    <span class="basis-0 material-icons-outlined mi-folder opacity-75 pr-2" />
                                    <span>{{ dialogData.userData.datapath }}</span>
                                </span>
                                <span>
                                    <small class="pt-3"><b>Project already created:</b> The data path cannot be changed anymore.</small>
                                </span>
                            </div>
                        </div>
                        <small class="pt-3"><b>Important:</b> This path cannot be changed after the project has been created!</small>
                    </Fieldset>
                </StepPanel>

                <StepPanel :value="stepIndices.features">
                    <div class="mb-2">
                        Select the features you want to use in this project. You can always turn additional features on or existing ones off later.
                    </div>

                    <Fieldset legend="Features" class="r-form-fieldset">
                        <div v-for="snapIn of optSnapIns" :key="snapIn.snapInID" class="flex align-items-center pb-1">
                            <Checkbox
                                v-model="uiOptions.optional_snapins"
                                :inputId="snapIn.snapInID"
                                :value="snapIn.snapInID"
                                size="large"
                                class="self-center"
                            />
                            <label :for="snapIn.snapInID" class="pl-1.5">{{ snapIn.options.optional!.label }}</label>
                        </div>
                    </Fieldset>
                </StepPanel>

                <StepPanel :value="stepIndices.connections">
                    <div class="mb-2">
                        Here you can select which connections - all or only specific ones - to make available for publishing or exporting your project. You can
                        always change this selection later.
                    </div>

                    <Fieldset legend="Connections" class="r-form-fieldset">
                        <div class="r-form-field">
                            <div class="grid grid-flow-row">
                                <div class="flex align-items-center">
                                    <ToggleSwitch
                                        v-model="dialogData.userData.options.use_all_connector_instances"
                                        inputId="useSelectConnectorInstances"
                                        :true-value="false"
                                        :false-value="true"
                                        @change="validator.refresh()"
                                        class="self-center"
                                    />
                                    <label for="useSelectConnectorInstances" class="pl-1.5">Use only the following connections:</label>
                                </div>

                                <div class="!h-full border border-solid rounded p-1 ml-3.5 mr-3.5 mt-1.5">
                                    <ConnectorInstancesSelect
                                        v-model="dialogData.userData.options.active_connector_instances"
                                        :disabled="dialogData.userData.options.use_all_connector_instances"
                                        class="w-full h-60"
                                    />
                                </div>
                            </div>
                        </div>
                    </Fieldset>
                </StepPanel>
            </StepPanels>
        </Stepper>
    </Form>

    <EditProjectDialogFooter
        v-if="newProject"
        :prev-callback="prevCallback"
        :next-callback="nextCallback"
        :next-name="nextName"
        :next-icon="activeStep >= lastStepIndex ? 'mi-done' : undefined"
        :next-icon-position="activeStep >= lastStepIndex ? 'left' : undefined"
        class="mt-auto"
    />
</template>

<style scoped lang="scss"></style>

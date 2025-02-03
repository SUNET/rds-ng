<script setup lang="ts">
import { Form } from "@primevue/forms";
import Fieldset from "primevue/fieldset";
import IftaLabel from "primevue/iftalabel";
import InputText from "primevue/inputtext";
import Textarea from "primevue/textarea";
import { ref } from "vue";
import * as yup from "yup";

import { useExtendedDialogTools } from "@common/ui/dialogs/ExtendedDialogTools";
import { useDirectives } from "@common/ui/Directives";

import MandatoryMark from "@common/ui/components/misc/MandatoryMark.vue";

const { dialogData, acceptDialog, useValidator } = useExtendedDialogTools();
const { vFocus } = useDirectives();

const form = ref();
const validator = useValidator(form, {
    name: yup.string().trim().required().label("Name").default(dialogData.userData.name),
    description: yup.string().label("Description").default(dialogData.userData.description)
});
</script>

<template>
    <Form ref="form" :resolver="validator.resolver" validate-on-mount @submit="acceptDialog" class="r-form">
        <Fieldset legend="General" class="r-form-fieldset">
            <span class="r-form-field">
                <IftaLabel>
                    <label>Name <MandatoryMark /></label>
                    <InputText name="name" v-model="dialogData.userData.name" fluid v-focus />
                </IftaLabel>
                <small>The name of the connection.</small>
            </span>

            <span class="r-form-field mt-5">
                <IftaLabel class="mb-[-0.5rem]">
                    <label>Description</label>
                    <Textarea name="description" v-model.trim="dialogData.userData.description" rows="3" fluid />
                </IftaLabel>
                <small>An (optional) connection description.</small>
            </span>
        </Fieldset>
    </Form>
</template>

<style scoped lang="scss"></style>

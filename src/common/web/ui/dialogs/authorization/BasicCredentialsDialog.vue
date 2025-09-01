<script setup lang="ts">
import { Form } from "@primevue/forms";
import Fieldset from "primevue/fieldset";
import IftaLabel from "primevue/iftalabel";
import InputText from "primevue/inputtext";
import Password from "primevue/password";
import { ref } from "vue";
import * as yup from "yup";
import LinkedText from "../../components/misc/LinkedText.vue";

import { useDirectives } from "../../Directives";
import { useExtendedDialogTools } from "../ExtendedDialogTools";

import MandatoryMark from "../../components/misc/MandatoryMark.vue";

const { dialogData, acceptDialog, useValidator } = useExtendedDialogTools();
const { vFocus } = useDirectives();

const form = ref();
const validator = useValidator(form, {
    name: yup.string().trim().required().label(dialogData.userData.userNameLabel),
    password: yup.string().required().label(dialogData.userData.userPasswordLabel)
});
const initialFormValues = ref({
    name: dialogData.userData.userName,
    password: dialogData.userData.userPassword
});
</script>

<template>
    <Form
        ref="form"
        :resolver="validator.resolver"
        :initial-values="initialFormValues"
        :validate-on-mount="false"
        :validate-on-blur="false"
        :validate-on-value-update="true"
        @submit="acceptDialog"
        class="r-form"
    >
        <div>
            The external services requires you to provide account credentials (<em>{{ dialogData.userData.userNameLabel.toLowerCase() }}</em> and
            <em>{{ dialogData.userData.userPasswordLabel.toLowerCase() }}</em
            >) in order to be used.
        </div>

        <Fieldset legend="Credentials" class="r-form-fieldset">
            <span class="r-form-field">
                <IftaLabel>
                    <InputText name="name" v-model.trim="dialogData.userData.userName" fluid v-focus />
                    <label>{{ dialogData.userData.userNameLabel }} <MandatoryMark /></label>
                </IftaLabel>
                <small>The {{ dialogData.userData.userNameLabel.toLowerCase() }} for the external service.</small>
            </span>

            <span class="r-form-field mt-5">
                <IftaLabel>
                    <Password name="password" v-model="dialogData.userData.userPassword" :feedback="false" fluid />
                    <label>{{ dialogData.userData.userPasswordLabel }} <MandatoryMark /></label>
                </IftaLabel>
                <small>The {{ dialogData.userData.userPasswordLabel.toLowerCase() }} for the external service.</small>
            </span>
        </Fieldset>

        <div v-if="!!dialogData.userData.helpLink">
            For further information about how to get credentials from the external service, you can visit
            <LinkedText :link="dialogData.userData.helpLink" text="this link" /> which will provide additional help.
        </div>
    </Form>
</template>

<style scoped lang="scss"></style>

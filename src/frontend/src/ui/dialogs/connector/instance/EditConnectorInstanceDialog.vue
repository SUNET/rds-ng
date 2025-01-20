<script setup lang="ts">
import Fieldset from "primevue/fieldset";
import IftaLabel from "primevue/iftalabel";
import InputText from "primevue/inputtext";
import Textarea from "primevue/textarea";
import { string as ystring } from "yup";

import { useExtendedDialogTools } from "@common/ui/dialogs/ExtendedDialogTools";
import { useDirectives } from "@common/ui/Directives";
import MandatoryMark from "@common/ui/components/misc/MandatoryMark.vue";

const { dialogData, acceptDialog, useValidator } = useExtendedDialogTools();
const { vFocus } = useDirectives();

const validator = useValidator({
    name: ystring().trim().required().label("Name").default(dialogData.userData.name),
    description: ystring().label("Description").default(dialogData.userData.description)
});
const name = validator.defineComponentBinds("name");
</script>

<template>
    <form @submit.prevent="acceptDialog" class="r-form">
        <Fieldset legend="General">
            <span class="r-form-field">
                <IftaLabel>
                    <label>Name <MandatoryMark /></label>
                    <InputText
                        name="name"
                        v-bind="name"
                        v-model="dialogData.userData.name"
                        class="w-full"
                        :class="{ 'p-invalid': validator.errors.name }"
                        v-focus
                    />
                </IftaLabel>
                <small>The name of the connection.</small>
            </span>

            <span class="r-form-field mt-5">
                <IftaLabel class="mb-[-0.5rem]">
                    <label>Description</label>
                    <Textarea name="description" v-model.trim="dialogData.userData.description" rows="3" class="w-full" />
                </IftaLabel>
                <small>An (optional) connection description.</small>
            </span>
        </Fieldset>
    </form>
</template>

<style scoped lang="scss"></style>

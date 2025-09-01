import { defineAsyncComponent } from "vue";

import { WebComponent } from "../../../component/WebComponent";
import { type BasicStrategyConfiguration } from "../../../integration/authorization/strategies/basic/BasicTypes";
import { extendedDialog, type ExtendedDialogResult } from "../ExtendedDialog";

/**
 * The data used by the ``basicCredentialsDialog`` dialog.
 */
export interface BasicCredentialsDialogData {
    userName: string;
    userNameLabel: string;

    userPassword: string;
    userPasswordLabel: string;

    helpLink: string;
}

/**
 * Shows the edit dialog for a connector instance.
 *
 * @param comp - The global component.
 * @param config - An optional basic strategy configuration.
 */
export async function basicCredentialsDialog(comp: WebComponent, config?: BasicStrategyConfiguration): ExtendedDialogResult<BasicCredentialsDialogData> {
    return extendedDialog<BasicCredentialsDialogData>(
        comp,
        defineAsyncComponent(() => import("./BasicCredentialsDialog.vue")),
        {
            header: "Account credentials",
            modal: true,
            contentClass: "max-w-[20vw] w-[20vw] w-full min-w-[40rem]"
        },
        {
            userName: "",
            userNameLabel: config?.user_id_label || "User name",
            userPassword: "",
            userPasswordLabel: config?.user_password_label || "Password",
            helpLink: config?.help_link || ""
        },
        {
            hasAcceptButton: true,
            acceptLabel: "Connect",
            acceptIcon: "material-icons-outlined mi-link",

            hasRejectButton: true,
            rejectLabel: "Cancel",
            rejectIcon: "material-icons-outlined mi-clear"
        },
        undefined,
        false
    );
}

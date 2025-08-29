import { defineAsyncComponent } from "vue";

import { WebComponent } from "../../../component/WebComponent";
import { extendedDialog, type ExtendedDialogResult } from "../ExtendedDialog";

/**
 * The data used by the ``basicCredentialsDialog`` dialog.
 */
export interface BasicCredentialsDialogData {
    userName: string;
    userNameLabel: string;

    userPassword: string;
    userPasswordLabel: string;
}

/**
 * Shows the edit dialog for a connector instance.
 *
 * @param comp - The global component.
 * @param userNameLabel - The label of the username.
 * @param userPasswordLabel - The label of the user password.
 */
export async function basicCredentialsDialog(
    comp: WebComponent,
    userNameLabel?: string,
    userPasswordLabel?: string
): ExtendedDialogResult<BasicCredentialsDialogData> {
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
            userNameLabel: userNameLabel || "User name",
            userPassword: "",
            userPasswordLabel: userPasswordLabel || "Password"
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

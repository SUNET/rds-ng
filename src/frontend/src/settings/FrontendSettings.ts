import { SettingID } from "@common/utils/config/SettingID";

import { OAuth2AuthorizationSettingIDs } from "@/settings/AuthorizationSettingIDs";

/**
 * Gets default values for all frontend settings.
 *
 * @returns - An object mapping the setting identifiers to their default values.
 */
export function getFrontendSettings(): Map<SettingID, any> {
    let settings = new Map<SettingID, any>();

    // Authorization settings
    settings.set(OAuth2AuthorizationSettingIDs.ClientID, "");
    settings.set(OAuth2AuthorizationSettingIDs.RedirectURL, "");

    return settings;
}

/**
 * Default values for dynamic configuration settings.
 */
export const enum FrontendDefaultSettings {
    IntegrationScheme = "basic",

    HostURL = "",
    HostEntrypointEndpoint = "/",
    HostAPIEndpoint = "/api/v1"
}

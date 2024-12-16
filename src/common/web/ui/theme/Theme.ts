import { definePreset, palette } from "@primevue/themes";
import Aura from "@primevue/themes/aura";

import { ThemeSettingIDs } from "../../settings/ThemeSettingIDs";
import { Configuration } from "../../utils/config/Configuration";

/**
 * Creates the theme for the application.
 */
export function theme(config: Configuration): any {
    return definePreset(Aura, {
        semantic: {
            primary: palette(config.value<string>(ThemeSettingIDs.PrimaryColor)),
            focusRing: {
                width: "0px",
                style: "solid",
                color: "transparent"
            },
            colorScheme: {
                light: {
                    surface: palette(config.value<string>(ThemeSettingIDs.LightSurfaceColor))
                },
                dark: {
                    surface: palette(config.value<string>(ThemeSettingIDs.DarkSurfaceColor))
                }
            }
        }
    });
}

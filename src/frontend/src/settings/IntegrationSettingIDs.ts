import { SettingID } from "@common/utils/config/SettingID";

/**
 * Identifiers for integration settings.
 *
 * @property Scheme - The integration scheme to use (value type: ``string``).
 */
export class IntegrationSettingIDS {
    public static readonly Scheme = new SettingID("integration", "scheme");
}

/**
 * Identifiers for host integration settings.
 *
 * @property URL - The full URL of the host (value type: ``string``).
 */
export class HostIntegrationSettingIDs {
    public static readonly URL = new SettingID("integration.host", "url");
}

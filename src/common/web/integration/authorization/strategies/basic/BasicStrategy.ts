import { WebComponent } from "../../../../component/WebComponent";
import { Service } from "../../../../services/Service";
import { RedirectionTarget } from "../../../../utils/HTMLUtils";
import { AuthorizationRequest } from "../../AuthorizationRequest";
import { AuthorizationStrategy } from "../AuthorizationStrategy";
import { BasicAuthorizationRequestData, type BasicStrategyConfiguration } from "./BasicTypes";

/**
 * Basic authorization strategy.
 */
export class BasicStrategy extends AuthorizationStrategy {
    public static readonly Strategy = "basic";

    private readonly _config: BasicStrategyConfiguration;

    public constructor(comp: WebComponent, svc: Service, config: BasicStrategyConfiguration) {
        super(comp, svc, BasicStrategy.Strategy, RedirectionTarget.Current);

        this._config = config;
    }

    protected initiateRequest(authRequest: AuthorizationRequest): void {
        /*const url = new URL(this._config.server.authorization_endpoint, new URL(this._config.server.host));
        url.searchParams.set("response_type", "code");
        url.searchParams.set("client_id", this._config.client.client_id);
        url.searchParams.set("scope", this._config.server.scope);
        url.searchParams.set("access_type", "offline");
        url.searchParams.set("approval_prompt", "auto");
        url.searchParams.set("redirect_uri", this._config.client.redirect_url);
        url.searchParams.set("state", authRequest.encodedPayload);
        this.redirect(url.toString());*/
        // TODO
    }

    protected getRequestData(_: AuthorizationRequest): any {
        // TODO
        return {
            user_id: "TODO",
            user_password: "TODO"
        } as BasicAuthorizationRequestData;
    }

    protected finishRequest(authRequest: AuthorizationRequest): void {
        // TODO
        /*
        if (this._redirectionTarget == RedirectionTarget.Blank) {
            // Even if there's no parent, this will work
            window.parent.close();
        } else {
            this.redirect(authRequest.payload.auth_issuer_url);
        }*/
    }
}

/**
 * Creates a new Basic strategy instance, automatically configuring it.
 *
 * @param comp - The main component.
 * @param svc - The service to use for message sending.
 * @param config - The strategy configuration.
 *
 * @returns - The newly created strategy.
 */
export function createBasicStrategy(comp: WebComponent, svc: Service, config: Record<string, any>): BasicStrategy {
    const basicConfig = config as BasicStrategyConfiguration;

    // Set defaults for non-critical settings
    if (!basicConfig.user_id_label) {
        basicConfig.user_id_label = "User ID";
    }
    if (!basicConfig.user_password_label) {
        basicConfig.user_password_label = "Password";
    }

    return new BasicStrategy(comp, svc, basicConfig);
}

import { WebComponent } from "../../../../component/WebComponent";
import { Service } from "../../../../services/Service";
import { RedirectionTarget } from "../../../../utils/HTMLUtils";
import { AuthorizationRequest } from "../../AuthorizationRequest";
import { AuthorizationExecutionType, AuthorizationStrategy } from "../AuthorizationStrategy";
import { type BasicAuthorizationRequestData, type BasicStrategyConfiguration } from "./BasicTypes";

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
        // TODO: Get credentials
        authRequest.extendedData = { user_id: "id", user_password: "pwd" } as BasicAuthorizationRequestData;

        // We execute the request immediately
        this.executeAuthorizationRequest(authRequest, AuthorizationExecutionType.Direct)
            .then(() => {})
            .catch((error) => {});
    }

    protected getRequestData(authRequest: AuthorizationRequest): any {
        return authRequest.extendedData as BasicAuthorizationRequestData;
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

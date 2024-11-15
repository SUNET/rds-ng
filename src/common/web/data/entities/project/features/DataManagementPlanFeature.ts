import { LayoutObject } from "@common/ui/components/propertyeditor/ProjectObjectStore";
import { Type } from "class-transformer";
import { ProjectFeature, type ProjectFeatureID } from "./ProjectFeature";

/**
 * The DMP metadata type.
 *
 *
 */
export type DataManagementPlan = LayoutObject[];

/**
 * Data class for the data management plan project feature.
 */
export class DataManagementPlanFeature extends ProjectFeature {
    public static readonly FeatureID: ProjectFeatureID = "dmp";

    // @ts-ignore
    @Type(() => LayoutObject)
    public readonly plan: DataManagementPlan;

    public constructor(plan: DataManagementPlan = []) {
        super();

        this.plan = plan;
    }

    public get featureID(): ProjectFeatureID {
        return DataManagementPlanFeature.FeatureID;
    }
}

import { Type } from "class-transformer";

import { LayoutObject } from "../../../../ui/components/propertyeditor/ProjectObjectStore";
import { ProjectFeature, type ProjectFeatureID } from "./ProjectFeature";

/**
 * The project metadata type.
 *
 *
 */
export type ProjectMetadata = LayoutObject[];

/**
 * Data class for the metadata project feature.
 */
export class ProjectMetadataFeature extends ProjectFeature {
    public static readonly FeatureID: ProjectFeatureID = "project_metadata";
    // @ts-ignore
    @Type(() => LayoutObject)
    public readonly metadata: ProjectMetadata;

    public constructor(metadata: ProjectMetadata = []) {
        super();

        this.metadata = metadata;
    }

    public get featureID(): ProjectFeatureID {
        return ProjectMetadataFeature.FeatureID;
    }
}

import { Type } from "class-transformer";

import { LayoutObject, SharedObject } from "../../../../ui/components/propertyeditor/ProjectObjectStore";
import { ProjectFeature, type ProjectFeatureID } from "./ProjectFeature";

/**
 * The project metadata type.
 *
 * TODO: Use proper type
 */
export type ProjectMetadata = LayoutObject[];

/**
 * The metadata objects type.
 *
 * TODO: Use proper type
 */
export type MetadataObjects = SharedObject[];

/**
 * Data class for the metadata project feature.
 */
export class ProjectMetadataFeature extends ProjectFeature {
    public static readonly FeatureID: ProjectFeatureID = "project_metadata";
    // @ts-ignore
    @Type(() => LayoutObject)
    public readonly metadata: ProjectMetadata;
    
    // @ts-ignore
    @Type(() => SharedObject)
    public readonly shared_objects: MetadataObjects;

    public constructor(metadata: ProjectMetadata = [], sharedObjects: MetadataObjects = []) {
        super();

        this.metadata = metadata;
        this.shared_objects = sharedObjects;
    }

    public get featureID(): ProjectFeatureID {
        return ProjectMetadataFeature.FeatureID;
    }
}

import { Transform, Type, plainToInstance } from "class-transformer";

import { LayoutObject } from "../../../../ui/components/propertyeditor/ProjectObjectStore";
import { ProjectFeature, type ProjectFeatureID } from "./ProjectFeature";

/**
 * @typedef {ResourcesMetadataKey}
 *
 * Represents the keys of the ResourcesMetadata object.
 */
export type ResourcesMetadataKey = keyof typeof ResourcesMetadata;

/**
 * The resources metadata type.
 *
 *
 */
export class ResourcesMetadata {
    [key: string]: LayoutObject;

    public constructor(metadata: { [key: string]: LayoutObject[] } = {}) {
        if (metadata.value === undefined) return;

        Object.entries(metadata.value).forEach(([key, value]: [ResourcesMetadataKey, LayoutObject]) => {
            if (value !== undefined) this[key as ResourcesMetadataKey] = plainToInstance(LayoutObject, value);
        });
    }
}

/**
 * Data class for the files project feature.
 */
export class ResourcesMetadataFeature extends ProjectFeature {
    public static readonly FeatureID: ProjectFeatureID = "resources_metadata";

    // @ts-ignore
    @Type(() => ResourcesMetadata)
    // @ts-ignore
    @Transform((value) => new ResourcesMetadata(value), { toClassOnly: false })
    public readonly metadata: ResourcesMetadata;

    public constructor(resourcesMetadata: ResourcesMetadata = {}) {
        super();

        this.metadata = resourcesMetadata;
    }

    public get featureID(): ProjectFeatureID {
        return ResourcesMetadataFeature.FeatureID;
    }
}

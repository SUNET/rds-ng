import { ResourcesMetadataFeature } from "@common/data/entities/project/features/ResourcesMetadataFeature";

import { SnapIn, type SnapInID } from "../SnapIn";

export class ResourcesMetadataSnapIn extends SnapIn {
    public static readonly SnapInID: SnapInID = "resources_metadata";

    public constructor() {
        super(ResourcesMetadataSnapIn.SnapInID, {
            name: "Data annotation",
            optional: {
                label: "Data annotation",
                feature: ResourcesMetadataFeature.FeatureID,
                description: "Annotate individual file objects with metadata."
            },
            tabPanel: {
                label: "Data annotation",
                loader: () => import("./ResourcesMetadataPanel.vue"),
                description: "Annotate individual file objects with metadata."
            }
        });
    }
}

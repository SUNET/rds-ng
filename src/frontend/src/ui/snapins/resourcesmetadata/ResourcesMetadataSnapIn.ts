import { ResourcesMetadataFeature } from "@common/data/entities/project/features/ResourcesMetadataFeature";

import { SnapIn, type SnapInID } from "../SnapIn";

export class ResourcesMetadataSnapIn extends SnapIn {
    public static readonly SnapInID: SnapInID = "resources_metadata";

    public constructor() {
        super(ResourcesMetadataSnapIn.SnapInID, {
            name: "Annotation",
            optional: {
                label: "Annotation",
                feature: ResourcesMetadataFeature.FeatureID
            },
            tabPanel: {
                label: "Annotation",
                loader: () => import("./ResourcesMetadataPanel.vue")
            }
        });
    }
}

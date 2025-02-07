import { ProjectMetadataFeature } from "@common/data/entities/project/features/ProjectMetadataFeature";

import { SnapIn, type SnapInID } from "../SnapIn";

export class ProjectMetadataSnapIn extends SnapIn {
    public static readonly SnapInID: SnapInID = "metadata";

    public constructor() {
        super(ProjectMetadataSnapIn.SnapInID, {
            name: "Publication Metadata",
            optional: {
                label: "Publication Metadata",
                feature: ProjectMetadataFeature.FeatureID,
                description: "The overall research metadata of the project."
            },
            tabPanel: {
                label: "Publication Metadata",
                loader: () => import("./ProjectMetadataPanel.vue"),
                description: "Add metadata describing your project."
            }
        });
    }
}

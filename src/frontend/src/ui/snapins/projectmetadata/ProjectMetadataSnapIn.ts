import { SnapIn, type SnapInID } from "../SnapIn";

export class ProjectMetadataSnapIn extends SnapIn {
    public static readonly SnapInID: SnapInID = "metadata";

    public constructor() {
        super(ProjectMetadataSnapIn.SnapInID, {
            name: "Metadata",
            tabPanel: {
                label: "Metadata",
                loader: () => import("./ProjectMetadataPanel.vue"),
                description: "Add metadata describing your project."
            }
        });
    }
}

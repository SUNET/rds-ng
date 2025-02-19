import json
from urllib.parse import quote

from rocrate.model.contextentity import ContextEntity
from rocrate.rocrate import ROCrate

from common.py.data.entities.project import Project
from common.py.data.entities.project.features import (ProjectFeatureID,
                                                      ProjectMetadataFeature)
from common.py.data.exporters import (ProjectExporter,
                                      ProjectExporterException,
                                      ProjectExporterID, ProjectExporterResult)


class ROCrateExporter(ProjectExporter):
    """
    ROCrate project exporter.
    """

    ExporterID: ProjectExporterID = "rocrate"

    def __init__(
        self,
    ):
        super().__init__(
            ROCrateExporter.ExporterID,
            name="RO-Crate",
            description="Exports to an RO-Crate (Research Object) file",
            extension="json",
            scope=[ProjectMetadataFeature.feature_id],
        )

    def export(
        self, project: Project, scope: ProjectFeatureID | None = None
    ) -> ProjectExporterResult:
        if scope == ProjectMetadataFeature.feature_id:
            return self._export_project_metadata(project)

        raise ProjectExporterException(f"Unsupported scope {scope}")

    def _export_project_metadata(self, project: Project) -> ProjectExporterResult:
        crate = ROCrate()

        # TODO: add contexts to profiles, get them from there
        crate.metadata.extra_contexts.append("https://datacite-metadata-schema.readthedocs.io/en/4.5/properties/")

        # add files
        for key, propertyObjects in project.features.resources_metadata.metadata.items():
            values = {}
            for po in propertyObjects:
                refObjects = [o for o in project.features.shared_objects if o.id in po.refs]
                refs = {}

                for o in refObjects:
                    refs[o.type] = [*refs.get(o.type, []), {"@id": quote(o.id)}]
                values = values | po.value | refs

            crate.add_file(key, properties=values, dest_path=quote(key.removeprefix("/")))

        # add shared objects
        for sharedObject in project.features.shared_objects:
            refObjects = [o for o in project.features.shared_objects if o.id in sharedObject.refs]
            refs = {}

            for o in refObjects:
                refs[o.type] = [*refs.get(o.type, []), {"@id": quote(o.id)}]

            p = {"@type": sharedObject.type} | sharedObject.value | refs

            crate.add(ContextEntity(crate, quote(sharedObject.id), properties=p))


        # add project metadata
        # is the root data set the right spot for this?
        root = crate.dereference("./")

        for m in [m for m in project.features.project_metadata.metadata if "datacite" in m.id]: # HACK
            refObjects = [o for o in project.features.shared_objects if o.id in m.refs]

            # add references
            for o in refObjects:
                root[o.type] = [*root.get(o.type, []), {"@id": quote(o.id)}]
            
            # add simple values
            for k, v in m.value.items():
                root[k] = v

        metadata_bytes = str.encode(json.dumps(crate.metadata.generate(), indent=4))

        return ProjectExporterResult(mimetype="application/ld+json", data=metadata_bytes)
    

import json
from urllib.parse import quote

from rocrate.model.contextentity import ContextEntity
from rocrate.model.data_entity import DataEntity
from rocrate.model.root_dataset import RootDataset
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
            file: DataEntity = crate.add_file(key, dest_path=quote(key.removeprefix("/"))) # pyright: ignore[reportAssignmentType]
            
            for po in propertyObjects:
                refObjects = [o for o in project.features.shared_objects if o.id in po.refs]

                # add simple values
                for k, v in po.value.items():
                    file[k] = v

                # add references
                for o in refObjects:
                    file[o.type] = [*file.get(o.type, []), {"@id": quote(o.id)}]

        # add shared objects
        for sharedObject in project.features.shared_objects:
            entity: ContextEntity = crate.add(ContextEntity(crate, quote(sharedObject.id), properties={"@type": sharedObject.type})) # pyright: ignore[reportAssignmentType]

            # add simple values
            for k, v in sharedObject.value.items():
                entity[k] = v

            # add references
            refObjects = [o for o in project.features.shared_objects if o.id in sharedObject.refs]
            for o in refObjects:
                entity[o.type] = [*entity.get(o.type, []), {"@id": quote(o.id)}]

        # add project metadata
        root: RootDataset = crate.dereference("./")

        for m in [m for m in project.features.project_metadata.metadata if "datacite" in m.id]: # HACK

            # add simple values
            for k, v in m.value.items():
                root[k] = v

            # add references
            refObjects = [o for o in project.features.shared_objects if o.id in m.refs]
            for o in refObjects:
                root[o.type] = [*root.get(o.type, []), {"@id": quote(o.id)}]

        metadata_bytes = str.encode(json.dumps(crate.metadata.generate(), indent=4))

        return ProjectExporterResult(mimetype="application/ld+json", data=metadata_bytes)
    

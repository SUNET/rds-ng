import abc

from ..entities.project import Project
from ..entities.project.features import ProjectFeatureID
from .project_exporter_descriptor import (
    ProjectExporterDescriptor,
    ProjectExporterID,
    ProjectExporterScope,
)
from .project_exporter_result import ProjectExporterResult


class ProjectExporter(abc.ABC):
    """
    Base class for project exporters.
    """

    def __init__(
        self,
        exporter_id: ProjectExporterID,
        *,
        name: str,
        description: str,
        extension: str,
        scope: ProjectExporterScope,
        default_filename: str = ""
    ):
        """
        Args:
            exporter_id: The unique ID of the exporter.
            name: The name.
            description: The description.
            extension: The extension of exported files.
            scope: The scope the exporter applies to.
            default_filename: A default filename used when none is given.
        """
        self._descriptor = ProjectExporterDescriptor(
            exporter_id=exporter_id,
            name=name,
            description=description,
            extension=extension,
            scope=scope,
            default_filename=default_filename,
        )

    @abc.abstractmethod
    def export(
        self, project: Project, scope: ProjectFeatureID | None = None
    ) -> ProjectExporterResult: ...

    @property
    def descriptor(self) -> ProjectExporterDescriptor:
        """
        The exporter descriptor.
        """
        return self._descriptor

    @property
    def exporter_id(self) -> ProjectExporterID:
        """
        The ID of the exporter.
        """
        return self._descriptor.exporter_id

    @property
    def name(self) -> str:
        """
        The exporter name.
        """
        return self._descriptor.name

    @property
    def description(self) -> str:
        """
        The exporter description.
        """
        return self._descriptor.description

    @property
    def extension(self) -> str:
        """
        The extension of exported files.
        """
        return self._descriptor.extension

    @property
    def scope(self) -> ProjectExporterScope:
        """
        The exporter's scope.
        """
        return self._descriptor.scope

    @property
    def default_filename(self) -> str:
        """
        The default filename used when none is given.
        """
        return self._descriptor.default_filename

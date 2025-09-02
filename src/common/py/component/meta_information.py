import typing

from semantic_version import Version

from ..utils.config import Configuration, InformationFile


class MetaInformation(InformationFile):
    """
    Accesses meta information about the entire project and its various component stored in a *JSON* file.
    """

    def __init__(
        self,
        config: Configuration,
        *,
        info_file: str = "/config/meta-information.json",
        env_prefix: str = "RDS_META"
    ):
        """
        Args:
            config: The global application configuration.
            info_file: The JSON file to load the meta information from.
            env_prefix: The prefix to use when generating the environment variable name of a setting.

        Raises:
            ValueError: If the information file couldn't be loaded.
        """
        super().__init__(info_file=info_file, env_prefix=env_prefix)

        self._config = config

        self._title, self._version = self._read_global_info()
        self._components = self._read_component_definitions()

    def _read_global_info(self) -> tuple[str, Version]:
        title: str = self._value("global.title", "<invalid>")
        version: Version = Version(self._value("global.version", "0.0.0"))
        return title, version

    def _read_component_definitions(
        self,
    ) -> typing.Dict[str, typing.Dict[str, typing.Any]]:
        comps_info: typing.Dict[str, typing.Dict[str, typing.Any]] = self._value(
            "components", {}
        )
        return comps_info

    @property
    def title(self) -> str:
        """
        The project title.
        """
        return self._title

    @property
    def version(self) -> Version:
        """
        The project version (see https://semver.org).
        """
        return self._version

    def get_components(self) -> typing.List[str]:
        """
        A list of all component names.

        Returns:
            The names of all components.
        """
        return list(self._components.keys())

    def get_component(self, comp: str) -> typing.Dict[str, typing.Any]:
        """
        Retrieves the meta information stored for a specific component.

        This meta information includes the ``name`` of the component, as well as its ``directory`` within the code structure (rooted at ``/src``).

        Args:
            comp: The name of the component.

        Returns:
            A dictionary containing the meta information.
        """
        if comp in self._components:
            return self._components[comp]

        return {
            "name": "<invalid>",
            "directory": "",
            "tech": "",
        }

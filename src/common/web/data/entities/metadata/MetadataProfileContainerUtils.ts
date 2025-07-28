import { type MetadataProfileContainerList, MetadataProfileContainerRole } from "./MetadataProfileContainer";

/**
 * Gets all containers from a list matching the specified category.
 *
 * @param containers - The list of containers.
 * @param category - The category to match.
 *
 * @returns - List of all matching containers.
 */
export function filterContainersByCategory(containers: MetadataProfileContainerList, category: string): MetadataProfileContainerList {
    return containers.filter((container) => container.category == category);
}

/**
 * Gets all containers from a list matching the specified role.
 *
 * @param containers - The list of containers.
 * @param roles - The roles to match.
 *
 * @returns - List of all matching containers.
 */
export function filterContainersByRoles(containers: MetadataProfileContainerList, roles: MetadataProfileContainerRole[]): MetadataProfileContainerList {
    return containers.filter((container) => roles.includes(container.role));
}

/**
 * Gets all containers from a list matching the specified category and role.
 *
 * @param containers - The list of containers.
 * @param category - The category to match.
 * @param roles - The roles to match.
 *
 * @returns - List of all matching containers.
 */
export function filterContainers(
    containers: MetadataProfileContainerList,
    category: string,
    roles: MetadataProfileContainerRole[]
): MetadataProfileContainerList {
    return containers.filter((container) => container.category == category && roles.includes(container.role));
}

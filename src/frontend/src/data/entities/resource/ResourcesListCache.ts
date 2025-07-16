import { Resource, ResourceType } from "@common/data/entities/resource/Resource.ts";
import { ResourcesList } from "@common/data/entities/resource/ResourcesList.ts";

/**
 * Cache to store a resources list.
 *
 * This is used to store a resources list incrementally, i.d., the existing list can be extended on demand.
 */
export class ResourcesListCache {
    private _resourcesList: ResourcesList | null = null;
    private _knownPaths: string[] = [];

    /**
     * Adds a new resources list to the cache.
     *
     * The new list must be either located under the root path or a new root path. Errors will be thrown if a push would potentially result in a corrupted
     * cache (i.e., when adding an already existing path, or gaps would occur).
     *
     * @param resources - The new resources list to add.
     *
     * @throws Error - When a push operation would result in a corrupted cache.
     */
    public push(resources: ResourcesList): void {
        // Adding a new root replaces everything else
        if (this.isRoot(resources.resource)) {
            this.clear();

            this._resourcesList = resources;
        } else {
            if (this.isEmpty()) {
                throw new Error(`Tried to push a non-root resources list (${resources.resource.filename}) into an empty cache`);
            } else if (this.contains(resources.resource.filename)) {
                throw new Error(`Tried to push an already existing resources list (${resources.resource.filename})`);
            }

            if (!this.insertIntoParent(this._resourcesList!, resources)) {
                throw new Error(`Unable to push the resources list (${resources.resource.filename}) into the cache`);
            }
        }

        this._knownPaths.push(resources.resource.filename);
    }

    /**
     * Checks whether a given path is contained in the cache.
     *
     * @param path - The path to check.
     */
    public contains(path: string): boolean {
        return this._knownPaths.includes(path);
    }

    /**
     * Whether the cache is empty.
     */
    public isEmpty(): boolean {
        return this._resourcesList == null;
    }

    /**
     * Clear the entire cache.
     */
    public clear(): void {
        this._resourcesList = null;
        this._knownPaths = [];
    }

    private isRoot(res: Resource): boolean {
        return res.type == ResourceType.Folder && (res.filename == "" || res.filename == "/");
    }

    private insertIntoParent(resources: ResourcesList, child: ResourcesList): boolean {
        // See if the current resources list contains the child
        for (let i = 0; i < resources.folders.length; ++i) {
            const folder = resources.folders[i];
            if (folder.resource.filename == child.resource.filename) {
                resources.folders[i] = child;
                return true;
            }

            // Only recurse deeper into the current sub-folder if the child's path starts with the folder's path
            if (child.resource.filename.startsWith(folder.resource.filename)) {
                return this.insertIntoParent(folder, child);
            }
        }

        return false;
    }
}

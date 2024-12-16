// @ts-ignore
import { v4 as uuidv4 } from "uuid";

/**
 * Represents a project object.
 */
/**
 * Represents a project object with an ID, value, and references.
 *
 * @abstract
 * @class ProjectObject
 */
export abstract class ProjectObject {
    id: string;
    value: { [key: string]: any };
    refs: string[];

    /**
     * Creates a new instance of ProjectObject.
     * @param id The object ID.
     * @param value The object value.
     * @param refs The object references.
     */
    protected constructor(id?: string, value: any = {}, refs: string[] = []) {
        this.id = id || uuidv4();
        this.value = value;
        this.refs = refs;
    }

    /**
     * Retrieves the unique identifier of the project object.
     *
     * @returns {string} The unique identifier of the project object.
     */
    getId(): string {
        return this.id;
    }

    /**
     * Retrieves the current values stored in the ProjectObject.
     *
     * @returns An object where the keys are strings and the values can be of any type.
     */
    getValues(): { [key: string]: any } {
        return this.value;
    }

    /**
     * Retrieves the list of the references that the object holds.
     *
     * @returns {string[]} An array of reference strings.
     */
    getReferences(): string[] {
        return this.refs;
    }

    /**
     * Sets the references for the project object.
     *
     * @param refs - An array of reference strings to be set.
     */
    setReferences(refs: string[]): void {
        this.refs = refs;
    }

    /**
     * Adds a reference string to the list of references.
     *
     * @param ref - The reference string to be added.
     */
    pushReference(ref: string): void {
        this.refs.push(ref);
    }
}

/**
 * Represents a layout object within a Profile.
 * Extends the `ProjectObject` class.
 */
export class LayoutObject extends ProjectObject {
    constructor(id?: string, value: any = {}, refs: string[] = []) {
        super(id, value, refs);
    }
}

/**
 * Represents a shared object that extends the `ProjectObject` class.
 * 

 */
export class SharedObject extends ProjectObject {
    type: string;

    constructor(type: string, id?: string, value: any = {}, refs: string[] = []) {
        super(id, value, refs);
        this.type = type;
    }

    /**
     * Retrieves the type of the shared object.
     *
     * @returns {string} The type of the shared object.
     */
    public getType(): string {
        return this.type;
    }
}

/**
 * Represents a store for project objects.
 */
export class ProjectObjectStore {
    public _objects: ProjectObject[];

    /**
     * Constructs a new ProjectObjectStore instance.
     */
    constructor() {
        this._objects = [];
    }

    /**
     * Sets the objects in the store.
     * @param objects - An array of project objects.
     */
    public setObjects(objects: ProjectObject[]): void {
        this._objects = objects;
    }

    /**
     * Exports the objects from the store.
     * @returns An array of project objects.
     */
    public exportObjects(): ProjectObject[] {
        return this._objects;
    }

    /**
     * Adds a project object to the store if no object with that ID exists.
     * @param object - The project object to add.
     *
     * @returns The project object with that ID, either existing or newly created.
     */
    public add(object: ProjectObject): ProjectObject {
        const existing = this.get(object.id);
        if (existing !== undefined) {
            return existing;
        }
        this._objects.push(object);
        return object;
    }

    /**
     * Retrieves a project object by its ID.
     * @param id - The ID of the project object.
     *
     * @returns The project object with the specified ID, or undefined if not found.
     */
    public get(id: string): ProjectObject | undefined {
        return this._objects.find((object) => object.id === id);
    }

    /**
     * Removes a project object from the store by its ID. Also removes all references to the object.
     * @param id - The ID of the project object to remove.
     */
    public remove(id: string): void {
        this._removeRefs(id);
        this._objects = this._objects.filter((object) => object.id !== id);
    }

    /**
     * Removes references to a project object by its ID.
     * @param id - The ID of the project object.
     */
    public _removeRefs(id: string | string[]): void {
        if (Array.isArray(id)) {
            id.forEach((i) => this._removeRefs(i));
            return;
        }
        this._objects.forEach((object) => {
            let matches = object.getReferences().filter((ref) => ref !== id);
            object.setReferences(matches);
        });
    }

    /**
     * Updates the value of a project object.
     * @param profileId - The profile ID of the project object (only for LayoutObjects).
     * @param inputId - The input ID of the project object.
     * @param id - The ID of the project object.
     * @param value - The new value for the project object.
     */
    public update(inputId: string, id: string, value: any): void {
        let object: ProjectObject;

        object = this.get(id)!;
        if (object !== undefined) {
            object["value"][inputId] = value;
        }
    }

    /**
     * Adds a reference to a project object.
     * @param id - The ID of the project object.
     * @param ref - The reference ID to add.
     *
     * @returns The updated project object, or undefined if the project object is not found.
     */
    public addRef(id: string, ref: string): ProjectObject | undefined {
        const object = this.get(id);
        if (object) {
            object.pushReference(ref);
        } else {
            return undefined;
        }
    }

    /**
     * Removes a reference from a project object.
     * @param id - The ID of the project object.
     * @param ref - The reference ID to remove.
     */
    public removeRef(id: string, ref: string): void {
        const object = this.get(id);
        if (object) {
            let matches = object.refs.filter((r) => r !== ref);
            object.setReferences(matches);
        }
    }

    /**
     * Retrieves the referenced objects of a project object.
     * @param id - The ID of the project object.
     *
     * @returns An array of reference IDs of the referenced objects.
     */
    public getReferencedObjects(id: string): string[] {
        const object = this.get(id);
        return object ? object.getReferences() : [];
    }

    /**
     * Retrieves project objects of a specific type.
     * @param type - The type of project objects to retrieve.
     *
     * @returns An array of project objects of the specified type.
     */
    public getObjectsByType(type: string): SharedObject[] {
        return this._objects.filter((obj: ProjectObject) => obj instanceof SharedObject && obj.type === type) as SharedObject[];
    }
}

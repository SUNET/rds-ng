---
sidebar_label: metadata_parser
title: data.metadata.metadata_parser
---

## MetadataParserQuery Objects

```python
@dataclass
class MetadataParserQuery()
```

MetadataParserQuery is a data class that represents a query for metadata parsing.

**Attributes**:

- `id` _str_ - The identifier for the metadata query.
- `value` _str_ - The value associated with the metadata query.

## MetadataParser Objects

```python
class MetadataParser()
```

MetadataParser class provides static methods to filter and retrieve metadata based on profiles and queries.

**Methods**:

- `filter_by_profile(profile_name` - str | List, metadata: MetadataSet) -&gt; List[Dict[str, Any]]:
  Filters the metadata entries by the given profile name(s).
- `getattr(metadata` - MetadataSet, query: MetadataParserQuery) -&gt; List[Dict[str, Any]]:
  Retrieves the value from metadata entries based on the given query.
- `getobj(metadata` - MetadataSet, id: str):
  Retrieves the metadata entry with the specified id.

#### list\_values

```python
@staticmethod
def list_values(
    profile: PropertyProfile,
    metadata: MetadataSet,
    shared_objects: SharedPropertyObjectsSet | None = None
) -> MetadataValueList
```

Retrieves all (filled out) values from a profile in an easy-to-process format.

#### validate\_profile

```python
@staticmethod
def validate_profile(profile: PropertyProfile) -> bool
```

Validates the given profile dictionary to ensure it contains the required metadata and layout information.

**Arguments**:

- `profile` _PropertyProfile_ - The profile dictionary to validate. It should contain &#x27;metadata&#x27; and optionally &#x27;layout&#x27; and &#x27;classes&#x27;.

**Returns**:

- `bool` - True if the profile is valid, False otherwise.

**Raises**:

- `ValueError` - If the profile is missing required metadata keys or if the layout references missing classes.
  The profile dictionary should have the following structure:
```
{
    'metadata': {
        'id': str,
        'displayLabel': str,
        'description': str,
        ...
    },
    'layout': [
        {
            'type': str,
            ...
        },
        ...
    ],
    'classes': {
        ...
    }
}
```

#### filter\_by\_profile

```python
@staticmethod
def filter_by_profile(profile_name: str | List,
                      metadata: MetadataSet) -> List[PropertyObject]
```

Filters the metadata by the given profile name(s).

**Arguments**:

- `profile_name` _str | List_ - A single profile name or a list of profile names to filter by.
- `metadata` _List[Dict[str, Any]]_ - A list of metadata dictionaries, each containing a &quot;profiles&quot; key.
  

**Returns**:

  List[Dict[str, Any]]: A list of metadata dictionaries that match the given profile name(s).

#### getattr

```python
@staticmethod
def getattr(metadata: MetadataSet, query: MetadataParserQuery) -> Any
```

Retrieve a list of dictionaries from metadata based on a query.

**Arguments**:

- `metadata` _List[Dict[str, Any]]_ - A list of dictionaries containing metadata.
- `query` _MetadataParserQuery_ - An object containing the query parameters with &#x27;id&#x27; and &#x27;value&#x27; attributes.
  

**Returns**:

  List[Dict[str, Any]]: A list of dictionaries that match the query criteria, or None if no match is found.

#### getobj

```python
@staticmethod
def getobj(metadata: MetadataSet, oid: str) -> PropertyObject | None
```

Retrieve an object from a list of metadata dictionaries by its ID.

**Arguments**:

- `metadata` _List[Dict[str, Any]]_ - A list of dictionaries containing metadata.
- `oid` _str_ - The ID of the object to retrieve.
  

**Returns**:

  Dict[str, Any]: The dictionary object with the specified ID.

#### get\_profile\_layout

```python
@staticmethod
def get_profile_layout(profile: PropertyProfile) -> ProfileLayout
```

Extracts the layout information from the given profile metadata.

**Arguments**:

- `profile_metadata` _PropertyProfile_ - A list of dictionaries containing profile metadata.
  

**Returns**:

- `ProfileLayout` - A list of dictionaries representing the layout information.

#### is\_property\_filled\_out

```python
@staticmethod
def is_property_filled_out(metadata: MetadataSet,
                           prop_id: str,
                           shared_objects: SharedPropertyObjectsSet
                           | None = None,
                           profile: PropertyProfile | None = None)
```

Checks if a property is filled out.

**Arguments**:

- `metadata` _dict_ - The metadata dictionary containing various objects.
- `prop_id` _str_ - The property ID to look up in the metadata.
- `shared_objects` _list, optional_ - A list of shared objects that may be referenced in the metadata. Defaults to an empty list.
- `profile` _dict, optional_ - A dictionary containing profile information, including class layouts and templates. Defaults to an empty dictionary.

#### validate\_metadata

```python
@staticmethod
def validate_metadata(
        profile: PropertyProfile,
        metadata: MetadataSet,
        shared_objects: SharedPropertyObjectsSet | None = None) -> None
```

Validates all property values of a filled-out profile.

**Arguments**:

- `profile` - The profile.
- `metadata` - The profile metadata values.
- `shared_objects` - List of shared objects.

#### is\_property\_valid

```python
@staticmethod
def is_property_valid(
        metadata: MetadataSet,
        profile: PropertyProfile,
        prop_id: str,
        shared_objects: SharedPropertyObjectsSet | None = None) -> bool
```

Checks if a specific property in the metadata is valid according to the given profile.

**Arguments**:

- `metadata` _dict_ - The metadata dictionary containing various properties.
- `profile` _dict_ - The profile dictionary that defines the layout and requirements for properties.
- `prop_id` _str_ - The identifier of the property to check.

**Returns**:

- `bool` - True if the property is filled out according to the profile, False otherwise.

**Raises**:

- `MetadataPropertyMissingError` - If the property is missing in the metadata or not defined in the profile.

**Notes**:

  - The function first checks if the property exists in the metadata.
  - It then verifies if the property is defined in the profile layout.
  - If the property has required input values, it checks if those values are present and non-empty.
  - If the property has a type defined in the profile, it ensures that the property has references.

#### get\_value\_list

```python
@staticmethod
def get_value_list(
        metadata: MetadataSet,
        prop_id: str,
        shared_objects: SharedPropertyObjectsSet | None = None,
        profile: PropertyProfile | None = None) -> List[Dict[str, str]]
```

Retrieves a dictionary of values based on the provided metadata, property ID, shared objects, and profile.

**Arguments**:

- `metadata` _dict_ - The metadata dictionary containing various objects.
- `prop_id` _str_ - The property ID to look up in the metadata.
- `shared_objects` _list, optional_ - A list of shared objects that may be referenced in the metadata. Defaults to an empty list.
- `profile` _PropertyProfile_ - A dictionary containing profile information, including class layouts and templates.
  

**Returns**:

- `dict` - A dictionary of values where keys are object IDs and values are the transformed values based on the metadata and profile.


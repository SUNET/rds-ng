---
sidebar_label: request_data
title: utils.request_data
---

## RequestData Objects

```python
class RequestData()
```

Class to easily access data from an HTTP request.

#### data

```python
@property
def data() -> DataType
```

The data of the response.

#### status\_code

```python
@property
def status_code() -> HTTPStatus
```

The status code of the response.

#### is\_erroneous

```python
@property
def is_erroneous() -> bool
```

Whether the response was erroneous.

#### error

```python
@property
def error() -> str
```

The error reason (in case the request failed).

#### from\_response

```python
@classmethod
def from_response(cls,
                  data_type: typing.Any,
                  resp: requests.Response,
                  *,
                  verify_response: bool = True) -> "RequestData"
```

Creates a data response from an HTTP response.

**Arguments**:

- `data_type` - The data type.
- `resp` - The HTTP response.
- `verify_response` - Whether to verify the response.
  

**Returns**:

  The newly created request data.

#### data\_from\_response

```python
@classmethod
def data_from_response(cls,
                       data_type: typing.Any,
                       resp: requests.Response,
                       *,
                       verify_response: bool = True) -> DataType
```

Creates a data response from an HTTP response and retrieves the data object.

**Arguments**:

- `data_type` - The data type.
- `resp` - The HTTP response.
- `verify_response` - Whether to verify the response.
  

**Returns**:

  The newly created data object.


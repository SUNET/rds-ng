---
sidebar_label: img_conversion
title: utils.img_conversion
---

#### convert\_image\_to\_img\_source

```python
def convert_image_to_img_source(image_file: str) -> str
```

Loads an image file and base64-encodes it as an HTML &#x27;img&#x27; source.

**Notes**:

  The file ending is used as the source file type.
  

**Arguments**:

- `image_file` - The image file to load.
  

**Returns**:

  The &#x27;img&#x27; source attribute.


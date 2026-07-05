# tf.keras.preprocessing.image.DirectoryIterator

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/preprocessing/image/DirectoryIterator](https://tensorflow.google.cn/api_docs/python/tf/keras/preprocessing/image/DirectoryIterator)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/legacy/preprocessing/image.py#L392-L512) |

Iterator capable of reading images from a directory on disk.

Inherits From: [`Iterator`](https://tensorflow.google.cn/api_docs/python/tf/keras/preprocessing/image/Iterator), [`PyDataset`](https://tensorflow.google.cn/api_docs/python/tf/keras/utils/PyDataset)

```
tf.keras.preprocessing.image.DirectoryIterator(
    directory,
    image_data_generator,
    target_size=(256, 256),
    color_mode='rgb',
    classes=None,
    class_mode='categorical',
    batch_size=32,
    shuffle=True,
    seed=None,
    data_format=None,
    save_to_dir=None,
    save_prefix='',
    save_format='png',
    follow_links=False,
    subset=None,
    interpolation='nearest',
    keep_aspect_ratio=False,
    dtype=None
)
```

DEPRECATED.

| Attributes | |

|  |  |
| --- | --- |
| `filepaths` | List of absolute paths to image files. |
| `labels` | Class labels of every observation. |
| `max_queue_size` |  |

|  |  |
| --- | --- |
| `num_batches` | Number of batches in the PyDataset. |
| `sample_weight` |  |

|  |  |
| --- | --- |
| `use_multiprocessing` |  |

|  |  |
| --- | --- |
| `workers` |  |

## Methods

### `on_epoch_end`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/legacy/preprocessing/image.py#L73-L74)

```
on_epoch_end()
```

Method called at the end of every epoch.

### `reset`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/legacy/preprocessing/image.py#L76-L77)

```
reset()
```

### `set_processing_attrs`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/legacy/preprocessing/image.py#L210-L296)

```
set_processing_attrs(
    image_data_generator,
    target_size,
    color_mode,
    data_format,
    save_to_dir,
    save_prefix,
    save_format,
    subset,
    interpolation,
    keep_aspect_ratio
)
```

Sets attributes to use later for processing files into a batch.

| Args | |

|  |  |
| --- | --- |
| `image_data_generator` | Instance of `ImageDataGenerator` to use for random transformations and normalization. |
| `target_size` | tuple of integers, dimensions to resize input images to. |
| `color_mode` | One of `"rgb"`, `"rgba"`, `"grayscale"`. Color mode to read images. |
| `data_format` | String, one of `channels_first`, `channels_last`. |
| `save_to_dir` | Optional directory where to save the pictures being yielded, in a viewable format. This is useful for visualizing the random transformations being applied, for debugging purposes. |
| `save_prefix` | String prefix to use for saving sample images (if `save_to_dir` is set). |
| `save_format` | Format to use for saving sample images (if `save_to_dir` is set). |
| `subset` | Subset of data (`"training"` or `"validation"`) if validation\_split is set in ImageDataGenerator. |
| `interpolation` | Interpolation method used to resample the image if the target size is different from that of the loaded image. Supported methods are "nearest", "bilinear", and "bicubic". If PIL version 1.1.3 or newer is installed, "lanczos" is also supported. If PIL version 3.4.0 or newer is installed, "box" and "hamming" are also supported. By default, "nearest" is used. |
| `keep_aspect_ratio` | Boolean, whether to resize images to a target size without aspect ratio distortion. The image is cropped in the center with target aspect ratio before resizing. |

### `__getitem__`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/legacy/preprocessing/image.py#L53-L68)

```
__getitem__(
    idx
)
```

Gets batch at position `index`.

| Args | |

|  |  |
| --- | --- |
| `index` | position of the batch in the PyDataset. |

| Returns | |
| A batch | |

### `__iter__`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/legacy/preprocessing/image.py#L102-L105)

```
__iter__()
```

### `__len__`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/legacy/preprocessing/image.py#L70-L71)

```
__len__()
```

| Class Variables | |

|  |  |
| --- | --- |
| allowed\_class\_modes |  |

```
{
 'binary',
 'categorical',
 'input',
 'sparse',
 None
}
```

|  |  |
| --- | --- |
| white\_list\_formats | `('png', 'jpg', 'jpeg', 'bmp', 'ppm', 'tif', 'tiff')` |
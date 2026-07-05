# tf.keras.preprocessing.image.Iterator

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/preprocessing/image/Iterator](https://tensorflow.google.cn/api_docs/python/tf/keras/preprocessing/image/Iterator)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/legacy/preprocessing/image.py#L19-L122) |

Base class for image data iterators.

Inherits From: [`PyDataset`](https://tensorflow.google.cn/api_docs/python/tf/keras/utils/PyDataset)

```
tf.keras.preprocessing.image.Iterator(
    n, batch_size, shuffle, seed
)
```

DEPRECATED.

Every `Iterator` must implement the `_get_batches_of_transformed_samples`
method.

| Args | |

|  |  |
| --- | --- |
| `n` | Integer, total number of samples in the dataset to loop over. |
| `batch_size` | Integer, size of a batch. |
| `shuffle` | Boolean, whether to shuffle the data between epochs. |
| `seed` | Random seeding for data shuffling. |

| Attributes | |

|  |  |
| --- | --- |
| `max_queue_size` |  |

|  |  |
| --- | --- |
| `num_batches` | Number of batches in the PyDataset. |
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
| white\_list\_formats | `('png', 'jpg', 'jpeg', 'bmp', 'ppm', 'tif', 'tiff')` |
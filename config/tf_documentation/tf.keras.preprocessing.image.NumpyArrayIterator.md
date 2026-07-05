# tf.keras.preprocessing.image.NumpyArrayIterator

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/preprocessing/image/NumpyArrayIterator](https://tensorflow.google.cn/api_docs/python/tf/keras/preprocessing/image/NumpyArrayIterator)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/legacy/preprocessing/image.py#L515-L679) |

Iterator yielding data from a Numpy array.

Inherits From: [`Iterator`](https://tensorflow.google.cn/api_docs/python/tf/keras/preprocessing/image/Iterator), [`PyDataset`](https://tensorflow.google.cn/api_docs/python/tf/keras/utils/PyDataset)

```
tf.keras.preprocessing.image.NumpyArrayIterator(
    x,
    y,
    image_data_generator,
    batch_size=32,
    shuffle=False,
    sample_weight=None,
    seed=None,
    data_format=None,
    save_to_dir=None,
    save_prefix='',
    save_format='png',
    subset=None,
    ignore_class_split=False,
    dtype=None
)
```

DEPRECATED.

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
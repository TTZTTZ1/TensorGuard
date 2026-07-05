# tf.keras.preprocessing.sequence.TimeseriesGenerator

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/preprocessing/sequence/TimeseriesGenerator](https://tensorflow.google.cn/api_docs/python/tf/keras/preprocessing/sequence/TimeseriesGenerator)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/legacy/preprocessing/sequence.py#L12-L176) |

Utility class for generating batches of temporal data.

Inherits From: [`PyDataset`](https://tensorflow.google.cn/api_docs/python/tf/keras/utils/PyDataset)

```
tf.keras.preprocessing.sequence.TimeseriesGenerator(
    data,
    targets,
    length,
    sampling_rate=1,
    stride=1,
    start_index=0,
    end_index=None,
    shuffle=False,
    reverse=False,
    batch_size=128
)
```

DEPRECATED.

This class takes in a sequence of data-points gathered at
equal intervals, along with time series parameters such as
stride, length of history, etc., to produce batches for
training/validation.

| Arguments | |

|  |  |
| --- | --- |
| `data` | Indexable generator (such as list or Numpy array) containing consecutive data points (timesteps). The data should be at 2D, and axis 0 is expected to be the time dimension. |
| `targets` | Targets corresponding to timesteps in `data`. It should have same length as `data`. |
| `length` | Length of the output sequences (in number of timesteps). |
| `sampling_rate` | Period between successive individual timesteps within sequences. For rate `r`, timesteps `data[i]`, `data[i-r]`, ... `data[i - length]` are used for create a sample sequence. |
| `stride` | Period between successive output sequences. For stride `s`, consecutive output samples would be centered around `data[i]`, `data[i+s]`, `data[i+2*s]`, etc. |
| `start_index` | Data points earlier than `start_index` will not be used in the output sequences. This is useful to reserve part of the data for test or validation. |
| `end_index` | Data points later than `end_index` will not be used in the output sequences. This is useful to reserve part of the data for test or validation. |
| `shuffle` | Whether to shuffle output samples, or instead draw them in chronological order. |
| `reverse` | Boolean: if `true`, timesteps in each output sample will be in reverse chronological order. |
| `batch_size` | Number of timeseries samples in each batch (except maybe the last one). |

| Returns | |
| A PyDataset instance. | |

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

### `get_config`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/legacy/preprocessing/sequence.py#L126-L159)

```
get_config()
```

Returns the TimeseriesGenerator configuration as Python dictionary.

| Returns | |
| A Python dictionary with the TimeseriesGenerator configuration. | |

### `on_epoch_end`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/trainers/data_adapters/py_dataset_adapter.py#L173-L175)

```
on_epoch_end()
```

Method called at the end of every epoch.

### `to_json`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/legacy/preprocessing/sequence.py#L161-L176)

```
to_json(
    **kwargs
)
```

Returns a JSON string containing the generator's configuration.

| Args | |

|  |  |
| --- | --- |
| `**kwargs` | Additional keyword arguments to be passed to `json.dumps()`. |

| Returns | |
| A JSON string containing the tokenizer configuration. | |

### `__getitem__`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/legacy/preprocessing/sequence.py#L101-L124)

```
__getitem__(
    index
)
```

Gets batch at position `index`.

| Args | |

|  |  |
| --- | --- |
| `index` | position of the batch in the PyDataset. |

| Returns | |
| A batch | |

### `__len__`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/legacy/preprocessing/sequence.py#L96-L99)

```
__len__()
```
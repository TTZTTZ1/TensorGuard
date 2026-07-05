# tf.keras.utils.Sequence

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/utils/Sequence](https://tensorflow.google.cn/api_docs/python/tf/keras/utils/Sequence)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/trainers/data_adapters/py_dataset_adapter.py#L18-L175) |

Base class for defining a parallel dataset using Python code.

#### View aliases

**Main aliases**

[`tf.keras.utils.Sequence`](https://tensorflow.google.cn/api_docs/python/tf/keras/utils/PyDataset)

```
tf.keras.utils.PyDataset(
    workers=1, use_multiprocessing=False, max_queue_size=10
)
```

Every `PyDataset` must implement the `__getitem__()` and the `__len__()`
methods. If you want to modify your dataset between epochs,
you may additionally implement `on_epoch_end()`.
The `__getitem__()` method should return a complete batch
(not a single sample), and the `__len__` method should return
the number of batches in the dataset (rather than the number of samples).

| Args | |

|  |  |
| --- | --- |
| `workers` | Number of workers to use in multithreading or multiprocessing. |
| `use_multiprocessing` | Whether to use Python multiprocessing for parallelism. Setting this to `True` means that your dataset will be replicated in multiple forked processes. This is necessary to gain compute-level (rather than I/O level) benefits from parallelism. However it can only be set to `True` if your dataset can be safely pickled. |
| `max_queue_size` | Maximum number of batches to keep in the queue when iterating over the dataset in a multithreaded or multipricessed setting. Reduce this value to reduce the CPU memory consumption of your dataset. Defaults to 10. |

#### Notes:

* `PyDataset` is a safer way to do multiprocessing.
  This structure guarantees that the model will only train
  once on each sample per epoch, which is not the case
  with Python generators.
* The arguments `workers`, `use_multiprocessing`, and `max_queue_size`
  exist to configure how `fit()` uses parallelism to iterate
  over the dataset. They are not being used by the `PyDataset` class
  directly. When you are manually iterating over a `PyDataset`,
  no parallelism is applied.

#### Example:

```
from skimage.io import imread
from skimage.transform import resize
import numpy as np
import math

# Here, `x_set` is list of path to the images
# and `y_set` are the associated classes.

class CIFAR10PyDataset(keras.utils.PyDataset):

    def __init__(self, x_set, y_set, batch_size, **kwargs):
        super().__init__(**kwargs)
        self.x, self.y = x_set, y_set
        self.batch_size = batch_size

    def __len__(self):
        # Return number of batches.
        return math.ceil(len(self.x) / self.batch_size)

    def __getitem__(self, idx):
        # Return x, y for batch idx.
        low = idx * self.batch_size
        # Cap upper bound at array length; the last batch may be smaller
        # if the total number of items is not a multiple of batch size.
        high = min(low + self.batch_size, len(self.x))
        batch_x = self.x[low:high]
        batch_y = self.y[low:high]

        return np.array([
            resize(imread(file_name), (200, 200))
               for file_name in batch_x]), np.array(batch_y)
```

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/trainers/data_adapters/py_dataset_adapter.py#L173-L175)

```
on_epoch_end()
```

Method called at the end of every epoch.

### `__getitem__`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/trainers/data_adapters/py_dataset_adapter.py#L146-L155)

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
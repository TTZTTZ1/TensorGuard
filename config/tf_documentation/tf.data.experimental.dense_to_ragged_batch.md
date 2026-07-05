# tf.data.experimental.dense_to_ragged_batch

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/data/experimental/dense_to_ragged_batch](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/dense_to_ragged_batch)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/experimental/ops/batching.py#L30-L91) |

A transformation that batches ragged elements into [`tf.RaggedTensor`](https://tensorflow.google.cn/api_docs/python/tf/RaggedTensor)s. (deprecated)

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.data.experimental.dense_to_ragged_batch`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/dense_to_ragged_batch)

```
tf.data.experimental.dense_to_ragged_batch(
    batch_size,
    drop_remainder=False,
    row_splits_dtype=tf.dtypes.int64
)

tf.dtypes.int64
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Ragged tensors](https://tensorflow.google.cn/guide/ragged_tensor) | * [Recommend movies for users with TensorFlow Ranking](https://tensorflow.google.cn/ranking/tutorials/quickstart) |

**Deprecated:** THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use [`tf.data.Dataset.ragged_batch`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset#ragged_batch) instead.

This transformation combines multiple consecutive elements of the input
dataset into a single element.

Like [`tf.data.Dataset.batch`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset#batch), the components of the resulting element will
have an additional outer dimension, which will be `batch_size` (or
`N % batch_size` for the last element if `batch_size` does not divide the
number of input elements `N` evenly and `drop_remainder` is `False`). If
your program depends on the batches having the same outer dimension, you
should set the `drop_remainder` argument to `True` to prevent the smaller
batch from being produced.

Unlike [`tf.data.Dataset.batch`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset#batch), the input elements to be batched may have
different shapes:

* If an input element is a [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) whose static [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) is
  fully defined, then it is batched as normal.
* If an input element is a [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) whose static [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) contains
  one or more axes with unknown size (i.e., `shape[i]=None`), then the output
  will contain a [`tf.RaggedTensor`](https://tensorflow.google.cn/api_docs/python/tf/RaggedTensor) that is ragged up to any of such
  dimensions.
* If an input element is a [`tf.RaggedTensor`](https://tensorflow.google.cn/api_docs/python/tf/RaggedTensor) or any other type, then it is
  batched as normal.

#### Example:

```
>>> dataset = tf.data.Dataset.from_tensor_slices(np.arange(6))
>>> dataset = dataset.map(lambda x: tf.range(x))
>>> dataset.element_spec.shape
TensorShape([None])
>>> dataset = dataset.apply(
...     tf.data.experimental.dense_to_ragged_batch(batch_size=2))
>>> for batch in dataset:
...   print(batch)
<tf.RaggedTensor [[], [0]]>
<tf.RaggedTensor [[0, 1], [0, 1, 2]]>
<tf.RaggedTensor [[0, 1, 2, 3], [0, 1, 2, 3, 4]]>
```

| Args | |

|  |  |
| --- | --- |
| `batch_size` | A [`tf.int64`](https://tensorflow.google.cn/api_docs/python/tf#int64) scalar [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor), representing the number of consecutive elements of this dataset to combine in a single batch. |
| `drop_remainder` | (Optional.) A [`tf.bool`](https://tensorflow.google.cn/api_docs/python/tf#bool) scalar [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor), representing whether the last batch should be dropped in the case it has fewer than `batch_size` elements; the default behavior is not to drop the smaller batch. |
| `row_splits_dtype` | The dtype that should be used for the `row_splits` of any new ragged tensors. Existing [`tf.RaggedTensor`](https://tensorflow.google.cn/api_docs/python/tf/RaggedTensor) elements do not have their row\_splits dtype changed. |

| Returns | |

|  |  |
| --- | --- |
| `Dataset` | A `Dataset`. |
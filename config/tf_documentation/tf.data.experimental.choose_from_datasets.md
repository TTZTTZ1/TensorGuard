# tf.data.experimental.choose_from_datasets

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/data/experimental/choose_from_datasets](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/choose_from_datasets)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/experimental/ops/interleave_ops.py#L170-L224) |

Creates a dataset that deterministically chooses elements from `datasets`. (deprecated)

```
tf.data.experimental.choose_from_datasets(
    datasets, choice_dataset, stop_on_empty_dataset=False
)
```

**Deprecated:** THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use [`tf.data.Dataset.choose_from_datasets(...)`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset#choose_from_datasets) instead. Note that, unlike the experimental endpoint, the non-experimental endpoint sets `stop_on_empty_dataset=True` by default. You should set this argument explicitly in case you would like to match the behavior of the experimental endpoint.

For example, given the following datasets:

```
datasets = [tf.data.Dataset.from_tensors("foo").repeat(),
            tf.data.Dataset.from_tensors("bar").repeat(),
            tf.data.Dataset.from_tensors("baz").repeat()]

# Define a dataset containing `[0, 1, 2, 0, 1, 2, 0, 1, 2]`.
choice_dataset = tf.data.Dataset.range(3).repeat(3)

result = tf.data.experimental.choose_from_datasets(datasets, choice_dataset)
```

The elements of `result` will be:

```
"foo", "bar", "baz", "foo", "bar", "baz", "foo", "bar", "baz"
```

| Args | |

|  |  |
| --- | --- |
| `datasets` | A non-empty list of [`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset) objects with compatible structure. |
| `choice_dataset` | A [`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset) of scalar [`tf.int64`](https://tensorflow.google.cn/api_docs/python/tf#int64) tensors between `0` and `len(datasets) - 1`. |
| `stop_on_empty_dataset` | If `True`, selection stops if it encounters an empty dataset. If `False`, it skips empty datasets. It is recommended to set it to `True`. Otherwise, the selected elements start off as the user intends, but may change as input datasets become empty. This can be difficult to detect since the dataset starts off looking correct. Default to `False` for backward compatibility. |

| Returns | |
| A dataset that interleaves elements from `datasets` according to the values of `choice_dataset`. | |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | If `datasets` or `choice_dataset` has the wrong type. |
| `ValueError` | If `datasets` is empty. |
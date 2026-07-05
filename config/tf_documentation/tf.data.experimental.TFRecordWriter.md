# tf.data.experimental.TFRecordWriter

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/data/experimental/TFRecordWriter](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/TFRecordWriter)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/experimental/ops/writers.py#L27-L126) |

Writes a dataset to a TFRecord file. (deprecated)

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.data.experimental.TFRecordWriter`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/TFRecordWriter)

```
tf.data.experimental.TFRecordWriter(
    filename, compression_type=None
)
```

**Deprecated:** THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
To write TFRecords to disk, use [`tf.io.TFRecordWriter`](https://tensorflow.google.cn/api_docs/python/tf/io/TFRecordWriter). To save and load the contents of a dataset, use [`tf.data.experimental.save`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/save) and [`tf.data.experimental.load`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/load)

The elements of the dataset must be scalar strings. To serialize dataset
elements as strings, you can use the [`tf.io.serialize_tensor`](https://tensorflow.google.cn/api_docs/python/tf/io/serialize_tensor) function.

```
dataset = tf.data.Dataset.range(3)
dataset = dataset.map(tf.io.serialize_tensor)
writer = tf.data.experimental.TFRecordWriter("/path/to/file.tfrecord")
writer.write(dataset)
```

To read back the elements, use `TFRecordDataset`.

```
dataset = tf.data.TFRecordDataset("/path/to/file.tfrecord")
dataset = dataset.map(lambda x: tf.io.parse_tensor(x, tf.int64))
```

To shard a `dataset` across multiple TFRecord files:

```
dataset = ... # dataset to be written

def reduce_func(key, dataset):
  filename = tf.strings.join([PATH_PREFIX, tf.strings.as_string(key)])
  writer = tf.data.experimental.TFRecordWriter(filename)
  writer.write(dataset.map(lambda _, x: x))
  return tf.data.Dataset.from_tensors(filename)

dataset = dataset.enumerate()
dataset = dataset.apply(tf.data.experimental.group_by_window(
  lambda i, _: i % NUM_SHARDS, reduce_func, tf.int64.max
))

# Iterate through the dataset to trigger data writing.
for _ in dataset:
  pass
```

| Args | |

|  |  |
| --- | --- |
| `filename` | a string path indicating where to write the TFRecord data. |
| `compression_type` | (Optional.) a string indicating what type of compression to use when writing the file. See `tf.io.TFRecordCompressionType` for what types of compression are available. Defaults to `None`. |

## Methods

### `write`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/experimental/ops/writers.py#L91-L126)

```
write(
    dataset
)
```

Writes a dataset to a TFRecord file.

An operation that writes the content of the specified dataset to the file
specified in the constructor.

If the file exists, it will be overwritten.

| Args | |

|  |  |
| --- | --- |
| `dataset` | a [`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset) whose elements are to be written to a file |

| Returns | |
| In graph mode, this returns an operation which when executed performs the write. In eager mode, the write is performed by the method itself and there is no return value. | |

Raises
TypeError: if `dataset` is not a [`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset).
TypeError: if the elements produced by the dataset are not scalar strings.
# tf.io.TFRecordWriter

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/io/TFRecordWriter](https://tensorflow.google.cn/api_docs/python/tf/io/TFRecordWriter)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/lib/io/tf_record.py#L211-L318) |

A class to write records to a TFRecords file.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.io.TFRecordWriter`](https://tensorflow.google.cn/api_docs/python/tf/io/TFRecordWriter), [`tf.compat.v1.python_io.TFRecordWriter`](https://tensorflow.google.cn/api_docs/python/tf/io/TFRecordWriter)

```
tf.io.TFRecordWriter(
    path, options=None
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [TFRecord and tf.train.Example](https://tensorflow.google.cn/tutorials/load_data/tfrecord) * [Graph-based Neural Structured Learning in TFX](https://tensorflow.google.cn/tfx/tutorials/tfx/neural_structured_learning) * [Graph regularization for sentiment classification using synthesized graphs](https://tensorflow.google.cn/neural_structured_learning/tutorials/graph_keras_lstm_imdb) * [Instance Segmentation with Model Garden](https://tensorflow.google.cn/tfmodels/vision/instance_segmentation) * [Semantic Segmentation with Model Garden](https://tensorflow.google.cn/tfmodels/vision/semantic_segmentation) |

[TFRecords tutorial](https://tensorflow.google.cn/tutorials/load_data/tfrecord)

TFRecords is a binary format which is optimized for high throughput data
retrieval, generally in conjunction with [`tf.data`](https://tensorflow.google.cn/api_docs/python/tf/data). `TFRecordWriter` is used
to write serialized examples to a file for later consumption. The key steps
are:

Ahead of time:

* [Convert data into a serialized format](https://tensorflow.google.cn/tutorials/load_data/tfrecord#tfexample)
* [Write the serialized data to one or more files](https://tensorflow.google.cn/tutorials/load_data/tfrecord#tfrecord_files_in_python)

  During training or evaluation:
* [Read serialized examples into memory](https://tensorflow.google.cn/tutorials/load_data/tfrecord#reading_a_tfrecord_file)
* [Parse (deserialize) examples](https://tensorflow.google.cn/tutorials/load_data/tfrecord#reading_a_tfrecord_file)

A minimal example is given below:

```
>>> import tempfile
>>> example_path = os.path.join(tempfile.gettempdir(), "example.tfrecords")
>>> np.random.seed(0)
```

```
>>> # Write the records to a file.
... with tf.io.TFRecordWriter(example_path) as file_writer:
...   for _ in range(4):
...     x, y = np.random.random(), np.random.random()
... 
...     record_bytes = tf.train.Example(features=tf.train.Features(feature={
...         "x": tf.train.Feature(float_list=tf.train.FloatList(value=[x])),
...         "y": tf.train.Feature(float_list=tf.train.FloatList(value=[y])),
...     })).SerializeToString()
...     file_writer.write(record_bytes)
```

```
>>> # Read the data back out.
>>> def decode_fn(record_bytes):
...   return tf.io.parse_single_example(
...       # Data
...       record_bytes,
... 
...       # Schema
...       {"x": tf.io.FixedLenFeature([], dtype=tf.float32),
...        "y": tf.io.FixedLenFeature([], dtype=tf.float32)}
...   )
```

```
>>> for batch in tf.data.TFRecordDataset([example_path]).map(decode_fn):
...   print("x = {x:.4f},  y = {y:.4f}".format(**batch))
x = 0.5488,  y = 0.7152
x = 0.6028,  y = 0.5449
x = 0.4237,  y = 0.6459
x = 0.4376,  y = 0.8918
```

This class implements `__enter__` and `__exit__`, and can be used
in `with` blocks like a normal file. (See the usage example above.)

| Args | |

|  |  |
| --- | --- |
| `path` | The path to the TFRecords file. |
| `options` | (optional) String specifying compression type, `TFRecordCompressionType`, or `TFRecordOptions` object. |

| Raises | |

|  |  |
| --- | --- |
| `IOError` | If `path` cannot be opened for writing. |
| `ValueError` | If valid compression\_type can't be determined from `options`. |

## Methods

### `close`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/lib/io/tf_record.py#L315-L317)

```
close()
```

Close the file.

### `flush`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/lib/io/tf_record.py#L311-L313)

```
flush()
```

Flush the file.

### `write`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/lib/io/tf_record.py#L303-L309)

```
write(
    record
)
```

Write a string record to the file.

| Args | |

|  |  |
| --- | --- |
| `record` | str |

### `__enter__`

```
__enter__()
```

**enter**(self: object) -> object

### `__exit__`

```
__exit__()
```

**exit**(self: tensorflow.python.lib.io.\_pywrap\_record\_io.RecordWriter, \*args) -> None
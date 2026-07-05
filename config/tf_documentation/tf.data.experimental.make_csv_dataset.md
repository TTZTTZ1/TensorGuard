# tf.data.experimental.make_csv_dataset

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/data/experimental/make_csv_dataset](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/make_csv_dataset)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/experimental/ops/readers.py#L327-L626) |

Reads CSV files into a dataset.

```
tf.data.experimental.make_csv_dataset(
    file_pattern,
    batch_size,
    column_names=None,
    column_defaults=None,
    label_name=None,
    select_columns=None,
    field_delim=',',
    use_quote_delim=True,
    na_value='',
    header=True,
    num_epochs=None,
    shuffle=True,
    shuffle_buffer_size=10000,
    shuffle_seed=None,
    prefetch_buffer_size=None,
    num_parallel_reads=None,
    sloppy=False,
    num_rows_for_inference=100,
    compression_type=None,
    ignore_errors=False,
    encoding='utf-8'
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [tf.data: Build TensorFlow input pipelines](https://tensorflow.google.cn/guide/data) * [Estimators](https://tensorflow.google.cn/guide/estimator) | * [Load CSV data](https://tensorflow.google.cn/tutorials/load_data/csv) * [Preprocessing data with TensorFlow Transform](https://tensorflow.google.cn/tfx/tutorials/transform/census) |

Reads CSV files into a dataset, where each element of the dataset is a
(features, labels) tuple that corresponds to a batch of CSV rows. The features
dictionary maps feature column names to `Tensor`s containing the corresponding
feature data, and labels is a `Tensor` containing the batch's label data.

By default, the first rows of the CSV files are expected to be headers listing
the column names. If the first rows are not headers, set `header=False` and
provide the column names with the `column_names` argument.

By default, the dataset is repeated indefinitely, reshuffling the order each
time. This behavior can be modified by setting the `num_epochs` and `shuffle`
arguments.

For example, suppose you have a CSV file containing

| Feature\_A | Feature\_B |
| --- | --- |
| 1 | "a" |
| 2 | "b" |
| 3 | "c" |
| 4 | "d" |

```
# No label column specified
dataset = tf.data.experimental.make_csv_dataset(filename, batch_size=2)
iterator = dataset.as_numpy_iterator()
print(dict(next(iterator)))
# prints a dictionary of batched features:
# OrderedDict([('Feature_A', array([1, 4], dtype=int32)),
#              ('Feature_B', array([b'a', b'd'], dtype=object))])
```

```
# Set Feature_B as label column
dataset = tf.data.experimental.make_csv_dataset(
    filename, batch_size=2, label_name="Feature_B")
iterator = dataset.as_numpy_iterator()
print(next(iterator))
# prints (features, labels) tuple:
# (OrderedDict([('Feature_A', array([1, 2], dtype=int32))]),
#  array([b'a', b'b'], dtype=object))
```

See the
[Load CSV data guide](https://tensorflow.google.cn/tutorials/load_data/csv) for
more examples of using `make_csv_dataset` to read CSV data.

| Args | |

|  |  |
| --- | --- |
| `file_pattern` | List of files or patterns of file paths containing CSV records. See [`tf.io.gfile.glob`](https://tensorflow.google.cn/api_docs/python/tf/io/gfile/glob) for pattern rules. |
| `batch_size` | An int representing the number of records to combine in a single batch. |
| `column_names` | An optional list of strings that corresponds to the CSV columns, in order. One per column of the input record. If this is not provided, infers the column names from the first row of the records. These names will be the keys of the features dict of each dataset element. |
| `column_defaults` | A optional list of default values for the CSV fields. One item per selected column of the input record. Each item in the list is either a valid CSV dtype (float32, float64, int32, int64, or string), or a `Tensor` with one of the aforementioned types. The tensor can either be a scalar default value (if the column is optional), or an empty tensor (if the column is required). If a dtype is provided instead of a tensor, the column is also treated as required. If this list is not provided, tries to infer types based on reading the first num\_rows\_for\_inference rows of files specified, and assumes all columns are optional, defaulting to `0` for numeric values and `""` for string values. If both this and `select_columns` are specified, these must have the same lengths, and `column_defaults` is assumed to be sorted in order of increasing column index. |
| `label_name` | A optional string corresponding to the label column. If provided, the data for this column is returned as a separate `Tensor` from the features dictionary. |
| `select_columns` | An optional list of integer indices or string column names, that specifies a subset of columns of CSV data to select. If column names are provided, these must correspond to names provided in `column_names` or inferred from the file header lines. When this argument is specified, only a subset of CSV columns will be parsed and returned, corresponding to the columns specified. Using this results in faster parsing and lower memory usage. If both this and `column_defaults` are specified, these must have the same lengths, and `column_defaults` is assumed to be sorted in order of increasing column index. |
| `field_delim` | An optional `string`. Defaults to `","`. Char delimiter to separate fields in a record. |
| `use_quote_delim` | An optional bool. Defaults to `True`. If false, treats double quotation marks as regular characters inside of the string fields. |
| `na_value` | Additional string to recognize as NA/NaN. |
| `header` | A bool that indicates whether the first rows of provided CSV files correspond to header lines with column names, and should not be included in the data. |
| `num_epochs` | An int specifying the number of times this dataset is repeated. If None, cycles through the dataset forever. |
| `shuffle` | A bool that indicates whether the input should be shuffled. |
| `shuffle_buffer_size` | Buffer size to use for shuffling. A large buffer size ensures better shuffling, but increases memory usage and startup time. |
| `shuffle_seed` | Randomization seed to use for shuffling. |
| `prefetch_buffer_size` | An int specifying the number of feature batches to prefetch for performance improvement. Recommended value is the number of batches consumed per training step. Defaults to auto-tune. |
| `num_parallel_reads` | Number of threads used to read CSV records from files. If >1, the results will be interleaved. Defaults to `1`. |
| `sloppy` | If `True`, reading performance will be improved at the cost of non-deterministic ordering. If `False`, the order of elements produced is deterministic prior to shuffling (elements are still randomized if `shuffle=True`. Note that if the seed is set, then order of elements after shuffling is deterministic). Defaults to `False`. |
| `num_rows_for_inference` | Number of rows of a file to use for type inference if record\_defaults is not provided. If None, reads all the rows of all the files. Defaults to 100. |
| `compression_type` | (Optional.) A [`tf.string`](https://tensorflow.google.cn/api_docs/python/tf#string) scalar evaluating to one of `""` (no compression), `"ZLIB"`, or `"GZIP"`. Defaults to no compression. |
| `ignore_errors` | (Optional.) If `True`, ignores errors with CSV file parsing, such as malformed data or empty lines, and moves on to the next valid CSV record. Otherwise, the dataset raises an error and stops processing when encountering any invalid records. Defaults to `False`. |
| `encoding` | Encoding to use when reading. Defaults to `UTF-8`. |

| Returns | |
| A dataset, where each element is a (features, labels) tuple that corresponds to a batch of `batch_size` CSV rows. The features dictionary maps feature column names to `Tensor`s containing the corresponding column data, and labels is a `Tensor` containing the column data for the label column specified by `label_name`. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If any of the arguments is malformed. |
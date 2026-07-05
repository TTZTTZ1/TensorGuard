# tf.io.TFRecordOptions

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/io/TFRecordOptions](https://tensorflow.google.cn/api_docs/python/tf/io/TFRecordOptions)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/lib/io/tf_record.py#L35-L145) |

Options used for manipulating TFRecord files.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.io.TFRecordOptions`](https://tensorflow.google.cn/api_docs/python/tf/io/TFRecordOptions), [`tf.compat.v1.python_io.TFRecordOptions`](https://tensorflow.google.cn/api_docs/python/tf/io/TFRecordOptions)

```
tf.io.TFRecordOptions(
    compression_type=None,
    flush_mode=None,
    input_buffer_size=None,
    output_buffer_size=None,
    window_bits=None,
    compression_level=None,
    compression_method=None,
    mem_level=None,
    compression_strategy=None
)
```

| Args | |

|  |  |
| --- | --- |
| `compression_type` | `"GZIP"`, `"ZLIB"`, or `""` (no compression). |
| `flush_mode` | flush mode or `None`, Default: Z\_NO\_FLUSH. |
| `input_buffer_size` | int or `None`. |
| `output_buffer_size` | int or `None`. |
| `window_bits` | int or `None`. |
| `compression_level` | 0 to 9, or `None`. |
| `compression_method` | compression method or `None`. |
| `mem_level` | 1 to 9, or `None`. |
| `compression_strategy` | strategy or `None`. Default: Z\_DEFAULT\_STRATEGY. |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If compression\_type is invalid. |

## Methods

### `get_compression_type_string`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/lib/io/tf_record.py#L97-L121)

```
@classmethod
get_compression_type_string(
    options
)
```

Convert various option types to a unified string.

| Args | |

|  |  |
| --- | --- |
| `options` | `TFRecordOption`, `TFRecordCompressionType`, or string. |

| Returns | |
| Compression type as string (e.g. `'ZLIB'`, `'GZIP'`, or `''`). | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If compression\_type is invalid. |

| Class Variables | |

|  |  |
| --- | --- |
| compression\_type\_map |  |

```
{
 0: '',
 1: 'ZLIB',
 2: 'GZIP'
}
```
# tf.lookup.KeyValueTensorInitializer

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/lookup/KeyValueTensorInitializer](https://tensorflow.google.cn/api_docs/python/tf/lookup/KeyValueTensorInitializer)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/lookup_ops.py#L521-L586) |

Table initializers given `keys` and `values` tensors.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.lookup.KeyValueTensorInitializer`](https://tensorflow.google.cn/api_docs/python/tf/lookup/KeyValueTensorInitializer)

```
tf.lookup.KeyValueTensorInitializer(
    keys, values, key_dtype=None, value_dtype=None, name=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [BERT Preprocessing with TF Text](https://tensorflow.google.cn/text/guide/bert_preprocessing_guide) * [Subword tokenizers](https://tensorflow.google.cn/text/guide/subwords_tokenizer) | * [Load text](https://tensorflow.google.cn/tutorials/load_data/text) * [Client-efficient large-model federated learning via `federated\_select` and sparse aggregation](https://tensorflow.google.cn/federated/tutorials/sparse_federated_learning) * [Federated Learning for Text Generation](https://tensorflow.google.cn/federated/tutorials/federated_learning_for_text_generation) * [Apache ORC Reader](https://tensorflow.google.cn/io/tutorials/orc) * [Feature Engineering using TFX Pipeline and TensorFlow Transform](https://tensorflow.google.cn/tfx/tutorials/tfx/penguin_tft) |

```
>>> keys_tensor = tf.constant(['a', 'b', 'c'])
>>> vals_tensor = tf.constant([7, 8, 9])
>>> input_tensor = tf.constant(['a', 'f'])
>>> init = tf.lookup.KeyValueTensorInitializer(keys_tensor, vals_tensor)
>>> table = tf.lookup.StaticHashTable(
...     init,
...     default_value=-1)
>>> table.lookup(input_tensor).numpy()
array([ 7, -1], dtype=int32)
```

| Args | |

|  |  |
| --- | --- |
| `keys` | The tensor for the keys. |
| `values` | The tensor for the values. |
| `key_dtype` | The `keys` data type. Used when `keys` is a python array. |
| `value_dtype` | The `values` data type. Used when `values` is a python array. |
| `name` | A name for the operation (optional). |

| Attributes | |

|  |  |
| --- | --- |
| `key_dtype` | The expected table key dtype. |
| `value_dtype` | The expected table value dtype. |

## Methods

### `initialize`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/lookup_ops.py#L567-L586)

```
initialize(
    table
)
```

Initializes the given `table` with `keys` and `values` tensors.

| Args | |

|  |  |
| --- | --- |
| `table` | The table to initialize. |

| Returns | |
| The operation that initializes the table. | |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | when the keys and values data types do not match the table key and value data types. |
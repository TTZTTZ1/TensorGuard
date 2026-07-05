# tf.strings.to_number

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/strings/to_number](https://tensorflow.google.cn/api_docs/python/tf/strings/to_number)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/string_ops.py#L462-L488) |

Converts each string in the input Tensor to the specified numeric type.

```
tf.strings.to_number(
    input,
    out_type=tf.dtypes.float32,
    name=None
)

tf.dtypes.float32
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Introduction to Tensors](https://tensorflow.google.cn/guide/tensor) * [Migrating Keras 2 code to multi-backend Keras 3](https://tensorflow.google.cn/guide/keras/migrating_to_keras_3) * [Signatures in TensorFlow Lite](https://tensorflow.google.cn/lite/guide/signatures) | * [Robust machine learning on streaming data using Kafka and Tensorflow-IO](https://tensorflow.google.cn/io/tutorials/kafka) * [TensorFlow 2 TPUEmbeddingLayer: Quick Start](https://tensorflow.google.cn/recommenders/examples/tpu_embedding_layer) * [Sending Different Data To Particular Clients With tff.federated\_select](https://tensorflow.google.cn/federated/tutorials/federated_select) |

(Note that int32 overflow results in an error while float overflow
results in a rounded value.)

#### Examples:

```
>>> tf.strings.to_number("1.55")
<tf.Tensor: shape=(), dtype=float32, numpy=1.55>
>>> tf.strings.to_number("3", tf.int32)
<tf.Tensor: shape=(), dtype=int32, numpy=3>
```

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor` of type `string`. |
| `out_type` | An optional [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) from: `tf.float32, tf.float64, tf.int32, tf.int64`. Defaults to `tf.float32`. The numeric type to interpret each string in `string_tensor` as. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `out_type`. | |
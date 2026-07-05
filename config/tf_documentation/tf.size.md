# tf.size

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/size](https://tensorflow.google.cn/api_docs/python/tf/size)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/array_ops.py#L760-L797) |

Returns the size of a tensor.

```
tf.size(
    input, out_type=None, name=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Matrix approximation with Core APIs](https://tensorflow.google.cn/guide/core/matrix_core) * [Introduction to Tensors](https://tensorflow.google.cn/guide/tensor) * [BERT Preprocessing with TF Text](https://tensorflow.google.cn/text/guide/bert_preprocessing_guide) | * [Scalable model compression](https://tensorflow.google.cn/tutorials/optimization/compression) * [Client-efficient large-model federated learning via `federated\_select` and sparse aggregation](https://tensorflow.google.cn/federated/tutorials/sparse_federated_learning) * [Sending Different Data To Particular Clients With tff.federated\_select](https://tensorflow.google.cn/federated/tutorials/federated_select) * [Human Pose Classification with MoveNet and TensorFlow Lite](https://tensorflow.google.cn/lite/tutorials/pose_classification) * [Federated Learning for Image Classification](https://tensorflow.google.cn/federated/tutorials/federated_learning_for_image_classification) |

See also [`tf.shape`](https://tensorflow.google.cn/api_docs/python/tf/shape).

Returns a 0-D `Tensor` representing the number of elements in `input`
of type `out_type`. Defaults to tf.int32.

#### For example:

```
>>> t = tf.constant([[[1, 1, 1], [2, 2, 2]], [[3, 3, 3], [4, 4, 4]]])
>>> tf.size(t)
<tf.Tensor: shape=(), dtype=int32, numpy=12>
```

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor` or `SparseTensor`. |
| `out_type` | (Optional) The specified non-quantized numeric output type of the operation. Defaults to [`tf.int32`](https://tensorflow.google.cn/api_docs/python/tf#int32). (Note: there is an experimental flag, `tf_shape_default_int64` that changes the default to [`tf.int64`](https://tensorflow.google.cn/api_docs/python/tf#int64). This is an unsupported, experimental setting that causes known breakages.) |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `out_type`. Defaults to [`tf.int32`](https://tensorflow.google.cn/api_docs/python/tf#int32). | |

## numpy compatibility

Equivalent to np.size()
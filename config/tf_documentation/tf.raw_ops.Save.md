# tf.raw_ops.Save

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Save](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Save)

---

Saves the input tensors to disk.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.Save`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Save)

```
tf.raw_ops.Save(
    filename, tensor_names, data, name=None
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [On-Device Training with TensorFlow Lite](https://tensorflow.google.cn/lite/examples/on_device_training/overview) |

The size of `tensor_names` must match the number of tensors in `data`. `data[i]`
is written to `filename` with name `tensor_names[i]`.

See also `SaveSlices`.

| Args | |

|  |  |
| --- | --- |
| `filename` | A `Tensor` of type `string`. Must have a single element. The name of the file to which we write the tensor. |
| `tensor_names` | A `Tensor` of type `string`. Shape `[N]`. The names of the tensors to be saved. |
| `data` | A list of `Tensor` objects. `N` tensors to save. |
| `name` | A name for the operation (optional). |

| Returns | |
| The created Operation. | |
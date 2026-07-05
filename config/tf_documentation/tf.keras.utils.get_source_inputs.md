# tf.keras.utils.get_source_inputs

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/utils/get_source_inputs](https://tensorflow.google.cn/api_docs/python/tf/keras/utils/get_source_inputs)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/ops/operation_utils.py#L370-L402) |

Returns the list of input tensors necessary to compute `tensor`.

```
tf.keras.utils.get_source_inputs(
    tensor
)
```

Output will always be a list of tensors
(potentially with 1 element).

| Args | |

|  |  |
| --- | --- |
| `tensor` | The tensor to start from. |

| Returns | |
| List of input tensors. | |
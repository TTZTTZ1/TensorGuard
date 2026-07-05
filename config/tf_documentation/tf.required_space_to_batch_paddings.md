# tf.required_space_to_batch_paddings

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/required_space_to_batch_paddings](https://tensorflow.google.cn/api_docs/python/tf/required_space_to_batch_paddings)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/array_ops.py#L3648-L3724) |

Calculate padding required to make block\_shape divide input\_shape.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.required_space_to_batch_paddings`](https://tensorflow.google.cn/api_docs/python/tf/required_space_to_batch_paddings)

```
tf.required_space_to_batch_paddings(
    input_shape, block_shape, base_paddings=None, name=None
)
```

This function can be used to calculate a suitable paddings argument for use
with space\_to\_batch\_nd and batch\_to\_space\_nd.

| Args | |

|  |  |
| --- | --- |
| `input_shape` | int32 Tensor of shape [N]. |
| `block_shape` | int32 Tensor of shape [N]. |
| `base_paddings` | Optional int32 Tensor of shape [N, 2]. Specifies the minimum amount of padding to use. All elements must be >= 0. If not specified, defaults to 0. |
| `name` | string. Optional name prefix. |

| Returns | |
| (paddings, crops), where: | |

`paddings` and `crops` are int32 Tensors of rank 2 and shape [N, 2]| `satisfying` | paddings[i, 0] = base\_paddings[i, 0]. 0 <= paddings[i, 1] - base\_paddings[i, 1] < block\_shape[i](/api_docs/python/tf/input_shape%5Bi%5D%20+%20paddings%5Bi,%200%5D%20+%20paddings%5Bi,%201%5D) % block\_shape[i] == 0 |

crops[i, 0] = 0
crops[i, 1] = paddings[i, 1] - base\_paddings[i, 1]

Raises: ValueError if called with incompatible shapes.
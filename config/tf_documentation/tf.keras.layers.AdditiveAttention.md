# tf.keras.layers.AdditiveAttention

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/AdditiveAttention](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/AdditiveAttention)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/attention/additive_attention.py#L6-L103) |

Additive attention layer, a.k.a. Bahdanau-style attention.

Inherits From: [`Attention`](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Attention), [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.AdditiveAttention(
    use_scale=True, dropout=0.0, **kwargs
)
```

Inputs are a list with 2 or 3 elements:

1. A `query` tensor of shape `(batch_size, Tq, dim)`.
2. A `value` tensor of shape `(batch_size, Tv, dim)`.
3. A optional `key` tensor of shape `(batch_size, Tv, dim)`. If none
   supplied, `value` will be used as `key`.

The calculation follows the steps:

1. Calculate attention scores using `query` and `key` with shape
   `(batch_size, Tq, Tv)` as a non-linear sum
   `scores = reduce_sum(tanh(query + key), axis=-1)`.
2. Use scores to calculate a softmax distribution with shape
   `(batch_size, Tq, Tv)`.
3. Use the softmax distribution to create a linear combination of `value`
   with shape `(batch_size, Tq, dim)`.

| Args | |

|  |  |
| --- | --- |
| `use_scale` | If `True`, will create a scalar variable to scale the attention scores. |
| `dropout` | Float between 0 and 1. Fraction of the units to drop for the attention scores. Defaults to `0.0`. |

| Call Args | |

|  |  |
| --- | --- |
| `inputs` | List of the following tensors: |

* `query`: Query tensor of shape `(batch_size, Tq, dim)`.
* `value`: Value tensor of shape `(batch_size, Tv, dim)`.
* `key`: Optional key tensor of shape `(batch_size, Tv, dim)`. If
  not given, will use `value` for both `key` and `value`, which is
  the most common case.| `mask` | List of the following tensors: |
* `query_mask`: A boolean mask tensor of shape `(batch_size, Tq)`.
  If given, the output will be zero at the positions where
  `mask==False`.
* `value_mask`: A boolean mask tensor of shape `(batch_size, Tv)`.
  If given, will apply the mask such that values at positions
  where `mask==False` do not contribute to the result.| `return_attention_scores` | bool, it `True`, returns the attention scores (after masking and softmax) as an additional output argument. |
  | `training` | Python boolean indicating whether the layer should behave in training mode (adding dropout) or in inference mode (no dropout). |
  | `use_causal_mask` | Boolean. Set to `True` for decoder self-attention. Adds a mask such that position `i` cannot attend to positions `j > i`. This prevents the flow of information from the future towards the past. Defaults to `False`. |

| Output | |
| Attention outputs of shape `(batch_size, Tq, dim)`. (Optional) Attention scores after masking and softmax with shape `(batch_size, Tq, Tv)`. | |

| Attributes | |

|  |  |
| --- | --- |
| `input` | Retrieves the input tensor(s) of a symbolic operation. |

Only returns the tensor(s) corresponding to the *first time*
the operation was called.| `output` | Retrieves the output tensor(s) of a layer. |

Only returns the tensor(s) corresponding to the *first time*
the operation was called.

## Methods

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/ops/operation.py#L191-L213)

```
@classmethod
from_config(
    config
)
```

Creates a layer from its config.

This method is the reverse of `get_config`,
capable of instantiating the same layer from the config
dictionary. It does not handle layer connectivity
(handled by Network), nor weights (handled by `set_weights`).

| Args | |

|  |  |
| --- | --- |
| `config` | A Python dictionary, typically the output of get\_config. |

| Returns | |
| A layer instance. | |

### `symbolic_call`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/ops/operation.py#L58-L70)

```
symbolic_call(
    *args, **kwargs
)
```
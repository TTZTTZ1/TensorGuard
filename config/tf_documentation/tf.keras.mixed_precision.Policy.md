# tf.keras.mixed_precision.Policy

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/mixed_precision/Policy](https://tensorflow.google.cn/api_docs/python/tf/keras/mixed_precision/Policy)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/dtype_policies/dtype_policy.py#L9-L164) |

A dtype policy for a Keras layer.

#### View aliases

**Main aliases**

[`tf.keras.dtype_policies.DTypePolicy`](https://tensorflow.google.cn/api_docs/python/tf/keras/DTypePolicy), [`tf.keras.mixed_precision.DTypePolicy`](https://tensorflow.google.cn/api_docs/python/tf/keras/DTypePolicy), [`tf.keras.mixed_precision.Policy`](https://tensorflow.google.cn/api_docs/python/tf/keras/DTypePolicy)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.keras.DTypePolicy`](https://tensorflow.google.cn/api_docs/python/tf/keras/DTypePolicy)

```
tf.keras.DTypePolicy(
    name
)
```

### Used in the notebooks

| Used in the guide |
| --- |
| * [Mixed precision](https://tensorflow.google.cn/guide/mixed_precision) |

A dtype policy determines a layer's computation and variable dtypes. Each
layer has a policy. Policies can be passed to the `dtype` argument of layer
constructors, or a global policy can be set with
[`keras.config.set_dtype_policy`](https://tensorflow.google.cn/api_docs/python/tf/keras/config/set_dtype_policy).

| Args | |

|  |  |
| --- | --- |
| `name` | The policy name, which determines the compute and variable dtypes. Can be any dtype name, such as `"float32"` or `"float64"`, which causes both the compute and variable dtypes will be that dtype. Can also be the string `"mixed_float16"` or `"mixed_bfloat16"`, which causes the compute dtype to be `float16` or `bfloat16` and the variable dtype to be `float32`. |

Typically you only need to interact with dtype policies when using mixed
precision, which is the use of float16 or bfloat16 for computations and
float32 for variables. This is why the term `mixed_precision` appears in the
API name. Mixed precision can be enabled by passing `"mixed_float16"` or
`"mixed_bfloat16"` to `keras.mixed_precision.set_dtype_policy()`.

```
>>> keras.config.set_dtype_policy("mixed_float16")
>>> layer1 = keras.layers.Dense(10)
>>> layer1.dtype_policy  # layer1 will automatically use mixed precision
<DTypePolicy "mixed_float16">
>>> # Can optionally override layer to use float32
>>> # instead of mixed precision.
>>> layer2 = keras.layers.Dense(10, dtype="float32")
>>> layer2.dtype_policy
<DTypePolicy "float32">
>>> # Set policy back to initial float32.
>>> keras.config.set_dtype_policy('float32')
```

In the example above, passing `dtype="float32"` to the layer is
equivalent to passing
`dtype=keras.config.DTypePolicy("float32")`.
In general, passing a dtype policy name to a layer is equivalent
to passing the corresponding policy, so it is never necessary
to explicitly construct a `DTypePolicy` object.

| Attributes | |

|  |  |
| --- | --- |
| `compute_dtype` | The compute dtype of this policy. |

This is the dtype layers will do their computations in. Typically layers
output tensors with the compute dtype as well.

Note that even if the compute dtype is float16 or bfloat16, hardware
devices may not do individual adds, multiplies, and other fundamental
operations in float16 or bfloat16, but instead may do some of them in
float32 for numeric stability. The compute dtype is the dtype of the
inputs and outputs of the ops that the layer executes.
Internally, many ops will do certain internal calculations in
float32 or some other device-internal intermediate format with higher
precision than float16/bfloat16, to increase numeric stability.|  |  |
| --- | --- |
| `name` | Returns the name of this policy. |
| `variable_dtype` | The variable dtype of this policy. |

This is the dtype layers will create their variables in, unless a layer
explicitly chooses a different dtype. If this is different than
[`DTypePolicy.compute_dtype`](https://tensorflow.google.cn/api_docs/python/tf/keras/DTypePolicy#compute_dtype), Layers will cast variables to
the compute dtype to avoid type errors.

Variable regularizers are run in the variable dtype, not the compute
dtype.

## Methods

### `convert_input`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/dtype_policies/dtype_policy.py#L137-L157)

```
convert_input(
    x, autocast, dtype
)
```

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/dtype_policies/dtype_policy.py#L162-L164)

```
@classmethod
from_config(
    config
)
```

### `get_config`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/dtype_policies/dtype_policy.py#L159-L160)

```
get_config()
```
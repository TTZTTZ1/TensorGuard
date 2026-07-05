# tf.random_normal_initializer

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/random_normal_initializer](https://tensorflow.google.cn/api_docs/python/tf/random_normal_initializer)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/init_ops_v2.py#L371-L434) |

Initializer that generates tensors with a normal distribution.

```
tf.random_normal_initializer(
    mean=0.0, stddev=0.05, seed=None
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [pix2pix: Image-to-image translation with a conditional GAN](https://tensorflow.google.cn/tutorials/generative/pix2pix) |

Initializers allow you to pre-specify an initialization strategy, encoded in
the Initializer object, without knowing the shape and dtype of the variable
being initialized.

#### Examples:

```
>>> def make_variables(k, initializer):
...   return (tf.Variable(initializer(shape=[k], dtype=tf.float32)),
...           tf.Variable(initializer(shape=[k, k], dtype=tf.float32)))
>>> v1, v2 = make_variables(3,
...                         tf.random_normal_initializer(mean=1., stddev=2.))
>>> v1
<tf.Variable ... shape=(3,) ... numpy=array([...], dtype=float32)>
>>> v2
<tf.Variable ... shape=(3, 3) ... numpy=
... 
>>> make_variables(4, tf.random_uniform_initializer(minval=-1., maxval=1.))
(<tf.Variable...shape=(4,) dtype=float32...>, <tf.Variable...shape=(4, 4) ...
```

| Args | |

|  |  |
| --- | --- |
| `mean` | a python scalar or a scalar tensor. Mean of the random values to generate. |
| `stddev` | a python scalar or a scalar tensor. Standard deviation of the random values to generate. |
| `seed` | A Python integer. Used to create random seeds. See [`tf.random.set_seed`](https://tensorflow.google.cn/api_docs/python/tf/random/set_seed) for behavior. |

## Methods

### `from_config`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/init_ops_v2.py#L76-L96)

```
@classmethod
from_config(
    config
)
```

Instantiates an initializer from a configuration dictionary.

#### Example:

```
initializer = RandomUniform(-1, 1)
config = initializer.get_config()
initializer = RandomUniform.from_config(config)
```

| Args | |

|  |  |
| --- | --- |
| `config` | A Python dictionary. It will typically be the output of `get_config`. |

| Returns | |
| An Initializer instance. | |

### `get_config`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/init_ops_v2.py#L429-L434)

```
get_config()
```

Returns the configuration of the initializer as a JSON-serializable dict.

| Returns | |
| A JSON-serializable Python dict. | |

### `__call__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/init_ops_v2.py#L410-L427)

```
__call__(
    shape,
    dtype=tf.dtypes.float32,
    **kwargs
)

tf.dtypes.float32
```

Returns a tensor object initialized as specified by the initializer.

| Args | |

|  |  |
| --- | --- |
| `shape` | Shape of the tensor. |
| `dtype` | Optional dtype of the tensor. Only floating point types are supported. |
| `**kwargs` | Additional keyword arguments. |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If the dtype is not floating point |
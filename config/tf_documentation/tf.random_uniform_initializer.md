# tf.random_uniform_initializer

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/random_uniform_initializer](https://tensorflow.google.cn/api_docs/python/tf/random_uniform_initializer)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/init_ops_v2.py#L302-L368) |

Initializer that generates tensors with a uniform distribution.

```
tf.random_uniform_initializer(
    minval=-0.05, maxval=0.05, seed=None
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Parametrized Quantum Circuits for Reinforcement Learning](https://tensorflow.google.cn/quantum/tutorials/quantum_reinforcement_learning) |

Initializers allow you to pre-specify an initialization strategy, encoded in
the Initializer object, without knowing the shape and dtype of the variable
being initialized.

#### Examples:

```
>>> def make_variables(k, initializer):
...   return (tf.Variable(initializer(shape=[k], dtype=tf.float32)),
...           tf.Variable(initializer(shape=[k, k], dtype=tf.float32)))
>>> v1, v2 = make_variables(3, tf.ones_initializer())
>>> v1
<tf.Variable ... shape=(3,) ... numpy=array([1., 1., 1.], dtype=float32)>
>>> v2
<tf.Variable ... shape=(3, 3) ... numpy=
array([[1., 1., 1.],
       [1., 1., 1.],
       [1., 1., 1.]], dtype=float32)>
>>> make_variables(4, tf.random_uniform_initializer(minval=-1., maxval=1.))
(<tf.Variable...shape=(4,) dtype=float32...>, <tf.Variable...shape=(4, 4) ...
```

| Args | |

|  |  |
| --- | --- |
| `minval` | A python scalar or a scalar tensor. Lower bound of the range of random values to generate (inclusive). |
| `maxval` | A python scalar or a scalar tensor. Upper bound of the range of random values to generate (exclusive). |
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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/init_ops_v2.py#L363-L368)

```
get_config()
```

Returns the configuration of the initializer as a JSON-serializable dict.

| Returns | |
| A JSON-serializable Python dict. | |

### `__call__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/init_ops_v2.py#L341-L361)

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
| `dtype` | Optional dtype of the tensor. Only floating point and integer types are supported. |
| `**kwargs` | Additional keyword arguments. |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If the dtype is not numeric. |
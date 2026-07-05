# tf.Module

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/Module](https://tensorflow.google.cn/api_docs/python/tf/Module)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/module/module.py#L29-L313) |

Base neural network module class.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.Module`](https://tensorflow.google.cn/api_docs/python/tf/Module)

```
tf.Module(
    name=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Introduction to modules, layers, and models](https://tensorflow.google.cn/guide/intro_to_modules) * [Better performance with tf.function](https://tensorflow.google.cn/guide/function) * [Distributed training with Core APIs and DTensor](https://tensorflow.google.cn/guide/core/distribution) * [Logistic regression for binary classification with Core APIs](https://tensorflow.google.cn/guide/core/logistic_regression_core) * [Multilayer perceptrons for digit recognition with Core APIs](https://tensorflow.google.cn/guide/core/mlp_core) | * [Distributed training with DTensors](https://tensorflow.google.cn/tutorials/distribute/dtensor_ml_tutorial) * [DeepDream](https://tensorflow.google.cn/tutorials/generative/deepdream) * [Simple audio recognition: Recognizing keywords](https://tensorflow.google.cn/tutorials/audio/simple_audio) * [Neural machine translation with attention](https://tensorflow.google.cn/text/tutorials/nmt_with_attention) * [Neural machine translation with a Transformer and Keras](https://tensorflow.google.cn/text/tutorials/transformer) |

A module is a named container for [`tf.Variable`](https://tensorflow.google.cn/api_docs/python/tf/Variable)s, other [`tf.Module`](https://tensorflow.google.cn/api_docs/python/tf/Module)s and
functions which apply to user input. For example a dense layer in a neural
network might be implemented as a [`tf.Module`](https://tensorflow.google.cn/api_docs/python/tf/Module):

```
>>> class Dense(tf.Module):
...   def __init__(self, input_dim, output_size, name=None):
...     super().__init__(name=name)
...     self.w = tf.Variable(
...       tf.random.normal([input_dim, output_size]), name='w')
...     self.b = tf.Variable(tf.zeros([output_size]), name='b')
...   def __call__(self, x):
...     y = tf.matmul(x, self.w) + self.b
...     return tf.nn.relu(y)
```

You can use the Dense layer as you would expect:

```
>>> d = Dense(input_dim=3, output_size=2)
>>> d(tf.ones([1, 3]))
<tf.Tensor: shape=(1, 2), dtype=float32, numpy=..., dtype=float32)>
```

By subclassing [`tf.Module`](https://tensorflow.google.cn/api_docs/python/tf/Module) instead of `object` any [`tf.Variable`](https://tensorflow.google.cn/api_docs/python/tf/Variable) or
[`tf.Module`](https://tensorflow.google.cn/api_docs/python/tf/Module) instances assigned to object properties can be collected using
the `variables`, `trainable_variables` or `submodules` property:

```
>>> d.variables
    (<tf.Variable 'b:0' shape=(2,) dtype=float32, numpy=...,
    dtype=float32)>,
    <tf.Variable 'w:0' shape=(3, 2) dtype=float32, numpy=..., dtype=float32)>)
```

Subclasses of [`tf.Module`](https://tensorflow.google.cn/api_docs/python/tf/Module) can also take advantage of the `_flatten` method
which can be used to implement tracking of any other types.

All [`tf.Module`](https://tensorflow.google.cn/api_docs/python/tf/Module) classes have an associated [`tf.name_scope`](https://tensorflow.google.cn/api_docs/python/tf/name_scope) which can be used
to group operations in TensorBoard and create hierarchies for variable names
which can help with debugging. We suggest using the name scope when creating
nested submodules/parameters or for forward methods whose graph you might want
to inspect in TensorBoard. You can enter the name scope explicitly using
`with self.name_scope:` or you can annotate methods (apart from `__init__`)
with [`@tf.Module.with_name_scope`](https://tensorflow.google.cn/api_docs/python/tf/Module#with_name_scope).

```
>>> class MLP(tf.Module):
...   def __init__(self, input_size, sizes, name=None):
...     super().__init__(name=name)
...     self.layers = []
...     with self.name_scope:
...       for size in sizes:
...         self.layers.append(Dense(input_dim=input_size, output_size=size))
...         input_size = size
...   @tf.Module.with_name_scope
...   def __call__(self, x):
...     for layer in self.layers:
...       x = layer(x)
...     return x
```

```
>>> module = MLP(input_size=5, sizes=[5, 5])
>>> module.variables
(<tf.Variable 'mlp/b:0' shape=(5,) dtype=float32, numpy=..., dtype=float32)>,
<tf.Variable 'mlp/w:0' shape=(5, 5) dtype=float32, numpy=...,
   dtype=float32)>,
<tf.Variable 'mlp/b:0' shape=(5,) dtype=float32, numpy=..., dtype=float32)>,
<tf.Variable 'mlp/w:0' shape=(5, 5) dtype=float32, numpy=...,
   dtype=float32)>)
```

| Attributes | |

|  |  |
| --- | --- |
| `name` | Returns the name of this module as passed or determined in the ctor. |

**Note:** This is not the same as the `self.name_scope.name` which includes
parent module names.| `name_scope` | Returns a [`tf.name_scope`](https://tensorflow.google.cn/api_docs/python/tf/name_scope) instance for this class. |
| `non_trainable_variables` | Sequence of non-trainable variables owned by this module and its submodules. |
**Note:** this method uses reflection to find variables on the current instance
and submodules. For performance reasons you may wish to cache the result
of calling this method if you don't expect the return value to change.|  |  |
| --- | --- |
| `submodules` | Sequence of all sub-modules. |

Submodules are modules which are properties of this module, or found as
properties of modules which are properties of this module (and so on).

```
>>> a = tf.Module()
>>> b = tf.Module()
>>> c = tf.Module()
>>> a.b = b
>>> b.c = c
>>> list(a.submodules) == [b, c]
True
>>> list(b.submodules) == [c]
True
>>> list(c.submodules) == []
True
```

|  |  |
| --- | --- |
| `trainable_variables` | Sequence of trainable variables owned by this module and its submodules. |

**Note:** this method uses reflection to find variables on the current instance
and submodules. For performance reasons you may wish to cache the result
of calling this method if you don't expect the return value to change.|  |  |
| --- | --- |
| `variables` | Sequence of variables owned by this module and its submodules. |
**Note:** this method uses reflection to find variables on the current instance
and submodules. For performance reasons you may wish to cache the result
of calling this method if you don't expect the return value to change.

## Methods

### `with_name_scope`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/module/module.py#L282-L313)

```
@classmethod
with_name_scope(
    method
)
```

Decorator to automatically enter the module name scope.

```
>>> class MyModule(tf.Module):
...   @tf.Module.with_name_scope
...   def __call__(self, x):
...     if not hasattr(self, 'w'):
...       self.w = tf.Variable(tf.random.normal([x.shape[1], 3]))
...     return tf.matmul(x, self.w)
```

Using the above module would produce [`tf.Variable`](https://tensorflow.google.cn/api_docs/python/tf/Variable)s and [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor)s whose
names included the module name:

```
>>> mod = MyModule()
>>> mod(tf.ones([1, 2]))
<tf.Tensor: shape=(1, 3), dtype=float32, numpy=..., dtype=float32)>
>>> mod.w
<tf.Variable 'my_module/Variable:0' shape=(2, 3) dtype=float32,
numpy=..., dtype=float32)>
```

| Args | |

|  |  |
| --- | --- |
| `method` | The method to wrap. |

| Returns | |
| The original method wrapped such that it enters the module's name scope. | |
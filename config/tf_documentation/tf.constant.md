# tf.constant

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/constant](https://tensorflow.google.cn/api_docs/python/tf/constant)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/constant_op.py#L177-L277) |

Creates a constant tensor from a tensor-like object.

```
tf.constant(
    value, dtype=None, shape=None, name='Const'
) -> Union[tf.Operation, ops._EagerTensorBase]

tf.Operation
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Better performance with tf.function](https://tensorflow.google.cn/guide/function) * [TF-NumPy Type Promotion](https://tensorflow.google.cn/guide/tf_numpy_type_promotion) * [Introduction to Tensors](https://tensorflow.google.cn/guide/tensor) * [Introduction to graphs and tf.function](https://tensorflow.google.cn/guide/intro_to_graphs) * [Migrate `tf.feature\_column`s to Keras preprocessing layers](https://tensorflow.google.cn/guide/migrate/migrating_feature_columns) | * [DeepDream](https://tensorflow.google.cn/tutorials/generative/deepdream) * [Load text](https://tensorflow.google.cn/tutorials/load_data/text) * [Playing CartPole with the Actor-Critic method](https://tensorflow.google.cn/tutorials/reinforcement_learning/actor_critic) * [Neural style transfer](https://tensorflow.google.cn/tutorials/generative/style_transfer) * [Custom training loop with Keras and MultiWorkerMirroredStrategy](https://tensorflow.google.cn/tutorials/distribute/multi_worker_with_ctl) |

**Note:** All eager [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) values are immutable (in contrast to
[`tf.Variable`](https://tensorflow.google.cn/api_docs/python/tf/Variable)). There is nothing especially *constant* about the value
returned from [`tf.constant`](https://tensorflow.google.cn/api_docs/python/tf/constant). This function is not fundamentally different from
[`tf.convert_to_tensor`](https://tensorflow.google.cn/api_docs/python/tf/convert_to_tensor). The name [`tf.constant`](https://tensorflow.google.cn/api_docs/python/tf/constant) comes from the `value` being
embedded in a `Const` node in the [`tf.Graph`](https://tensorflow.google.cn/api_docs/python/tf/Graph). [`tf.constant`](https://tensorflow.google.cn/api_docs/python/tf/constant) is useful
for asserting that the value can be embedded that way.

If the argument `dtype` is not specified, then the type is inferred from
the type of `value`.

```
>>> # Constant 1-D Tensor from a python list.
>>> tf.constant([1, 2, 3, 4, 5, 6])
<tf.Tensor: shape=(6,), dtype=int32,
    numpy=array([1, 2, 3, 4, 5, 6], dtype=int32)>
>>> # Or a numpy array
>>> a = np.array([[1, 2, 3], [4, 5, 6]])
>>> tf.constant(a)
<tf.Tensor: shape=(2, 3), dtype=int64, numpy=
  array([[1, 2, 3],
         [4, 5, 6]])>
```

If `dtype` is specified, the resulting tensor values are cast to the requested
`dtype`.

```
>>> tf.constant([1, 2, 3, 4, 5, 6], dtype=tf.float64)
<tf.Tensor: shape=(6,), dtype=float64,
    numpy=array([1., 2., 3., 4., 5., 6.])>
```

If `shape` is set, the `value` is reshaped to match. Scalars are expanded to
fill the `shape`:

```
>>> tf.constant(0, shape=(2, 3))
  <tf.Tensor: shape=(2, 3), dtype=int32, numpy=
  array([[0, 0, 0],
         [0, 0, 0]], dtype=int32)>
>>> tf.constant([1, 2, 3, 4, 5, 6], shape=[2, 3])
<tf.Tensor: shape=(2, 3), dtype=int32, numpy=
  array([[1, 2, 3],
         [4, 5, 6]], dtype=int32)>
```

[`tf.constant`](https://tensorflow.google.cn/api_docs/python/tf/constant) has no effect if an eager Tensor is passed as the `value`, it
even transmits gradients:

```
>>> v = tf.Variable([0.0])
>>> with tf.GradientTape() as g:
...     loss = tf.constant(v + v)
>>> g.gradient(loss, v).numpy()
array([2.], dtype=float32)
```

But, since [`tf.constant`](https://tensorflow.google.cn/api_docs/python/tf/constant) embeds the value in the [`tf.Graph`](https://tensorflow.google.cn/api_docs/python/tf/Graph) this fails for
symbolic tensors:

```
>>> with tf.compat.v1.Graph().as_default():
...   i = tf.compat.v1.placeholder(shape=[None, None], dtype=tf.float32)
...   t = tf.constant(i)
Traceback (most recent call last):
... 
TypeError: ...
```

[`tf.constant`](https://tensorflow.google.cn/api_docs/python/tf/constant) will create tensors on the current device. Inputs which are
already tensors maintain their placements unchanged.

#### Related Ops:

* [`tf.convert_to_tensor`](https://tensorflow.google.cn/api_docs/python/tf/convert_to_tensor) is similar but:

  + It has no `shape` argument.
  + Symbolic tensors are allowed to pass through.

  ```
  >>> with tf.compat.v1.Graph().as_default():
  ...   i = tf.compat.v1.placeholder(shape=[None, None], dtype=tf.float32)
  ...   t = tf.convert_to_tensor(i)
  ```
* [`tf.fill`](https://tensorflow.google.cn/api_docs/python/tf/fill): differs in a few ways:

  + [`tf.constant`](https://tensorflow.google.cn/api_docs/python/tf/constant) supports arbitrary constants, not just uniform scalar
    Tensors like [`tf.fill`](https://tensorflow.google.cn/api_docs/python/tf/fill).
  + [`tf.fill`](https://tensorflow.google.cn/api_docs/python/tf/fill) creates an Op in the graph that is expanded at runtime, so it
    can efficiently represent large tensors.
  + Since [`tf.fill`](https://tensorflow.google.cn/api_docs/python/tf/fill) does not embed the value, it can produce dynamically
    sized outputs.

| Args | |

|  |  |
| --- | --- |
| `value` | A constant value (or list) of output type `dtype`. |
| `dtype` | The type of the elements of the resulting tensor. |
| `shape` | Optional dimensions of resulting tensor. |
| `name` | Optional name for the tensor. |

| Returns | |
| A Constant Tensor. | |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | if shape is incorrectly specified or unsupported. |
| `ValueError` | if called on a symbolic tensor. |
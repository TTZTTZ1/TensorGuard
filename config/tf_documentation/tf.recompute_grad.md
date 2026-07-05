# tf.recompute_grad

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/recompute_grad](https://tensorflow.google.cn/api_docs/python/tf/recompute_grad)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/custom_gradient.py#L600-L770) |

Defines a function as a recompute-checkpoint for the tape auto-diff.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.recompute_grad`](https://tensorflow.google.cn/api_docs/python/tf/recompute_grad)

```
tf.recompute_grad(
    f
)
```

Tape checkpointing is a technique to reduce the memory consumption of the
auto-diff tape:

* Without tape checkpointing operations and intermediate values are
  recorded to the tape for use in the backward pass.
* With tape checkpointing, only the function call and its inputs are
  recorded. During back-propagation the `recompute_grad` custom gradient
  ([`tf.custom_gradient`](https://tensorflow.google.cn/api_docs/python/tf/custom_gradient)) recomputes the function under a localized Tape object.
  This recomputation of the function during backpropagation performs redundant
  calculation, but reduces the overall memory usage of the Tape.

```
>>> y = tf.Variable(1.0)
```

```
>>> def my_function(x):
...   tf.print('running')
...   z = x*y
...   return z
```

```
>>> my_function_recompute = tf.recompute_grad(my_function)
```

```
>>> with tf.GradientTape() as tape:
...   r = tf.constant(1.0)
...   for i in range(4):
...     r = my_function_recompute(r)
running
running
running
running
```

```
>>> grad = tape.gradient(r, [y])
running
running
running
running
```

Without `recompute_grad`, the tape contains all intermitate steps, and no
recomputation is performed.

```
>>> with tf.GradientTape() as tape:
...   r = tf.constant(1.0)
...   for i in range(4):
...     r = my_function(r)
running
running
running
running
```

```
>>> grad = tape.gradient(r, [y])
```

If `f` was a [`tf.keras`](https://tensorflow.google.cn/api_docs/python/tf/keras) `Model` or `Layer` object, methods and attributes
such as `f.variables` are not available on the returned function `g`.
Either keep a reference of `f` , or use `g.__wrapped__` for accessing
these variables and methods.

```
>>> def print_running_and_return(x):
...   tf.print("running")
...   return x
```

```
>>> model = tf.keras.Sequential([
...   tf.keras.layers.Lambda(print_running_and_return),
...   tf.keras.layers.Dense(2)
... ])
```

```
>>> model_recompute = tf.recompute_grad(model)
```

```
>>> with tf.GradientTape(persistent=True) as tape:
...   r = tf.constant([[1,2]])
...   for i in range(4):
...     r = model_recompute(r)
running
running
running
running
```

```
>>> grad = tape.gradient(r, model.variables)
running
running
running
running
```

Alternatively, use the `__wrapped__` attribute to access the original
model object.

```
>>> grad = tape.gradient(r, model_recompute.__wrapped__.variables)
running
running
running
running
```

| Args | |

|  |  |
| --- | --- |
| `f` | function `f(*x)` that returns a `Tensor` or sequence of `Tensor` outputs. |

| Returns | |
| A function `g` wrapping `f` that defines a custom gradient, which recomputes `f` on the backwards pass of a gradient call. | |
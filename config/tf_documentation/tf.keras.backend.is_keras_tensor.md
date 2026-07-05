# tf.keras.backend.is_keras_tensor

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/backend/is_keras_tensor](https://tensorflow.google.cn/api_docs/python/tf/keras/backend/is_keras_tensor)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/backend/common/keras_tensor.py#L302-L313) |

Returns whether `x` is a Keras tensor.

#### View aliases

**Main aliases**

[`tf.keras.utils.is_keras_tensor`](https://tensorflow.google.cn/api_docs/python/tf/keras/backend/is_keras_tensor)

```
tf.keras.backend.is_keras_tensor(
    x
)
```

A "Keras tensor" is a *symbolic tensor*, such as a tensor
that was created via `Input()`. A "symbolic tensor"
can be understood as a placeholder -- it does not
contain any actual numerical data, only a shape and dtype.
It can be used for building Functional models, but it
cannot be used in actual computations.
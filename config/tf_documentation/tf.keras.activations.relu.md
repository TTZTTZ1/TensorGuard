# tf.keras.activations.relu

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/activations/relu](https://tensorflow.google.cn/api_docs/python/tf/keras/activations/relu)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/activations/activations.py#L6-L52) |

Applies the rectified linear unit activation function.

```
tf.keras.activations.relu(
    x, negative_slope=0.0, max_value=None, threshold=0.0
)
```

With default values, this returns the standard ReLU activation:
`max(x, 0)`, the element-wise maximum of 0 and the input tensor.

Modifying default parameters allows you to use non-zero thresholds,
change the max value of the activation,
and to use a non-zero multiple of the input for values below the threshold.

#### Examples:

```
>>> x = [-10, -5, 0.0, 5, 10]
>>> keras.activations.relu(x)
[ 0.,  0.,  0.,  5., 10.]
>>> keras.activations.relu(x, negative_slope=0.5)
[-5. , -2.5,  0. ,  5. , 10. ]
>>> keras.activations.relu(x, max_value=5.)
[0., 0., 0., 5., 5.]
>>> keras.activations.relu(x, threshold=5.)
[-0., -0.,  0.,  0., 10.]
```

| Args | |

|  |  |
| --- | --- |
| `x` | Input tensor. |
| `negative_slope` | A `float` that controls the slope for values lower than the threshold. |
| `max_value` | A `float` that sets the saturation threshold (the largest value the function will return). |
| `threshold` | A `float` giving the threshold value of the activation function below which values will be damped or set to zero. |

| Returns | |
| A tensor with the same shape and dtype as input `x`. | |
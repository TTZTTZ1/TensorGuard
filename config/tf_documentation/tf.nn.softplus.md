# tf.nn.softplus

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/nn/softplus](https://tensorflow.google.cn/api_docs/python/tf/nn/softplus)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L628-L651) |

Computes elementwise softplus: `softplus(x) = log(exp(x) + 1)`.

#### View aliases

**Main aliases**

[`tf.nn.softplus`](https://tensorflow.google.cn/api_docs/python/tf/math/softplus)

```
tf.math.softplus(
    features, name=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Introduction to gradients and automatic differentiation](https://tensorflow.google.cn/guide/autodiff) | * [TFP Probabilistic Layers: Regression](https://tensorflow.google.cn/probability/examples/Probabilistic_Layers_Regression) * [Gaussian Process Latent Variable Models](https://tensorflow.google.cn/probability/examples/Gaussian_Process_Latent_Variable_Model) * [Bayesian Modeling with Joint Distribution](https://tensorflow.google.cn/probability/examples/Modeling_with_JointDistribution) |

`softplus` is a smooth approximation of `relu`. Like `relu`, `softplus` always
takes on positive values.

![](https://tensorflow.google.cn/images/softplus.png)

#### Example:

```
>>> import tensorflow as tf
>>> tf.math.softplus(tf.range(0, 2, dtype=tf.float32)).numpy()
array([0.6931472, 1.3132616], dtype=float32)
```

| Args | |

|  |  |
| --- | --- |
| `features` | `Tensor` |
| `name` | Optional: name to associate with this operation. |

| Returns | |
| `Tensor` | |
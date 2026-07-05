# tf.nn.silu

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/nn/silu](https://tensorflow.google.cn/api_docs/python/tf/nn/silu)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/nn_impl.py#L430-L483) |

Computes the SiLU or Swish activation function: `x * sigmoid(beta * x)`.

#### View aliases

**Main aliases**

[`tf.nn.swish`](https://tensorflow.google.cn/api_docs/python/tf/nn/silu)

```
tf.nn.silu(
    features, beta=1.0
)
```

beta : Hyperparameter for Swish activation function. Default value 1.0.

The SiLU activation function was introduced in "Gaussian Error Linear Units
(GELUs)" [Hendrycks et al. 2016](https://arxiv.org/abs/1606.08415) and
"Sigmoid-Weighted Linear Units for Neural Network Function Approximation in
Reinforcement Learning"
[Elfwing et al. 2017](https://arxiv.org/abs/1702.03118) and was independently
discovered (and called swish) in "Searching for Activation Functions"
[Ramachandran et al. 2017](https://arxiv.org/abs/1710.05941)

| Args | |

|  |  |
| --- | --- |
| `features` | A `Tensor` representing preactivation values. |
| `beta` | A 'Tensor' representing value of beta hyperparameter. |

| Returns | |
| The activation value. | |
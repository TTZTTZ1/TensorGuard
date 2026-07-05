# tf.nn.relu

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/nn/relu](https://tensorflow.google.cn/api_docs/python/tf/nn/relu)

---

Computes rectified linear: `max(features, 0)`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.nn.relu`](https://tensorflow.google.cn/api_docs/python/tf/nn/relu)

```
tf.nn.relu(
    features: Annotated[Any, TV_Relu_T], name=None
) -> Annotated[Any, TV_Relu_T]
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Introduction to modules, layers, and models](https://tensorflow.google.cn/guide/intro_to_modules) * [Multilayer perceptrons for digit recognition with Core APIs](https://tensorflow.google.cn/guide/core/mlp_core) * [Understanding masking & padding](https://tensorflow.google.cn/guide/keras/understanding_masking_and_padding) | * [Custom layers](https://tensorflow.google.cn/tutorials/customization/custom_layers) * [Generating Images with BigBiGAN](https://tensorflow.google.cn/hub/tutorials/bigbigan_with_tf_hub) * [Examining the TensorFlow Graph](https://tensorflow.google.cn/tensorboard/graphs) |

See: <https://en.wikipedia.org/wiki/Rectifier_(neural_networks)>
Example usage:

```
>>> tf.nn.relu([-2., 0., 3.]).numpy()
array([0., 0., 3.], dtype=float32)
```

| Args | |

|  |  |
| --- | --- |
| `features` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`, `qint8`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `features`. | |
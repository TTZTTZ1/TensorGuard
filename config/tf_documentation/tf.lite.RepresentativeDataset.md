# tf.lite.RepresentativeDataset

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/lite/RepresentativeDataset](https://tensorflow.google.cn/api_docs/python/tf/lite/RepresentativeDataset)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/lite/python/lite.py#L161-L182) |

Representative dataset used to optimize the model.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.lite.RepresentativeDataset`](https://tensorflow.google.cn/api_docs/python/tf/lite/RepresentativeDataset)

```
tf.lite.RepresentativeDataset(
    input_gen
)
```

This is a generator function that provides a small dataset to calibrate or
estimate the range, i.e, (min, max) of all floating-point arrays in the model
(such as model input, activation outputs of intermediate layers, and model
output) for quantization. Usually, this is a small subset of a few hundred
samples randomly chosen, in no particular order, from the training or
evaluation dataset.

| Args | |

|  |  |
| --- | --- |
| `input_gen` | A generator function that generates input samples for the model and has the same order, type and shape as the inputs to the model. Usually, this is a small subset of a few hundred samples randomly chosen, in no particular order, from the training or evaluation dataset. |
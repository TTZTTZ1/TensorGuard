# tf.lite.Optimize

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/lite/Optimize](https://tensorflow.google.cn/api_docs/python/tf/lite/Optimize)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/lite/python/lite.py#L102-L157) |

Enum defining the optimizations to apply when generating a tflite model.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.lite.Optimize`](https://tensorflow.google.cn/api_docs/python/tf/lite/Optimize)

DEFAULT
The default optimization strategy that enables post-training quantization.
The type of post-training quantization that will be used is dependent on
the other converter options supplied. Refer to the
[documentation](/lite/performance/post_training_quantization) for further
information on the types available and how to use them.

OPTIMIZE\_FOR\_SIZE
Deprecated. Does the same as DEFAULT.

OPTIMIZE\_FOR\_LATENCY
Deprecated. Does the same as DEFAULT.

EXPERIMENTAL\_SPARSITY
Experimental flag, subject to change.

```
Enable optimization by taking advantage of the sparse model weights
trained with pruning.

The converter will inspect the sparsity pattern of the model weights and
do its best to improve size and latency.
The flag can be used alone to optimize float32 models with sparse weights.
It can also be used together with the DEFAULT optimization mode to
optimize quantized models with sparse weights.
```

| Class Variables | |

|  |  |
| --- | --- |
| DEFAULT | `<Optimize.DEFAULT: 'DEFAULT'>` |
| EXPERIMENTAL\_SPARSITY | `<Optimize.EXPERIMENTAL_SPARSITY: 'EXPERIMENTAL_SPARSITY'>` |
| OPTIMIZE\_FOR\_LATENCY | `<Optimize.OPTIMIZE_FOR_LATENCY: 'OPTIMIZE_FOR_LATENCY'>` |
| OPTIMIZE\_FOR\_SIZE | `<Optimize.OPTIMIZE_FOR_SIZE: 'OPTIMIZE_FOR_SIZE'>` |
# tf.nn.compute_average_loss

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/nn/compute_average_loss](https://tensorflow.google.cn/api_docs/python/tf/nn/compute_average_loss)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/nn_impl_distribute.py#L70-L142) |

Scales per-example losses with sample\_weights and computes their average.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.nn.compute_average_loss`](https://tensorflow.google.cn/api_docs/python/tf/nn/compute_average_loss)

```
tf.nn.compute_average_loss(
    per_example_loss, sample_weight=None, global_batch_size=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Use TPUs](https://tensorflow.google.cn/guide/tpu) * [Distributed training with TensorFlow](https://tensorflow.google.cn/guide/distributed_training) | * [Custom training with tf.distribute.Strategy](https://tensorflow.google.cn/tutorials/distribute/custom_training) * [Custom training loop with Keras and MultiWorkerMirroredStrategy](https://tensorflow.google.cn/tutorials/distribute/multi_worker_with_ctl) * [Parameter server training with ParameterServerStrategy](https://tensorflow.google.cn/tutorials/distribute/parameter_server_training) |

Usage with distribution strategy and custom training loop:

```
with strategy.scope():
  def compute_loss(labels, predictions, sample_weight=None):

    # If you are using a `Loss` class instead, set reduction to `NONE` so that
    # we can do the reduction afterwards and divide by global batch size.
    per_example_loss = tf.keras.losses.sparse_categorical_crossentropy(
        labels, predictions)

    # Compute loss that is scaled by sample_weight and by global batch size.
    return tf.nn.compute_average_loss(
        per_example_loss,
        sample_weight=sample_weight,
        global_batch_size=GLOBAL_BATCH_SIZE)
```

| Args | |

|  |  |
| --- | --- |
| `per_example_loss` | Per-example loss. |
| `sample_weight` | Optional weighting for each example. |
| `global_batch_size` | Optional global batch size value. Defaults to (size of first dimension of `losses`) \* (number of replicas). |

| Returns | |
| Scalar loss value, obtained by summing the `per_example_loss` and dividing by `global_batch_size`. If `global_batch_size` is zero, the result is zero. | |
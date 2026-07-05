# tf.nn.scale_regularization_loss

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/nn/scale_regularization_loss](https://tensorflow.google.cn/api_docs/python/tf/nn/scale_regularization_loss)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/nn_impl_distribute.py#L27-L67) |

Scales the sum of the given regularization losses by number of replicas.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.nn.scale_regularization_loss`](https://tensorflow.google.cn/api_docs/python/tf/nn/scale_regularization_loss)

```
tf.nn.scale_regularization_loss(
    regularization_loss
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Distributed training with TensorFlow](https://tensorflow.google.cn/guide/distributed_training) | * [Custom training with tf.distribute.Strategy](https://tensorflow.google.cn/tutorials/distribute/custom_training) * [Custom training loop with Keras and MultiWorkerMirroredStrategy](https://tensorflow.google.cn/tutorials/distribute/multi_worker_with_ctl) * [Parameter server training with ParameterServerStrategy](https://tensorflow.google.cn/tutorials/distribute/parameter_server_training) |

Usage with distribution strategy and custom training loop:

```
with strategy.scope():
  def compute_loss(self, label, predictions):
    per_example_loss = tf.keras.losses.sparse_categorical_crossentropy(
        labels, predictions)

    # Compute loss that is scaled by sample_weight and by global batch size.
    loss = tf.nn.compute_average_loss(
        per_example_loss,
        sample_weight=sample_weight,
        global_batch_size=GLOBAL_BATCH_SIZE)

    # Add scaled regularization losses.
    loss += tf.nn.scale_regularization_loss(tf.nn.l2_loss(weights))
    return loss
```

| Args | |

|  |  |
| --- | --- |
| `regularization_loss` | Regularization loss. |

| Returns | |
| Scalar loss value. | |
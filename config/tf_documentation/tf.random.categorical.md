# tf.random.categorical

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/random/categorical](https://tensorflow.google.cn/api_docs/python/tf/random/categorical)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/random_ops.py#L394-L421) |

Draws samples from a categorical distribution.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.random.categorical`](https://tensorflow.google.cn/api_docs/python/tf/random/categorical)

```
tf.random.categorical(
    logits, num_samples, dtype=None, seed=None, name=None
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Generate music with an RNN](https://tensorflow.google.cn/tutorials/audio/music_generation) * [Playing CartPole with the Actor-Critic method](https://tensorflow.google.cn/tutorials/reinforcement_learning/actor_critic) * [Text generation with an RNN](https://tensorflow.google.cn/text/tutorials/text_generation) * [Wiki40B Language Models](https://tensorflow.google.cn/hub/tutorials/wiki40b_lm) * [Federated Learning for Text Generation](https://tensorflow.google.cn/federated/tutorials/federated_learning_for_text_generation) |

#### Example:

```
# samples has shape [1, 5], where each value is either 0 or 1 with equal
# probability.
samples = tf.random.categorical(tf.math.log([[0.5, 0.5]]), 5)
```

| Args | |

|  |  |
| --- | --- |
| `logits` | 2-D Tensor with shape `[batch_size, num_classes]`. Each slice `[i, :]` represents the unnormalized log-probabilities for all classes. |
| `num_samples` | 0-D. Number of independent samples to draw for each row slice. |
| `dtype` | The integer type of the output: `int32` or `int64`. Defaults to `int64`. |
| `seed` | A Python integer. Used to create a random seed for the distribution. See [`tf.random.set_seed`](https://tensorflow.google.cn/api_docs/python/tf/random/set_seed) for behavior. |
| `name` | Optional name for the operation. |

| Returns | |
| The drawn samples of shape `[batch_size, num_samples]`. | |
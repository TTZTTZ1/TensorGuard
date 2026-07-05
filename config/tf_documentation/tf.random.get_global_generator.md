# tf.random.get_global_generator

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/random/get_global_generator](https://tensorflow.google.cn/api_docs/python/tf/random/get_global_generator)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/stateful_random_ops.py#L975-L997) |

Retrieves the global generator.

#### View aliases

**Main aliases**

[`tf.random.experimental.get_global_generator`](https://tensorflow.google.cn/api_docs/python/tf/random/get_global_generator)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.random.experimental.get_global_generator`](https://tensorflow.google.cn/api_docs/python/tf/random/get_global_generator), [`tf.compat.v1.random.get_global_generator`](https://tensorflow.google.cn/api_docs/python/tf/random/get_global_generator)

```
tf.random.get_global_generator()
```

### Used in the notebooks

| Used in the guide |
| --- |
| * [Random number generation](https://tensorflow.google.cn/guide/random_numbers) |

This function will create the global generator the first time it is called,
and the generator will be placed at the default device at that time, so one
needs to be careful when this function is first called. Using a generator
placed on a less-ideal device will incur performance regression.

| Returns | |
| The global [`tf.random.Generator`](https://tensorflow.google.cn/api_docs/python/tf/random/Generator) object. | |
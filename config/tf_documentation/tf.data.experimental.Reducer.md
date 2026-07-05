# tf.data.experimental.Reducer

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/data/experimental/Reducer](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/Reducer)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/experimental/ops/grouping.py#L388-L428) |

A reducer is used for reducing a set of elements.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.data.experimental.Reducer`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/Reducer)

```
tf.data.experimental.Reducer(
    init_func, reduce_func, finalize_func
)
```

A reducer is represented as a tuple of the three functions:

* init\_func - to define initial value: key => initial state
* reducer\_func - operation to perform on values with same key: (old state, input) => new state
* finalize\_func - value to return in the end: state => result

For example,

```
def init_func(_):
  return (0.0, 0.0)

def reduce_func(state, value):
  return (state[0] + value['features'], state[1] + 1)

def finalize_func(s, n):
  return s / n

reducer = tf.data.experimental.Reducer(init_func, reduce_func, finalize_func)
```

| Attributes | |

|  |  |
| --- | --- |
| `finalize_func` |  |

|  |  |
| --- | --- |
| `init_func` |  |

|  |  |
| --- | --- |
| `reduce_func` |  |
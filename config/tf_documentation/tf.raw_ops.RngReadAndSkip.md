# tf.raw_ops.RngReadAndSkip

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RngReadAndSkip](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RngReadAndSkip)

---

Advance the counter of a counter-based RNG.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.RngReadAndSkip`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RngReadAndSkip)

```
tf.raw_ops.RngReadAndSkip(
    resource, alg, delta, name=None
)
```

The state of the RNG after
`rng_read_and_skip(n)` will be the same as that after `uniform([n])`
(or any other distribution). The actual increment added to the
counter is an unspecified implementation choice.

In the case that the input algorithm is RNG\_ALG\_AUTO\_SELECT, the counter in the state needs to be of size int64[2], the current maximal counter size among algorithms. In this case, this op will manage the counter as if it is an 128-bit integer with layout [lower\_64bits, higher\_64bits]. If an algorithm needs less than 128 bits for the counter, it should use the left portion of the int64[2]. In this way, the int64[2] is compatible with all current RNG algorithms (Philox, ThreeFry and xla::RandomAlgorithm::RNG\_DEFAULT). Downstream RNG ops can thus use this counter with any RNG algorithm.

| Args | |

|  |  |
| --- | --- |
| `resource` | A `Tensor` of type `resource`. The handle of the resource variable that stores the state of the RNG. The state consists of the counter followed by the key. |
| `alg` | A `Tensor` of type `int32`. The RNG algorithm. |
| `delta` | A `Tensor` of type `uint64`. The amount of advancement. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `int64`. | |
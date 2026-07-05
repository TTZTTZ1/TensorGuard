# tf.raw_ops.ComputeAccidentalHits

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ComputeAccidentalHits](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ComputeAccidentalHits)

---

Computes the ids of the positions in sampled\_candidates that match true\_labels.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ComputeAccidentalHits`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ComputeAccidentalHits)

```
tf.raw_ops.ComputeAccidentalHits(
    true_classes, sampled_candidates, num_true, seed=0, seed2=0, name=None
)
```

When doing log-odds NCE, the result of this op should be passed through a
SparseToDense op, then added to the logits of the sampled candidates. This has
the effect of 'removing' the sampled labels that match the true labels by
making the classifier sure that they are sampled labels.

| Args | |

|  |  |
| --- | --- |
| `true_classes` | A `Tensor` of type `int64`. The true\_classes output of UnpackSparseLabels. |
| `sampled_candidates` | A `Tensor` of type `int64`. The sampled\_candidates output of CandidateSampler. |
| `num_true` | An `int`. Number of true labels per context. |
| `seed` | An optional `int`. Defaults to `0`. If either seed or seed2 are set to be non-zero, the random number generator is seeded by the given seed. Otherwise, it is seeded by a random seed. |
| `seed2` | An optional `int`. Defaults to `0`. An second seed to avoid seed collision. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (indices, ids, weights). | |
| `indices` | A `Tensor` of type `int32`. |
| `ids` | A `Tensor` of type `int64`. |
| `weights` | A `Tensor` of type `float32`. |
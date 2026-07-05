# tf.raw_ops.NonMaxSuppressionWithOverlaps

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/NonMaxSuppressionWithOverlaps](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/NonMaxSuppressionWithOverlaps)

---

Greedily selects a subset of bounding boxes in descending order of score,

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.NonMaxSuppressionWithOverlaps`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/NonMaxSuppressionWithOverlaps)

```
tf.raw_ops.NonMaxSuppressionWithOverlaps(
    overlaps,
    scores,
    max_output_size,
    overlap_threshold,
    score_threshold,
    name=None
)
```

pruning away boxes that have high overlaps
with previously selected boxes. Bounding boxes with score less than
`score_threshold` are removed. N-by-n overlap values are supplied as square matrix,
which allows for defining a custom overlap criterium (eg. intersection over union,
intersection over area, etc.).

The output of this operation is a set of integers indexing into the input
collection of bounding boxes representing the selected boxes. The bounding
box coordinates corresponding to the selected indices can then be obtained
using the `tf.gather operation`. For example:

selected\_indices = tf.image.non\_max\_suppression\_with\_overlaps(
overlaps, scores, max\_output\_size, overlap\_threshold, score\_threshold)
selected\_boxes = tf.gather(boxes, selected\_indices)

| Args | |

|  |  |
| --- | --- |
| `overlaps` | A `Tensor` of type `float32`. A 2-D float tensor of shape `[num_boxes, num_boxes]` representing the n-by-n box overlap values. |
| `scores` | A `Tensor` of type `float32`. A 1-D float tensor of shape `[num_boxes]` representing a single score corresponding to each box (each row of boxes). |
| `max_output_size` | A `Tensor` of type `int32`. A scalar integer tensor representing the maximum number of boxes to be selected by non max suppression. |
| `overlap_threshold` | A `Tensor` of type `float32`. A 0-D float tensor representing the threshold for deciding whether boxes overlap too. |
| `score_threshold` | A `Tensor` of type `float32`. A 0-D float tensor representing the threshold for deciding when to remove boxes based on score. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `int32`. | |
# tf.image.non_max_suppression_padded

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/image/non_max_suppression_padded](https://tensorflow.google.cn/api_docs/python/tf/image/non_max_suppression_padded)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/image_ops_impl.py#L5403-L5493) |

Greedily selects a subset of bounding boxes in descending order of score.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.image.non_max_suppression_padded`](https://tensorflow.google.cn/api_docs/python/tf/image/non_max_suppression_padded)

```
tf.image.non_max_suppression_padded(
    boxes,
    scores,
    max_output_size,
    iou_threshold=0.5,
    score_threshold=float('-inf'),
    pad_to_max_output_size=False,
    name=None,
    sorted_input=False,
    canonicalized_coordinates=False,
    tile_size=512
)
```

Performs algorithmically equivalent operation to tf.image.non\_max\_suppression,
with the addition of an optional parameter which zero-pads the output to
be of size `max_output_size`.
The output of this operation is a tuple containing the set of integers
indexing into the input collection of bounding boxes representing the selected
boxes and the number of valid indices in the index set. The bounding box
coordinates corresponding to the selected indices can then be obtained using
the [`tf.slice`](https://tensorflow.google.cn/api_docs/python/tf/slice) and [`tf.gather`](https://tensorflow.google.cn/api_docs/python/tf/gather) operations. For example:

```
  selected_indices_padded, num_valid = tf.image.non_max_suppression_padded(
      boxes, scores, max_output_size, iou_threshold,
      score_threshold, pad_to_max_output_size=True)
  selected_indices = tf.slice(
      selected_indices_padded, tf.constant([0]), num_valid)
  selected_boxes = tf.gather(boxes, selected_indices)
```

| Args | |

|  |  |
| --- | --- |
| `boxes` | a tensor of rank 2 or higher with a shape of [..., num\_boxes, 4]. Dimensions except the last two are batch dimensions. |
| `scores` | a tensor of rank 1 or higher with a shape of [..., num\_boxes]. |
| `max_output_size` | a scalar integer `Tensor` representing the maximum number of boxes to be selected by non max suppression. Note that setting this value to a large number may result in OOM error depending on the system workload. |
| `iou_threshold` | a float representing the threshold for deciding whether boxes overlap too much with respect to IoU (intersection over union). |
| `score_threshold` | a float representing the threshold for box scores. Boxes with a score that is not larger than this threshold will be suppressed. |
| `pad_to_max_output_size` | whether to pad the output idx to max\_output\_size. Must be set to True when the input is a batch of images. |
| `name` | name of operation. |
| `sorted_input` | a boolean indicating whether the input boxes and scores are sorted in descending order by the score. |
| `canonicalized_coordinates` | if box coordinates are given as `[y_min, x_min, y_max, x_max]`, setting to True eliminate redundant computation to canonicalize box coordinates. |
| `tile_size` | an integer representing the number of boxes in a tile, i.e., the maximum number of boxes per image that can be used to suppress other boxes in parallel; larger tile\_size means larger parallelism and potentially more redundant work. |

| Returns | |
| idx: a tensor with a shape of [..., num\_boxes] representing the indices selected by non-max suppression. The leading dimensions are the batch dimensions of the input boxes. All numbers are within [0, num\_boxes). For each image (i.e., idx[i]), only the first num\_valid[i] indices (i.e., idx[i][:num\_valid[i]]) are valid. num\_valid: a tensor of rank 0 or higher with a shape of [...] representing the number of valid indices in idx. Its dimensions are the batch dimensions of the input boxes. | |
| `Raises` | ValueError: When set pad\_to\_max\_output\_size to False for batched input. |
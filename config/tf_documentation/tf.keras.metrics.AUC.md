# tf.keras.metrics.AUC

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/AUC](https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/AUC)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/confusion_metrics.py#L1070-L1579) |

Approximates the AUC (Area under the curve) of the ROC or PR curves.

Inherits From: [`Metric`](https://tensorflow.google.cn/api_docs/python/tf/keras/Metric)

```
tf.keras.metrics.AUC(
    num_thresholds=200,
    curve='ROC',
    summation_method='interpolation',
    name=None,
    dtype=None,
    thresholds=None,
    multi_label=False,
    num_labels=None,
    label_weights=None,
    from_logits=False
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Classification on imbalanced data](https://tensorflow.google.cn/tutorials/structured_data/imbalanced_data) * [Client-efficient large-model federated learning via `federated\_select` and sparse aggregation](https://tensorflow.google.cn/federated/tutorials/sparse_federated_learning) |

The AUC (Area under the curve) of the ROC (Receiver operating
characteristic; default) or PR (Precision Recall) curves are quality
measures of binary classifiers. Unlike the accuracy, and like cross-entropy
losses, ROC-AUC and PR-AUC evaluate all the operational points of a model.

This class approximates AUCs using a Riemann sum. During the metric
accumulation phrase, predictions are accumulated within predefined buckets
by value. The AUC is then computed by interpolating per-bucket averages.
These buckets define the evaluated operational points.

This metric creates four local variables, `true_positives`,
`true_negatives`, `false_positives` and `false_negatives` that are used to
compute the AUC. To discretize the AUC curve, a linearly spaced set of
thresholds is used to compute pairs of recall and precision values. The area
under the ROC-curve is therefore computed using the height of the recall
values by the false positive rate, while the area under the PR-curve is the
computed using the height of the precision values by the recall.

This value is ultimately returned as `auc`, an idempotent operation that
computes the area under a discretized curve of precision versus recall
values (computed using the aforementioned variables). The `num_thresholds`
variable controls the degree of discretization with larger numbers of
thresholds more closely approximating the true AUC. The quality of the
approximation may vary dramatically depending on `num_thresholds`. The
`thresholds` parameter can be used to manually specify thresholds which
split the predictions more evenly.

For a best approximation of the real AUC, `predictions` should be
distributed approximately uniformly in the range `[0, 1]` (if
`from_logits=False`). The quality of the AUC approximation may be poor if
this is not the case. Setting `summation_method` to 'minoring' or 'majoring'
can help quantify the error in the approximation by providing lower or upper
bound estimate of the AUC.

If `sample_weight` is `None`, weights default to 1.
Use `sample_weight` of 0 to mask values.

| Args | |

|  |  |
| --- | --- |
| `num_thresholds` | (Optional) The number of thresholds to use when discretizing the roc curve. Values must be > 1. Defaults to `200`. |
| `curve` | (Optional) Specifies the name of the curve to be computed, `'ROC'` (default) or `'PR'` for the Precision-Recall-curve. |
| `summation_method` | (Optional) Specifies the [Riemann summation method](https://en.wikipedia.org/wiki/Riemann_sum) used. 'interpolation' (default) applies mid-point summation scheme for `ROC`. For PR-AUC, interpolates (true/false) positives but not the ratio that is precision (see Davis & Goadrich 2006 for details); 'minoring' applies left summation for increasing intervals and right summation for decreasing intervals; 'majoring' does the opposite. |
| `name` | (Optional) string name of the metric instance. |
| `dtype` | (Optional) data type of the metric result. |
| `thresholds` | (Optional) A list of floating point values to use as the thresholds for discretizing the curve. If set, the `num_thresholds` parameter is ignored. Values should be in `[0, 1]`. Endpoint thresholds equal to {`-epsilon`, `1+epsilon`} for a small positive epsilon value will be automatically included with these to correctly handle predictions equal to exactly 0 or 1. |
| `multi_label` | boolean indicating whether multilabel data should be treated as such, wherein AUC is computed separately for each label and then averaged across labels, or (when `False`) if the data should be flattened into a single label before AUC computation. In the latter case, when multilabel data is passed to AUC, each label-prediction pair is treated as an individual data point. Should be set to `False` for multi-class data. |
| `num_labels` | (Optional) The number of labels, used when `multi_label` is True. If `num_labels` is not specified, then state variables get created on the first call to `update_state`. |
| `label_weights` | (Optional) list, array, or tensor of non-negative weights used to compute AUCs for multilabel data. When `multi_label` is True, the weights are applied to the individual label AUCs when they are averaged to produce the multi-label AUC. When it's False, they are used to weight the individual label predictions in computing the confusion matrix on the flattened data. Note that this is unlike `class_weights` in that `class_weights` weights the example depending on the value of its label, whereas `label_weights` depends only on the index of that label before flattening; therefore `label_weights` should not be used for multi-class data. |
| `from_logits` | boolean indicating whether the predictions (`y_pred` in `update_state`) are probabilities or sigmoid logits. As a rule of thumb, when using a keras loss, the `from_logits` constructor argument of the loss should match the AUC `from_logits` constructor argument. |

#### Example:

```
>>> m = keras.metrics.AUC(num_thresholds=3)
>>> m.update_state([0, 0, 1, 1], [0, 0.5, 0.3, 0.9])
>>> # threshold values are [0 - 1e-7, 0.5, 1 + 1e-7]
>>> # tp = [2, 1, 0], fp = [2, 0, 0], fn = [0, 1, 2], tn = [0, 2, 2]
>>> # tp_rate = recall = [1, 0.5, 0], fp_rate = [1, 0, 0]
>>> # auc = ((((1 + 0.5) / 2) * (1 - 0)) + (((0.5 + 0) / 2) * (0 - 0)))
>>> #     = 0.75
>>> m.result()
0.75
```

```
>>> m.reset_state()
>>> m.update_state([0, 0, 1, 1], [0, 0.5, 0.3, 0.9],
...                sample_weight=[1, 0, 0, 1])
>>> m.result()
1.0
```

Usage with `compile()` API:

```
# Reports the AUC of a model outputting a probability.
model.compile(optimizer='sgd',
              loss=keras.losses.BinaryCrossentropy(),
              metrics=[keras.metrics.AUC()])

# Reports the AUC of a model outputting a logit.
model.compile(optimizer='sgd',
              loss=keras.losses.BinaryCrossentropy(from_logits=True),
              metrics=[keras.metrics.AUC(from_logits=True)])
```

| Attributes | |

|  |  |
| --- | --- |
| `dtype` |  |

|  |  |
| --- | --- |
| `thresholds` | The thresholds used for evaluating AUC. |
| `variables` |  |

## Methods

### `add_variable`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/metric.py#L186-L202)

```
add_variable(
    shape, initializer, dtype=None, aggregation='sum', name=None
)
```

### `add_weight`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/metric.py#L204-L208)

```
add_weight(
    shape=(), initializer=None, dtype=None, name=None
)
```

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/metric.py#L226-L228)

```
@classmethod
from_config(
    config
)
```

### `get_config`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/confusion_metrics.py#L1560-L1579)

```
get_config()
```

Return the serializable config of the metric.

### `interpolate_pr_auc`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/confusion_metrics.py#L1395-L1483)

```
interpolate_pr_auc()
```

Interpolation formula inspired by section 4 of Davis & Goadrich 2006.

<https://www.biostat.wisc.edu/~page/rocpr.pdf>

Note here we derive & use a closed formula not present in the paper
as follows:

```
Precision = TP / (TP + FP) = TP / P
```

Modeling all of TP (true positive), FP (false positive) and their sum
P = TP + FP (predicted positive) as varying linearly within each
interval [A, B] between successive thresholds, we get

```
Precision slope = dTP / dP
                = (TP_B - TP_A) / (P_B - P_A)
                = (TP - TP_A) / (P - P_A)
Precision = (TP_A + slope * (P - P_A)) / P
```

The area within the interval is (slope / total\_pos\_weight) times

```
int_A^B{Precision.dP} = int_A^B{(TP_A + slope * (P - P_A)) * dP / P}
int_A^B{Precision.dP} = int_A^B{slope * dP + intercept * dP / P}
```

where intercept = TP\_A - slope \* P\_A = TP\_B - slope \* P\_B, resulting in

```
int_A^B{Precision.dP} = TP_B - TP_A + intercept * log(P_B / P_A)
```

Bringing back the factor (slope / total\_pos\_weight) we'd put aside, we
get

```
slope * [dTP + intercept *  log(P_B / P_A)] / total_pos_weight
```

where dTP == TP\_B - TP\_A.

Note that when P\_A == 0 the above calculation simplifies into

```
int_A^B{Precision.dTP} = int_A^B{slope * dTP}
                       = slope * (TP_B - TP_A)
```

which is really equivalent to imputing constant precision throughout the
first bucket having >0 true positives.

| Returns | |

|  |  |
| --- | --- |
| `pr_auc` | an approximation of the area under the P-R curve. |

### `reset_state`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/confusion_metrics.py#L1548-L1558)

```
reset_state()
```

Reset all of the metric state variables.

This function is called between epochs/steps,
when a metric is evaluated during training.

### `result`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/confusion_metrics.py#L1485-L1546)

```
result()
```

Compute the current metric value.

| Returns | |
| A scalar tensor, or a dictionary of scalar tensors. | |

### `stateless_reset_state`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/metric.py#L164-L177)

```
stateless_reset_state()
```

### `stateless_result`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/metric.py#L148-L162)

```
stateless_result(
    metric_variables
)
```

### `stateless_update_state`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/metric.py#L115-L138)

```
stateless_update_state(
    metric_variables, *args, **kwargs
)
```

### `update_state`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/confusion_metrics.py#L1338-L1393)

```
update_state(
    y_true, y_pred, sample_weight=None
)
```

Accumulates confusion matrix statistics.

| Args | |

|  |  |
| --- | --- |
| `y_true` | The ground truth values. |
| `y_pred` | The predicted values. |
| `sample_weight` | Optional weighting of each example. Can be a tensor whose rank is either 0, or the same rank as `y_true`, and must be broadcastable to `y_true`. Defaults to `1`. |

### `__call__`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/metric.py#L217-L220)

```
__call__(
    *args, **kwargs
)
```

Call self as a function.
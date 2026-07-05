# tf.keras.metrics.Mean

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/Mean](https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/Mean)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/reduction_metrics.py#L94-L157) |

Compute the (weighted) mean of the given values.

Inherits From: [`Metric`](https://tensorflow.google.cn/api_docs/python/tf/keras/Metric)

```
tf.keras.metrics.Mean(
    name='mean', dtype=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Effective Tensorflow 2](https://tensorflow.google.cn/guide/effective_tf2) * [Mixed precision](https://tensorflow.google.cn/guide/mixed_precision) * [Use TPUs](https://tensorflow.google.cn/guide/tpu) | * [TensorFlow 2 quickstart for experts](https://tensorflow.google.cn/tutorials/quickstart/advanced) * [Custom training: walkthrough](https://tensorflow.google.cn/tutorials/customization/custom_training_walkthrough) * [Custom training with tf.distribute.Strategy](https://tensorflow.google.cn/tutorials/distribute/custom_training) * [Convolutional Variational Autoencoder](https://tensorflow.google.cn/tutorials/generative/cvae) * [Training with Orbit](https://tensorflow.google.cn/tfmodels/orbit/index) |

For example, if values is `[1, 3, 5, 7]` then the mean is 4.
If `sample_weight` was specified as `[1, 1, 0, 0]` then the mean would be 2.

This metric creates two variables, `total` and `count`.
The mean value returned is simply `total` divided by `count`.

| Args | |

|  |  |
| --- | --- |
| `name` | (Optional) string name of the metric instance. |
| `dtype` | (Optional) data type of the metric result. |

#### Example:

```
>>> m = Mean()
>>> m.update_state([1, 3, 5, 7])
>>> m.result()
4.0
```

```
>>> m.reset_state()
>>> m.update_state([1, 3, 5, 7], sample_weight=[1, 1, 0, 0])
>>> m.result()
2.0
```

```
<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`dtype`<a id="dtype"></a>
</td>
<td>

</td>
</tr><tr>
<td>
`variables`<a id="variables"></a>
</td>
<td>

</td>
</tr>
</table>

## Methods

<h3 id="add_variable"><code>add_variable</code></h3>

<a target="_blank" class="external" href="https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/metric.py#L186-L202">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>add_variable(
    shape, initializer, dtype=None, aggregation=&#x27;sum&#x27;, name=None
)
</code></pre>

<h3 id="add_weight"><code>add_weight</code></h3>

<a target="_blank" class="external" href="https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/metric.py#L204-L208">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>add_weight(
    shape=(), initializer=None, dtype=None, name=None
)
</code></pre>

<h3 id="from_config"><code>from_config</code></h3>

<a target="_blank" class="external" href="https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/metric.py#L226-L228">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_config(
    config
)
</code></pre>

<h3 id="get_config"><code>get_config</code></h3>

<a target="_blank" class="external" href="https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/metric.py#L222-L224">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_config()
</code></pre>

Return the serializable config of the metric.

<h3 id="reset_state"><code>reset_state</code></h3>

<a target="_blank" class="external" href="https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/reduction_metrics.py#L150-L152">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reset_state()
</code></pre>

Reset all of the metric state variables.

This function is called between epochs/steps,
when a metric is evaluated during training.

<h3 id="result"><code>result</code></h3>

<a target="_blank" class="external" href="https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/reduction_metrics.py#L154-L157">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>result()
</code></pre>

Compute the current metric value.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A scalar tensor, or a dictionary of scalar tensors.
</td>
</tr>

</table>

<h3 id="stateless_reset_state"><code>stateless_reset_state</code></h3>

<a target="_blank" class="external" href="https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/metric.py#L164-L177">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>stateless_reset_state()
</code></pre>

<h3 id="stateless_result"><code>stateless_result</code></h3>

<a target="_blank" class="external" href="https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/metric.py#L148-L162">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>stateless_result(
    metric_variables
)
</code></pre>

<h3 id="stateless_update_state"><code>stateless_update_state</code></h3>

<a target="_blank" class="external" href="https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/metric.py#L115-L138">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>stateless_update_state(
    metric_variables, *args, **kwargs
)
</code></pre>

<h3 id="update_state"><code>update_state</code></h3>

<a target="_blank" class="external" href="https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/reduction_metrics.py#L137-L148">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>update_state(
    values, sample_weight=None
)
</code></pre>

Accumulate statistics for the metric.

<h3 id="__call__"><code>__call__</code></h3>

<a target="_blank" class="external" href="https://github.com/keras-team/keras/tree/v3.3.3/keras/src/metrics/metric.py#L217-L220">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__call__(
    *args, **kwargs
)
</code></pre>

Call self as a function.
```
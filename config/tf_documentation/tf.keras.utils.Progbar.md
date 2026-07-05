# tf.keras.utils.Progbar

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/utils/Progbar](https://tensorflow.google.cn/api_docs/python/tf/keras/utils/Progbar)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/utils/progbar.py#L11-L269) |

Displays a progress bar.

```
tf.keras.utils.Progbar(
    target,
    width=20,
    verbose=1,
    interval=0.05,
    stateful_metrics=None,
    unit_name='step'
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Distributed training with DTensors](https://tensorflow.google.cn/tutorials/distribute/dtensor_ml_tutorial) * [Using DTensors with Keras](https://tensorflow.google.cn/tutorials/distribute/dtensor_keras_tutorial) |

| Args | |

|  |  |
| --- | --- |
| `target` | Total number of steps expected, None if unknown. |
| `width` | Progress bar width on screen. |
| `verbose` | Verbosity mode, 0 (silent), 1 (verbose), 2 (semi-verbose) |
| `stateful_metrics` | Iterable of string names of metrics that should *not* be averaged over time. Metrics in this list will be displayed as-is. All others will be averaged by the progbar before display. |
| `interval` | Minimum visual progress update interval (in seconds). |
| `unit_name` | Display name for step counts (usually "step" or "sample"). |

## Methods

### `add`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/utils/progbar.py#L210-L211)

```
add(
    n, values=None
)
```

### `update`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/utils/progbar.py#L62-L208)

```
update(
    current, values=None, finalize=None
)
```

Updates the progress bar.

| Args | |

|  |  |
| --- | --- |
| `current` | Index of current step. |
| `values` | List of tuples: `(name, value_for_last_step)`. If `name` is in `stateful_metrics`, `value_for_last_step` will be displayed as-is. Else, an average of the metric over time will be displayed. |
| `finalize` | Whether this is the last update for the progress bar. If `None`, defaults to `current >= self.target`. |
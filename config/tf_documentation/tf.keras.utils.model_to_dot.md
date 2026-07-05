# tf.keras.utils.model_to_dot

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/utils/model_to_dot](https://tensorflow.google.cn/api_docs/python/tf/keras/utils/model_to_dot)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/utils/model_visualization.py#L179-L347) |

Convert a Keras model to dot format.

```
tf.keras.utils.model_to_dot(
    model,
    show_shapes=False,
    show_dtype=False,
    show_layer_names=True,
    rankdir='TB',
    expand_nested=False,
    dpi=200,
    subgraph=False,
    show_layer_activations=False,
    show_trainable=False,
    **kwargs
)
```

| Args | |

|  |  |
| --- | --- |
| `model` | A Keras model instance. |
| `show_shapes` | whether to display shape information. |
| `show_dtype` | whether to display layer dtypes. |
| `show_layer_names` | whether to display layer names. |
| `rankdir` | `rankdir` argument passed to PyDot, a string specifying the format of the plot: `"TB"` creates a vertical plot; `"LR"` creates a horizontal plot. |
| `expand_nested` | whether to expand nested Functional models into clusters. |
| `dpi` | Image resolution in dots per inch. |
| `subgraph` | whether to return a `pydot.Cluster` instance. |
| `show_layer_activations` | Display layer activations (only for layers that have an `activation` property). |
| `show_trainable` | whether to display if a layer is trainable. |

| Returns | |
| A `pydot.Dot` instance representing the Keras model or a `pydot.Cluster` instance representing nested model if `subgraph=True`. | |
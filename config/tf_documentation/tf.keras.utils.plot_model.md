# tf.keras.utils.plot_model

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/utils/plot_model](https://tensorflow.google.cn/api_docs/python/tf/keras/utils/plot_model)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/utils/model_visualization.py#L350-L465) |

Converts a Keras model to dot format and save to a file.

```
tf.keras.utils.plot_model(
    model,
    to_file='model.png',
    show_shapes=False,
    show_dtype=False,
    show_layer_names=False,
    rankdir='TB',
    expand_nested=False,
    dpi=200,
    show_layer_activations=False,
    show_trainable=False,
    **kwargs
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Load text](https://tensorflow.google.cn/tutorials/load_data/text) * [pix2pix: Image-to-image translation with a conditional GAN](https://tensorflow.google.cn/tutorials/generative/pix2pix) * [Load a pandas DataFrame](https://tensorflow.google.cn/tutorials/load_data/pandas_dataframe) * [Transfer learning with YAMNet for environmental sound classification](https://tensorflow.google.cn/tutorials/audio/transfer_learning_audio) * [Image segmentation](https://tensorflow.google.cn/tutorials/images/segmentation) |

#### Example:

```
inputs = ...
outputs = ...
model = keras.Model(inputs=inputs, outputs=outputs)

dot_img_file = '/tmp/model_1.png'
keras.utils.plot_model(model, to_file=dot_img_file, show_shapes=True)
```

| Args | |

|  |  |
| --- | --- |
| `model` | A Keras model instance |
| `to_file` | File name of the plot image. |
| `show_shapes` | whether to display shape information. |
| `show_dtype` | whether to display layer dtypes. |
| `show_layer_names` | whether to display layer names. |
| `rankdir` | `rankdir` argument passed to PyDot, a string specifying the format of the plot: `"TB"` creates a vertical plot; `"LR"` creates a horizontal plot. |
| `expand_nested` | whether to expand nested Functional models into clusters. |
| `dpi` | Image resolution in dots per inch. |
| `show_layer_activations` | Display layer activations (only for layers that have an `activation` property). |
| `show_trainable` | whether to display if a layer is trainable. |

| Returns | |
| A Jupyter notebook Image object if Jupyter is installed. This enables in-line display of the model plots in notebooks. | |
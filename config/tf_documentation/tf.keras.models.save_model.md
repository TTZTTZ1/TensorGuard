# tf.keras.models.save_model

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/models/save_model](https://tensorflow.google.cn/api_docs/python/tf/keras/models/save_model)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/saving/saving_api.py#L18-L113) |

Saves a model as a `.keras` file.

```
tf.keras.models.save_model(
    model, filepath, overwrite=True, **kwargs
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Train and serve a TensorFlow model with TensorFlow Serving](https://tensorflow.google.cn/tfx/tutorials/serving/rest_simple) |

| Args | |

|  |  |
| --- | --- |
| `model` | Keras model instance to be saved. |
| `filepath` | `str` or `pathlib.Path` object. Path where to save the model. |
| `overwrite` | Whether we should overwrite any existing model at the target location, or instead ask the user via an interactive prompt. |

#### Example:

```
model = keras.Sequential(
    [
        keras.layers.Dense(5, input_shape=(3,)),
        keras.layers.Softmax(),
    ],
)
model.save("model.keras")
loaded_model = keras.saving.load_model("model.keras")
x = keras.random.uniform((10, 3))
assert np.allclose(model.predict(x), loaded_model.predict(x))
```

Note that `model.save()` is an alias for `keras.saving.save_model()`.

The saved `.keras` file contains:

* The model's configuration (architecture)
* The model's weights
* The model's optimizer's state (if any)

Thus models can be reinstantiated in the exact same state.
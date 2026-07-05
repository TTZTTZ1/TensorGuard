# tf.keras.models.load_model

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/models/load_model](https://tensorflow.google.cn/api_docs/python/tf/keras/models/load_model)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/saving/saving_api.py#L116-L205) |

Loads a model saved via `model.save()`.

```
tf.keras.models.load_model(
    filepath, custom_objects=None, compile=True, safe_mode=True
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Introduction to modules, layers, and models](https://tensorflow.google.cn/guide/intro_to_modules) * [Migrate `tf.feature\_column`s to Keras preprocessing layers](https://tensorflow.google.cn/guide/migrate/migrating_feature_columns) * [Migrate the SavedModel workflow](https://tensorflow.google.cn/guide/migrate/saved_model) * [Migrating your TFLite code to TF2](https://tensorflow.google.cn/guide/migrate/tflite) * [Multi-GPU and distributed training](https://tensorflow.google.cn/guide/keras/distributed_training) | * [Save and load a model using a distribution strategy](https://tensorflow.google.cn/tutorials/distribute/save_and_load) * [Save and load models](https://tensorflow.google.cn/tutorials/keras/save_and_load) * [Distributed training with Keras](https://tensorflow.google.cn/tutorials/distribute/keras) * [Multi-worker training with Keras](https://tensorflow.google.cn/tutorials/distribute/multi_worker_with_keras) * [Transfer learning with TensorFlow Hub](https://tensorflow.google.cn/tutorials/images/transfer_learning_with_hub) |

| Args | |

|  |  |
| --- | --- |
| `filepath` | `str` or `pathlib.Path` object, path to the saved model file. |
| `custom_objects` | Optional dictionary mapping names (strings) to custom classes or functions to be considered during deserialization. |
| `compile` | Boolean, whether to compile the model after loading. |
| `safe_mode` | Boolean, whether to disallow unsafe `lambda` deserialization. When `safe_mode=False`, loading an object has the potential to trigger arbitrary code execution. This argument is only applicable to the Keras v3 model format. Defaults to `True`. |

| Returns | |
| A Keras model instance. If the original model was compiled, and the argument `compile=True` is set, then the returned model will be compiled. Otherwise, the model will be left uncompiled. | |

#### Example:

```
model = keras.Sequential([
    keras.layers.Dense(5, input_shape=(3,)),
    keras.layers.Softmax()])
model.save("model.keras")
loaded_model = keras.saving.load_model("model.keras")
x = np.random.random((10, 3))
assert np.allclose(model.predict(x), loaded_model.predict(x))
```

Note that the model variables may have different name values
(`var.name` property, e.g. `"dense_1/kernel:0"`) after being reloaded.
It is recommended that you use layer attributes to
access specific variables, e.g. `model.get_layer("dense_1").kernel`.
# tf.saved_model.load

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/saved_model/load](https://tensorflow.google.cn/api_docs/python/tf/saved_model/load)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/saved_model/load.py#L820-L913) |

Load a SavedModel from `export_dir`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.saved_model.load_v2`](https://tensorflow.google.cn/api_docs/python/tf/saved_model/load)

```
tf.saved_model.load(
    export_dir, tags=None, options=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Using the SavedModel format](https://tensorflow.google.cn/guide/saved_model) * [Extension types](https://tensorflow.google.cn/guide/extension_type) * [Import a JAX model using JAX2TF](https://tensorflow.google.cn/guide/jax2tf) * [Migrate the SavedModel workflow](https://tensorflow.google.cn/guide/migrate/saved_model) * [Ragged tensors](https://tensorflow.google.cn/guide/ragged_tensor) | * [Save and load a model using a distribution strategy](https://tensorflow.google.cn/tutorials/distribute/save_and_load) * [Load text](https://tensorflow.google.cn/tutorials/load_data/text) * [Simple audio recognition: Recognizing keywords](https://tensorflow.google.cn/tutorials/audio/simple_audio) * [Transfer learning with YAMNet for environmental sound classification](https://tensorflow.google.cn/tutorials/audio/transfer_learning_audio) * [Distributed training with DTensors](https://tensorflow.google.cn/tutorials/distribute/dtensor_ml_tutorial) |

Signatures associated with the SavedModel are available as functions:

```
imported = tf.saved_model.load(path)
f = imported.signatures["serving_default"]
print(f(x=tf.constant([[1.]])))
```

Objects exported with [`tf.saved_model.save`](https://tensorflow.google.cn/api_docs/python/tf/saved_model/save) additionally have trackable
objects and functions assigned to attributes:

```
exported = tf.train.Checkpoint(v=tf.Variable(3.))
exported.f = tf.function(
    lambda x: exported.v * x,
    input_signature=[tf.TensorSpec(shape=None, dtype=tf.float32)])
tf.saved_model.save(exported, path)
imported = tf.saved_model.load(path)
assert 3. == imported.v.numpy()
assert 6. == imported.f(x=tf.constant(2.)).numpy()
```

*Loading Keras models*

Keras models are trackable, so they can be saved to SavedModel. The object
returned by [`tf.saved_model.load`](https://tensorflow.google.cn/api_docs/python/tf/saved_model/load) is not a Keras object (i.e. doesn't have
`.fit`, `.predict`, etc. methods). A few attributes and functions are still
available: `.variables`, `.trainable_variables` and `.__call__`.

```
model = tf.keras.Model(...)
tf.saved_model.save(model, path)
imported = tf.saved_model.load(path)
outputs = imported(inputs)
```

Use [`tf.keras.models.load_model`](https://tensorflow.google.cn/api_docs/python/tf/keras/models/load_model) to restore the Keras model.

*Importing SavedModels from TensorFlow 1.x*

1.x SavedModels APIs have a flat graph instead of [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function) objects.
These SavedModels will be loaded with the following attributes:

* `.signatures`: A dictionary mapping signature names to functions.
* `.prune(feeds, fetches)`: A method which allows you to extract
  functions for new subgraphs. This is equivalent to importing the SavedModel
  and naming feeds and fetches in a Session from TensorFlow 1.x.

  ```
  imported = tf.saved_model.load(path_to_v1_saved_model)
  pruned = imported.prune("x:0", "out:0")
  pruned(tf.ones([]))
  ```

  See [`tf.compat.v1.wrap_function`](https://tensorflow.google.cn/api_docs/python/tf/compat/v1/wrap_function) for details.
* `.variables`: A list of imported variables.
* `.graph`: The whole imported graph.
* `.restore(save_path)`: A function that restores variables from a checkpoint
  saved from `tf.compat.v1.Saver`.

*Consuming SavedModels asynchronously*

When consuming SavedModels asynchronously (the producer is a separate
process), the SavedModel directory will appear before all files have been
written, and [`tf.saved_model.load`](https://tensorflow.google.cn/api_docs/python/tf/saved_model/load) will fail if pointed at an incomplete
SavedModel. Rather than checking for the directory, check for
"saved\_model\_dir/saved\_model.pb". This file is written atomically as the last
[`tf.saved_model.save`](https://tensorflow.google.cn/api_docs/python/tf/saved_model/save) file operation.

| Args | |

|  |  |
| --- | --- |
| `export_dir` | The SavedModel directory to load from. |
| `tags` | A tag or sequence of tags identifying the MetaGraph to load. Optional if the SavedModel contains a single MetaGraph, as for those exported from [`tf.saved_model.save`](https://tensorflow.google.cn/api_docs/python/tf/saved_model/save). |
| `options` | [`tf.saved_model.LoadOptions`](https://tensorflow.google.cn/api_docs/python/tf/saved_model/LoadOptions) object that specifies options for loading. |

| Returns | |
| A trackable object with a `signatures` attribute mapping from signature keys to functions. If the SavedModel was exported by [`tf.saved_model.save`](https://tensorflow.google.cn/api_docs/python/tf/saved_model/save), it also points to trackable objects, functions, debug info which it has been saved. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If `tags` don't match a MetaGraph in the SavedModel. |
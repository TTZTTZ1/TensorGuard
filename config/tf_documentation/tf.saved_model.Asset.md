# tf.saved_model.Asset

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/saved_model/Asset](https://tensorflow.google.cn/api_docs/python/tf/saved_model/Asset)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/trackable/asset.py#L30-L112) |

Represents a file asset to hermetically include in a SavedModel.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.saved_model.Asset`](https://tensorflow.google.cn/api_docs/python/tf/saved_model/Asset)

```
tf.saved_model.Asset(
    path
)
```

### Used in the notebooks

| Used in the guide |
| --- |
| * [Subword tokenizers](https://tensorflow.google.cn/text/guide/subwords_tokenizer) |

A SavedModel can include arbitrary files, called assets, that are needed
for its use. For example a vocabulary file used initialize a lookup table.

When a trackable object is exported via [`tf.saved_model.save()`](https://tensorflow.google.cn/api_docs/python/tf/saved_model/save), all the
`Asset`s reachable from it are copied into the SavedModel assets directory.
Upon loading, the assets and the serialized functions that depend on them
will refer to the correct filepaths inside the SavedModel directory.

#### Example:

```
filename = tf.saved_model.Asset("file.txt")

@tf.function(input_signature=[])
def func():
  return tf.io.read_file(filename)

trackable_obj = tf.train.Checkpoint()
trackable_obj.func = func
trackable_obj.filename = filename
tf.saved_model.save(trackable_obj, "/tmp/saved_model")

# The created SavedModel is hermetic, it does not depend on
# the original file and can be moved to another path.
tf.io.gfile.remove("file.txt")
tf.io.gfile.rename("/tmp/saved_model", "/tmp/new_location")

reloaded_obj = tf.saved_model.load("/tmp/new_location")
print(reloaded_obj.func())
```

| Attributes | |

|  |  |
| --- | --- |
| `asset_path` | A path, or a 0-D [`tf.string`](https://tensorflow.google.cn/api_docs/python/tf#string) tensor with path to the asset. |
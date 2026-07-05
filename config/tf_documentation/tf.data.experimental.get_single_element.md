# tf.data.experimental.get_single_element

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/data/experimental/get_single_element](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/get_single_element)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/experimental/ops/get_single_element.py#L21-L109) |

Returns the single element of the `dataset` as a nested structure of tensors. (deprecated)

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.data.experimental.get_single_element`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/get_single_element)

```
tf.data.experimental.get_single_element(
    dataset
)
```

**Deprecated:** THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use [`tf.data.Dataset.get_single_element()`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset#get_single_element).

The function enables you to use a [`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset) in a stateless
"tensor-in tensor-out" expression, without creating an iterator.
This facilitates the ease of data transformation on tensors using the
optimized [`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset) abstraction on top of them.

For example, lets consider a `preprocessing_fn` which would take as an
input the raw features and returns the processed feature along with
it's label.

```
def preprocessing_fn(raw_feature):
  # ... the raw_feature is preprocessed as per the use-case
  return feature

raw_features = ...  # input batch of BATCH_SIZE elements.
dataset = (tf.data.Dataset.from_tensor_slices(raw_features)
           .map(preprocessing_fn, num_parallel_calls=BATCH_SIZE)
           .batch(BATCH_SIZE))

processed_features = tf.data.experimental.get_single_element(dataset)
```

In the above example, the `raw_features` tensor of length=BATCH\_SIZE
was converted to a [`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset). Next, each of the `raw_feature` was
mapped using the `preprocessing_fn` and the processed features were
grouped into a single batch. The final `dataset` contains only one element
which is a batch of all the processed features.

**Note:** The `dataset` should contain only one element.

Now, instead of creating an iterator for the `dataset` and retrieving the
batch of features, the [`tf.data.experimental.get_single_element()`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/get_single_element) function
is used to skip the iterator creation process and directly output the batch
of features.

This can be particularly useful when your tensor transformations are
expressed as [`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset) operations, and you want to use those
transformations while serving your model.

```
model = ... # A pre-built or custom model

class PreprocessingModel(tf.keras.Model):
  def __init__(self, model):
    super().__init__(self)
    self.model = model

  @tf.function(input_signature=[...])
  def serving_fn(self, data):
    ds = tf.data.Dataset.from_tensor_slices(data)
    ds = ds.map(preprocessing_fn, num_parallel_calls=BATCH_SIZE)
    ds = ds.batch(batch_size=BATCH_SIZE)
    return tf.argmax(
      self.model(tf.data.experimental.get_single_element(ds)),
      axis=-1
    )

preprocessing_model = PreprocessingModel(model)
your_exported_model_dir = ... # save the model to this path.
tf.saved_model.save(preprocessing_model, your_exported_model_dir,
              signatures={'serving_default': preprocessing_model.serving_fn})
```

| Args | |

|  |  |
| --- | --- |
| `dataset` | A [`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset) object containing a single element. |

| Returns | |
| A nested structure of [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) objects, corresponding to the single element of `dataset`. | |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | if `dataset` is not a [`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset) object. |
| `InvalidArgumentError` | (at runtime) if `dataset` does not contain exactly one element. |
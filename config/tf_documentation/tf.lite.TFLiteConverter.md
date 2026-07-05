# tf.lite.TFLiteConverter

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/lite/TFLiteConverter](https://tensorflow.google.cn/api_docs/python/tf/lite/TFLiteConverter)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/lite/python/lite.py#L1948-L2216) |

Converts a TensorFlow model into TensorFlow Lite model.

```
tf.lite.TFLiteConverter(
    funcs, trackable_obj=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Migrating your TFLite code to TF2](https://tensorflow.google.cn/guide/migrate/tflite) * [TensorFlow Lite Model Analyzer](https://tensorflow.google.cn/lite/guide/model_analyzer) * [Cluster preserving quantization aware training (CQAT) Keras example](https://tensorflow.google.cn/model_optimization/guide/combine/cqat_example) * [Pruning preserving quantization aware training (PQAT) Keras example](https://tensorflow.google.cn/model_optimization/guide/combine/pqat_example) * [Signatures in TensorFlow Lite](https://tensorflow.google.cn/lite/guide/signatures) | * [Image classification](https://tensorflow.google.cn/tutorials/images/classification) * [Post-training integer quantization](https://tensorflow.google.cn/lite/performance/post_training_integer_quant) * [Inspecting Quantization Errors with Quantization Debugger](https://tensorflow.google.cn/lite/performance/quantization_debugger) * [Jax Model Conversion For TFLite](https://tensorflow.google.cn/lite/examples/jax_conversion/jax_to_tflite) * [Post-training dynamic range quantization](https://tensorflow.google.cn/lite/performance/post_training_quant) |

#### Example usage:

```
# Converting a SavedModel to a TensorFlow Lite model.
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
tflite_model = converter.convert()

# Converting a tf.Keras model to a TensorFlow Lite model.
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Converting ConcreteFunctions to a TensorFlow Lite model.
converter = tf.lite.TFLiteConverter.from_concrete_functions([func], model)
tflite_model = converter.convert()

# Converting a Jax model to a TensorFlow Lite model.
converter = tf.lite.TFLiteConverter.experimental_from_jax(
    [func], [[ ('input1', input1), ('input2', input2)]])
tflite_model = converter.convert()
```

| Args | |

|  |  |
| --- | --- |
| `funcs` | List of TensorFlow ConcreteFunctions. The list should not contain duplicate elements. |
| `trackable_obj` | tf.AutoTrackable object associated with `funcs`. A reference to this object needs to be maintained so that Variables do not get garbage collected since functions have a weak reference to Variables. This is only required when the tf.AutoTrackable object is not maintained by the user (e.g. `from_saved_model`). |

| Attributes | |

|  |  |
| --- | --- |
| `optimizations` | Experimental flag, subject to change. Set of optimizations to apply. e.g {tf.lite.Optimize.DEFAULT}. (default None, must be None or a set of values of type [`tf.lite.Optimize`](https://tensorflow.google.cn/api_docs/python/tf/lite/Optimize)) |
| `representative_dataset` | A generator function used for integer quantization where each generated sample has the same order, type and shape as the inputs to the model. Usually, this is a small subset of a few hundred samples randomly chosen, in no particular order, from the training or evaluation dataset. This is an optional attribute, but required for full integer quantization, i.e, if [`tf.int8`](https://tensorflow.google.cn/api_docs/python/tf#int8) is the only supported type in `target_spec.supported_types`. Refer to [`tf.lite.RepresentativeDataset`](https://tensorflow.google.cn/api_docs/python/tf/lite/RepresentativeDataset). (default None) |
| `target_spec` | Experimental flag, subject to change. Specifications of target device, including supported ops set, supported types and a set of user's defined TensorFlow operators required in the TensorFlow Lite runtime. Refer to [`tf.lite.TargetSpec`](https://tensorflow.google.cn/api_docs/python/tf/lite/TargetSpec). |
| `inference_input_type` | Data type of the input layer. Note that integer types (tf.int8 and tf.uint8) are currently only supported for post training integer quantization and quantization aware training. (default tf.float32, must be in {tf.float32, tf.int8, tf.uint8}) |
| `inference_output_type` | Data type of the output layer. Note that integer types (tf.int8 and tf.uint8) are currently only supported for post training integer quantization and quantization aware training. (default tf.float32, must be in {tf.float32, tf.int8, tf.uint8}) |
| `allow_custom_ops` | Boolean indicating whether to allow custom operations. When False, any unknown operation is an error. When True, custom ops are created for any op that is unknown. The developer needs to provide these to the TensorFlow Lite runtime with a custom resolver. (default False) |
| `exclude_conversion_metadata` | Whether not to embed the conversion metadata into the converted model. (default False) |
| `experimental_new_converter` | Experimental flag, subject to change. Enables MLIR-based conversion. (default True) |
| `experimental_new_quantizer` | Experimental flag, subject to change. Enables MLIR-based quantization conversion instead of Flatbuffer-based conversion. (default True) |
| `experimental_enable_resource_variables` | Experimental flag, subject to change. Enables [resource variables](https://tensorflow.org/guide/migrate/tf1_vs_tf2#resourcevariables_instead_of_referencevariables) to be converted by this converter. This is only allowed if the from\_saved\_model interface is used. (default True) |

## Methods

### `convert`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/lite/python/lite.py#L2203-L2216)

```
convert()
```

Converts a TensorFlow GraphDef based on instance variables.

| Returns | |
| The converted data in serialized format. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | No concrete functions is specified. Multiple concrete functions are specified. Input shape is not specified. Invalid quantization parameters. |

### `experimental_from_jax`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/lite/python/lite.py#L2174-L2200)

```
@classmethod
experimental_from_jax(
    serving_funcs, inputs
)
```

Creates a TFLiteConverter object from a Jax model with its inputs. (deprecated)

**Deprecated:** THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use `jax2tf.convert` and ([`lite.TFLiteConverter.from_saved_model`](https://tensorflow.google.cn/api_docs/python/tf/lite/TFLiteConverter#from_saved_model) or [`lite.TFLiteConverter.from_concrete_functions`](https://tensorflow.google.cn/api_docs/python/tf/lite/TFLiteConverter#from_concrete_functions)) instead.

| Args | |

|  |  |
| --- | --- |
| `serving_funcs` | A array of Jax functions with all the weights applied already. |
| `inputs` | A array of Jax input placeholders tuples list, e.g., jnp.zeros(INPUT\_SHAPE). Each tuple list should correspond with the serving function. |

| Returns | |
| TFLiteConverter object. | |

### `from_concrete_functions`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/lite/python/lite.py#L2030-L2070)

```
@classmethod
from_concrete_functions(
    funcs, trackable_obj=None
)
```

Creates a TFLiteConverter object from ConcreteFunctions.

| Args | |

|  |  |
| --- | --- |
| `funcs` | List of TensorFlow ConcreteFunctions. The list should not contain duplicate elements. Currently converter can only convert a single ConcreteFunction. Converting multiple functions is under development. |
| `trackable_obj` | An `AutoTrackable` object (typically `tf.module`) associated with `funcs`. A reference to this object needs to be maintained so that Variables do not get garbage collected since functions have a weak reference to Variables. |

| Returns | |
| TFLiteConverter object. | |

| Raises | |
| Invalid input type. | |

### `from_keras_model`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/lite/python/lite.py#L2157-L2172)

```
@classmethod
from_keras_model(
    model
)
```

Creates a TFLiteConverter object from a Keras model.

| Args | |

|  |  |
| --- | --- |
| `model` | tf.Keras.Model |

| Returns | |
| TFLiteConverter object. | |

### `from_saved_model`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/lite/python/lite.py#L2072-L2155)

```
@classmethod
from_saved_model(
    saved_model_dir, signature_keys=None, tags=None
)
```

Creates a TFLiteConverter object from a SavedModel directory.

| Args | |

|  |  |
| --- | --- |
| `saved_model_dir` | SavedModel directory to convert. |
| `signature_keys` | List of keys identifying SignatureDef containing inputs and outputs. Elements should not be duplicated. By default the `signatures` attribute of the MetaGraphdef is used. (default saved\_model.signatures) |
| `tags` | Set of tags identifying the MetaGraphDef within the SavedModel to analyze. All tags in the tag set must be present. (default {tf.saved\_model.SERVING} or {'serve'}) |

| Returns | |
| TFLiteConverter object. | |

| Raises | |
| Invalid signature keys. | |
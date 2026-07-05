# tf.lite.Interpreter

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/lite/Interpreter](https://tensorflow.google.cn/api_docs/python/tf/lite/Interpreter)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/lite/python/interpreter.py#L348-L966) |

Interpreter interface for running TensorFlow Lite models.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.lite.Interpreter`](https://tensorflow.google.cn/api_docs/python/tf/lite/Interpreter)

```
tf.lite.Interpreter(
    model_path=None,
    model_content=None,
    experimental_delegates=None,
    num_threads=None,
    experimental_op_resolver_type=tf.lite.experimental.OpResolverType.AUTO,
    experimental_preserve_all_tensors=False,
    experimental_disable_delegate_clustering=False
)

tf.lite.experimental.OpResolverType.AUTO
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Signatures in TensorFlow Lite](https://tensorflow.google.cn/lite/guide/signatures) * [Cluster preserving quantization aware training (CQAT) Keras example](https://tensorflow.google.cn/model_optimization/guide/combine/cqat_example) * [Pruning preserving quantization aware training (PQAT) Keras example](https://tensorflow.google.cn/model_optimization/guide/combine/pqat_example) * [Weight clustering in Keras example](https://tensorflow.google.cn/model_optimization/guide/clustering/clustering_example) * [Sparsity and cluster preserving quantization aware training (PCQAT) Keras example](https://tensorflow.google.cn/model_optimization/guide/combine/pcqat_example) | * [Image classification](https://tensorflow.google.cn/tutorials/images/classification) * [Post-training integer quantization](https://tensorflow.google.cn/lite/performance/post_training_integer_quant) * [Jax Model Conversion For TFLite](https://tensorflow.google.cn/lite/examples/jax_conversion/jax_to_tflite) * [On-Device Training with TensorFlow Lite](https://tensorflow.google.cn/lite/examples/on_device_training/overview) * [Artistic Style Transfer with TensorFlow Lite](https://tensorflow.google.cn/lite/examples/style_transfer/overview) |

Models obtained from `TfLiteConverter` can be run in Python with
`Interpreter`.

As an example, lets generate a simple Keras model and convert it to TFLite
(`TfLiteConverter` also supports other input formats with `from_saved_model`
and `from_concrete_function`)

```
>>> x = np.array([[1.], [2.]])
>>> y = np.array([[2.], [4.]])
>>> model = tf.keras.models.Sequential([
...           tf.keras.layers.Dropout(0.2),
...           tf.keras.layers.Dense(units=1, input_shape=[1])
...         ])
>>> model.compile(optimizer='sgd', loss='mean_squared_error')
>>> model.fit(x, y, epochs=1)
>>> converter = tf.lite.TFLiteConverter.from_keras_model(model)
>>> tflite_model = converter.convert()
```

`tflite_model` can be saved to a file and loaded later, or directly into the
`Interpreter`. Since TensorFlow Lite pre-plans tensor allocations to optimize
inference, the user needs to call `allocate_tensors()` before any inference.

```
>>> interpreter = tf.lite.Interpreter(model_content=tflite_model)
>>> interpreter.allocate_tensors()  # Needed before execution!
```

#### Sample execution:

```
>>> output = interpreter.get_output_details()[0]  # Model has single output.
>>> input = interpreter.get_input_details()[0]  # Model has single input.
>>> input_data = tf.constant(1., shape=[1, 1])
>>> interpreter.set_tensor(input['index'], input_data)
>>> interpreter.invoke()
>>> interpreter.get_tensor(output['index']).shape
(1, 1)
```

Use `get_signature_runner()` for a more user-friendly inference API.

| Args | |

|  |  |
| --- | --- |
| `model_path` | Path to TF-Lite Flatbuffer file. |
| `model_content` | Content of model. |
| `experimental_delegates` | Experimental. Subject to change. List of [TfLiteDelegate](https://tensorflow.google.cn/lite/performance/delegates) objects returned by lite.load\_delegate(). |
| `num_threads` | Sets the number of threads used by the interpreter and available to CPU kernels. If not set, the interpreter will use an implementation-dependent default number of threads. Currently, only a subset of kernels, such as conv, support multi-threading. num\_threads should be >= -1. Setting num\_threads to 0 has the effect to disable multithreading, which is equivalent to setting num\_threads to 1. If set to the value -1, the number of threads used will be implementation-defined and platform-dependent. |
| `experimental_op_resolver_type` | The op resolver used by the interpreter. It must be an instance of OpResolverType. By default, we use the built-in op resolver which corresponds to tflite::ops::builtin::BuiltinOpResolver in C++. |
| `experimental_preserve_all_tensors` | If true, then intermediate tensors used during computation are preserved for inspection, and if the passed op resolver type is AUTO or BUILTIN, the type will be changed to BUILTIN\_WITHOUT\_DEFAULT\_DELEGATES so that no Tensorflow Lite default delegates are applied. If false, getting intermediate tensors could result in undefined values or None, especially when the graph is successfully modified by the Tensorflow Lite default delegate. |
| `experimental_disable_delegate_clustering` | If true, don't perform delegate clustering during delegate graph partitioning phase. Disabling delegate clustering will make the execution order of ops respect the explicitly-inserted control dependencies in the graph (inserted via `with tf.control_dependencies()`) since the TF Lite converter will drop control dependencies by default. Most users shouldn't turn this flag to True if they don't insert explicit control dependencies or the graph execution order is expected. For automatically inserted control dependencies (with [`tf.Variable`](https://tensorflow.google.cn/api_docs/python/tf/Variable), `tf.Print` etc), the user doesn't need to turn this flag to True since they are respected by default. Note that this flag is currently experimental, and it might be removed/updated if the TF Lite converter doesn't drop such control dependencies in the model. Default is False. |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If the interpreter was unable to create. |

## Methods

### `allocate_tensors`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/lite/python/interpreter.py#L529-L531)

```
allocate_tensors()
```

### `get_input_details`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/lite/python/interpreter.py#L673-L702)

```
get_input_details()
```

Gets model input tensor details.

| Returns | |
| A list in which each item is a dictionary with details about an input tensor. Each dictionary contains the following fields that describe the tensor: | |

* `name`: The tensor name.
* `index`: The tensor index in the interpreter.
* `shape`: The shape of the tensor.
* `shape_signature`: Same as `shape` for models with known/fixed shapes.
  If any dimension sizes are unknown, they are indicated with `-1`.
* `dtype`: The numpy data type (such as `np.int32` or `np.uint8`).
* `quantization`: Deprecated, use `quantization_parameters`. This field
  only works for per-tensor quantization, whereas
  `quantization_parameters` works in all cases.
* `quantization_parameters`: A dictionary of parameters used to quantize
  the tensor:
  ~ `scales`: List of scales (one if per-tensor quantization).
  ~ `zero_points`: List of zero\_points (one if per-tensor quantization).
  ~ `quantized_dimension`: Specifies the dimension of per-axis
  quantization, in the case of multiple scales/zero\_points.
* `sparsity_parameters`: A dictionary of parameters used to encode a
  sparse tensor. This is empty if the tensor is dense.

### `get_output_details`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/lite/python/interpreter.py#L751-L762)

```
get_output_details()
```

Gets model output tensor details.

| Returns | |
| A list in which each item is a dictionary with details about an output tensor. The dictionary contains the same fields as described for `get_input_details()`. | |

### `get_signature_list`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/lite/python/interpreter.py#L764-L789)

```
get_signature_list()
```

Gets list of SignatureDefs in the model.

Example,

```
signatures = interpreter.get_signature_list()
print(signatures)

# {
#   'add': {'inputs': ['x', 'y'], 'outputs': ['output_0']}
# }

Then using the names in the signature list you can get a callable from
get_signature_runner().
```

| Returns | |
| A list of SignatureDef details in a dictionary structure. It is keyed on the SignatureDef method name, and the value holds dictionary of inputs and outputs. | |

### `get_signature_runner`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/lite/python/interpreter.py#L814-L859)

```
get_signature_runner(
    signature_key=None
)
```

Gets callable for inference of specific SignatureDef.

Example usage,

```
interpreter = tf.lite.Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()
fn = interpreter.get_signature_runner('div_with_remainder')
output = fn(x=np.array([3]), y=np.array([2]))
print(output)
# {
#   'quotient': array([1.], dtype=float32)
#   'remainder': array([1.], dtype=float32)
# }
```

None can be passed for signature\_key if the model has a single Signature
only.

All names used are this specific SignatureDef names.

| Args | |

|  |  |
| --- | --- |
| `signature_key` | Signature key for the SignatureDef, it can be None if and only if the model has a single SignatureDef. Default value is None. |

| Returns | |
| This returns a callable that can run inference for SignatureDef defined by argument 'signature\_key'. The callable will take key arguments corresponding to the arguments of the SignatureDef, that should have numpy values. The callable will returns dictionary that maps from output names to numpy values of the computed results. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If passed signature\_key is invalid. |

### `get_tensor`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/lite/python/interpreter.py#L861-L876)

```
get_tensor(
    tensor_index, subgraph_index=0
)
```

Gets the value of the output tensor (get a copy).

If you wish to avoid the copy, use `tensor()`. This function cannot be used
to read intermediate results.

| Args | |

|  |  |
| --- | --- |
| `tensor_index` | Tensor index of tensor to get. This value can be gotten from the 'index' field in get\_output\_details. |
| `subgraph_index` | Index of the subgraph to fetch the tensor. Default value is 0, which means to fetch from the primary subgraph. |

| Returns | |
| a numpy array. | |

### `get_tensor_details`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/lite/python/interpreter.py#L656-L671)

```
get_tensor_details()
```

Gets tensor details for every tensor with valid tensor details.

Tensors where required information about the tensor is not found are not
added to the list. This includes temporary tensors without a name.

| Returns | |
| A list of dictionaries containing tensor information. | |

### `invoke`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/lite/python/interpreter.py#L928-L941)

```
invoke()
```

Invoke the interpreter.

Be sure to set the input sizes, allocate tensors and fill values before
calling this. Also, note that this function releases the GIL so heavy
computation can be done in the background while the Python interpreter
continues. No other function on this object should be called while the
invoke() call has not finished.

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | When the underlying interpreter fails raise ValueError. |

### `reset_all_variables`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/lite/python/interpreter.py#L943-L944)

```
reset_all_variables()
```

### `resize_tensor_input`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/lite/python/interpreter.py#L722-L749)

```
resize_tensor_input(
    input_index, tensor_size, strict=False
)
```

Resizes an input tensor.

| Args | |

|  |  |
| --- | --- |
| `input_index` | Tensor index of input to set. This value can be gotten from the 'index' field in get\_input\_details. |
| `tensor_size` | The tensor\_shape to resize the input to. |
| `strict` | Only unknown dimensions can be resized when `strict` is True. Unknown dimensions are indicated as `-1` in the `shape_signature` attribute of a given tensor. (default False) |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If the interpreter could not resize the input tensor. |

#### Usage:

```
interpreter = Interpreter(model_content=tflite_model)
interpreter.resize_tensor_input(0, [num_test_images, 224, 224, 3])
interpreter.allocate_tensors()
interpreter.set_tensor(0, test_images)
interpreter.invoke()
```

### `set_tensor`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/lite/python/interpreter.py#L704-L720)

```
set_tensor(
    tensor_index, value
)
```

Sets the value of the input tensor.

Note this copies data in `value`.

If you want to avoid copying, you can use the `tensor()` function to get a
numpy buffer pointing to the input buffer in the tflite interpreter.

| Args | |

|  |  |
| --- | --- |
| `tensor_index` | Tensor index of tensor to set. This value can be gotten from the 'index' field in get\_input\_details. |
| `value` | Value of tensor to set. |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If the interpreter could not set the tensor. |

### `tensor`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/lite/python/interpreter.py#L878-L926)

```
tensor(
    tensor_index
)
```

Returns function that gives a numpy view of the current tensor buffer.

This allows reading and writing to this tensors w/o copies. This more
closely mirrors the C++ Interpreter class interface's tensor() member, hence
the name. Be careful to not hold these output references through calls
to `allocate_tensors()` and `invoke()`. This function cannot be used to read
intermediate results.

#### Usage:

```
interpreter.allocate_tensors()
input = interpreter.tensor(interpreter.get_input_details()[0]["index"])
output = interpreter.tensor(interpreter.get_output_details()[0]["index"])
for i in range(10):
  input().fill(3.)
  interpreter.invoke()
  print("inference %s" % output())
```

Notice how this function avoids making a numpy array directly. This is
because it is important to not hold actual numpy views to the data longer
than necessary. If you do, then the interpreter can no longer be invoked,
because it is possible the interpreter would resize and invalidate the
referenced tensors. The NumPy API doesn't allow any mutability of the
the underlying buffers.

#### WRONG:

```
input = interpreter.tensor(interpreter.get_input_details()[0]["index"])()
output = interpreter.tensor(interpreter.get_output_details()[0]["index"])()
interpreter.allocate_tensors()  # This will throw RuntimeError
for i in range(10):
  input.fill(3.)
  interpreter.invoke()  # this will throw RuntimeError since input,output
```

| Args | |

|  |  |
| --- | --- |
| `tensor_index` | Tensor index of tensor to get. This value can be gotten from the 'index' field in get\_output\_details. |

| Returns | |
| A function that can return a new numpy array pointing to the internal TFLite tensor state at any point. It is safe to hold the function forever, but it is not safe to hold the numpy array forever. | |
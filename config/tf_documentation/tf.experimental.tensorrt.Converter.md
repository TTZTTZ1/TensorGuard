# tf.experimental.tensorrt.Converter

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/experimental/tensorrt/Converter](https://tensorflow.google.cn/api_docs/python/tf/experimental/tensorrt/Converter)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/compiler/tensorrt/trt_convert.py#L1076-L1769) |

An offline converter for TF-TRT transformation for TF 2.0 SavedModels.

```
tf.experimental.tensorrt.Converter(
    input_saved_model_dir=None,
    input_saved_model_tags=None,
    input_saved_model_signature_key=None,
    use_dynamic_shape=None,
    dynamic_shape_profile_strategy=None,
    max_workspace_size_bytes=DEFAULT_TRT_MAX_WORKSPACE_SIZE_BYTES,
    precision_mode=TrtPrecisionMode.FP32,
    minimum_segment_size=3,
    maximum_cached_engines=1,
    use_calibration=True,
    allow_build_at_runtime=True,
    conversion_params=None
)
```

Windows support is provided experimentally. No guarantee is made regarding
functionality or engineering support. Use at your own risk.

There are several ways to run the conversion:

1. FP32/FP16 precision

   ```
   params = tf.experimental.tensorrt.ConversionParams(
       precision_mode='FP16')
   converter = tf.experimental.tensorrt.Converter(
       input_saved_model_dir="my_dir", conversion_params=params)
   converter.convert()
   converter.save(output_saved_model_dir)
   ```

   In this case, no TRT engines will be built or saved in the converted
   SavedModel. But if input data is available during conversion, we can still
   build and save the TRT engines to reduce the cost during inference (see
   option 2 below).
2. FP32/FP16 precision with pre-built engines

   ```
   params = tf.experimental.tensorrt.ConversionParams(
       precision_mode='FP16',
       # Set this to a large enough number so it can cache all the engines.
       maximum_cached_engines=16)
   converter = tf.experimental.tensorrt.Converter(
       input_saved_model_dir="my_dir", conversion_params=params)
   converter.convert()

   # Define a generator function that yields input data, and use it to execute
   # the graph to build TRT engines.
   def my_input_fn():
     for _ in range(num_runs):
       inp1, inp2 = ...
       yield inp1, inp2

   converter.build(input_fn=my_input_fn)  # Generate corresponding TRT engines
   converter.save(output_saved_model_dir)  # Generated engines will be saved.
   ```

   In this way, one engine will be built/saved for each unique input shapes of
   the TRTEngineOp. This is good for applications that cannot afford building
   engines during inference but have access to input data that is similar to
   the one used in production (for example, that has the same input shapes).
   Also, the generated TRT engines is platform dependent, so we need to run
   `build()` in an environment that is similar to production (e.g. with
   same type of GPU).
3. INT8 precision and calibration with pre-built engines

   ```
   params = tf.experimental.tensorrt.ConversionParams(
       precision_mode='INT8',
       # Currently only one INT8 engine is supported in this mode.
       maximum_cached_engines=1,
       use_calibration=True)
   converter = tf.experimental.tensorrt.Converter(
       input_saved_model_dir="my_dir", conversion_params=params)

   # Define a generator function that yields input data, and run INT8
   # calibration with the data. All input data should have the same shape.
   # At the end of convert(), the calibration stats (e.g. range information)
   # will be saved and can be used to generate more TRT engines with different
   # shapes. Also, one TRT engine will be generated (with the same shape as
   # the calibration data) for save later.
   def my_calibration_input_fn():
     for _ in range(num_runs):
       inp1, inp2 = ...
       yield inp1, inp2

   converter.convert(calibration_input_fn=my_calibration_input_fn)

   # (Optional) Generate more TRT engines offline (same as the previous
   # option), to avoid the cost of generating them during inference.
   def my_input_fn():
     for _ in range(num_runs):
       inp1, inp2 = ...
       yield inp1, inp2
   converter.build(input_fn=my_input_fn)

   # Save the TRT engine and the engines.
   converter.save(output_saved_model_dir)
   ```
4. To use dynamic shape, we need to call the build method with an input
   function to generate profiles. This step is similar to the INT8 calibration
   step described above. The converter also needs to be created with
   use\_dynamic\_shape=True and one of the following profile\_strategies for
   creating profiles based on the inputs produced by the input function:

   * `Range`: create one profile that works for inputs with dimension values
     in the range of [min\_dims, max\_dims] where min\_dims and max\_dims are
     derived from the provided inputs.
   * `Optimal`: create one profile for each input. The profile only works for
     inputs with the same dimensions as the input it is created for. The GPU
     engine will be run with optimal performance with such inputs.
   * `Range+Optimal`: create the profiles for both `Range` and `Optimal`.

| Args | |

|  |  |
| --- | --- |
| `input_saved_model_dir` | the directory to load the SavedModel which contains the input graph to transforms. Required. |
| `input_saved_model_tags` | list of tags to load the SavedModel. |
| `input_saved_model_signature_key` | the key of the signature to optimize the graph for. |
| `use_dynamic_shape` | whether to enable dynamic shape support. None is equivalent to False in the current implementation. |
| `dynamic_shape_profile_strategy` | one of the strings in supported\_profile\_strategies(). None is equivalent to Range in the current implementation. |
| `max_workspace_size_bytes` | the maximum GPU temporary memory that the TRT engine can use at execution time. This corresponds to the 'workspaceSize' parameter of nvinfer1::IBuilder::setMaxWorkspaceSize(). |
| `precision_mode` | one of the strings in TrtPrecisionMode.supported\_precision\_modes(). |
| `minimum_segment_size` | the minimum number of nodes required for a subgraph to be replaced by TRTEngineOp. |
| `maximum_cached_engines` | max number of cached TRT engines for dynamic TRT ops. Created TRT engines for a dynamic dimension are cached. If the number of cached engines is already at max but none of them supports the input shapes, the TRTEngineOp will fall back to run the original TF subgraph that corresponds to the TRTEngineOp. |
| `use_calibration` | this argument is ignored if precision\_mode is not INT8. If set to True, a calibration graph will be created to calibrate the missing ranges. The calibration graph must be converted to an inference graph by running calibration with calibrate(). If set to False, quantization nodes will be expected for every tensor in the graph (excluding those which will be fused). If a range is missing, an error will occur. Please note that accuracy may be negatively affected if there is a mismatch between which tensors TRT quantizes and which tensors were trained with fake quantization. |
| `allow_build_at_runtime` | whether to allow building TensorRT engines during runtime if no prebuilt TensorRT engine can be found that can handle the given inputs during runtime, then a new TensorRT engine is built at runtime if allow\_build\_at\_runtime=True, and otherwise native TF is used. |
| `conversion_params` | a TrtConversionParams instance (deprecated). |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | if the combination of the parameters is invalid. |

## Methods

### `build`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/compiler/tensorrt/trt_convert.py#L1464-L1557)

```
build(
    input_fn
)
```

Run inference with converted graph in order to build TensorRT engines.

If the conversion requires INT8 calibration, then a reference to the
calibration function was stored during the call to convert(). Calibration
will be performed while we build the TensorRT engines.

| Args | |

|  |  |
| --- | --- |
| `input_fn` | a generator function that provides the input data as a single array, OR a list or tuple of the arrays OR a dict, which will be used to execute the converted signature to generate TRT engines. Example 1: `def input\_fn(): # Let's assume a network with 1 input tensor. # We generate 2 sets of dummy input data: input\_shapes = [(1, 16), # 1st shape (2, 32)] # 2nd shape for shapes in input\_shapes: # return an input tensor yield np.zeros(shape).astype(np.float32)' |

Example 2:
`def input_fn():
# Let's assume a network with 2 input tensors.
# We generate 3 sets of dummy input data:
input_shapes = [[(1, 16), (2, 16)], # 1st input list
[(2, 32), (4, 32)], # 2nd list of two tensors
[(4, 32), (8, 32)]] # 3rd input list
for shapes in input_shapes:
# return a list of input tensors
yield [np.zeros(x).astype(np.float32) for x in shapes]`

| Raises | |

|  |  |
| --- | --- |
| `NotImplementedError` | build() is already called. |
| `RuntimeError` | the input\_fx is None. |

### `convert`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/compiler/tensorrt/trt_convert.py#L1360-L1462)

```
convert(
    calibration_input_fn=None
)
```

Convert the input SavedModel in 2.0 format.

| Args | |

|  |  |
| --- | --- |
| `calibration_input_fn` | a generator function that yields input data as a list or tuple or dict, which will be used to execute the converted signature for calibration. All the returned input data should have the same shape. Example: `def input_fn(): yield input1, input2, input3` |

If dynamic\_shape\_mode==False, (or if the graph has static input shapes)
then we run calibration and build the calibrated engine during
conversion.

If dynamic\_shape\_mode==True (and the graph has any unknown input
shape), then the reference to calibration\_input\_fn is stored, and the
calibration is actually performed when we build the engine (see
build()).

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | if the input combination is invalid. |

| Returns | |
| The TF-TRT converted Function. | |

### `save`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/compiler/tensorrt/trt_convert.py#L1559-L1665)

```
save(
    output_saved_model_dir, save_gpu_specific_engines=True, options=None
)
```

Save the converted SavedModel.

| Args | |

|  |  |
| --- | --- |
| `output_saved_model_dir` | directory to saved the converted SavedModel. |
| `save_gpu_specific_engines` | whether to save TRT engines that have been built. When True, all engines are saved and when False, the engines are not saved and will be rebuilt at inference time. By using save\_gpu\_specific\_engines=False after doing INT8 calibration, inference can be done on different GPUs than the GPU that the model was calibrated and saved on. |
| `options` | [`tf.saved_model.SaveOptions`](https://tensorflow.google.cn/api_docs/python/tf/saved_model/SaveOptions) object for configuring save options. |

| Raises | |

|  |  |
| --- | --- |
| `RuntimeError` | if the needed calibration hasn't been done. |

### `summary`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/compiler/tensorrt/trt_convert.py#L1667-L1769)

```
summary(
    line_length=160, detailed=True, print_fn=None
)
```

This method describes the results of the conversion by TF-TRT.

It includes information such as the name of the engine, the number of nodes
per engine, the input and output dtype, along with the input shape of each
TRTEngineOp.

| Args | |

|  |  |
| --- | --- |
| `line_length` | Default line length when printing on the console. Minimum 160 characters long. |
| `detailed` | Whether or not to show the nodes inside each TRTEngineOp. |
| `print_fn` | Print function to use. Defaults to `print`. It will be called on each line of the summary. You can set it to a custom function in order to capture the string summary. |

| Raises | |

|  |  |
| --- | --- |
| `RuntimeError` | if the graph is not converted. |
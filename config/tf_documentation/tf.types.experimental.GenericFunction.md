# tf.types.experimental.GenericFunction

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/types/experimental/GenericFunction](https://tensorflow.google.cn/api_docs/python/tf/types/experimental/GenericFunction)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/types/core.py#L186-L368) |

Base class for polymorphic graph functions.

Inherits From: [`Callable`](https://tensorflow.google.cn/api_docs/python/tf/types/experimental/Callable)

#### View aliases

**Main aliases**

[`tf.types.experimental.GenericFunction`](https://tensorflow.google.cn/api_docs/python/tf/types/experimental/PolymorphicFunction)

Graph functions are Python callable objects that dispatch calls to a
TensorFlow graph. Polymorphic graph functions can be backed by multiple TF
graphs, and automatically select the appropriate specialization based on the
type of input they were called with. They may also create specializations on
the fly if necessary, for example by tracing.

Also see [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function).

| Attributes | |

|  |  |
| --- | --- |
| `function_type` | Returns a FunctionType describing this callable. |

## Methods

### `experimental_get_compiler_ir`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/types/core.py#L251-L368)

```
experimental_get_compiler_ir(
    *args, **kwargs
)
```

Returns compiler IR for the compiled function.

This API is intended *only* for debugging as there are no guarantees on
backwards compatibility of returned IR or the allowed values of `stage`.

| Args | |

|  |  |
| --- | --- |
| `*args` | compilation args supports inputs either: (1) all inputs are TensorSpec or (2) all inputs are tf.Tensor/Python variables. |
| `**kwargs` | Keyword arguments used for compilation. Same requirement as compiliation args. |

| Returns | |
| Function callable with the following kwargs: | |

* `stage` at which the compiler IR should be serialized. Allowed values
  are:
  + `hlo`: HLO output after conversion from TF
    ([https://www.tensorflow.org/xla/operation\_semantics](https://tensorflow.google.cn/xla/operation_semantics)).
  + `hlo_serialized`: Like stage=`hlo`, but the output is a serialized
    HLO module proto (a bytes object).
  + `optimized_hlo`: HLO after compiler optimizations.
  + `optimized_hlo_serialized`: Like stage=`optimized_hlo`, but the
    output is a serialized HLO module proto (a bytes object).
  + `optimized_hlo_dot`: optimized HLO in DOT format suitable for
    Graphviz.
* `device_name` can be either None, in which case the preferred device
  is used for compilation, or a device name. It can be a full device
  name, or a partial one, e.g., `/device:CPU:0`.

For example, for

```
@tf.function(jit_compile=True)
def f(x):
  return x + 1

f.experimental_get_compiler_ir(tf.random.normal([10, 10])(stage='hlo')
```

the output is:

```
HloModule a_inference_f_13__.9

ENTRY %a_inference_f_13__.9 (arg0.1: f32[10,10]) -> f32[10,10] {
  %arg0.1 = f32[10,10]{1,0} parameter(0), parameter_replication={false}
  %reshape.2 = f32[10,10]{1,0} reshape(f32[10,10]{1,0} %arg0.1)
  %constant.3 = f32[] constant(1)
  %broadcast.4 = f32[10,10]{1,0} broadcast(f32[] %constant.3)
  %add.5 = f32[10,10]{1,0} add(f32[10,10]{1,0} %reshape.2,
                               f32[10,10]{1,0} %broadcast.4)
  %reshape.6 = f32[10,10]{1,0} reshape(f32[10,10]{1,0} %add.5)
  %tuple.7 = (f32[10,10]{1,0}) tuple(f32[10,10]{1,0} %reshape.6)
  ROOT %get-tuple-element.8 = f32[10,10]{1,0}
    get-tuple-element((f32[10,10]{1,0}) %tuple.7), index=0
}
```

Here is another example using tf.TensorSpec inputs:

```
y = tf.Variable(tf.zeros([10, 20], dtype=tf.float32))

@tf.function(jit_compile=True)
def f(x):
  return x + y

hlo_str = f.experimental_get_compiler_ir(tf.TensorSpec(shape=(10,
20)))(stage='hlo')
```

The output is:

```
HloModule a_inference_f_120__.8,
entry_computation_layout={(f32[10,20]{1,0},f32[10,20]{1,0})->f32[10,20]{1,0} }

ENTRY %a_inference_f_120__.8 (arg0.1: f32[10,20], arg1.2: f32[10,20]) ->
f32[10,20] {
  %arg0.1 = f32[10,20]{1,0} parameter(0), parameter_replication={false},
  metadata={op_name="XLA_Args"}
  %reshape.3 = f32[10,20]{1,0} reshape(f32[10,20]{1,0} %arg0.1)
  %arg1.2 = f32[10,20]{1,0} parameter(1), parameter_replication={false},
  metadata={op_name="XLA_Args"}
  %add.4 = f32[10,20]{1,0} add(f32[10,20]{1,0} %reshape.3, f32[10,20]{1,0}
  %arg1.2), metadata={op_type="AddV2" op_name="add"
  source_file="<ipython-input-16-ea04879c1873>" source_line=4}
  %reshape.5 = f32[10,20]{1,0} reshape(f32[10,20]{1,0} %add.4),
  metadata={op_name="XLA_Retvals"}
  %tuple.6 = (f32[10,20]{1,0}) tuple(f32[10,20]{1,0} %reshape.5),
  metadata={op_name="XLA_Retvals"}
  ROOT %get-tuple-element.7 = f32[10,20]{1,0}
  get-tuple-element((f32[10,20]{1,0}) %tuple.6), index=0,
  metadata={op_name="XLA_Retvals"}
}
</td>
</tr>

</table>
```

The HLO module accepts a flat list of inputs. To retrieve the order
of these inputs signatures, users can call the
`concrete_fn.structured_input_signature` and `concrete_fn.captured_inputs`:

```
# Use concrete_fn to get the hlo_module flat_args.
concrete_fn = f.get_concrete_function(tf.TensorSpec(shape=(10, 20)))
flat_args = list(
    tf.nest.flatten(concrete_fn.structured_input_signature)
    ) + concrete_fn.captured_inputs
```

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | (1) If an invalid `stage` is selected (2) or if applied to a function which is not compiled (`jit_compile=True` is not set). (3) or if input shapes are not fully defined for tf.TensorSpec inputs |
| `TypeError` | When called with input in graph mode. |

### `get_concrete_function`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/types/core.py#L203-L249)

```
@abc.abstractmethod
get_concrete_function(
    *args, **kwargs
) -> tf.types.experimental.ConcreteFunction

tf.types.experimental.ConcreteFunction
```

Returns a `ConcreteFunction` specialized to input types.

The arguments specified by `args` and `kwargs` follow normal function call
rules. The returned `ConcreteFunction` has the same set of positional and
keyword arguments as `self`, but their types are compatible to the types
specified by `args` and `kwargs` (though not neccessarily equal).

```
>>> @tf.function
... def f(x):
...   return x
>>> f_concrete = f.get_concrete_function(tf.constant(1.0))
>>> f_concrete = f.get_concrete_function(x=tf.constant(1.0))
```

Unlike normal calls, `get_concrete_function` allow type specifiers instead
of TensorFlow objects, so for example [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor)s may be replaced with
[`tf.TensorSpec`](https://tensorflow.google.cn/api_docs/python/tf/TensorSpec)s.

```
>>> @tf.function
... def f(x):
...   return x
>>> f_concrete = f.get_concrete_function(tf.TensorSpec([], tf.float64))
```

If the function definition allows only one specialization, `args` and
`kwargs` may be omitted altogether.

```
>>> @tf.function(input_signature=[tf.TensorSpec(None, tf.float32)])
... def f(x):
...   return x
>>> f_concrete = f.get_concrete_function()
```

The returned `ConcreteFunction` can be called normally:

```
>>> f_concrete(tf.constant(1.0))
<tf.Tensor: shape=(), dtype=float32, numpy=1.0>
>>> f_concrete(x=tf.constant(1.0))
<tf.Tensor: shape=(), dtype=float32, numpy=1.0>
```

| Args | |

|  |  |
| --- | --- |
| `*args` | inputs to specialize on. |
| `**kwargs` | inputs to specialize on. |

| Returns | |
| A `ConcreteFunction`. | |

### `__call__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/types/core.py#L124-L139)

```
__call__(
    *args, **kwargs
)
```

Executes this callable.

This behaves like a regular op - in eager mode, it immediately starts
execution, returning results. In graph mode, it creates ops which return
symbolic TensorFlow values (like [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor), [`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset),
etc.). For example, [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function) callables typically generate a
[`tf.raw_ops.PartitionedCall`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/PartitionedCall) op, but not always - the
exact operations being generated are an internal implementation detail.

| Args | |

|  |  |
| --- | --- |
| `*args` | positional argument for this call |
| `**kwargs` | keyword arguments for this call |

| Returns | |
| The execution results. | |
# tf.keras.layers.GRU

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/GRU](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/GRU)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/rnn/gru.py#L330-L689) |

Gated Recurrent Unit - Cho et al. 2014.

Inherits From: [`RNN`](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/RNN), [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.GRU(
    units,
    activation='tanh',
    recurrent_activation='sigmoid',
    use_bias=True,
    kernel_initializer='glorot_uniform',
    recurrent_initializer='orthogonal',
    bias_initializer='zeros',
    kernel_regularizer=None,
    recurrent_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    kernel_constraint=None,
    recurrent_constraint=None,
    bias_constraint=None,
    dropout=0.0,
    recurrent_dropout=0.0,
    seed=None,
    return_sequences=False,
    return_state=False,
    go_backwards=False,
    stateful=False,
    unroll=False,
    reset_after=True,
    use_cudnn='auto',
    **kwargs
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Working with preprocessing layers](https://tensorflow.google.cn/guide/keras/preprocessing_layers) | * [Transfer learning for video classification with MoViNet](https://tensorflow.google.cn/tutorials/video/transfer_learning_with_movinet) * [Neural machine translation with attention](https://tensorflow.google.cn/text/tutorials/nmt_with_attention) * [Recommending movies: retrieval using a sequential model](https://tensorflow.google.cn/recommenders/examples/sequential_retrieval) * [Text generation with an RNN](https://tensorflow.google.cn/text/tutorials/text_generation) |

Based on available runtime hardware and constraints, this layer
will choose different implementations (cuDNN-based or backend-native)
to maximize the performance. If a GPU is available and all
the arguments to the layer meet the requirement of the cuDNN kernel
(see below for details), the layer will use a fast cuDNN implementation
when using the TensorFlow backend.

The requirements to use the cuDNN implementation are:

1. `activation` == `tanh`
2. `recurrent_activation` == `sigmoid`
3. `dropout` == 0 and `recurrent_dropout` == 0
4. `unroll` is `False`
5. `use_bias` is `True`
6. `reset_after` is `True`
7. Inputs, if use masking, are strictly right-padded.
8. Eager execution is enabled in the outermost context.

There are two variants of the GRU implementation. The default one is based
on [v3](https://arxiv.org/abs/1406.1078v3) and has reset gate applied to
hidden state before matrix multiplication. The other one is based on
[original](https://arxiv.org/abs/1406.1078v1) and has the order reversed.

The second variant is compatible with CuDNNGRU (GPU-only) and allows
inference on CPU. Thus it has separate biases for `kernel` and
`recurrent_kernel`. To use this variant, set `reset_after=True` and
`recurrent_activation='sigmoid'`.

#### For example:

```
>>> inputs = np.random.random((32, 10, 8))
>>> gru = keras.layers.GRU(4)
>>> output = gru(inputs)
>>> output.shape
(32, 4)
>>> gru = keras.layers.GRU(4, return_sequences=True, return_state=True)
>>> whole_sequence_output, final_state = gru(inputs)
>>> whole_sequence_output.shape
(32, 10, 4)
>>> final_state.shape
(32, 4)
```

| Args | |

|  |  |
| --- | --- |
| `units` | Positive integer, dimensionality of the output space. |
| `activation` | Activation function to use. Default: hyperbolic tangent (`tanh`). If you pass `None`, no activation is applied (ie. "linear" activation: `a(x) = x`). |
| `recurrent_activation` | Activation function to use for the recurrent step. Default: sigmoid (`sigmoid`). If you pass `None`, no activation is applied (ie. "linear" activation: `a(x) = x`). |
| `use_bias` | Boolean, (default `True`), whether the layer should use a bias vector. |
| `kernel_initializer` | Initializer for the `kernel` weights matrix, used for the linear transformation of the inputs. Default: `"glorot_uniform"`. |
| `recurrent_initializer` | Initializer for the `recurrent_kernel` weights matrix, used for the linear transformation of the recurrent state. Default: `"orthogonal"`. |
| `bias_initializer` | Initializer for the bias vector. Default: `"zeros"`. |
| `kernel_regularizer` | Regularizer function applied to the `kernel` weights matrix. Default: `None`. |
| `recurrent_regularizer` | Regularizer function applied to the `recurrent_kernel` weights matrix. Default: `None`. |
| `bias_regularizer` | Regularizer function applied to the bias vector. Default: `None`. |
| `activity_regularizer` | Regularizer function applied to the output of the layer (its "activation"). Default: `None`. |
| `kernel_constraint` | Constraint function applied to the `kernel` weights matrix. Default: `None`. |
| `recurrent_constraint` | Constraint function applied to the `recurrent_kernel` weights matrix. Default: `None`. |
| `bias_constraint` | Constraint function applied to the bias vector. Default: `None`. |
| `dropout` | Float between 0 and 1. Fraction of the units to drop for the linear transformation of the inputs. Default: 0. |
| `recurrent_dropout` | Float between 0 and 1. Fraction of the units to drop for the linear transformation of the recurrent state. Default: 0. |
| `seed` | Random seed for dropout. |
| `return_sequences` | Boolean. Whether to return the last output in the output sequence, or the full sequence. Default: `False`. |
| `return_state` | Boolean. Whether to return the last state in addition to the output. Default: `False`. |
| `go_backwards` | Boolean (default `False`). If `True`, process the input sequence backwards and return the reversed sequence. |
| `stateful` | Boolean (default: `False`). If `True`, the last state for each sample at index i in a batch will be used as initial state for the sample of index i in the following batch. |
| `unroll` | Boolean (default: `False`). If `True`, the network will be unrolled, else a symbolic loop will be used. Unrolling can speed-up a RNN, although it tends to be more memory-intensive. Unrolling is only suitable for short sequences. |
| `reset_after` | GRU convention (whether to apply reset gate after or before matrix multiplication). `False` is `"before"`, `True` is `"after"` (default and cuDNN compatible). |
| `use_cudnn` | Whether to use a cuDNN-backed implementation. `"auto"` will attempt to use cuDNN when feasible, and will fallback to the default implementation if not. |

| Call arguments | |

|  |  |
| --- | --- |
| `inputs` | A 3D tensor, with shape `(batch, timesteps, feature)`. |
| `mask` | Binary tensor of shape `(samples, timesteps)` indicating whether a given timestep should be masked (optional). An individual `True` entry indicates that the corresponding timestep should be utilized, while a `False` entry indicates that the corresponding timestep should be ignored. Defaults to `None`. |
| `training` | Python boolean indicating whether the layer should behave in training mode or in inference mode. This argument is passed to the cell when calling it. This is only relevant if `dropout` or `recurrent_dropout` is used (optional). Defaults to `None`. |
| `initial_state` | List of initial state tensors to be passed to the first call of the cell (optional, `None` causes creation of zero-filled initial state tensors). Defaults to `None`. |

| Attributes | |

|  |  |
| --- | --- |
| `activation` |  |

|  |  |
| --- | --- |
| `bias_constraint` |  |

|  |  |
| --- | --- |
| `bias_initializer` |  |

|  |  |
| --- | --- |
| `bias_regularizer` |  |

|  |  |
| --- | --- |
| `dropout` |  |

|  |  |
| --- | --- |
| `input` | Retrieves the input tensor(s) of a symbolic operation. |

Only returns the tensor(s) corresponding to the *first time*
the operation was called.| `kernel_constraint` |  |

|  |  |
| --- | --- |
| `kernel_initializer` |  |

|  |  |
| --- | --- |
| `kernel_regularizer` |  |

|  |  |
| --- | --- |
| `output` | Retrieves the output tensor(s) of a layer. |

Only returns the tensor(s) corresponding to the *first time*
the operation was called.| `recurrent_activation` |  |

|  |  |
| --- | --- |
| `recurrent_constraint` |  |

|  |  |
| --- | --- |
| `recurrent_dropout` |  |

|  |  |
| --- | --- |
| `recurrent_initializer` |  |

|  |  |
| --- | --- |
| `recurrent_regularizer` |  |

|  |  |
| --- | --- |
| `reset_after` |  |

|  |  |
| --- | --- |
| `units` |  |

|  |  |
| --- | --- |
| `use_bias` |  |

## Methods

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/rnn/gru.py#L687-L689)

```
@classmethod
from_config(
    config
)
```

Creates a layer from its config.

This method is the reverse of `get_config`,
capable of instantiating the same layer from the config
dictionary. It does not handle layer connectivity
(handled by Network), nor weights (handled by `set_weights`).

| Args | |

|  |  |
| --- | --- |
| `config` | A Python dictionary, typically the output of get\_config. |

| Returns | |
| A layer instance. | |

### `get_initial_state`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/rnn/rnn.py#L306-L321)

```
get_initial_state(
    batch_size
)
```

### `inner_loop`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/rnn/gru.py#L535-L577)

```
inner_loop(
    sequences, initial_state, mask, training=False
)
```

### `reset_state`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/rnn/rnn.py#L327-L330)

```
reset_state()
```

### `reset_states`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/rnn/rnn.py#L323-L325)

```
reset_states()
```

### `symbolic_call`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/ops/operation.py#L58-L70)

```
symbolic_call(
    *args, **kwargs
)
```
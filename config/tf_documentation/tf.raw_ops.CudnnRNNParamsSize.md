# tf.raw_ops.CudnnRNNParamsSize

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CudnnRNNParamsSize](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CudnnRNNParamsSize)

---

Computes size of weights that can be used by a Cudnn RNN model.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.CudnnRNNParamsSize`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CudnnRNNParamsSize)

```
tf.raw_ops.CudnnRNNParamsSize(
    num_layers,
    num_units,
    input_size,
    T,
    S,
    rnn_mode='lstm',
    input_mode='linear_input',
    direction='unidirectional',
    dropout=0,
    seed=0,
    seed2=0,
    num_proj=0,
    name=None
)
```

Return the params size that can be used by the Cudnn RNN model. Subsequent
weight allocation and initialization should use this size.

num\_layers: Specifies the number of layers in the RNN model.
num\_units: Specifies the size of the hidden state.
input\_size: Specifies the size of the input state.
rnn\_mode: Indicates the type of the RNN model.
input\_mode: Indicate whether there is a linear projection between the input and
The actual computation before the first layer. 'skip\_input' is only allowed
when input\_size == num\_units; 'auto\_select' implies 'skip\_input' when
input\_size == num\_units; otherwise, it implies 'linear\_input'.
direction: Indicates whether a bidirectional model will be used.
dir = (direction == bidirectional) ? 2 : 1
dropout: dropout probability. When set to 0., dropout is disabled.
seed: the 1st part of a seed to initialize dropout.
seed2: the 2nd part of a seed to initialize dropout.
params\_size: The size of the params buffer that should be allocated and
initialized for this RNN model. Note that this params buffer may not be
compatible across GPUs. Please use CudnnRNNParamsWeights and
CudnnRNNParamsBiases to save and restore them in a way that is compatible
across different runs.

| Args | |

|  |  |
| --- | --- |
| `num_layers` | A `Tensor` of type `int32`. |
| `num_units` | A `Tensor` of type `int32`. |
| `input_size` | A `Tensor` of type `int32`. |
| `T` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) from: `tf.bfloat16, tf.half, tf.float32, tf.float64`. |
| `S` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) from: `tf.int32, tf.int64`. |
| `rnn_mode` | An optional `string` from: `"rnn_relu", "rnn_tanh", "lstm", "gru"`. Defaults to `"lstm"`. |
| `input_mode` | An optional `string` from: `"linear_input", "skip_input", "auto_select"`. Defaults to `"linear_input"`. |
| `direction` | An optional `string` from: `"unidirectional", "bidirectional"`. Defaults to `"unidirectional"`. |
| `dropout` | An optional `float`. Defaults to `0`. |
| `seed` | An optional `int`. Defaults to `0`. |
| `seed2` | An optional `int`. Defaults to `0`. |
| `num_proj` | An optional `int`. Defaults to `0`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `S`. | |
# tf.raw_ops.CudnnRNNBackpropV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CudnnRNNBackpropV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CudnnRNNBackpropV2)

---

Backprop step of CudnnRNN.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.CudnnRNNBackpropV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CudnnRNNBackpropV2)

```
tf.raw_ops.CudnnRNNBackpropV2(
    input,
    input_h,
    input_c,
    params,
    output,
    output_h,
    output_c,
    output_backprop,
    output_h_backprop,
    output_c_backprop,
    reserve_space,
    host_reserved,
    rnn_mode='lstm',
    input_mode='linear_input',
    direction='unidirectional',
    dropout=0,
    seed=0,
    seed2=0,
    name=None
)
```

Compute the backprop of both data and weights in a RNN. Takes an extra
"host\_reserved" inupt than CudnnRNNBackprop, which is used to determine RNN
cudnnRNNAlgo\_t and cudnnMathType\_t.

rnn\_mode: Indicates the type of the RNN model.
input\_mode: Indicates whether there is a linear projection between the input and
the actual computation before the first layer. 'skip\_input' is only allowed
when input\_size == num\_units; 'auto\_select' implies 'skip\_input' when
input\_size == num\_units; otherwise, it implies 'linear\_input'.
direction: Indicates whether a bidirectional model will be used. Should be
"unidirectional" or "bidirectional".
dropout: Dropout probability. When set to 0., dropout is disabled.
seed: The 1st part of a seed to initialize dropout.
seed2: The 2nd part of a seed to initialize dropout.
input: A 3-D tensor with the shape of [seq\_length, batch\_size, input\_size].
input\_h: A 3-D tensor with the shape of [num\_layer \* dir, batch\_size,
num\_units].
input\_c: For LSTM, a 3-D tensor with the shape of
[num\_layer \* dir, batch, num\_units]. For other models, it is ignored.
params: A 1-D tensor that contains the weights and biases in an opaque layout.
The size must be created through CudnnRNNParamsSize, and initialized
separately. Note that they might not be compatible across different
generations. So it is a good idea to save and restore
output: A 3-D tensor with the shape of [seq\_length, batch\_size,
dir \* num\_units].
output\_h: The same shape has input\_h.
output\_c: The same shape as input\_c for LSTM. An empty tensor for other models.
output\_backprop: A 3-D tensor with the same shape as output in the forward pass.
output\_h\_backprop: A 3-D tensor with the same shape as output\_h in the forward
pass.
output\_c\_backprop: A 3-D tensor with the same shape as output\_c in the forward
pass.
reserve\_space: The same reserve\_space produced in the forward operation.
host\_reserved: The same host\_reserved produced in the forward operation.
input\_backprop: The backprop to input in the forward pass. Has the same shape
as input.
input\_h\_backprop: The backprop to input\_h in the forward pass. Has the same
shape as input\_h.
input\_c\_backprop: The backprop to input\_c in the forward pass. Has the same
shape as input\_c.
params\_backprop: The backprop to the params buffer in the forward pass. Has the
same shape as params.

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`. |
| `input_h` | A `Tensor`. Must have the same type as `input`. |
| `input_c` | A `Tensor`. Must have the same type as `input`. |
| `params` | A `Tensor`. Must have the same type as `input`. |
| `output` | A `Tensor`. Must have the same type as `input`. |
| `output_h` | A `Tensor`. Must have the same type as `input`. |
| `output_c` | A `Tensor`. Must have the same type as `input`. |
| `output_backprop` | A `Tensor`. Must have the same type as `input`. |
| `output_h_backprop` | A `Tensor`. Must have the same type as `input`. |
| `output_c_backprop` | A `Tensor`. Must have the same type as `input`. |
| `reserve_space` | A `Tensor`. Must have the same type as `input`. |
| `host_reserved` | A `Tensor` of type `int8`. |
| `rnn_mode` | An optional `string` from: `"rnn_relu", "rnn_tanh", "lstm", "gru"`. Defaults to `"lstm"`. |
| `input_mode` | An optional `string` from: `"linear_input", "skip_input", "auto_select"`. Defaults to `"linear_input"`. |
| `direction` | An optional `string` from: `"unidirectional", "bidirectional"`. Defaults to `"unidirectional"`. |
| `dropout` | An optional `float`. Defaults to `0`. |
| `seed` | An optional `int`. Defaults to `0`. |
| `seed2` | An optional `int`. Defaults to `0`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (input\_backprop, input\_h\_backprop, input\_c\_backprop, params\_backprop). | |
| `input_backprop` | A `Tensor`. Has the same type as `input`. |
| `input_h_backprop` | A `Tensor`. Has the same type as `input`. |
| `input_c_backprop` | A `Tensor`. Has the same type as `input`. |
| `params_backprop` | A `Tensor`. Has the same type as `input`. |
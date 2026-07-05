# tf.raw_ops.BlockLSTMGrad

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/BlockLSTMGrad](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/BlockLSTMGrad)

---

Computes the LSTM cell backward propagation for the entire time sequence.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.BlockLSTMGrad`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/BlockLSTMGrad)

```
tf.raw_ops.BlockLSTMGrad(
    seq_len_max,
    x,
    cs_prev,
    h_prev,
    w,
    wci,
    wcf,
    wco,
    b,
    i,
    cs,
    f,
    o,
    ci,
    co,
    h,
    cs_grad,
    h_grad,
    use_peephole,
    name=None
)
```

This implementation is to be used in conjunction of LSTMBlock.

| Args | |

|  |  |
| --- | --- |
| `seq_len_max` | A `Tensor` of type `int64`. Maximum time length actually used by this input. Outputs are padded with zeros beyond this length. |
| `x` | A `Tensor`. Must be one of the following types: `half`, `float32`. The sequence input to the LSTM, shape (timelen, batch\_size, num\_inputs). |
| `cs_prev` | A `Tensor`. Must have the same type as `x`. Value of the initial cell state. |
| `h_prev` | A `Tensor`. Must have the same type as `x`. Initial output of cell (to be used for peephole). |
| `w` | A `Tensor`. Must have the same type as `x`. The weight matrix. |
| `wci` | A `Tensor`. Must have the same type as `x`. The weight matrix for input gate peephole connection. |
| `wcf` | A `Tensor`. Must have the same type as `x`. The weight matrix for forget gate peephole connection. |
| `wco` | A `Tensor`. Must have the same type as `x`. The weight matrix for output gate peephole connection. |
| `b` | A `Tensor`. Must have the same type as `x`. The bias vector. |
| `i` | A `Tensor`. Must have the same type as `x`. The input gate over the whole time sequence. |
| `cs` | A `Tensor`. Must have the same type as `x`. The cell state before the tanh over the whole time sequence. |
| `f` | A `Tensor`. Must have the same type as `x`. The forget gate over the whole time sequence. |
| `o` | A `Tensor`. Must have the same type as `x`. The output gate over the whole time sequence. |
| `ci` | A `Tensor`. Must have the same type as `x`. The cell input over the whole time sequence. |
| `co` | A `Tensor`. Must have the same type as `x`. The cell after the tanh over the whole time sequence. |
| `h` | A `Tensor`. Must have the same type as `x`. The output h vector over the whole time sequence. |
| `cs_grad` | A `Tensor`. Must have the same type as `x`. The current gradient of cs. |
| `h_grad` | A `Tensor`. Must have the same type as `x`. The gradient of h vector. |
| `use_peephole` | A `bool`. Whether to use peephole weights. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (x\_grad, cs\_prev\_grad, h\_prev\_grad, w\_grad, wci\_grad, wcf\_grad, wco\_grad, b\_grad). | |
| `x_grad` | A `Tensor`. Has the same type as `x`. |
| `cs_prev_grad` | A `Tensor`. Has the same type as `x`. |
| `h_prev_grad` | A `Tensor`. Has the same type as `x`. |
| `w_grad` | A `Tensor`. Has the same type as `x`. |
| `wci_grad` | A `Tensor`. Has the same type as `x`. |
| `wcf_grad` | A `Tensor`. Has the same type as `x`. |
| `wco_grad` | A `Tensor`. Has the same type as `x`. |
| `b_grad` | A `Tensor`. Has the same type as `x`. |
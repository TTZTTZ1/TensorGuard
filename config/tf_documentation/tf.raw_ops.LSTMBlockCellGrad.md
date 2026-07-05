# tf.raw_ops.LSTMBlockCellGrad

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/LSTMBlockCellGrad](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/LSTMBlockCellGrad)

---

Computes the LSTM cell backward propagation for 1 timestep.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.LSTMBlockCellGrad`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/LSTMBlockCellGrad)

```
tf.raw_ops.LSTMBlockCellGrad(
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
    cs_grad,
    h_grad,
    use_peephole,
    name=None
)
```

This implementation is to be used in conjunction of LSTMBlockCell.

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `half`, `float32`. The input to the LSTM cell, shape (batch\_size, num\_inputs). |
| `cs_prev` | A `Tensor`. Must have the same type as `x`. The previous cell state. |
| `h_prev` | A `Tensor`. Must have the same type as `x`. The previous h state. |
| `w` | A `Tensor`. Must have the same type as `x`. The weight matrix. |
| `wci` | A `Tensor`. Must have the same type as `x`. The weight matrix for input gate peephole connection. |
| `wcf` | A `Tensor`. Must have the same type as `x`. The weight matrix for forget gate peephole connection. |
| `wco` | A `Tensor`. Must have the same type as `x`. The weight matrix for output gate peephole connection. |
| `b` | A `Tensor`. Must have the same type as `x`. The bias vector. |
| `i` | A `Tensor`. Must have the same type as `x`. The input gate. |
| `cs` | A `Tensor`. Must have the same type as `x`. The cell state before the tanh. |
| `f` | A `Tensor`. Must have the same type as `x`. The forget gate. |
| `o` | A `Tensor`. Must have the same type as `x`. The output gate. |
| `ci` | A `Tensor`. Must have the same type as `x`. The cell input. |
| `co` | A `Tensor`. Must have the same type as `x`. The cell after the tanh. |
| `cs_grad` | A `Tensor`. Must have the same type as `x`. The current gradient of cs. |
| `h_grad` | A `Tensor`. Must have the same type as `x`. The gradient of h vector. |
| `use_peephole` | A `bool`. Whether the cell uses peephole connections. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (cs\_prev\_grad, dicfo, wci\_grad, wcf\_grad, wco\_grad). | |
| `cs_prev_grad` | A `Tensor`. Has the same type as `x`. |
| `dicfo` | A `Tensor`. Has the same type as `x`. |
| `wci_grad` | A `Tensor`. Has the same type as `x`. |
| `wcf_grad` | A `Tensor`. Has the same type as `x`. |
| `wco_grad` | A `Tensor`. Has the same type as `x`. |
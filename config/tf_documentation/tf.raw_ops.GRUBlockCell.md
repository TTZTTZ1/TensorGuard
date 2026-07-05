# tf.raw_ops.GRUBlockCell

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/GRUBlockCell](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/GRUBlockCell)

---

Computes the GRU cell forward propagation for 1 time step.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.GRUBlockCell`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/GRUBlockCell)

```
tf.raw_ops.GRUBlockCell(
    x, h_prev, w_ru, w_c, b_ru, b_c, name=None
)
```

Args
x: Input to the GRU cell.
h\_prev: State input from the previous GRU cell.
w\_ru: Weight matrix for the reset and update gate.
w\_c: Weight matrix for the cell connection gate.
b\_ru: Bias vector for the reset and update gate.
b\_c: Bias vector for the cell connection gate.

Returns
r: Output of the reset gate.
u: Output of the update gate.
c: Output of the cell connection gate.
h: Current state of the GRU cell.

Note on notation of the variables:

Concatenation of a and b is represented by a\_b
Element-wise dot product of a and b is represented by ab
Element-wise dot product is represented by \circ
Matrix multiplication is represented by \*

Biases are initialized with :
`b_ru` - constant\_initializer(1.0)
`b_c` - constant\_initializer(0.0)

This kernel op implements the following mathematical equations:

```
x_h_prev = [x, h_prev]

[r_bar u_bar] = x_h_prev * w_ru + b_ru

r = sigmoid(r_bar)
u = sigmoid(u_bar)

h_prevr = h_prev \circ r

x_h_prevr = [x h_prevr]

c_bar = x_h_prevr * w_c + b_c
c = tanh(c_bar)

h = (1-u) \circ c + u \circ h_prev
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `float32`. |
| `h_prev` | A `Tensor`. Must have the same type as `x`. |
| `w_ru` | A `Tensor`. Must have the same type as `x`. |
| `w_c` | A `Tensor`. Must have the same type as `x`. |
| `b_ru` | A `Tensor`. Must have the same type as `x`. |
| `b_c` | A `Tensor`. Must have the same type as `x`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (r, u, c, h). | |
| `r` | A `Tensor`. Has the same type as `x`. |
| `u` | A `Tensor`. Has the same type as `x`. |
| `c` | A `Tensor`. Has the same type as `x`. |
| `h` | A `Tensor`. Has the same type as `x`. |
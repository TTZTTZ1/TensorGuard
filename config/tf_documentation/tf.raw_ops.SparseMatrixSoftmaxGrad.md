# tf.raw_ops.SparseMatrixSoftmaxGrad

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseMatrixSoftmaxGrad](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseMatrixSoftmaxGrad)

---

Calculates the gradient of the SparseMatrixSoftmax op.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.SparseMatrixSoftmaxGrad`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseMatrixSoftmaxGrad)

```
tf.raw_ops.SparseMatrixSoftmaxGrad(
    softmax, grad_softmax, type, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `softmax` | A `Tensor` of type `variant`. A CSRSparseMatrix. |
| `grad_softmax` | A `Tensor` of type `variant`. The gradient of `softmax`. |
| `type` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) from: `tf.float32, tf.float64`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |
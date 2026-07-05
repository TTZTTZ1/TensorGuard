# tf.raw_ops.SparseCross

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseCross](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseCross)

---

Generates sparse cross from a list of sparse and dense tensors.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.SparseCross`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseCross)

```
tf.raw_ops.SparseCross(
    indices,
    values,
    shapes,
    dense_inputs,
    hashed_output,
    num_buckets,
    hash_key,
    out_type,
    internal_type,
    name=None
)
```

The op takes two lists, one of 2D `SparseTensor` and one of 2D `Tensor`, each
representing features of one feature column. It outputs a 2D `SparseTensor` with
the batchwise crosses of these features.

For example, if the inputs are

```
inputs[0]: SparseTensor with shape = [2, 2]
[0, 0]: "a"
[1, 0]: "b"
[1, 1]: "c"

inputs[1]: SparseTensor with shape = [2, 1]
[0, 0]: "d"
[1, 0]: "e"

inputs[2]: Tensor [["f"], ["g"]]
```

then the output will be

```
shape = [2, 2]
[0, 0]: "a_X_d_X_f"
[1, 0]: "b_X_e_X_g"
[1, 1]: "c_X_e_X_g"
```

if hashed\_output=true then the output will be

```
shape = [2, 2]
[0, 0]: FingerprintCat64(
            Fingerprint64("f"), FingerprintCat64(
                Fingerprint64("d"), Fingerprint64("a")))
[1, 0]: FingerprintCat64(
            Fingerprint64("g"), FingerprintCat64(
                Fingerprint64("e"), Fingerprint64("b")))
[1, 1]: FingerprintCat64(
            Fingerprint64("g"), FingerprintCat64(
                Fingerprint64("e"), Fingerprint64("c")))
```

| Args | |

|  |  |
| --- | --- |
| `indices` | A list of `Tensor` objects with type `int64`. 2-D. Indices of each input `SparseTensor`. |
| `values` | A list of `Tensor` objects with types from: `int64`, `string`. 1-D. values of each `SparseTensor`. |
| `shapes` | A list with the same length as `indices` of `Tensor` objects with type `int64`. 1-D. Shapes of each `SparseTensor`. |
| `dense_inputs` | A list of `Tensor` objects with types from: `int64`, `string`. 2-D. Columns represented by dense `Tensor`. |
| `hashed_output` | A `bool`. If true, returns the hash of the cross instead of the string. This will allow us avoiding string manipulations. |
| `num_buckets` | An `int` that is `>= 0`. It is used if hashed\_output is true. output = hashed\_value%num\_buckets if num\_buckets > 0 else hashed\_value. |
| `hash_key` | An `int`. Specify the hash\_key that will be used by the `FingerprintCat64` function to combine the crosses fingerprints. |
| `out_type` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) from: `tf.int64, tf.string`. |
| `internal_type` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) from: `tf.int64, tf.string`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (output\_indices, output\_values, output\_shape). | |
| `output_indices` | A `Tensor` of type `int64`. |
| `output_values` | A `Tensor` of type `out_type`. |
| `output_shape` | A `Tensor` of type `int64`. |
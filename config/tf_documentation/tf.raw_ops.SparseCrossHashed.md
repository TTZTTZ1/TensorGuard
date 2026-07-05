# tf.raw_ops.SparseCrossHashed

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseCrossHashed](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseCrossHashed)

---

Generates sparse cross from a list of sparse and dense tensors.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.SparseCrossHashed`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseCrossHashed)

```
tf.raw_ops.SparseCrossHashed(
    indices,
    values,
    shapes,
    dense_inputs,
    num_buckets,
    strong_hash,
    salt,
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
| `num_buckets` | A `Tensor` of type `int64`. It is used if hashed\_output is true. output = hashed\_value%num\_buckets if num\_buckets > 0 else hashed\_value. |
| `strong_hash` | A `Tensor` of type `bool`. boolean, if true, siphash with salt will be used instead of farmhash. |
| `salt` | A `Tensor` of type `int64`. Specify the salt that will be used by the siphash function. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (output\_indices, output\_values, output\_shape). | |
| `output_indices` | A `Tensor` of type `int64`. |
| `output_values` | A `Tensor` of type `int64`. |
| `output_shape` | A `Tensor` of type `int64`. |
# tf.nest.pack_sequence_as

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/nest/pack_sequence_as](https://tensorflow.google.cn/api_docs/python/tf/nest/pack_sequence_as)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/util/nest.py#L423-L539) |

Returns a given flattened sequence packed into a given structure.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.nest.pack_sequence_as`](https://tensorflow.google.cn/api_docs/python/tf/nest/pack_sequence_as)

```
tf.nest.pack_sequence_as(
    structure, flat_sequence, expand_composites=False
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Variational Inference on Probabilistic Graphical Models with Joint Distributions](https://tensorflow.google.cn/probability/examples/Variational_Inference_and_Joint_Distributions) * [Substantial Undocumented Infection Facilitates the Rapid Dissemination of Novel Coronavirus (SARS-CoV2)](https://tensorflow.google.cn/probability/examples/Undocumented_Infection_and_the_Dissemination_of_SARS-CoV2) * [Networks](https://tensorflow.google.cn/agents/tutorials/8_networks_tutorial) * [Random noise generation in TFF](https://tensorflow.google.cn/federated/tutorials/random_noise_generation) * [Bayesian Modeling with Joint Distribution](https://tensorflow.google.cn/probability/examples/Modeling_with_JointDistribution) |

Refer to [tf.nest](https://tensorflow.google.cn/api_docs/python/tf/nest)
for the definition of a structure.

If `structure` is an atom, `flat_sequence` must be a single-item list;
in this case the return value is `flat_sequence[0]`.

If `structure` is or contains a dict instance, the keys will be sorted to
pack the flat sequence in deterministic order. This is true also for
`OrderedDict` instances: their sequence order is ignored, the sorting order of
keys is used instead. The same convention is followed in `flatten`.
This correctly repacks dicts and `OrderedDict`s after they have been
flattened, and also allows flattening an `OrderedDict` and then repacking it
back using a corresponding plain dict, or vice-versa.
Dictionaries with non-sortable keys cannot be flattened.

#### Examples:

1. Python dict:

   ```
   >>> structure = { "key3": "", "key1": "", "key2": "" }
   >>> flat_sequence = ["value1", "value2", "value3"]
   >>> tf.nest.pack_sequence_as(structure, flat_sequence)
     {'key3': 'value3', 'key1': 'value1', 'key2': 'value2'}
   ```
2. For a nested python tuple:

   ```
   >>> structure = (('a','b'), ('c','d','e'), 'f')
   >>> flat_sequence = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
   >>> tf.nest.pack_sequence_as(structure, flat_sequence)
     ((1.0, 2.0), (3.0, 4.0, 5.0), 6.0)
   ```
3. For a nested dictionary of dictionaries:

   ```
   >>> structure = { "key3": {"c": ('alpha', 'beta'), "a": ('gamma')},
   ...               "key1": {"e": "val1", "d": "val2"} }
   >>> flat_sequence = ['val2', 'val1', 3.0, 1.0, 2.0]
   >>> tf.nest.pack_sequence_as(structure, flat_sequence)
     {'key3': {'c': (1.0, 2.0), 'a': 3.0}, 'key1': {'e': 'val1', 'd': 'val2'} }
   ```
4. Numpy array (considered a scalar):

   ```
   >>> structure = ['a']
   >>> flat_sequence = [np.array([[1, 2], [3, 4]])]
   >>> tf.nest.pack_sequence_as(structure, flat_sequence)
     [array([[1, 2],
            [3, 4]])]
   ```
5. tf.Tensor (considered a scalar):

   ```
   >>> structure = ['a']
   >>> flat_sequence = [tf.constant([[1., 2., 3.], [4., 5., 6.]])]
   >>> tf.nest.pack_sequence_as(structure, flat_sequence)
     [<tf.Tensor: shape=(2, 3), dtype=float32,
      numpy= array([[1., 2., 3.], [4., 5., 6.]], dtype=float32)>]
   ```
6. [`tf.RaggedTensor`](https://tensorflow.google.cn/api_docs/python/tf/RaggedTensor): This is a composite tensor thats representation consists
   of a flattened list of 'values' and a list of 'row\_splits' which indicate how
   to chop up the flattened list into different rows. For more details on
   [`tf.RaggedTensor`](https://tensorflow.google.cn/api_docs/python/tf/RaggedTensor), please visit
   https://www.tensorflow.org/api\_docs/python/tf/RaggedTensor.

With `expand_composites=False`, we treat RaggedTensor as a scalar.

```
>>> structure = { "foo": tf.ragged.constant([[1, 2], [3]]),
...               "bar": tf.constant([[5]]) }
>>> flat_sequence = [ "one", "two" ]
>>> tf.nest.pack_sequence_as(structure, flat_sequence,
... expand_composites=False)
  {'foo': 'two', 'bar': 'one'}
```

With `expand_composites=True`, we expect that the flattened input contains
the tensors making up the ragged tensor i.e. the values and row\_splits
tensors.

```
>>> structure = { "foo": tf.ragged.constant([[1., 2.], [3.]]),
...               "bar": tf.constant([[5.]]) }
>>> tensors = tf.nest.flatten(structure, expand_composites=True)
>>> print(tensors)
  [<tf.Tensor: shape=(1, 1), dtype=float32, numpy=array([[5.]],
   dtype=float32)>,
   <tf.Tensor: shape=(3,), dtype=float32, numpy=array([1., 2., 3.],
   dtype=float32)>,
   <tf.Tensor: shape=(3,), dtype=int64, numpy=array([0, 2, 3])>]
>>> verified_tensors = [tf.debugging.check_numerics(t, 'invalid tensor: ')
...                     if t.dtype==tf.float32 else t
...                     for t in tensors]
>>> tf.nest.pack_sequence_as(structure, verified_tensors,
...                          expand_composites=True)
  {'foo': <tf.RaggedTensor [[1.0, 2.0], [3.0]]>,
   'bar': <tf.Tensor: shape=(1, 1), dtype=float32, numpy=array([[5.]],
   dtype=float32)>}
```

| Args | |

|  |  |
| --- | --- |
| `structure` | Nested structure, whose structure is given by nested lists, tuples, and dicts. Note: numpy arrays and strings are considered scalars. |
| `flat_sequence` | flat sequence to pack. |
| `expand_composites` | If true, then composite tensors such as [`tf.sparse.SparseTensor`](https://tensorflow.google.cn/api_docs/python/tf/sparse/SparseTensor) and [`tf.RaggedTensor`](https://tensorflow.google.cn/api_docs/python/tf/RaggedTensor) are expanded into their component tensors. |

| Returns | |

|  |  |
| --- | --- |
| `packed` | `flat_sequence` converted to have the same recursive structure as `structure`. |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If `flat_sequence` and `structure` have different atom counts. |
| `TypeError` | `structure` is or contains a dict with non-sortable keys. |
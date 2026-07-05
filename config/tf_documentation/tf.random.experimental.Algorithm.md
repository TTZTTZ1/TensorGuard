# tf.random.experimental.Algorithm

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/random/experimental/Algorithm](https://tensorflow.google.cn/api_docs/python/tf/random/experimental/Algorithm)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/random_ops_util.py#L30-L55) |

A random-number-generation (RNG) algorithm.

#### View aliases

**Main aliases**

[`tf.random.experimental.Algorithm`](https://tensorflow.google.cn/api_docs/python/tf/random/Algorithm)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.random.Algorithm`](https://tensorflow.google.cn/api_docs/python/tf/random/Algorithm), [`tf.compat.v1.random.experimental.Algorithm`](https://tensorflow.google.cn/api_docs/python/tf/random/Algorithm)

Many random-number generators (e.g. the `alg` argument of
[`tf.random.Generator`](https://tensorflow.google.cn/api_docs/python/tf/random/Generator) and [`tf.random.stateless_uniform`](https://tensorflow.google.cn/api_docs/python/tf/random/stateless_uniform)) in TF allow
you to choose the algorithm used to generate the (pseudo-)random
numbers. You can set the algorithm to be one of the options below.

* `PHILOX`: The Philox algorithm introduced in the paper ["Parallel
  Random Numbers: As Easy as 1, 2,
  3"](https://www.thesalmons.org/john/random123/papers/random123sc11.pdf).
* `THREEFRY`: The ThreeFry algorithm introduced in the paper
  ["Parallel Random Numbers: As Easy as 1, 2,
  3"](https://www.thesalmons.org/john/random123/papers/random123sc11.pdf).
* `AUTO_SELECT`: Allow TF to automatically select the algorithm
  depending on the accelerator device. Note that with this option,
  running the same TF program on different devices may result in
  different random numbers. Also note that TF may select an
  algorithm that is different from `PHILOX` and `THREEFRY`.

| Class Variables | |

|  |  |
| --- | --- |
| AUTO\_SELECT | `<Algorithm.AUTO_SELECT: 3>` |
| PHILOX | `<Algorithm.PHILOX: 1>` |
| THREEFRY | `<Algorithm.THREEFRY: 2>` |
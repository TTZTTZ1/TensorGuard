# tf.random.set_seed

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/random/set_seed](https://tensorflow.google.cn/api_docs/python/tf/random/set_seed)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/random_seed.py#L210-L358) |

Sets the global random seed.

```
tf.random.set_seed(
    seed
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Distributed training with Core APIs and DTensor](https://tensorflow.google.cn/guide/core/distribution) * [Logistic regression for binary classification with Core APIs](https://tensorflow.google.cn/guide/core/logistic_regression_core) * [Multilayer perceptrons for digit recognition with Core APIs](https://tensorflow.google.cn/guide/core/mlp_core) * [Optimizers with Core APIs](https://tensorflow.google.cn/guide/core/optimizers_core) * [Quickstart for the TensorFlow Core APIs](https://tensorflow.google.cn/guide/core/quickstart_core) | * [Generate music with an RNN](https://tensorflow.google.cn/tutorials/audio/music_generation) * [Simple audio recognition: Recognizing keywords](https://tensorflow.google.cn/tutorials/audio/simple_audio) * [Playing CartPole with the Actor-Critic method](https://tensorflow.google.cn/tutorials/reinforcement_learning/actor_critic) * [TensorFlow Probability Case Study: Covariance Estimation](https://tensorflow.google.cn/probability/examples/TensorFlow_Probability_Case_Study_Covariance_Estimation) * [TFP Release Notes notebook (0.11.0)](https://tensorflow.google.cn/probability/examples/TFP_Release_Notebook_0_11_0) |

Operations that rely on a random seed actually derive it from two seeds:
the global and operation-level seeds. This sets the global seed.

Its interactions with operation-level seeds is as follows:

1. If neither the global seed nor the operation seed is set: A randomly
   picked seed is used for this op.
2. If the global seed is set, but the operation seed is not:
   The system deterministically picks an operation seed in conjunction with
   the global seed so that it gets a unique random sequence. Within the
   same version of tensorflow and user code, this sequence is deterministic.
   However across different versions, this sequence might change. If the
   code depends on particular seeds to work, specify both global
   and operation-level seeds explicitly.
3. If the operation seed is set, but the global seed is not set:
   A default global seed and the specified operation seed are used to
   determine the random sequence.
4. If both the global and the operation seed are set:
   Both seeds are used in conjunction to determine the random sequence.

To illustrate the user-visible effects, consider these examples:

If neither the global seed nor the operation seed is set, we get different
results for every call to the random op and every re-run of the program:

```
print(tf.random.uniform([1]))  # generates 'A1'
print(tf.random.uniform([1]))  # generates 'A2'
```

(now close the program and run it again)

```
print(tf.random.uniform([1]))  # generates 'A3'
print(tf.random.uniform([1]))  # generates 'A4'
```

If the global seed is set but the operation seed is not set, we get different
results for every call to the random op, but the same sequence for every
re-run of the program:

```
tf.random.set_seed(1234)
print(tf.random.uniform([1]))  # generates 'A1'
print(tf.random.uniform([1]))  # generates 'A2'
```

(now close the program and run it again)

```
tf.random.set_seed(1234)
print(tf.random.uniform([1]))  # generates 'A1'
print(tf.random.uniform([1]))  # generates 'A2'
```

The reason we get 'A2' instead 'A1' on the second call of [`tf.random.uniform`](https://tensorflow.google.cn/api_docs/python/tf/random/uniform)
above is because the second call uses a different operation seed.

Note that [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function) acts like a re-run of a program in this case. When
the global seed is set but operation seeds are not set, the sequence of random
numbers are the same for each [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function). For example:

```
tf.random.set_seed(1234)

@tf.function
def f():
  a = tf.random.uniform([1])
  b = tf.random.uniform([1])
  return a, b

@tf.function
def g():
  a = tf.random.uniform([1])
  b = tf.random.uniform([1])
  return a, b

print(f())  # prints '(A1, A2)'
print(g())  # prints '(A1, A2)'
```

If the operation seed is set, we get different results for every call to the
random op, but the same sequence for every re-run of the program:

```
print(tf.random.uniform([1], seed=1))  # generates 'A1'
print(tf.random.uniform([1], seed=1))  # generates 'A2'
```

(now close the program and run it again)

```
print(tf.random.uniform([1], seed=1))  # generates 'A1'
print(tf.random.uniform([1], seed=1))  # generates 'A2'
```

The reason we get 'A2' instead 'A1' on the second call of [`tf.random.uniform`](https://tensorflow.google.cn/api_docs/python/tf/random/uniform)
above is because the same [`tf.random.uniform`](https://tensorflow.google.cn/api_docs/python/tf/random/uniform) kernel (i.e. internal
representation) is used by TensorFlow for all calls of it with the same
arguments, and the kernel maintains an internal counter which is incremented
every time it is executed, generating different results.

Calling [`tf.random.set_seed`](https://tensorflow.google.cn/api_docs/python/tf/random/set_seed) will reset any such counters:

```
tf.random.set_seed(1234)
print(tf.random.uniform([1], seed=1))  # generates 'A1'
print(tf.random.uniform([1], seed=1))  # generates 'A2'
tf.random.set_seed(1234)
print(tf.random.uniform([1], seed=1))  # generates 'A1'
print(tf.random.uniform([1], seed=1))  # generates 'A2'
```

When multiple identical random ops are wrapped in a [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function), their
behaviors change because the ops no long share the same counter. For example:

```
@tf.function
def foo():
  a = tf.random.uniform([1], seed=1)
  b = tf.random.uniform([1], seed=1)
  return a, b
print(foo())  # prints '(A1, A1)'
print(foo())  # prints '(A2, A2)'

@tf.function
def bar():
  a = tf.random.uniform([1])
  b = tf.random.uniform([1])
  return a, b
print(bar())  # prints '(A1, A2)'
print(bar())  # prints '(A3, A4)'
```

The second call of `foo` returns '(A2, A2)' instead of '(A1, A1)' because
[`tf.random.uniform`](https://tensorflow.google.cn/api_docs/python/tf/random/uniform) maintains an internal counter. If you want `foo` to return
'(A1, A1)' every time, use the stateless random ops such as
[`tf.random.stateless_uniform`](https://tensorflow.google.cn/api_docs/python/tf/random/stateless_uniform). Also see [`tf.random.experimental.Generator`](https://tensorflow.google.cn/api_docs/python/tf/random/Generator) for
a new set of stateful random ops that use external variables to manage their
states.

| Args | |

|  |  |
| --- | --- |
| `seed` | integer. |
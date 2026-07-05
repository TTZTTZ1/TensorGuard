# tf.keras.datasets.boston_housing.load_data

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/datasets/boston_housing/load_data](https://tensorflow.google.cn/api_docs/python/tf/keras/datasets/boston_housing/load_data)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/datasets/boston_housing.py#L7-L70) |

Loads the Boston Housing dataset.

```
tf.keras.datasets.boston_housing.load_data(
    path='boston_housing.npz', test_split=0.2, seed=113
)
```

This is a dataset taken from the StatLib library which is maintained at
Carnegie Mellon University.

**Warning:** This dataset has an ethical problem: the authors of this
dataset included a variable, "B", that may appear to assume that racial
self-segregation influences house prices. As such, we strongly discourage
the use of this dataset, unless in the context of illustrating ethical
issues in data science and machine learning.

Samples contain 13 attributes of houses at different locations around the
Boston suburbs in the late 1970s. Targets are the median values of
the houses at a location (in k$).

The attributes themselves are defined in the
[StatLib website](http://lib.stat.cmu.edu/datasets/boston).

| Args | |

|  |  |
| --- | --- |
| `path` | path where to cache the dataset locally (relative to `~/.keras/datasets`). |
| `test_split` | fraction of the data to reserve as test set. |
| `seed` | Random seed for shuffling the data before computing the test split. |

| Returns | |
| Tuple of NumPy arrays: `(x_train, y_train), (x_test, y_test)`. | |

**x\_train, x\_test**: NumPy arrays with shape `(num_samples, 13)`
containing either the training samples (for x\_train),
or test samples (for y\_train).

**y\_train, y\_test**: NumPy arrays of shape `(num_samples,)` containing the
target scalars. The targets are float scalars typically between 10 and
50 that represent the home prices in k$.
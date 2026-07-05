# tf.keras.utils.set_random_seed

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/utils/set_random_seed](https://tensorflow.google.cn/api_docs/python/tf/keras/utils/set_random_seed)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/utils/rng_utils.py#L10-L56) |

Sets all random seeds (Python, NumPy, and backend framework, e.g. TF).

```
tf.keras.utils.set_random_seed(
    seed
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Use TF1.x models in TF2 workflows](https://tensorflow.google.cn/guide/migrate/model_mapping) | * [Using DTensors with Keras](https://tensorflow.google.cn/tutorials/distribute/dtensor_keras_tutorial) |

You can use this utility to make almost any Keras program fully
deterministic. Some limitations apply in cases where network communications
are involved (e.g. parameter server distribution), which creates additional
sources of randomness, or when certain non-deterministic cuDNN ops are
involved.

Calling this utility is equivalent to the following:

```
import random
random.seed(seed)

import numpy as np
np.random.seed(seed)

import tensorflow as tf  # Only if TF is installed
tf.random.set_seed(seed)

import torch  # Only if the backend is 'torch'
torch.manual_seed(seed)
```

Note that the TensorFlow seed is set even if you're not using TensorFlow
as your backend framework, since many workflows leverage [`tf.data`](https://tensorflow.google.cn/api_docs/python/tf/data)
pipelines (which feature random shuffling). Likewise many workflows
might leverage NumPy APIs.

| Arguments | |

|  |  |
| --- | --- |
| `seed` | Integer, the random seed to use. |
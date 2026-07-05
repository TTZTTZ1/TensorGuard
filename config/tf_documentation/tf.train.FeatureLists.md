# tf.train.FeatureLists

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/train/FeatureLists](https://tensorflow.google.cn/api_docs/python/tf/train/FeatureLists)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/core/example/feature.proto) |

Mainly used as part of a [`tf.train.SequenceExample`](https://tensorflow.google.cn/api_docs/python/tf/train/SequenceExample).

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.train.FeatureLists`](https://tensorflow.google.cn/api_docs/python/tf/train/FeatureLists)

Contains a list of [`tf.train.Feature`](https://tensorflow.google.cn/api_docs/python/tf/train/Feature)s.

The [`tf.train.SequenceExample`](https://tensorflow.google.cn/api_docs/python/tf/train/SequenceExample) proto can be thought of as a
proto implementation of the following python type:

```
# tf.train.Feature
Feature = Union[List[bytes],
                List[int64],
                List[float]]

# tf.train.FeatureList
FeatureList = List[Feature]

# tf.train.FeatureLists
FeatureLists = Dict[str, FeatureList]

class SequenceExample(typing.NamedTuple):
  context: Dict[str, Feature]
  feature_lists: FeatureLists
```

This proto implements the `Dict[str, FeatureList]` portion.

| Attributes | |

|  |  |
| --- | --- |
| `feature_list` | `repeated FeatureListEntry feature_list` |

## Child Classes

[`class FeatureListEntry`](https://tensorflow.google.cn/api_docs/python/tf/train/FeatureLists/FeatureListEntry)
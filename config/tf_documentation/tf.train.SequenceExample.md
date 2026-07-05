# tf.train.SequenceExample

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/train/SequenceExample](https://tensorflow.google.cn/api_docs/python/tf/train/SequenceExample)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/core/example/example.proto) |

A `SequenceExample` represents a sequence of features and some context.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.train.SequenceExample`](https://tensorflow.google.cn/api_docs/python/tf/train/SequenceExample)

It can be thought of as a proto-implementation of the following python type:

```
Feature = Union[List[bytes],
                List[int64],
                List[float]]

class SequenceExample(typing.NamedTuple):
  context: Dict[str, Feature]
  feature_lists: Dict[str, List[Feature]]
```

To implement this as protos it's broken up into sub-messages as follows:

```
# tf.train.Feature
Feature = Union[List[bytes],
                List[int64],
                List[float]]

# tf.train.FeatureList
FeatureList = List[Feature]

# tf.train.FeatureLists
FeatureLists = Dict[str, FeatureList]

# tf.train.SequenceExample
class SequenceExample(typing.NamedTuple):
  context: Dict[str, Feature]
  feature_lists: FeatureLists
```

To parse a `SequenceExample` in TensorFlow refer to the
[`tf.io.parse_sequence_example`](https://tensorflow.google.cn/api_docs/python/tf/io/parse_sequence_example) function.

The `context` contains features which apply to the entire
example. The `feature_lists` contain a key, value map where each key is
associated with a repeated set of [`tf.train.Features`](https://tensorflow.google.cn/api_docs/python/tf/train/Features) (a [`tf.train.FeatureList`](https://tensorflow.google.cn/api_docs/python/tf/train/FeatureList)).
A `FeatureList` represents the values of a feature identified by its key
over time / frames.

Below is a `SequenceExample` for a movie recommendation application recording a
sequence of ratings by a user. The time-independent features ("locale",
"age", "favorites") describing the user are part of the context. The sequence
of movies the user rated are part of the feature\_lists. For each movie in the
sequence we have information on its name and actors and the user's rating.
This information is recorded in three separate `feature_list`s.
In the example below there are only two movies. All three `feature_list`s,
namely "movie\_ratings", "movie\_names", and "actors" have a feature value for
both movies. Note, that "actors" is itself a `bytes_list` with multiple
strings per movie.

```
  context: {
    feature: {
      key  : "locale"
      value: {
        bytes_list: {
          value: [ "pt_BR" ]
        }
      }
    }
    feature: {
      key  : "age"
      value: {
        float_list: {
          value: [ 19.0 ]
        }
      }
    }
    feature: {
      key  : "favorites"
      value: {
        bytes_list: {
          value: [ "Majesty Rose", "Savannah Outen", "One Direction" ]
        }
      }
    }
  }
  feature_lists: {
    feature_list: {
      key  : "movie_ratings"
      value: {
        feature: {
          float_list: {
            value: [ 4.5 ]
          }
        }
        feature: {
          float_list: {
            value: [ 5.0 ]
          }
        }
      }
    }
    feature_list: {
      key  : "movie_names"
      value: {
        feature: {
          bytes_list: {
            value: [ "The Shawshank Redemption" ]
          }
        }
        feature: {
          bytes_list: {
            value: [ "Fight Club" ]
          }
        }
      }
    }
    feature_list: {
      key  : "actors"
      value: {
        feature: {
          bytes_list: {
            value: [ "Tim Robbins", "Morgan Freeman" ]
          }
        }
        feature: {
          bytes_list: {
            value: [ "Brad Pitt", "Edward Norton", "Helena Bonham Carter" ]
          }
        }
      }
    }
  }
```

A conformant `SequenceExample` data set obeys the following conventions:

`context`:

* All conformant context features `K` must obey the same conventions as
  a conformant Example's features (see above).

`feature_lists`:

* A `FeatureList L` may be missing in an example; it is up to the
  parser configuration to determine if this is allowed or considered
  an empty list (zero length).
* If a `FeatureList L` exists, it may be empty (zero length).
* If a `FeatureList L` is non-empty, all features within the `FeatureList`
  must have the same data type `T`. Even across `SequenceExample`s, the type `T`
  of the `FeatureList` identified by the same key must be the same. An entry
  without any values may serve as an empty feature.
* If a `FeatureList L` is non-empty, it is up to the parser configuration
  to determine if all features within the `FeatureList` must
  have the same size. The same holds for this `FeatureList` across multiple
  examples.
* For sequence modeling ([example](https://github.com/tensorflow/nmt)), the
  feature lists represent a sequence of frames. In this scenario, all
  `FeatureList`s in a `SequenceExample` have the same number of `Feature`
  messages, so that the i-th element in each `FeatureList` is part of the
  i-th frame (or time step).

**Examples of conformant and non-conformant examples' `FeatureLists`:**

Conformant `FeatureLists`:

```
    feature_lists: { feature_list: {
      key: "movie_ratings"
      value: { feature: { float_list: { value: [ 4.5 ] } }
               feature: { float_list: { value: [ 5.0 ] } } }
    } }
```

Non-conformant `FeatureLists` (mismatched types):

```
    feature_lists: { feature_list: {
      key: "movie_ratings"
      value: { feature: { float_list: { value: [ 4.5 ] } }
               feature: { int64_list: { value: [ 5 ] } } }
    } }
```

Conditionally conformant `FeatureLists`, the parser configuration determines
if the feature sizes must match:

```
    feature_lists: { feature_list: {
      key: "movie_ratings"
      value: { feature: { float_list: { value: [ 4.5 ] } }
               feature: { float_list: { value: [ 5.0, 6.0 ] } } }
    } }
```

**Examples of conformant and non-conformant `SequenceExample`s:**

Conformant pair of SequenceExample:

```
    feature_lists: { feature_list: {
      key: "movie_ratings"
      value: { feature: { float_list: { value: [ 4.5 ] } }
               feature: { float_list: { value: [ 5.0 ] } } }
     } }

    feature_lists: { feature_list: {
      key: "movie_ratings"
      value: { feature: { float_list: { value: [ 4.5 ] } }
               feature: { float_list: { value: [ 5.0 ] } }
               feature: { float_list: { value: [ 2.0 ] } } }
     } }
```

Conformant pair of `SequenceExample`s:

```
    feature_lists: { feature_list: {
      key: "movie_ratings"
      value: { feature: { float_list: { value: [ 4.5 ] } }
               feature: { float_list: { value: [ 5.0 ] } } }
     } }

    feature_lists: { feature_list: {
      key: "movie_ratings"
      value: { }
     } }
```

Conditionally conformant pair of `SequenceExample`s, the parser configuration
determines if the second `feature_lists` is consistent (zero-length) or
invalid (missing "movie\_ratings"):

```
    feature_lists: { feature_list: {
      key: "movie_ratings"
      value: { feature: { float_list: { value: [ 4.5 ] } }
               feature: { float_list: { value: [ 5.0 ] } } }
     } }

   feature_lists: { }
```

Non-conformant pair of `SequenceExample`s (mismatched types):

```
    feature_lists: { feature_list: {
      key: "movie_ratings"
      value: { feature: { float_list: { value: [ 4.5 ] } }
               feature: { float_list: { value: [ 5.0 ] } } }
     } }

    feature_lists: { feature_list: {
      key: "movie_ratings"
      value: { feature: { int64_list: { value: [ 4 ] } }
               feature: { int64_list: { value: [ 5 ] } }
               feature: { int64_list: { value: [ 2 ] } } }
     } }
```

Conditionally conformant pair of `SequenceExample`s; the parser configuration
determines if the feature sizes must match:

```
    feature_lists: { feature_list: {
      key: "movie_ratings"
      value: { feature: { float_list: { value: [ 4.5 ] } }
               feature: { float_list: { value: [ 5.0 ] } } }
    } }

    feature_lists: { feature_list: {
      key: "movie_ratings"
      value: { feature: { float_list: { value: [ 4.0 ] } }
              feature: { float_list: { value: [ 5.0, 3.0 ] } }
    } }
```

| Attributes | |

|  |  |
| --- | --- |
| `context` | `Features context` |
| `feature_lists` | `FeatureLists feature_lists` |
# tf.data.experimental.AutoShardPolicy

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/data/experimental/AutoShardPolicy](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/AutoShardPolicy)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/ops/options.py#L88-L152) |

Represents the type of auto-sharding to use.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.data.experimental.AutoShardPolicy`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/AutoShardPolicy)

OFF: No sharding will be performed.

AUTO: Attempts FILE-based sharding, falling back to DATA-based sharding.

FILE: Shards by input files (i.e. each worker will get a set of files to
process). When this option is selected, make sure that there is at least as
many files as workers. If there are fewer input files than workers, a runtime
error will be raised.

DATA: Shards by elements produced by the dataset. Each worker will process the
whole dataset and discard the portion that is not for itself. Note that for
this mode to correctly partitions the dataset elements, the dataset needs to
produce elements in a deterministic order.

HINT: Looks for the presence of `shard(SHARD_HINT, ...)` which is treated as a
placeholder to replace with `shard(num_workers, worker_index)`.

| Class Variables | |

|  |  |
| --- | --- |
| AUTO | `<AutoShardPolicy.AUTO: 0>` |
| DATA | `<AutoShardPolicy.DATA: 2>` |
| FILE | `<AutoShardPolicy.FILE: 1>` |
| HINT | `<AutoShardPolicy.HINT: 3>` |
| OFF | `<AutoShardPolicy.OFF: -1>` |
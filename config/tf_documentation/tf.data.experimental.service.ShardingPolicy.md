# tf.data.experimental.service.ShardingPolicy

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/data/experimental/service/ShardingPolicy](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/service/ShardingPolicy)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/experimental/ops/data_service_ops.py#L47-L115) |

Specifies how to shard data among tf.data service workers.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.data.experimental.service.ShardingPolicy`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/service/ShardingPolicy)

OFF: No sharding will be performed. Each worker produces the entire dataset
without any sharding. With this mode, the best practice is to shuffle the
dataset nondeterministically so that workers process the dataset in different
orders. If workers are restarted or join the cluster mid-job, they will begin
processing the dataset from the beginning.

DYNAMIC: The input dataset is dynamically split among workers at runtime. Each
worker gets the next split when it reads data from the dispatcher. Data is
produced non-deterministically in this mode. Dynamic sharding works well with
varying-sized tf.data service clusters, e.g., when you need to auto-scale your
workers. Dynamic sharding provides at-most once visitation guarantees. No
examples will be repeated, but some may be missed if a tf.data service worker
gets restarted while processing a file.

The following are static sharding policies. The semantics are similar to
[`tf.data.experimental.AutoShardPolicy`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/AutoShardPolicy). These policies require:

* The tf.data service cluster is configured with a fixed list of workers
  in DispatcherConfig.
* Each client only reads from the local tf.data service worker.

If a worker is restarted while performing static sharding, the worker will
begin processing its shard again from the beginning.

FILE: Shards by input files (i.e. each worker will get a fixed set of files to
process). When this option is selected, make sure that there is at least as
many files as workers. If there are fewer input files than workers, a runtime
error will be raised.

DATA: Shards by elements produced by the dataset. Each worker will process the
whole dataset and discard the portion that is not for itself. Note that for
this mode to correctly partition the dataset elements, the dataset needs to
produce elements in a deterministic order.

FILE\_OR\_DATA: Attempts FILE-based sharding, falling back to DATA-based
sharding on failure.

HINT: Looks for the presence of `shard(SHARD_HINT, ...)` which is treated as a
placeholder to replace with `shard(num_workers, worker_index)`.

| Class Variables | |

|  |  |
| --- | --- |
| DATA | `<ShardingPolicy.DATA: 3>` |
| DYNAMIC | `<ShardingPolicy.DYNAMIC: 1>` |
| FILE | `<ShardingPolicy.FILE: 2>` |
| FILE\_OR\_DATA | `<ShardingPolicy.FILE_OR_DATA: 4>` |
| HINT | `<ShardingPolicy.HINT: 5>` |
| OFF | `<ShardingPolicy.OFF: 0>` |
# tf.train.ServerDef

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/train/ServerDef](https://tensorflow.google.cn/api_docs/python/tf/train/ServerDef)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/core/protobuf/tensorflow_server.proto) |

A ProtocolMessage

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.train.ServerDef`](https://tensorflow.google.cn/api_docs/python/tf/train/ServerDef)

| Attributes | |

|  |  |
| --- | --- |
| `cluster` | `ClusterDef cluster` |
| `cluster_device_filters` | `ClusterDeviceFilters cluster_device_filters` |
| `default_session_config` | `ConfigProto default_session_config` |
| `job_name` | `string job_name` |
| `port` | `int32 port` |
| `protocol` | `string protocol` |
| `replica` | `int32 replica` |
| `task_index` | `int32 task_index` |
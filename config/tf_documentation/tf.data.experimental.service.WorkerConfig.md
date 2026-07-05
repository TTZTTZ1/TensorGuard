# tf.data.experimental.service.WorkerConfig

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/data/experimental/service/WorkerConfig](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/service/WorkerConfig)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/experimental/service/server_lib.py#L292-L345) |

Configuration class for tf.data service dispatchers.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.data.experimental.service.WorkerConfig`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/service/WorkerConfig)

```
tf.data.experimental.service.WorkerConfig(
    dispatcher_address,
    worker_address=None,
    port=0,
    protocol=None,
    heartbeat_interval_ms=None,
    dispatcher_timeout_ms=None,
    data_transfer_protocol=None,
    data_transfer_address=None
)
```

| Fields | |

|  |  |
| --- | --- |
| `dispatcher_address` | Specifies the address of the dispatcher. |
| `worker_address` | Specifies the address of the worker server. This address is passed to the dispatcher so that the dispatcher can tell clients how to connect to this worker. |
| `port` | Specifies the port to bind to. A value of 0 indicates that the worker can bind to any available port. |
| `protocol` | A string indicating the protocol to be used by the worker to connect to the dispatcher. E.g. "grpc". |
| `heartbeat_interval_ms` | How often the worker should heartbeat to the dispatcher, in milliseconds. If not set, the runtime will select a reasonable default. A higher value will reduce the load on the dispatcher, while a lower value will reduce the time it takes to reclaim resources from finished jobs. |
| `dispatcher_timeout_ms` | How long, in milliseconds, to retry requests to the dispatcher before giving up and reporting an error. Defaults to 1 hour. |
| `data_transfer_protocol` | A string indicating the protocol to be used by the worker to transfer data to the client. E.g. "grpc". |
| `data_transfer_address` | A string indicating the data transfer address of the worker server. |

| Attributes | |

|  |  |
| --- | --- |
| `dispatcher_address` | A `namedtuple` alias for field number 0 |
| `worker_address` | A `namedtuple` alias for field number 1 |
| `port` | A `namedtuple` alias for field number 2 |
| `protocol` | A `namedtuple` alias for field number 3 |
| `heartbeat_interval_ms` | A `namedtuple` alias for field number 4 |
| `dispatcher_timeout_ms` | A `namedtuple` alias for field number 5 |
| `data_transfer_protocol` | A `namedtuple` alias for field number 6 |
| `data_transfer_address` | A `namedtuple` alias for field number 7 |
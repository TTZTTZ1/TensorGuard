# tf.data.experimental.service.DispatchServer

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/data/experimental/service/DispatchServer](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/service/DispatchServer)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/experimental/service/server_lib.py#L130-L289) |

An in-process tf.data service dispatch server.

```
tf.data.experimental.service.DispatchServer(
    config=None, start=True
)
```

A [`tf.data.experimental.service.DispatchServer`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/service/DispatchServer) coordinates a cluster of
[`tf.data.experimental.service.WorkerServer`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/service/WorkerServer)s. When the workers start, they
register themselves with the dispatcher.

```
>>> dispatcher = tf.data.experimental.service.DispatchServer()
>>> dispatcher_address = dispatcher.target.split("://")[1]
>>> worker = tf.data.experimental.service.WorkerServer(
...     tf.data.experimental.service.WorkerConfig(
...     dispatcher_address=dispatcher_address))
>>> dataset = tf.data.Dataset.range(10)
>>> dataset = dataset.apply(tf.data.experimental.service.distribute(
...     processing_mode="parallel_epochs", service=dispatcher.target))
>>> print(list(dataset.as_numpy_iterator()))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

When starting a dedicated tf.data dispatch process, use join() to block
after starting up the server, until the server terminates.

```
dispatcher = tf.data.experimental.service.DispatchServer(
    tf.data.experimental.service.DispatcherConfig(port=5050))
dispatcher.join()
```

Call stop() to gracefully terminate the dispatcher. The server automatically
stops when all reference to it have been deleted.

To start a `DispatchServer` in fault-tolerant mode, set `work_dir` and
`fault_tolerant_mode` like below:

```
dispatcher = tf.data.experimental.service.DispatchServer(
    tf.data.experimental.service.DispatcherConfig(
        port=5050,
        work_dir="gs://my-bucket/dispatcher/work_dir",
        fault_tolerant_mode=True))
```

| Args | |

|  |  |
| --- | --- |
| `config` | (Optional.) A [`tf.data.experimental.service.DispatcherConfig`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/service/DispatcherConfig) configration. If `None`, the dispatcher will use default configuration values. |
| `start` | (Optional.) Boolean, indicating whether to start the server after creating it. Defaults to True. |

| Attributes | |

|  |  |
| --- | --- |
| `target` | Returns a target that can be used to connect to the server. |

```
>>> dispatcher = tf.data.experimental.service.DispatchServer()
>>> dataset = tf.data.Dataset.range(10)
>>> dataset = dataset.apply(tf.data.experimental.service.distribute(
...     processing_mode="parallel_epochs", service=dispatcher.target))
```

The returned string will be in the form protocol://address, e.g.
"grpc://localhost:5050".

## Methods

### `join`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/experimental/service/server_lib.py#L221-L236)

```
join() -> None
```

Blocks until the server has shut down.

This is useful when starting a dedicated dispatch process.

```
dispatcher = tf.data.experimental.service.DispatchServer(
    tf.data.experimental.service.DispatcherConfig(port=5050))
dispatcher.join()
```

| Raises | |

|  |  |
| --- | --- |
| [`tf.errors.OpError`](https://tensorflow.google.cn/api_docs/python/tf/errors/OpError) | Or one of its subclasses if an error occurs while joining the server. |

### `start`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/experimental/service/server_lib.py#L209-L219)

```
start()
```

Starts this server.

```
>>> dispatcher = tf.data.experimental.service.DispatchServer(start=False)
>>> dispatcher.start()
```

| Raises | |

|  |  |
| --- | --- |
| [`tf.errors.OpError`](https://tensorflow.google.cn/api_docs/python/tf/errors/OpError) | Or one of its subclasses if an error occurs while starting the server. |

### `stop`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/experimental/service/server_lib.py#L238-L245)

```
stop() -> None
```

Stops the server.

| Raises | |

|  |  |
| --- | --- |
| [`tf.errors.OpError`](https://tensorflow.google.cn/api_docs/python/tf/errors/OpError) | Or one of its subclasses if an error occurs while stopping the server. |
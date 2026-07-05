# tf.data.experimental.service.WorkerServer

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/data/experimental/service/WorkerServer](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/service/WorkerServer)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/experimental/service/server_lib.py#L348-L478) |

An in-process tf.data service worker server.

```
tf.data.experimental.service.WorkerServer(
    config, start=True
)
```

A [`tf.data.experimental.service.WorkerServer`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/service/WorkerServer) performs [`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset)
processing for user-defined datasets, and provides the resulting elements over
RPC. A worker is associated with a single
[`tf.data.experimental.service.DispatchServer`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/service/DispatchServer).

```
>>> dispatcher = tf.data.experimental.service.DispatchServer()
>>> dispatcher_address = dispatcher.target.split("://")[1]
>>> worker = tf.data.experimental.service.WorkerServer(
...     tf.data.experimental.service.WorkerConfig(
...         dispatcher_address=dispatcher_address))
>>> dataset = tf.data.Dataset.range(10)
>>> dataset = dataset.apply(tf.data.experimental.service.distribute(
...     processing_mode="parallel_epochs", service=dispatcher.target))
>>> print(list(dataset.as_numpy_iterator()))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

When starting a dedicated tf.data worker process, use join() to block
after starting up the worker, until the worker terminates.

```
worker = tf.data.experimental.service.WorkerServer(
    port=5051, dispatcher_address="localhost:5050")
worker.join()
```

Call stop() to gracefully terminate the worker. The worker automatically stops
when all reference to it have been deleted.

| Args | |

|  |  |
| --- | --- |
| `config` | A [`tf.data.experimental.service.WorkerConfig`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/service/WorkerConfig) configration. |
| `start` | (Optional.) Boolean, indicating whether to start the server after creating it. Defaults to True. |

## Methods

### `join`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/experimental/service/server_lib.py#L419-L436)

```
join() -> None
```

Blocks until the server has shut down.

This is useful when starting a dedicated worker process.

```
worker_server = tf.data.experimental.service.WorkerServer(
    port=5051, dispatcher_address="localhost:5050")
worker_server.join()
```

This method currently blocks forever.

| Raises | |

|  |  |
| --- | --- |
| [`tf.errors.OpError`](https://tensorflow.google.cn/api_docs/python/tf/errors/OpError) | Or one of its subclasses if an error occurs while joining the server. |

### `start`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/experimental/service/server_lib.py#L410-L417)

```
start() -> None
```

Starts this server.

| Raises | |

|  |  |
| --- | --- |
| [`tf.errors.OpError`](https://tensorflow.google.cn/api_docs/python/tf/errors/OpError) | Or one of its subclasses if an error occurs while starting the server. |

### `stop`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/experimental/service/server_lib.py#L438-L445)

```
stop() -> None
```

Stops the server.

| Raises | |

|  |  |
| --- | --- |
| [`tf.errors.OpError`](https://tensorflow.google.cn/api_docs/python/tf/errors/OpError) | Or one of its subclasses if an error occurs while stopping the server. |
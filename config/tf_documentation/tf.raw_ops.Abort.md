# tf.raw_ops.Abort

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Abort](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Abort)

---

Raise a exception to abort the process when called.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.Abort`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Abort)

```
tf.raw_ops.Abort(
    error_msg='', exit_without_error=False, name=None
)
```

If exit\_without\_error is true, the process will exit normally,
otherwise it will exit with a SIGABORT signal.

Returns nothing but an exception.

| Args | |

|  |  |
| --- | --- |
| `error_msg` | An optional `string`. Defaults to `""`. A string which is the message associated with the exception. |
| `exit_without_error` | An optional `bool`. Defaults to `False`. |
| `name` | A name for the operation (optional). |

| Returns | |
| The created Operation. | |
# tf.autograph.set_verbosity

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/autograph/set_verbosity](https://tensorflow.google.cn/api_docs/python/tf/autograph/set_verbosity)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/autograph/utils/ag_logging.py#L36-L84) |

Sets the AutoGraph verbosity level.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.autograph.set_verbosity`](https://tensorflow.google.cn/api_docs/python/tf/autograph/set_verbosity)

```
tf.autograph.set_verbosity(
    level, alsologtostdout=False
)
```

*Debug logging in AutoGraph*

More verbose logging is useful to enable when filing bug reports or doing
more in-depth debugging.

There are two means to control the logging verbosity:

* The `set_verbosity` function
* The `AUTOGRAPH_VERBOSITY` environment variable

`set_verbosity` takes precedence over the environment variable.

#### For example:

```
import os
import tensorflow as tf

os.environ['AUTOGRAPH_VERBOSITY'] = '5'
# Verbosity is now 5

tf.autograph.set_verbosity(0)
# Verbosity is now 0

os.environ['AUTOGRAPH_VERBOSITY'] = '1'
# No effect, because set_verbosity was already called.
```

Logs entries are output to [absl](https://abseil.io)'s
[default output](https://abseil.io/docs/python/guides/logging),
with `INFO` level.
Logs can be mirrored to stdout by using the `alsologtostdout` argument.
Mirroring is enabled by default when Python runs in interactive mode.

| Args | |

|  |  |
| --- | --- |
| `level` | int, the verbosity level; larger values specify increased verbosity; 0 means no logging. When reporting bugs, it is recommended to set this value to a larger number, like 10. |
| `alsologtostdout` | bool, whether to also output log messages to `sys.stdout`. |
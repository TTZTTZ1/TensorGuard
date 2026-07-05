# tf.saved_model.experimental.TrackableResource

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/saved_model/experimental/TrackableResource](https://tensorflow.google.cn/api_docs/python/tf/saved_model/experimental/TrackableResource)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/trackable/resource.py#L233-L286) |

Holds a Tensor which a tf.function can capture.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.saved_model.experimental.TrackableResource`](https://tensorflow.google.cn/api_docs/python/tf/saved_model/experimental/TrackableResource)

```
tf.saved_model.experimental.TrackableResource(
    device=''
)
```

A TrackableResource is most useful for stateful Tensors that require
initialization, such as [`tf.lookup.StaticHashTable`](https://tensorflow.google.cn/api_docs/python/tf/lookup/StaticHashTable). `TrackableResource`s
are discovered by traversing the graph of object attributes, e.g. during
[`tf.saved_model.save`](https://tensorflow.google.cn/api_docs/python/tf/saved_model/save).

A TrackableResource has three methods to override:

* `_create_resource` should create the resource tensor handle.
* `_initialize` should initialize the resource held at `self.resource_handle`.
* `_destroy_resource` is called upon a `TrackableResource`'s destruction
  and should decrement the resource's ref count. For most resources, this
  should be done with a call to [`tf.raw_ops.DestroyResourceOp`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DestroyResourceOp).

#### Example usage:

```
>>> class DemoResource(tf.saved_model.experimental.TrackableResource):
...   def __init__(self):
...     super().__init__()
...     self._initialize()
...   def _create_resource(self):
...     return tf.raw_ops.VarHandleOp(dtype=tf.float32, shape=[2])
...   def _initialize(self):
...     tf.raw_ops.AssignVariableOp(
...         resource=self.resource_handle, value=tf.ones([2]))
...   def _destroy_resource(self):
...     tf.raw_ops.DestroyResourceOp(resource=self.resource_handle)
>>> class DemoModule(tf.Module):
...   def __init__(self):
...     self.resource = DemoResource()
...   def increment(self, tensor):
...     return tensor + tf.raw_ops.ReadVariableOp(
...         resource=self.resource.resource_handle, dtype=tf.float32)
>>> demo = DemoModule()
>>> demo.increment([5, 1])
<tf.Tensor: shape=(2,), dtype=float32, numpy=array([6., 2.], dtype=float32)>
```

| Args | |

|  |  |
| --- | --- |
| `device` | A string indicating a required placement for this resource, e.g. "CPU" if this resource must be created on a CPU device. A blank device allows the user to place resource creation, so generally this should be blank unless the resource only makes sense on one device. |

| Attributes | |

|  |  |
| --- | --- |
| `resource_handle` | Returns the resource handle associated with this Resource. |
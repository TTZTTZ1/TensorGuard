# tf.keras.mixed_precision.set_global_policy

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/mixed_precision/set_global_policy](https://tensorflow.google.cn/api_docs/python/tf/keras/mixed_precision/set_global_policy)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/dtype_policies/dtype_policy.py#L302-L330) |

Sets the default dtype policy globally.

#### View aliases

**Main aliases**

[`tf.keras.mixed_precision.set_dtype_policy`](https://tensorflow.google.cn/api_docs/python/tf/keras/config/set_dtype_policy), [`tf.keras.mixed_precision.set_global_policy`](https://tensorflow.google.cn/api_docs/python/tf/keras/config/set_dtype_policy)

```
tf.keras.config.set_dtype_policy(
    policy
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Mixed precision](https://tensorflow.google.cn/guide/mixed_precision) | * [Image classification with Model Garden](https://tensorflow.google.cn/tfmodels/vision/image_classification) * [Instance Segmentation with Model Garden](https://tensorflow.google.cn/tfmodels/vision/instance_segmentation) * [Object detection with Model Garden](https://tensorflow.google.cn/tfmodels/vision/object_detection) * [Semantic Segmentation with Model Garden](https://tensorflow.google.cn/tfmodels/vision/semantic_segmentation) |

#### Example:

```
>>> keras.config.set_dtype_policy("mixed_float16")
```
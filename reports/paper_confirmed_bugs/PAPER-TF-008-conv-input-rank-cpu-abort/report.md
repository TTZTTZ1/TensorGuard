# PAPER-TF-008: Convolution Rank Mismatch CPU Abort

## Summary

The appendix reports a CPU/GPU inconsistency for convolution APIs with invalid input rank. GPU returns `InvalidArgumentError`; CPU aborts through a fatal check.

## Expected Behavior

CPU and GPU should consistently reject the invalid rank with a framework-level exception.

## Observed Behavior

```text
GPU: tensorflow.python.framework.errors_impl.InvalidArgumentError: convolution input must be 4-dimensional: [10] [Op:Conv2D]
CPU: Check failed: index >= 0 && index < num_total_dims Invalid index from the dimension: 3, 0, C
*** Check failure stack trace: ***
Aborted
```

## Minimal Reproduction

```python
import tensorflow as tf

value = tf.zeros([10], dtype=tf.float32)
filters = tf.zeros([5, 5, 1, 8], dtype=tf.float32)
tf.nn.atrous_conv2d(value, filters, rate=1, padding="VALID")
```

## Related APIs Mentioned In Appendix

`tf.nn.conv2d`, `tf.nn.conv3d`, `tf.nn.depthwise_conv2d`, `tf.nn.depthwise_conv2d_backprop_filter`, `tf.raw_ops.Conv2D`, `tf.raw_ops.Conv3D`, `tf.raw_ops.DepthwiseConv2dNative`, `tf.raw_ops.Conv2DBackpropFilter`, `tf.raw_ops.Conv3DBackpropFilterV2`.

## Source

`基于大语言模型的深度学习库模糊测试.pdf`, appendix "缺陷触发代码示例".

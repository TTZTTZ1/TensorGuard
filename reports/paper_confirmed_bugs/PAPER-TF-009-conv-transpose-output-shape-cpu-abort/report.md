# PAPER-TF-009: Conv Transpose Output Shape CPU Abort

## Summary

The appendix reports a CPU/GPU inconsistency for transposed convolution APIs with malformed `output_shape`.

## Expected Behavior

CPU and GPU should consistently reject the malformed `output_shape` with a framework-level exception.

## Observed Behavior

```text
GPU: tensorflow.python.framework.errors_impl.InvalidArgumentError: Conv2DBackpropInput requires input_sizes to contain 4 values or 2 values, but got: 3 [Op:Conv2DBackpropInput]
CPU: Check failed: index >= 0 && index < num_total_dims Invalid index from the dimension: 3, 0, C
*** Check failure stack trace: ***
Aborted
```

## Minimal Reproduction

```python
import tensorflow as tf

x = tf.random.normal([1, 4, 4, 3])
f = tf.random.normal([3, 3, 3, 3])
tf.nn.conv2d_transpose(
    x,
    f,
    output_shape=(2, 4, 2),
    strides=[1, 2, 2, 1],
    padding="SAME",
)
```

## Related APIs Mentioned In Appendix

`tf.nn.conv1d_transpose`, `tf.nn.conv3d_transpose`, `tf.nn.depthwise_conv2d_backprop_input`, `tf.raw_ops.Conv2DBackpropInput`, `tf.raw_ops.Conv3DBackpropInputV2`, `tf.raw_ops.DepthwiseConv2dNativeBackpropInput`.

## Source

`基于大语言模型的深度学习库模糊测试.pdf`, appendix "缺陷触发代码示例".

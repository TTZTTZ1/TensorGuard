# PAPER-TF-004: `FusedPadConv2D` Rank Validation Check Failure

## Summary

The appendix reports that `tf.raw_ops.FusedPadConv2D` aborts when given a rank-2 input with convolution-style paddings and filter.

## Expected Behavior

TensorFlow should raise a normal rank/shape validation error.

## Observed Behavior

```text
Check failed: d < dims() (2 vs. 2)
*** Check failure stack trace: ***
Aborted
```

## Minimal Reproduction

```python
import tensorflow as tf

tf.raw_ops.FusedPadConv2D(
    input=tf.zeros([3, 2], tf.float32),
    paddings=[[0, 0], [1, 1], [1, 1], [0, 0]],
    filter=tf.zeros([2, 2, 1, 1], tf.float32),
    mode="REFLECT",
    strides=[1, 1, 1, 1],
    padding="VALID",
)
```

## Source

`基于大语言模型的深度学习库模糊测试.pdf`, appendix "缺陷触发代码示例".

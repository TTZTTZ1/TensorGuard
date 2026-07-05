# PAPER-TF-005: `conv2d_transpose` Fatal Check Failure

## Summary

The appendix reports that a malformed `tf.nn.conv2d_transpose` call aborts the TensorFlow process.

## Expected Behavior

TensorFlow should reject malformed argument types or shapes with a normal exception.

## Observed Behavior

```text
Check failed: d < dims() (2 vs. 0)
*** Check failure stack trace: ***
Aborted
```

## Minimal Reproduction

```python
import tensorflow as tf

output_image = tf.random.normal([1, 3, 3, 8])
tf.nn.conv2d_transpose(
    output_image,
    8,
    (2, 2),
    strides=(2, 2),
    padding="SAME",
)
```

## Source

`基于大语言模型的深度学习库模糊测试.pdf`, appendix "缺陷触发代码示例".

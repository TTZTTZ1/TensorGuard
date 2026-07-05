# PAPER-TF-001: `LinearOperatorLowRankUpdate` Gradient Segfault

## Summary

The appendix reports that differentiating through `tf.linalg.LinearOperatorLowRankUpdate(...).matmul(...)` can terminate the process with a segmentation fault.

## Expected Behavior

TensorFlow should reject the incompatible gradient/input shape with a normal exception.

## Observed Behavior

```text
Segmentation fault
```

## Minimal Reproduction

```python
import tensorflow as tf

base = tf.linalg.LinearOperatorIdentity(num_rows=3)
u = tf.random.normal([3, 3])
g = tf.constant([4.0])

with tf.GradientTape() as tape:
    result = tf.linalg.LinearOperatorLowRankUpdate(base, u, u).matmul(base)

tape.watch(result)
tape.gradient(result, [u], [g])
```

## Source

`基于大语言模型的深度学习库模糊测试.pdf`, appendix "缺陷触发代码示例".

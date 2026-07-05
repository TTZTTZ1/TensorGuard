# PAPER-TF-003: `TensorScatterUpdate` Rank Check Failure

## Summary

The appendix reports that malformed scatter indices can abort TensorFlow through a fatal internal check.

## Expected Behavior

TensorFlow should reject malformed scatter index/update shapes with a normal exception.

## Observed Behavior

```text
Check failed: d < dims() (1 vs. 1)
*** Check failure stack trace: ***
Aborted
```

## Minimal Reproduction

```python
import tensorflow as tf

tf.raw_ops.TensorScatterUpdate(
    tensor=tf.zeros([8], tf.int32),
    indices=tf.constant([[[4]]]),
    updates=tf.constant([3]),
)
```

## Related APIs Mentioned In Appendix

`tf.raw_ops.TensorScatterAdd`, `tf.raw_ops.TensorScatterSub`, `tf.raw_ops.TensorScatterMin`, `tf.raw_ops.TensorScatterMax`.

## Source

`基于大语言模型的深度学习库模糊测试.pdf`, appendix "缺陷触发代码示例".

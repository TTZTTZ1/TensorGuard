# PAPER-TF-007: MaxPool CPU Floating Point Exception

## Summary

The appendix reports a CPU/GPU behavioral discrepancy for invalid MaxPool inputs. GPU does not crash, while CPU terminates with a floating point exception.

## Expected Behavior

CPU and GPU should consistently reject invalid pooling dimensions with a clear framework exception.

## Observed Behavior

```text
GPU: No crash
CPU: Floating point exception
```

## Minimal Reproduction

```python
import tensorflow as tf

input_data = tf.constant(
    [[[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]],
    dtype=tf.float32,
)
pool = tf.keras.layers.MaxPool1D(pool_size=3, strides=1, padding="valid")
y = pool(input_data)
print(y)
```

## Related APIs Mentioned In Appendix

`tf.keras.layers.MaxPool2D`, `tf.keras.layers.MaxPool3D`, `tf.keras.layers.MaxPooling1D`, `tf.keras.layers.MaxPooling2D`, `tf.keras.layers.MaxPooling3D`, `tf.nn.max_pool`, `tf.nn.max_pool1d`, `tf.nn.max_pool2d`, `tf.nn.max_pool3d`, `tf.nn.pool`, `tf.raw_ops.MaxPool`, `tf.raw_ops.MaxPool3D`.

## Source

`基于大语言模型的深度学习库模糊测试.pdf`, appendix "缺陷触发代码示例".

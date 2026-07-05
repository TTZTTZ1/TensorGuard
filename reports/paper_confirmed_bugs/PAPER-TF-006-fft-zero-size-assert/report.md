# PAPER-TF-006: `tf.signal.irfft` Zero-Sized FFT Assertion

## Summary

The appendix reports that `tf.signal.irfft` can abort on a malformed input with a zero-sized FFT assertion.

## Expected Behavior

TensorFlow should reject the input shape/dtype combination with a normal exception.

## Observed Behavior

```text
Assertion failure
no zero-sized FFTs
Aborted
```

## Minimal Reproduction

```python
import numpy as np
import tensorflow as tf

input_tensor = np.array([[[1], [2]], [[3], [4]]])
output_tensor = tf.signal.irfft(input_tensor)
print(output_tensor)
```

## Related APIs Mentioned In Appendix

`tf.signal.irfft2d`, `tf.signal.irfft3d`, `tf.signal.rfft`, `tf.signal.rfft2d`, `tf.signal.rfft3d`, `tf.signal.inverse_stft`.

## Source

`基于大语言模型的深度学习库模糊测试.pdf`, appendix "缺陷触发代码示例".

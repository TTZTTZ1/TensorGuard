# PAPER-TF-002: `LookupTableExportV2` Dtype Check Failure

## Summary

The appendix reports that exporting an integer `StaticHashTable` as string keys/values through `tf.raw_ops.LookupTableExportV2` aborts the process.

## Expected Behavior

TensorFlow should raise a normal dtype mismatch exception.

## Observed Behavior

```text
Check failed: dtype() == expected_dtype (7 vs. 9)
*** Check failure stack trace: ***
Aborted
```

## Minimal Reproduction

```python
import tensorflow as tf

table = tf.lookup.StaticHashTable(
    tf.lookup.KeyValueTensorInitializer(
        tf.constant([0], dtype=tf.int64),
        tf.constant([1], dtype=tf.int64),
    ),
    default_value=-1,
)

tf.raw_ops.LookupTableExportV2(
    table_handle=table.resource_handle,
    Tkeys=tf.string,
    Tvalues=tf.string,
)
```

## Source

`基于大语言模型的深度学习库模糊测试.pdf`, appendix "缺陷触发代码示例".

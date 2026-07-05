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

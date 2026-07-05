# tf.keras.applications.imagenet_utils.decode_predictions

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/applications/imagenet_utils/decode_predictions](https://tensorflow.google.cn/api_docs/python/tf/keras/applications/imagenet_utils/decode_predictions)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/applications/imagenet_utils.py#L116-L158) |

Decodes the prediction of an ImageNet model.

```
tf.keras.applications.imagenet_utils.decode_predictions(
    preds, top=5
)
```

| Args | |

|  |  |
| --- | --- |
| `preds` | NumPy array encoding a batch of predictions. |
| `top` | Integer, how many top-guesses to return. Defaults to `5`. |

| Returns | |
| A list of lists of top class prediction tuples `(class_name, class_description, score)`. One list of tuples per sample in batch input. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | In case of invalid shape of the `pred` array (must be 2D). |
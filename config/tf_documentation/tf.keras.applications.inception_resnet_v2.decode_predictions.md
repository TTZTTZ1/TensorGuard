# tf.keras.applications.inception_resnet_v2.decode_predictions

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/applications/inception_resnet_v2/decode_predictions](https://tensorflow.google.cn/api_docs/python/tf/keras/applications/inception_resnet_v2/decode_predictions)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/applications/inception_resnet_v2.py#L384-L386) |

Decodes the prediction of an ImageNet model.

```
tf.keras.applications.inception_resnet_v2.decode_predictions(
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
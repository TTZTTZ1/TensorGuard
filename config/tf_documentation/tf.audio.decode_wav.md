# tf.audio.decode_wav

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/audio/decode_wav](https://tensorflow.google.cn/api_docs/python/tf/audio/decode_wav)

---

Decode a 16-bit PCM WAV file to a float tensor.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.audio.decode_wav`](https://tensorflow.google.cn/api_docs/python/tf/audio/decode_wav)

```
tf.audio.decode_wav(
    contents: Annotated[Any, _atypes.String],
    desired_channels: int = -1,
    desired_samples: int = -1,
    name=None
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Simple audio recognition: Recognizing keywords](https://tensorflow.google.cn/tutorials/audio/simple_audio) * [Transfer learning with YAMNet for environmental sound classification](https://tensorflow.google.cn/tutorials/audio/transfer_learning_audio) |

The -32768 to 32767 signed 16-bit values will be scaled to -1.0 to 1.0 in float.

When desired\_channels is set, if the input contains fewer channels than this
then the last channel will be duplicated to give the requested number, else if
the input has more channels than requested then the additional channels will be
ignored.

If desired\_samples is set, then the audio will be cropped or padded with zeroes
to the requested length.

The first output contains a Tensor with the content of the audio samples. The
lowest dimension will be the number of channels, and the second will be the
number of samples. For example, a ten-sample-long stereo WAV file should give an
output shape of [10, 2].

| Args | |

|  |  |
| --- | --- |
| `contents` | A `Tensor` of type `string`. The WAV-encoded audio, usually from a file. |
| `desired_channels` | An optional `int`. Defaults to `-1`. Number of sample channels wanted. |
| `desired_samples` | An optional `int`. Defaults to `-1`. Length of audio requested. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (audio, sample\_rate). | |
| `audio` | A `Tensor` of type `float32`. |
| `sample_rate` | A `Tensor` of type `int32`. |
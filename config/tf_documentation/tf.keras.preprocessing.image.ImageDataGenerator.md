# tf.keras.preprocessing.image.ImageDataGenerator

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/preprocessing/image/ImageDataGenerator](https://tensorflow.google.cn/api_docs/python/tf/keras/preprocessing/image/ImageDataGenerator)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/legacy/preprocessing/image.py#L949-L1547) |

DEPRECATED.

```
tf.keras.preprocessing.image.ImageDataGenerator(
    featurewise_center=False,
    samplewise_center=False,
    featurewise_std_normalization=False,
    samplewise_std_normalization=False,
    zca_whitening=False,
    zca_epsilon=1e-06,
    rotation_range=0,
    width_shift_range=0.0,
    height_shift_range=0.0,
    brightness_range=None,
    shear_range=0.0,
    zoom_range=0.0,
    channel_shift_range=0.0,
    fill_mode='nearest',
    cval=0.0,
    horizontal_flip=False,
    vertical_flip=False,
    rescale=None,
    preprocessing_function=None,
    data_format=None,
    validation_split=0.0,
    interpolation_order=1,
    dtype=None
)
```

### Used in the notebooks

| Used in the guide |
| --- |
| * [tf.data: Build TensorFlow input pipelines](https://tensorflow.google.cn/guide/data) |

## Methods

### `apply_transform`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/legacy/preprocessing/image.py#L1385-L1447)

```
apply_transform(
    x, transform_parameters
)
```

Applies a transformation to an image according to given parameters.

| Args | |

|  |  |
| --- | --- |
| `x` | 3D tensor, single image. |
| `transform_parameters` | Dictionary with string - parameter pairs describing the transformation. Currently, the following parameters from the dictionary are used: |

* `'theta'`: Float. Rotation angle in degrees.
* `'tx'`: Float. Shift in the x direction.
* `'ty'`: Float. Shift in the y direction.
* `'shear'`: Float. Shear angle in degrees.
* `'zx'`: Float. Zoom in the x direction.
* `'zy'`: Float. Zoom in the y direction.
* `'flip_horizontal'`: Boolean. Horizontal flip.
* `'flip_vertical'`: Boolean. Vertical flip.
* `'channel_shift_intensity'`: Float. Channel shift intensity.
* `'brightness'`: Float. Brightness shift intensity.

| Returns | |
| A transformed version of the input (same shape). | |

### `fit`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/legacy/preprocessing/image.py#L1462-L1547)

```
fit(
    x, augment=False, rounds=1, seed=None
)
```

Fits the data generator to some sample data.

This computes the internal data stats related to the
data-dependent transformations, based on an array of sample data.

Only required if `featurewise_center` or
`featurewise_std_normalization` or `zca_whitening`
are set to `True`.

When `rescale` is set to a value, rescaling is applied to
sample data before computing the internal data stats.

| Args | |

|  |  |
| --- | --- |
| `x` | Sample data. Should have rank 4. In case of grayscale data, the channels axis should have value 1, in case of RGB data, it should have value 3, and in case of RGBA data, it should have value 4. |
| `augment` | Boolean (default: False). Whether to fit on randomly augmented samples. |
| `rounds` | Int (default: 1). If using data augmentation (`augment=True`), this is how many augmentation passes over the data to use. |
| `seed` | Int (default: None). Random seed. |

### `flow`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/legacy/preprocessing/image.py#L1089-L1118)

```
flow(
    x,
    y=None,
    batch_size=32,
    shuffle=True,
    sample_weight=None,
    seed=None,
    save_to_dir=None,
    save_prefix='',
    save_format='png',
    ignore_class_split=False,
    subset=None
)
```

### `flow_from_dataframe`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/legacy/preprocessing/image.py#L1159-L1230)

```
flow_from_dataframe(
    dataframe,
    directory=None,
    x_col='filename',
    y_col='class',
    weight_col=None,
    target_size=(256, 256),
    color_mode='rgb',
    classes=None,
    class_mode='categorical',
    batch_size=32,
    shuffle=True,
    seed=None,
    save_to_dir=None,
    save_prefix='',
    save_format='png',
    subset=None,
    interpolation='nearest',
    validate_filenames=True,
    **kwargs
)
```

### `flow_from_directory`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/legacy/preprocessing/image.py#L1120-L1157)

```
flow_from_directory(
    directory,
    target_size=(256, 256),
    color_mode='rgb',
    classes=None,
    class_mode='categorical',
    batch_size=32,
    shuffle=True,
    seed=None,
    save_to_dir=None,
    save_prefix='',
    save_format='png',
    follow_links=False,
    subset=None,
    interpolation='nearest',
    keep_aspect_ratio=False
)
```

### `get_random_transform`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/legacy/preprocessing/image.py#L1294-L1383)

```
get_random_transform(
    img_shape, seed=None
)
```

Generates random parameters for a transformation.

| Args | |

|  |  |
| --- | --- |
| `img_shape` | Tuple of integers. Shape of the image that is transformed. |
| `seed` | Random seed. |

| Returns | |
| A dictionary containing randomly chosen parameters describing the transformation. | |

### `random_transform`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/legacy/preprocessing/image.py#L1449-L1460)

```
random_transform(
    x, seed=None
)
```

Applies a random transformation to an image.

| Args | |

|  |  |
| --- | --- |
| `x` | 3D tensor, single image. |
| `seed` | Random seed. |

| Returns | |
| A randomly transformed version of the input (same shape). | |

### `standardize`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/legacy/preprocessing/image.py#L1232-L1292)

```
standardize(
    x
)
```

Applies the normalization configuration in-place to a batch of inputs.

`x` is changed in-place since the function is mainly used internally
to standardize images and feed them to your network. If a copy of `x`
would be created instead it would have a significant performance cost.
If you want to apply this method without changing the input in-place
you can call the method creating a copy before:

standardize(np.copy(x))

| Args | |

|  |  |
| --- | --- |
| `x` | Batch of inputs to be normalized. |

| Returns | |
| The inputs, normalized. | |
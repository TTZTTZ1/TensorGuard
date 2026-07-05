# Confirmed Bug Summary

Source: `基于大语言模型的深度学习库模糊测试.pdf`, appendix "缺陷触发代码示例".

Total: 14 confirmed trigger examples.

- PyTorch: 5
- TensorFlow: 9

## PyTorch

| ID | API | Type |
| --- | --- | --- |
| PAPER-PT-001 | `torch.arange` | Floating point exception |
| PAPER-PT-002 | `torch.nn.functional.ctc_loss` | Double free / memory corruption |
| PAPER-PT-003 | `torch.nn.LSTMCell` | Segmentation fault |
| PAPER-PT-004 | `torch.sparse.mm` | Allocator corruption / invalid free |
| PAPER-PT-005 | `torch.nn.BatchNorm1d` | Internal assert |

## TensorFlow

| ID | API | Type |
| --- | --- | --- |
| PAPER-TF-001 | `tf.linalg.LinearOperatorLowRankUpdate` | Segmentation fault |
| PAPER-TF-002 | `tf.raw_ops.LookupTableExportV2` | Fatal dtype check failure |
| PAPER-TF-003 | `tf.raw_ops.TensorScatterUpdate` | Fatal rank check failure |
| PAPER-TF-004 | `tf.raw_ops.FusedPadConv2D` | Fatal rank check failure |
| PAPER-TF-005 | `tf.nn.conv2d_transpose` | Fatal check failure |
| PAPER-TF-006 | `tf.signal.irfft` | Assertion failure |
| PAPER-TF-007 | `tf.keras.layers.MaxPool1D` | CPU floating point exception |
| PAPER-TF-008 | `tf.nn.atrous_conv2d` | CPU/GPU exception inconsistency |
| PAPER-TF-009 | `tf.nn.conv2d_transpose` | CPU/GPU exception inconsistency |

## Usage

The web replay page can read `index.json`, then load each entry's `meta.json`, `repro.py`, and `report.md`.

Run these reproducers only in isolated subprocesses. Several entries intentionally crash or abort the Python process.

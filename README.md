<p align="center">
  <h1 align="center">🛡️ TensorGuard</h1>
  <p align="center">面向深度学习框架的 LLM 辅助模糊测试与缺陷证据管理工作台</p>
  <p align="center">
    <img src="https://img.shields.io/badge/Python-3.10-3776AB?logo=python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/PyTorch-2.11-EE4C2C?logo=pytorch&logoColor=white" alt="PyTorch">
    <img src="https://img.shields.io/badge/TensorFlow-2.21-FF6F00?logo=tensorflow&logoColor=white" alt="TensorFlow">
    <img src="https://img.shields.io/badge/LLM-Powered-9B59B6?logo=openai&logoColor=white" alt="LLM">
  </p>
</p>

---

## 📖 项目简介

TensorGuard 是一个面向 PyTorch 和 TensorFlow 的**自动化模糊测试与缺陷证据管理工作台**。它利用大语言模型（LLM）生成和变异测试程序，通过 CPU/GPU 差分检测发现深度学习框架中的潜在缺陷。

### 🎯 核心创新

| 创新点 | 说明 |
|--------|------|
| **结构化约束引导** | 基于 DeepSeek 蒸馏的 API 参数约束库，引导 LLM 生成高质量种子 |
| **四层修复管线** | 静态清洗 → 语法修复 → 递归裁剪 → 错误反馈重生成 |
| **自适应重采样** | 根据约束复杂度动态调整采样策略，提升有效率 |
| **CPU/GPU 差分 Oracle** | 通过 AST 变换自动生成双版本代码，检测执行差异 |

### 🏗️ 系统架构

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              TensorGuard 系统架构                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌────────────┐ │
│  │   DeepSeek   │───▶│    Qwen      │───▶│   InCoder    │───▶│  差分检测   │ │
│  │  约束蒸馏    │    │  种子生成    │    │  演化变异    │    │   Oracle   │ │
│  └──────────────┘    └──────────────┘    └──────────────┘    └────────────┘ │
│         │                   │                   │                   │       │
│         ▼                   ▼                   ▼                   ▼       │
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │                    四层种子修复管线                                      ││
│  │  Layer 1: 静态清洗  │  Layer 2: 语法修复  │  Layer 3: 递归裁剪  │  L4: 重生成 ││
│  └─────────────────────────────────────────────────────────────────────────┘│
│         │                                                           │       │
│         ▼                                                           ▼       │
│  ┌──────────────┐                                          ┌──────────────┐ │
│  │  实验数据    │                                          │  Bug 证据    │ │
│  │  experiment/ │                                          │   reports/   │ │
│  └──────────────┘                                          └──────────────┘ │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## ✨ 功能特性

### 🔬 核心能力

- **结构化约束引导的种子生成**：基于 DeepSeek 蒸馏的 API 参数约束库，结合 Qwen2.5-Coder 生成高质量种子程序
- **四层种子修复管线**：静态清洗 → 语法修复 → 递归裁剪 → 错误反馈重生成，显著提升种子有效率
- **自适应重采样**：根据约束复杂度动态调整采样策略
- **InCoder 演化变异**：使用 InCoder-6B 进行 infill 变异，扩展测试覆盖面
- **CPU/GPU 差分 Oracle**：通过 AST 变换生成 CPU/GPU 双版本代码，检测执行差异

### 🖥️ Web 工作台

- **Dashboard**：API 总览、已确认 Bug 统计、运行环境信息
- **单 API 运行**：选择 API、运行模式、实时查看进度和 GPU 监控
- **候选审查**：查看检测到的异常候选、加入候选列表
- **Bug 复现**：运行最小复现代码、生成证据报告

---

## 🖼️ 界面展示

### 系统总览 Dashboard

![系统总览](docs/screenshots/01-overview-dashboard.png)

- API 覆盖统计（PyTorch: 1568 / TensorFlow: 3040）
- 已确认 Bug 数量
- 运行环境信息

### 已确认 Bug 列表

![已确认Bug](docs/screenshots/02-overview-bugs.png)

- 结构化归档的缺陷证据
- 支持查看详情和复现

### 单 API 运行 - 选择目标

![API选择](docs/screenshots/03-api-run-selector.png)

- 选择框架（PyTorch/TensorFlow）
- 选择目标 API
- 配置运行模式

### 单 API 运行 - 执行进度

![运行进度](docs/screenshots/04-api-run-progress.png)

- 实时显示各阶段进展
- GPU 监控曲线
- 种子生成、变异、检测状态

### 单 API 运行 - 结果分析

![结果分析](docs/screenshots/05-api-run-results.png)

- 有效程序数量
- 异常/崩溃统计
- Trace 检测结果

### Bug 复现

![Bug复现](docs/screenshots/06-bug-replay.png)

- 最小复现代码
- 环境配置选择
- 执行结果与证据报告

---

## 📁 项目结构

```
TensorGuard/
├── 🧠 核心模块
│   ├── codex.py              # 种子生成入口（Qwen/Codex）
│   ├── qwen_seed.py          # Qwen 种子生成器 + 四层修复管线
│   ├── ev_generation.py      # 演化模糊测试主循环
│   ├── driver.py             # 批量运行驱动器
│   ├── torch2cuda.py         # CPU/GPU 差分检测 oracle
│   └── model.py              # SpanLM 模型封装（InCoder/CodeGen）
│
├── 🛠️ 工具库
│   ├── util/                 # 核心工具库（AST 变换、种子池、插桩等）
│   ├── mycoverage/           # 多进程执行器与覆盖率追踪
│   └── process_file.py       # 代码清洗工具链
│
├── 📊 数据与配置
│   ├── experiment/           # DeepSeek 蒸馏的 Prompt/Constraint Library
│   ├── data/                 # API 列表与 Prompt 模板
│   └── config/               # TensorFlow API 文档与配置
│
├── 🌐 Web 工作台
│   └── webapp/               # 后端 + Vue.js 前端
│
├── 📝 报告与测试
│   ├── reports/              # Bug 报告与复现证据
│   └── test/                 # 单元测试
│
└── 🚀 运行脚本
    └── scripts/              # 各种运行脚本
```

---

## 🚀 快速开始

### 环境要求

| 项目 | 要求 |
|------|------|
| Python | 3.10 |
| PyTorch | 2.11.0+cu130 |
| TensorFlow | 2.21.0 |
| GPU | 推荐（CPU 也可运行但较慢） |

### 安装

**推荐方式：使用 environment.yml（完整环境）**

```bash
# 克隆仓库
git clone https://github.com/TTZTTZ1/TensorGuard.git
cd TensorGuard

# 创建完整环境（包含CUDA支持）
conda env create -f environment.yml
conda activate tensorguard
```

**备选方式：手动安装**

```bash
# 创建虚拟环境
conda create -n tensorguard python=3.10
conda activate tensorguard

# 安装 PyTorch（需要CUDA 13.0）
pip install torch==2.11.0+cu130 --index-url https://download.pytorch.org/whl/cu130

# 安装其他依赖
pip install -r requirements.txt
```

### 单 API 端到端演示

```bash
# 运行单个 API 的完整测试流程
python3 scripts/run_one_api_demo.py \
  --lib torch \
  --api torch.nn.functional.conv1d \
  --out demo_runs/conv1d \
  --mode demo

# 干跑模式（不加载模型，快速验证流程）
python3 scripts/run_one_api_demo.py \
  --lib torch \
  --api torch.nn.functional.conv1d \
  --out demo_runs/conv1d_dry \
  --mode demo \
  --dry_run
```

### 全量运行

**方式一：通过单 API 脚本（推荐）**

```bash
# 运行所有 PyTorch API（1568 个）
python3 scripts/run_all_apis.py --lib torch

# 运行所有 TensorFlow API（3040 个）
python3 scripts/run_all_apis.py --lib tf

# 并行运行（2 个 worker）
python3 scripts/run_all_apis.py --lib torch --max_workers 2

# 断点续传（跳过已完成的 API）
python3 scripts/run_all_apis.py --lib torch --resume

# 干跑模式（不加载模型）
python3 scripts/run_all_apis.py --lib torch --dry_run
```

**方式二：直接调用各模块**

```bash
# 运行所有 PyTorch API
python3 scripts/run_all_apis_direct.py --lib torch

# 运行所有 TensorFlow API
python3 scripts/run_all_apis_direct.py --lib tf
```

输出目录：`batch_runs/<lib>_<timestamp>/`，包含：
- `<api>/`：每个 API 的运行结果
- `batch_summary.json`：批量运行摘要

### 启动 Web 工作台

```bash
python3 webapp/server.py --host 127.0.0.1 --port 8008
```

打开浏览器访问 `http://127.0.0.1:8008/`

---

## 🔍 检测流程

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  约束加载   │───▶│  种子生成   │───▶│  修复验证   │───▶│  演化变异   │───▶│  差分检测   │───▶│  证据归档   │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
     │                   │                   │                   │                   │                   │
     ▼                   ▼                   ▼                   ▼                   ▼                   ▼
 从 experiment/     Qwen2.5-Coder      四层管线修复       InCoder-6B        torch2cuda.py      存入 reports/
 读取约束          生成候选程序        语法/语义错误      infill 变异        CPU/GPU 对比       支持 Web 审查
```

---

## 📊 实验数据

### API 覆盖

| 框架 | API 数量 | 说明 |
|------|----------|------|
| PyTorch | 1,568 | 完整 API 清单 |
| TensorFlow | 3,040 | 完整 API 清单 |

### 已发现缺陷

项目已发现多个 PyTorch 和 TensorFlow 中的潜在缺陷，详见 `reports/` 目录。

每个缺陷包含：
- `repro.py`：最小复现代码
- `report.md`：问题描述与观测结果
- `meta.json`：环境元数据

---

## ⚙️ 配置说明

### API 列表

| 文件 | 说明 |
|------|------|
| `data/torch_apis.txt` | PyTorch API 清单（1,568 个） |
| `data/tf_apis.txt` | TensorFlow API 清单（3,040 个） |
| `data/torch_apis_100sample.txt` | 100 API 采样子集（用于消融实验） |

### 消融实验配置

`qwen_seed.py` 支持五种消融模式：

| 模式 | 说明 |
|------|------|
| `full` | 完整方法（结构化约束 + 四层修复 + 自适应重采样）|
| `no_constraints` | 移除结构化约束 |
| `no_repair` | 仅保留静态清洗 |
| `no_layer4` | 关闭错误反馈重生成 |
| `no_resample` | 强制单次采样 |

```bash
python3 qwen_seed.py --library torch \
  --apilist data/torch_apis.txt \
  --out_dir codex_seed_programs/torch-qwen \
  --constraints_dir experiment/torch \
  --ablation full
```

### 运行模式说明

| 模式 | 用途 | 参数 |
|------|------|------|
| `demo` | 快速演示、验证流程 | 少量样本、短超时 |
| `full` | 完整测试、发现缺陷 | 全量样本、长超时 |

---

## 🙏 致谢

本项目基于以下开源模型：

| 模型 | 用途 | 链接 |
|------|------|------|
| **Qwen2.5-Coder** | 种子生成 | [HuggingFace](https://huggingface.co/Qwen/Qwen2.5-Coder) |
| **InCoder** | 代码变异 | [HuggingFace](https://huggingface.co/facebook/incoder-6B) |
| **DeepSeek** | 约束蒸馏（离线） | [GitHub](https://github.com/deepseek-ai) |

---

## 📄 许可证

本项目仅供学术研究与竞赛使用。

---

<p align="center">
  <sub>Made with ❤️ for Deep Learning Framework Security</sub>
</p>

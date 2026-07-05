"""
生成 4.3.5 节本文方法与基线方法的整体对比图。
PyTorch 与 TensorFlow 各输出一张图，每张图包含 2x2 子图，
子图标号 (a)~(d) 置于子图下方。
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib.ticker import LogLocator, FuncFormatter

# ---------------------------------------------------------------------------
# 基础配置
# ---------------------------------------------------------------------------
mpl.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'PingFang SC',
                                   'Noto Sans CJK SC', 'WenQuanYi Zen Hei',
                                   'Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False
mpl.rcParams['font.size'] = 11
mpl.rcParams['axes.linewidth'] = 0.8
mpl.rcParams['axes.edgecolor'] = '#333333'

# 论文级颜色方案
COLOR_PYTORCH   = '#0891B2'
COLOR_TF        = '#F59E0B'
COLOR_HIGHLIGHT = '#0F2A4A'
COLOR_NEUTRAL   = '#64748B'
COLOR_LIGHT     = '#CBD5E1'

# ---------------------------------------------------------------------------
# 数据：来自论文表 4.5 / 4.6
# ---------------------------------------------------------------------------
methods = ["FreeFuzz", "DeepREL", "TitanFuzz", "本文方法"]

pt_data = {
    "api":     [643, 1071, 1212, 1374],
    "line":    [67728, 82839, 117318, 128049],
    "valid":   [282945, 3801440, 282200, 293710],
    "bug_api": [0, 9, 1, 4],
    "bug":     [0, 2, 0, 3],
}
tf_data = {
    "api":     [1324, 1591, 1880, 2236],
    "line":    [74761, 108995, 131397, 147545],
    "valid":   [1323431, 2938560, 411986, 435140],
    "bug_api": [0, 0, 4, 4],
    "bug":     [0, 0, 3, 4],
}


# ---------------------------------------------------------------------------
# 绘图函数
# ---------------------------------------------------------------------------
def _bar_colors(base_color, n=4, highlight_last=True):
    """生成柱体颜色列表，最后一根（本文方法）以高亮色突出。"""
    colors = [base_color] * n
    if highlight_last:
        colors[-1] = COLOR_HIGHLIGHT
    return colors


def plot_simple(ax, values, base_color, ylabel, fmt="{:,}", log_scale=False):
    """单系列柱状图，本文方法柱体以深色突出。"""
    x = np.arange(len(methods))
    bars = ax.bar(x, values, width=0.55,
                  color=_bar_colors(base_color),
                  edgecolor='white', linewidth=0.8)

    ax.set_xticks(x)
    ax.set_xticklabels(methods, fontsize=10)
    ax.set_ylabel(ylabel, fontsize=10.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.grid(True, linestyle='--', alpha=0.35)
    ax.set_axisbelow(True)

    if log_scale:
        ax.set_yscale('log')
        ax.set_ylim(1e5, 1e7)
        ax.yaxis.set_major_locator(LogLocator(base=10.0, numticks=10))
        ax.yaxis.set_minor_locator(
            LogLocator(base=10.0, subs=(2.0, 3.0, 5.0), numticks=20))
        ax.yaxis.set_major_formatter(
            FuncFormatter(lambda v, _: f"{int(v):,}" if v >= 1 else ""))
        for bar in bars:
            h = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2,
                    h * 1.08, fmt.format(int(h)),
                    ha='center', va='bottom', fontsize=9)
    else:
        ymax = max(values) if max(values) > 0 else 1
        ax.set_ylim(0, ymax * 1.18)
        offset = ymax * 0.012
        for bar in bars:
            h = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2,
                    h + offset, fmt.format(int(h)),
                    ha='center', va='bottom', fontsize=9)


def plot_bug_grouped(ax, bug_api_vals, bug_vals, base_color):
    """分组柱状图：左柱为缺陷 API 数（中性色），右柱为缺陷数（框架色）。"""
    x = np.arange(len(methods))
    width = 0.36

    colors_left = [COLOR_LIGHT] * 3 + [COLOR_HIGHLIGHT]
    colors_right = [base_color] * 3 + [COLOR_HIGHLIGHT]

    b1 = ax.bar(x - width / 2, bug_api_vals, width,
                color=colors_left, edgecolor='white', linewidth=0.8,
                label='缺陷API数')
    b2 = ax.bar(x + width / 2, bug_vals, width,
                color=colors_right, edgecolor='white', linewidth=0.8,
                label='缺陷数')

    ax.set_xticks(x)
    ax.set_xticklabels(methods, fontsize=10)
    ax.set_ylabel('缺陷数量 (个)', fontsize=10.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.grid(True, linestyle='--', alpha=0.35)
    ax.set_axisbelow(True)

    ymax = max(max(bug_api_vals), max(bug_vals))
    ax.set_ylim(0, ymax + 1.8 if ymax > 0 else 2)
    ax.set_yticks(np.arange(0, ymax + 2, 1 if ymax <= 6 else 2))

    for bars in (b1, b2):
        for bar in bars:
            h = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, h + 0.15,
                    str(int(h)), ha='center', va='bottom', fontsize=9)

    ax.legend(loc='upper left', frameon=False, fontsize=9)


def make_framework_figure(data, base_color, framework_name, fname):
    """生成单个框架的 2x2 子图。"""
    fig, axes = plt.subplots(2, 2, figsize=(12, 8.2))

    # (a) API 覆盖广度
    plot_simple(axes[0, 0], data['api'], base_color, '覆盖 API 数 (个)')
    # (b) 底层代码行覆盖深度
    plot_simple(axes[0, 1], data['line'], base_color, '底层代码行覆盖数 (行)')
    # (c) 有效程序数量（对数刻度）
    plot_simple(axes[1, 0], data['valid'], base_color,
                '有效程序数量 (条, 对数刻度)', log_scale=True)
    # (d) 缺陷检测能力
    plot_bug_grouped(axes[1, 1], data['bug_api'], data['bug'], base_color)

    # 子图标号置于子图下方
    subplot_titles = [
        '(a) API 覆盖广度',
        '(b) 底层代码行覆盖深度',
        '(c) 有效程序数量',
        '(d) 缺陷检测能力',
    ]
    positions = [(0, 0), (0, 1), (1, 0), (1, 1)]
    for (i, j), title in zip(positions, subplot_titles):
        ax = axes[i, j]
        ax.text(0.5, -0.22, title, transform=ax.transAxes,
                ha='center', va='top',
                fontsize=12, fontweight='bold', color='#1a1a1a')

    plt.tight_layout()
    plt.subplots_adjust(hspace=0.45, wspace=0.28)
    fig.savefig(fname, dpi=300, bbox_inches='tight')
    plt.close(fig)
    print(f'  -> {fname}')


# ---------------------------------------------------------------------------
# 生成
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    print('Generating figures...')
    make_framework_figure(pt_data, COLOR_PYTORCH, 'PyTorch',
                          'fig_4_x_pytorch.png')
    make_framework_figure(tf_data, COLOR_TF, 'TensorFlow',
                          'fig_4_x_tensorflow.png')
    print('Done.')
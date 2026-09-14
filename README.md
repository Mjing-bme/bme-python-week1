# bme-python-week1

生物医学工程科研编程 · 第一周练习仓库
从「会 Python 基础」到「能用 Python 独立处理科研数据」。

> 仓库地址：https://github.com/Mjing-bme/bme-python-week1
> 作者：Mj（中南大学生物工程 · 生医工/电子信息方向备考）
>
> 学习路线：Python → NumPy/Pandas/Matplotlib/SciPy → Git →
> 生物医学数据分析 → 生物医学信号处理 → ECG/EEG → 机器学习 → 深度学习 → 医学图像

## 环境

| 项目 | 版本 |
|---|---|
| Python | 3.13.9（Anaconda，安装于 `E:\Anaconda`） |
| numpy | 2.3.5 |
| pandas | 2.3.3 |
| matplotlib | 3.10.6 |
| scipy | 1.16.3 |
| 编辑器 | VS Code + Jupyter 扩展 |

安装依赖（换电脑时用）：
```bash
pip install -r requirements.txt
```

## 目录结构

```
bme-python-week1/
├── README.md          # 本文件
├── requirements.txt   # 依赖版本
├── .gitignore
├── data/              # 数据（不传 GitHub，可用脚本重新生成）
│   └── make_data.py   #   模拟监护数据的生成脚本
├── notebooks/         # 每天一个 Jupyter Notebook
├── scripts/           # 可复用的 .py 模块
├── outputs/           # 图 与 结果表
└── notes/             # 学习记录（Obsidian 格式）
```

## 如何运行

```bash
# 1. 生成本周使用的模拟监护数据
python data/make_data.py

# 2. 打开 Notebook
#    VS Code 左侧点开 notebooks/day01_numpy_basics.ipynb，右上角选择内核
```

## 数据说明

`data/vitals_raw.csv`：一台床旁监护仪对一名患者的 8 小时连续监测记录。

| 列名 | 含义 | 单位 |
|---|---|---|
| `time_min` | 距开始监测的时间 | 分钟 |
| `time_h` | 距开始监测的时间 | 小时 |
| `hr_bpm` | 心率 | 次/分 |
| `spo2_pct` | 血氧饱和度 | % |
| `rr_bpm` | 呼吸频率 | 次/分 |
| `sbp_mmHg` | 收缩压 | mmHg |

> ⚠️ 数据为**模拟生成**，其中**刻意包含了若干数据质量问题**，
> 需要在使用前自行检查。真实临床数据同样需要这一步。

## 本周进度

- [ ] Day 1 NumPy 数组基础
- [ ] Day 2 索引 / 切片 / 布尔索引 / 统计
- [ ] Day 3 广播 / 向量化 / 卷积平滑
- [ ] Day 4 Pandas 读取与清洗
- [ ] Day 5 Pandas 筛选与分组统计
- [ ] Day 6 Matplotlib 科研可视化
- [ ] Day 7 SciPy 初识 + 独立验收项目

## 主要发现

（Day 7 结束后，在这里写 3 条最重要的数据结论，每条附对应图或表）

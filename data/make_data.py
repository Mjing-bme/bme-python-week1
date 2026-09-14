"""
make_data.py —— 生成 Day1~Day6 使用的模拟临床监护数据

数据背景（科研场景）：
    一台床旁监护仪以固定间隔记录一名患者的 5 项生命体征，共 8 小时。
    采样间隔 48 秒 → 8 小时 = 480 分钟 / 0.8 分钟 = 600 个采样点。

为什么要"模拟"而不是直接下载真实数据：
    1. 真实数据（PhysioNet 等）留到第二周做 ECG 用，本周先专注练工具
    2. 模拟数据可以精确控制"数据质量问题"——科研里 80% 的时间花在发现和
       处理脏数据上，所以这份数据里**故意埋了异常**，等你去发现
    3. 随机种子固定，谁跑都得到同一份数据（可复现性 = 科研基本要求）

运行方式（在 VS Code 终端里）：
    python data/make_data.py

输出：data/vitals_raw.csv
"""

from pathlib import Path
import numpy as np
import pandas as pd

# 固定随机种子：保证每次生成的数据完全一致（可复现）
rng = np.random.default_rng(20260301)

N = 600          # 采样点数
DT_MIN = 0.8     # 采样间隔（分钟），0.8 min = 48 s
t_min = np.arange(N) * DT_MIN    # 时间轴，单位：分钟
t_h = t_min / 60.0               # 时间轴，单位：小时

# ---------- 1. 心率 hr_bpm：整体缓慢上升（62 → 78）+ 呼吸性波动 + 噪声 ----------
hr = 62 + 16 * np.sqrt(t_h / 8.0)          # 用 sqrt 而不是直线，避免"完美线性"的假数据感
hr = hr + 3 * np.sin(2 * np.pi * t_min / 4.0)   # 周期 4 分钟的生理波动
hr = hr + rng.normal(0, 1.5, N)                 # 随机噪声
hr = np.clip(hr, 55, 115)                       # 生理合理区间

# ---------- 2. 血氧 spo2_pct：小幅波动，偶尔短暂下降到 88（临床关注点） ----------
spo2 = 98 - 1.2 * np.sin(2 * np.pi * t_h / 2.5) - 0.02 * t_h
spo2 = spo2 + rng.normal(0, 0.4, N)

# ---------- 3. 呼吸频率 rr_bpm：周期约 12 分钟的缓慢波动 ----------
rr = 16 + 2 * np.sin(2 * np.pi * t_min / 12.0) + rng.normal(0, 0.8, N)
rr = np.clip(rr, 9, 26)

# ---------- 4. 收缩压 sbp_mmHg：缓慢上升 + 偶发波动 ----------
sbp = 128 + 0.9 * t_h + 6 * np.sin(2 * np.pi * t_min / 45.0) + rng.normal(0, 3, N)

record = pd.DataFrame({
    "time_min": np.round(t_min, 2),
    "time_h": np.round(t_h, 4),
    "hr_bpm": np.round(hr, 1),
    "spo2_pct": np.round(spo2, 1),
    "rr_bpm": np.round(rr, 1),
    "sbp_mmHg": np.round(sbp, 1),
})

# =============================================================
# 以下是"污染"步骤：故意埋入真实数据中常见的质量问题
# 你不需要现在就看懂，Day 1 的任务就是发现它们
# =============================================================

# 第 1 次血氧探头脱落：连续 6 个采样点（约 5 分钟）无读数
record.loc[231:236, "spo2_pct"] = np.nan
record.loc[231:236, "hr_bpm"] = np.nan

# 第 2 次血氧探头脱落：更长的一段（约 15 分钟）
record.loc[402:420, "spo2_pct"] = np.nan

# 袖带加压或患者活动的瞬间干扰：单点极端值
record.loc[78, "sbp_mmHg"] = 260.0
record.loc[150, "sbp_mmHg"] = 35.0
record.loc[310, "hr_bpm"] = 215.0      # 明显超出该患者监控上限

# 探针误饱和：连续一段时间读数被"截顶"在 88.0，看似正常但其实是误差
record.loc[520:536, "spo2_pct"] = 88.0

out_dir = Path(__file__).resolve().parent
out_path = out_dir / "vitals_raw.csv"
record.to_csv(out_path, index=False, float_format="%.2f")

print(f"已生成：{out_path}")
print(f"形状：{record.shape}（行=采样点，列=指标）")
print(f"列名：{list(record.columns)}")

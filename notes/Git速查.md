# Git 每日操作速查（Day1 建立，每天照着做）

仓库：https://github.com/Mjing-bme/bme-python-week1
本地：`F:\MyProjects\bme-python-week1`
账号：Mj <mjing539breeze@gmail.com>　GitHub 用户名：Mjing-bme

## 每天收尾时的 4 条命令

```powershell
cd F:\MyProjects\bme-python-week1

git status                      # 1. 先看有哪些改动（养成"提交前先看"的习惯）
git add -A                      # 2. 把改动加入暂存区（-A = 包括新增和删除）
git commit -m "Day2: 索引切片与布尔筛选"   # 3. 提交到本地
git push                        # 4. 推到 GitHub（已配好免密码）
```

## commit message 写法

格式：`DayN: 做了什么`

| 好的例子 | 为什么好 |
|---|---|
| `Day2: 完成 axis 与布尔索引练习` | 有日期、有主题、能判断进度 |
| `Day4: 清洗临床数据，处理缺失值与重复行` | 说清具体动作 |
| `fix: 修正心率越界筛选条件` | 小修改用 fix 前缀 |

❌ 避免：`update`、`aaa`、`111`、`提交` —— 三个月后你完全看不懂自己做了什么。

## 查看历史 / 回看改动

```powershell
git log --oneline               # 简洁的提交历史
git log --oneline -5            # 只看最近 5 条
git show <commit号前7位>         # 看某次提交改了什么
git diff                        # 看当前未暂存的改动
git diff --stat                 # 只看改了哪些文件、多少行
```

## 常见问题的解法

| 情况 | 命令 |
|---|---|
| 提交信息写错了（还没 push） | `git commit --amend -m "正确信息"` |
| 忘了加某个文件进上次提交 | `git add 文件` 然后 `git commit --amend --no-edit` |
| 想看自己是不是有权限推 | `git remote -v`，应显示 origin 指向 Mjing-bme |
| 推不上去报认证错误 | 终端执行 `gh auth setup-git` 重配凭证 |

## 本周不要碰（Day7 之后再学）

`git branch` / `git merge` / `git rebase` / `git reset --hard` / `git stash`

说明：`git reset --hard` 会**永久丢掉未提交的改动**，初学者最容易在这里丢代码。
在学会 `git status` + `git commit` 之前，不要用任何带 `--hard` 的命令。

## 为什么数据文件没被提交？

`.gitignore` 里写了 `data/*.csv` 和 `outputs/*.csv`。
因为数据能由 `data/make_data.py` 重新生成，所以仓库只保留"生成脚本"。
验证一下：

```powershell
git check-ignore -v data/vitals_raw.csv
# 输出：.gitignore:15:data/*.csv	data/vitals_raw.csv   ← 说明规则生效
```

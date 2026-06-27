# 插图资源

本目录用于存放教材中的配图、草图导出文件和后续的 draw.io 图示。

## 当前约定

- `scripts/generate_chapter_figures.py` 用于生成基础数学示意图
- 当前首批配图覆盖第 1 到第 3 章
- 后续复杂结构图可以继续补充 draw.io 原始文件

## 重新生成配图

在项目根目录执行：

```bash
uv run python scripts/generate_chapter_figures.py
```

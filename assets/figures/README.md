# 插图资源

本目录用于存放教材中的配图、草图导出文件和后续的 draw.io 图示。

## 当前约定

- `scripts/generate_chapter_figures.py` 用于生成基础数学示意图
- 当前首批配图覆盖第 1 到第 5 章，并已补入第 7、8、9、12、15、16、17、18、19、20 章的首张主图
- 第 15、16、17、18、19、20 章已继续补入多批服务例题讲解的辅助图
- 后续复杂结构图可以继续补充 draw.io 原始文件
- 全书插图优先级与实施清单见 `docs/superpowers/specs/2026-06-29-book-figure-priority-plan.md`

## 重新生成配图

在项目根目录执行：

```bash
uv run python scripts/generate_chapter_figures.py
```

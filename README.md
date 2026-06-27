<div class="hero">
  <h1>机器学习数学教材</h1>
  <p>一套面向弱数学基础学习者的中文教材，用更直观的方式理解机器学习所需的数学。</p>
</div>

[开始阅读](chapters/01-foundations.md){ .md-button .md-button--primary }
[阅读前言](docs/preface.md){ .md-button }
[查看学习路径](docs/learning-path.md){ .md-button }
[浏览章节目录](chapters/README.md){ .md-button }

<div class="section-note">
本教材强调四件事同时成立：<strong>讲清直觉</strong>、<strong>配图辅助理解</strong>、<strong>给出 Python 小实验</strong>、<strong>用 LaTeX 正确呈现公式</strong>。
</div>

<p class="reading-tip">第一次进入本书时，建议先阅读“前言”，再按第 1 章到第 4 章的顺序推进。</p>

## 适合谁读

- 数学基础较弱，尤其缺少系统大学数学训练的学生
- 想学机器学习，但一看到公式就容易畏难的自学者
- 希望先建立直觉、再逐步进入形式化表达的读者

## 你会得到什么

- 从“看不懂公式”过渡到“能读懂模型表达”
- 从单个变量过渡到向量、矩阵、梯度和概率
- 通过图示、代码和小例子，把抽象数学变成可观察的对象

## 推荐入口

- :material-rocket-launch:{ .lg .middle } **从第一章开始**

  ---

  如果你希望按照教材顺序进入，优先从公式阅读与函数直觉开始。

  [进入第一章](chapters/01-foundations.md)

- :material-map-outline:{ .lg .middle } **先看学习路径**

  ---

  如果你担心自己数学基础薄弱，建议先看完整学习路径再决定阅读顺序。

  [查看学习路径](docs/learning-path.md)

- :material-view-list:{ .lg .middle } **直接浏览目录**

  ---

  如果你已经有一定基础，可以直接从章节目录跳到想学的部分。

  [章节目录](chapters/README.md)

- :material-book-open-page-variant:{ .lg .middle } **了解教材设计**

  ---

  想知道这本书为什么这样组织、章节之间怎样衔接，可以先看教材总纲。

  [教材总纲](docs/book-outline.md)
{: .grid .cards}

## 教材特点

- **先讲直觉，再讲符号**

  ---

  优先帮助你理解公式在描述什么，再进入形式化表达。

- **每章尽量配图**

  ---

  函数、向量、距离、变化率、梯度等抽象概念都会尽量给出图示。

- **每章尽量有 Python 小实验**

  ---

  让读者通过可执行代码观察数值变化，而不是只停留在静态定义上。

- **章节之间有明确主线**

  ---

  从函数到向量，从矩阵到微积分，再到概率统计和模型理解，逐步推进。
{: .grid .cards}

## 当前阅读建议

<span class="chapter-badge">推荐顺序</span> 第 1 章 -> 第 2 章 -> 第 3 章 -> 第 4 章

<p class="reading-tip">如果你是第一次系统学习机器学习数学，这四章构成最关键的起步阶段。</p>

## 章节主线

1. 数学准备与公式阅读
2. 函数、图像与变化率
3. 向量与几何直觉
4. 矩阵与线性变换
5. 导数与优化直觉
6. 多元微积分基础
7. 概率论基础
8. 随机变量与常见分布
9. 统计学基础与估计
10. 损失函数与优化方法
11. 特征值、奇异值分解与降维
12. 神经网络中的数学基础

## 站点说明

- 在线阅读地址：`https://albertandking.github.io/math/`
- 本地预览命令：`uv run python scripts/build_site_docs.py` 后执行 `uv run mkdocs serve`
- 静态构建命令：`uv run python scripts/build_site_docs.py` 后执行 `uv run mkdocs build --strict`
- GitHub Actions 工作流：`.github/workflows/deploy-pages.yml`

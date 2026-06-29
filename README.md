<div class="hero">
  <h1>机器学习数学教材</h1>
  <p>一套面向数学基础较弱学习者的中文教材，帮助你从直觉、图示、代码与公式四条线索中，逐步建立机器学习所需的数学理解。</p>
</div>

[开始阅读](chapters/01-foundations.md){ .md-button .md-button--primary }
[先读前言](docs/preface.md){ .md-button }
[先看路径](docs/learning-path.md){ .md-button }
[按目录选读](chapters/README.md){ .md-button }

<div class="section-note">
本教材希望把“能读懂公式”和“能理解模型”放在同一条学习路径里推进。整本书会尽量同时做到：<strong>先讲清直觉</strong>、<strong>再用图示帮助理解</strong>、<strong>再用 Python 小实验观察现象</strong>、<strong>最后把关键关系稳定地写成 LaTeX 公式</strong>。
</div>

<p class="reading-tip">第一次阅读本书时，建议先阅读“前言”，再按第 1 章到第 4 章的顺序学习。这个起步阶段的重点不是尽快接触复杂模型，而是先把公式阅读、函数视角、向量表示和矩阵表达这套基础语言真正建立起来。</p>

## 适合谁读

- 数学基础较弱，尤其缺少系统大学数学训练的学生
- 想学机器学习，但一看到公式就容易畏难的自学者
- 希望先建立直觉、再逐步进入形式化表达的读者

## 你会得到什么

- 从“看不懂公式”过渡到“能读懂模型表达”
- 从单个变量过渡到向量、矩阵、梯度和概率
- 通过图示、代码和小例子，把抽象数学变成可观察的对象

## 从这里开始

- :material-rocket-launch:{ .lg .middle } **从第一章开始**

  ---

  如果你希望按照教材顺序进入，最稳妥的方式是先从公式阅读与函数直觉开始，再逐步进入向量和矩阵。

  [进入第 1 章](chapters/01-foundations.md)

- :material-map-outline:{ .lg .middle } **先看学习路径**

  ---

  如果你担心自己基础不稳，建议先看完整学习路径，明确“先学什么、为什么先学、后面怎样衔接”之后再进入正文。

  [进入学习路径](docs/learning-path.md)

- :material-view-list:{ .lg .middle } **按目录选读**

  ---

  如果你已经具备一些函数、向量或概率基础，可以先浏览章节目录，再按自己的问题跳到最需要的部分。

  [进入章节目录](chapters/README.md)

- :material-book-open-page-variant:{ .lg .middle } **了解教材设计**

  ---

  如果你想先理解这本书为什么这样组织、章节之间怎样衔接、每章分别承担什么作用，可以先看教材总纲。

  [查看教材总纲](docs/book-outline.md)
{: .grid .cards}

## 这本书怎么讲

- **先讲直觉，再讲符号**

  ---

  优先帮助你理解公式在描述什么，再进入形式化表达。

- **尽量先图示，再抽象**

  ---

  函数、向量、距离、变化率、梯度等抽象概念都会尽量先用图示建立直觉。

- **尽量先观察，再下定义**

  ---

  让读者通过可执行代码观察数值变化，再回到定义、公式与推导。

- **章节之间有明确主线**

  ---

  从函数到向量，从矩阵到微积分，再到概率统计和模型理解，逐步推进。
{: .grid .cards}

## 第一次阅读建议

<span class="chapter-badge">推荐顺序</span> 第 1 章 -> 第 2 章 -> 第 3 章 -> 第 4 章

<p class="reading-tip">如果你是第一次系统学习机器学习数学，这四章构成最关键的起步阶段。它们会先帮你建立“读符号、看关系、理解表示”的底层能力，后面遇到微积分、概率统计和模型训练时，阅读负担会明显下降。</p>

## 章节主线

1. 数学准备与公式阅读
2. 函数、图像与变化率
3. 向量与几何直觉
4. 矩阵与线性变换
5. 特征值、特征向量与奇异值分解
6. 一元微积分基础
7. 多元微积分与梯度
8. 优化方法
9. 概率论基础
10. 随机变量与常见分布
11. 统计学基础与估计
12. 线性模型中的数学
13. 神经网络的数学基础
14. 通过模型复盘数学

## 站点说明

- 在线阅读地址：`https://albertandking.github.io/math/`
- 本地预览命令：`uv run python scripts/build_site_docs.py` 后执行 `uv run mkdocs serve`
- 静态构建命令：`uv run python scripts/build_site_docs.py` 后执行 `uv run mkdocs build --strict`
- GitHub Actions 工作流：`.github/workflows/deploy-pages.yml`

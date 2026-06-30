# 机器学习数学教材

<div class="page-hero" markdown="1">
<p class="page-kicker">面向数学基础较弱学习者的机器学习数学教材</p>

一套帮助你从**直觉、图示、代码与公式**四条线索中，逐步建立机器学习所需数学理解的中文教材。

本教材希望把“能读懂公式”和“能理解模型”放在同一条学习路径里推进：先讲清直觉，再用图示帮助理解，再用 Python 小实验观察现象，最后把关键关系稳定地写成 LaTeX 公式。

第一次阅读时，建议先阅读[前言](docs/preface.md)，再按**第 1 章到第 4 章**的顺序学习。起步阶段的重点不是尽快接触复杂模型，而是先把**公式阅读、函数视角、向量表示和矩阵表达**这套基础语言真正建立起来。

<div class="hero-actions">
  <a class="md-button md-button--primary" href="chapters/01-foundations.md">从第 1 章开始</a>
  <a class="md-button" href="docs/learning-path.md">先看学习路径</a>
  <a class="md-button" href="chapters/README.md">浏览章节目录</a>
</div>
</div>

## 如何开始

<div class="entry-grid">
  <a class="entry-card" href="docs/preface.md">
    <strong>第一次系统学习</strong>
    <span>先读前言，再从第 1 章进入，按最稳妥的顺序起步。</span>
  </a>
  <a class="entry-card" href="docs/learning-path.md">
    <strong>基础还不够稳</strong>
    <span>先看学习路径，明确先学什么、为什么先学、后面怎样衔接。</span>
  </a>
  <a class="entry-card" href="chapters/README.md">
    <strong>带着问题查书</strong>
    <span>先看章节目录，再按主题或模型定位到最需要的那一章。</span>
  </a>
  <a class="entry-card" href="docs/chapter-dependency-map.md">
    <strong>阅读中途卡住</strong>
    <span>先修地图会告诉你当前该回补哪条基础主线。</span>
  </a>
</div>

## 适合谁读与收获

<div class="panel-grid">
  <div class="info-panel" markdown="1">
  <strong>适合谁读</strong>

  - 数学基础较弱，尤其缺少系统大学数学训练的学生
  - 想学机器学习，但一看到公式就容易畏难的自学者
  - 希望先建立直觉、再逐步进入形式化表达的读者
  </div>
  <div class="info-panel" markdown="1">
  <strong>你会得到什么</strong>

  - 从“看不懂公式”过渡到“能读懂**模型表达**”
  - 从单个变量过渡到**向量、矩阵、梯度、概率与优化**
  - 通过**图示、代码和小例子**，把抽象数学变成可观察的对象
  - 建立从基础篇到进阶篇的连续学习路径
  </div>
</div>

## 这本书怎么讲

- **先讲直觉，再讲符号**：优先帮助你理解公式在描述什么，再进入形式化表达。
- **尽量先图示，再抽象**：函数、向量、距离、变化率、梯度等抽象概念都会尽量先用图示建立直觉。
- **尽量先观察，再下定义**：让读者通过可执行代码观察数值变化，再回到定义、公式与推导。
- **章节之间有明确主线**：从函数到向量，从矩阵到微积分，再到概率统计、模型理解与进阶主题，逐步推进。

## 第一次阅读建议

如果你不确定自己该选哪条路径，可以先记住一个最稳妥的顺序：**前言 -> 第 1 章 -> 第 2 章 -> 第 3 章 -> 第 4 章**。这条路径的任务，不是尽快接触更多模型，而是先把公式阅读、函数视角、向量表示和矩阵表达这套基础语言真正建立起来。只要前四章读顺，后面进入微积分、概率统计和模型章节时，阅读负担会明显下降。

## 全书结构

<div class="panel-grid panel-grid-tight">
  <div class="info-panel">
    <strong>基础篇</strong>
    <p>第 1 到第 14 章，重点建立公式阅读、表示、优化、概率统计和模型理解这套骨架。</p>
  </div>
  <div class="info-panel">
    <strong>进阶篇</strong>
    <p>第 15 到第 20 章，继续把这套骨架延伸到矩阵微积分、似然、信息论、凸优化、泛化分析和现代结构。</p>
  </div>
</div>

如果你想查看完整章节目录与跳读入口，建议直接进入[章节目录](chapters/README.md)；如果你希望在线阅读，可直接访问[站点首页](https://albertandking.github.io/math/)。

## 站点与构建

- 在线阅读地址：[https://albertandking.github.io/math/](https://albertandking.github.io/math/)
- 本地预览：先运行 `uv run python scripts/build_site_docs.py`，再运行 `uv run mkdocs serve`
- 静态构建：先运行 `uv run python scripts/build_site_docs.py`，再运行 `uv run mkdocs build --strict`
- GitHub Actions 工作流：`.github/workflows/deploy-pages.yml`

# 章节目录

<div class="page-hero page-hero-compact" markdown="1">
本页不是简单的章节清单，而是整本书的阅读导航页。第一次阅读时，它帮助你找到最稳妥的起步顺序；已经有部分基础时，它也能帮助你按主题回到最需要补的那一章。

<div class="hero-actions">
  <a class="md-button md-button--primary" href="01-foundations.md">从第 1 章开始</a>
  <a class="md-button" href="../docs/learning-path.md">先看学习路径</a>
  <a class="md-button" href="../docs/chapter-dependency-map.md">查看先修地图</a>
</div>
</div>

## 三种进入方式

<div class="entry-grid entry-grid-3">
  <a class="entry-card" href="01-foundations.md">
    <strong>第一次系统学习</strong>
    <span>先按第 1 到第 4 章推进，建立公式阅读、函数视角、向量表示和矩阵表达这套基础语言。</span>
  </a>
  <a class="entry-card" href="#完整目录">
    <strong>已经有部分基础</strong>
    <span>直接从下方完整目录按主线定位，再按自己的问题跳读。</span>
  </a>
  <a class="entry-card" href="../docs/chapter-dependency-map.md">
    <strong>读到中途卡住</strong>
    <span>优先查看先修地图，先判断该往回补哪一章、哪条主线。</span>
  </a>
</div>

## 第一次阅读

第一次进入正文时，最容易出现的问题不是“哪一章最难”，而是不确定自己应该先建立哪种数学能力。下面这四章之所以被放在起步阶段，并不是因为它们最简单，而是因为它们共同承担了后续所有章节都要反复调用的基础工作。

<div class="grid cards" markdown>

- **第 1 章 数学准备与公式阅读**

  ---

  解决“看不懂公式在说什么”的问题，是进入后续所有内容的起点。

  [进入第 1 章](01-foundations.md)

- **第 2 章 函数、图像与变化率**

  ---

  建立函数视角，开始理解变化率、割线和导数直觉。

  [进入第 2 章](02-functions-and-change.md)

- **第 3 章 向量与几何直觉**

  ---

  从单个数字过渡到成组特征，理解距离、方向、点积与相似性。

  [进入第 3 章](03-vectors-and-geometry.md)

- **第 4 章 矩阵与线性变换**

  ---

  继续把向量思维拓展到矩阵和线性映射，为后续模型表达打基础。

  [进入第 4 章](04-matrices-and-transformations.md)

</div>

## 完整目录

如果你已经完成前四章，或者本来就带着某个明确问题进入这本书，那么下面这份完整目录可以帮助你按主题定位。阅读时不必把它当成孤立章节列表，而应把它看成一条逐步展开的主线：从数学表达走向数据表示，再走向变化、优化、概率统计，最后回到具体模型，并继续进入第 15 到第 20 章的进阶篇。

<div class="grid cards" markdown>

- **第 1 章 数学准备与公式阅读**  
  [阅读](01-foundations.md)

- **第 2 章 函数、图像与变化率**  
  [阅读](02-functions-and-change.md)

- **第 3 章 向量与几何直觉**  
  [阅读](03-vectors-and-geometry.md)

- **第 4 章 矩阵与线性变换**  
  [阅读](04-matrices-and-transformations.md)

- **第 5 章 特征值、特征向量与奇异值分解**  
  [阅读](05-eigenvalues-and-svd.md)

- **第 6 章 一元微积分基础**  
  [阅读](06-single-variable-calculus.md)

- **第 7 章 多元微积分与梯度**  
  [阅读](07-multivariable-calculus.md)

- **第 8 章 优化方法**  
  [阅读](08-optimization.md)

- **第 9 章 概率论基础**  
  [阅读](09-probability-basics.md)

- **第 10 章 随机变量与常见分布**  
  [阅读](10-random-variables-and-distributions.md)

- **第 11 章 统计学基础与估计**  
  [阅读](11-statistics-and-inference.md)

- **第 12 章 线性模型中的数学**  
  [阅读](12-linear-models.md)

- **第 13 章 神经网络的数学基础**  
  [阅读](13-neural-network-math.md)

- **第 14 章 通过模型复盘数学**  
  [阅读](14-math-review-through-models.md)

- **第 15 章 矩阵微积分与自动求导**  
  [阅读](15-matrix-calculus-and-autodiff.md)

- **第 16 章 最大似然、最大后验与概率建模**  
  [阅读](16-likelihood-bayes-and-probabilistic-modeling.md)

- **第 17 章 信息论基础**  
  [阅读](17-information-theory.md)

- **第 18 章 凸优化与约束优化**  
  [阅读](18-convex-and-constrained-optimization.md)

- **第 19 章 泛化、正则化与偏差-方差**  
  [阅读](19-generalization-regularization-and-bias-variance.md)

- **第 20 章 卷积、序列与注意力的数学入口**  
  [阅读](20-convolutions-sequences-and-attention.md)

</div>

## 阅读方式建议

- 零基础读者：先按第 1 章到第 4 章顺序推进，把最基本的数学语言读顺，再继续进入微积分、概率统计和模型部分
- 进入单章之后：先读“本章导读”和“直觉解释”，再结合“图示理解”和“Python 小实验”建立感受，最后回到公式、推导与模型联系去收束理解
- 带着具体问题查书：先定位“与机器学习的联系”或“本章知识结构”，再回到前面的核心概念与例题补齐需要的数学

## 每章统一模板

每章都尽量按同一套结构展开：本章导读 → 学习目标 → 本章为什么重要 → 先修知识清单 → 直觉解释 → 核心概念 → 例题与推导 → 图示理解 → Python 小实验 → 与机器学习的联系 → 常见误区 → 练习题 → 本章知识结构 → 本章小结。这样安排的目的，是让读者既能在正文里连续理解概念，也能在章末重新整理知识脉络。

完整的章节模板与写作规范以[教材总纲](../docs/book-outline.md#chapter-template)为准。



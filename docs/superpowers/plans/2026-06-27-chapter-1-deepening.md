# 第 1 章加深与中文教材风格化 实现计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 把第 1 章试点改写为带编号结构块、分层加深、习题分层、知识结构的中文教材风格，核心阅读体验保持轻证明、先直觉。

**Architecture:** 单文件内容改写（`chapters/01-foundations.md`）+ 极小 CSS 增量（`assets/stylesheets/extra.css` 加 3 个分层徽标类）。结构块复用 Material `admonition`，分层折叠用 `pymdownx.details`，分层徽标用 `attr_list`+`md_in_html` 内联 span。无测试框架；每个任务以 `mkdocs build --strict` 零警告 + 结构性 grep 校验作为验收。

**Tech Stack:** MkDocs + Material 主题；markdown 扩展 `admonition / attr_list / md_in_html / pymdownx.details / pymdownx.arithmatex`。沙箱内 `uv` 离线，统一用已存在的 `.venv` 直接构建。

## Global Constraints

- 设计依据：`docs/superpowers/specs/2026-06-27-chapters-1-5-deepening-design.md`，以其为准。
- 定位不变：核心层保持「先直觉、轻证明」叙述性正文；形式化只进 admonition 盒，不侵入正文流。
- 编号约定：每章内按类型分别连续编号（定义 1.1…、例 1.1…、习题 1.1…）；引用写「类型 章.序号」。
- admonition 映射：定义→`abstract`、性质→`note`、例→`example`、注→`info`；进阶/拓展可折叠用 `???`。
- 构建命令（Windows git bash）：先 `.venv/Scripts/python.exe scripts/build_site_docs.py`，再 `.venv/Scripts/python.exe -m mkdocs build --strict`。验收标准：除 Material 团队的 MkDocs 2.0 横幅外，无 WARNING / 无「does not contain an anchor」。
- `site_docs/` 是构建产物，已被 `.gitignore` 忽略，不提交。
- 工作分支：`deepen-chapters-1-5`。

---

### Task 1：新增分层徽标 CSS

**Files:**
- Modify: `assets/stylesheets/extra.css`（在 `.chapter-pill` 规则之后追加）

**Interfaces:**
- Produces: CSS 类 `.lv-core`、`.lv-ext`、`.lv-adv`，供后续任务在小节标题后以 `<span class="lv-xxx">` 内联使用。

- [ ] **Step 1：追加徽标样式**

在 `assets/stylesheets/extra.css` 中 `.chapter-pill { … }` 规则块之后追加：

```css
.md-typeset .lv-core,
.md-typeset .lv-ext,
.md-typeset .lv-adv {
  display: inline-block;
  margin-left: 0.45rem;
  padding: 0.08rem 0.5rem;
  border-radius: 999px;
  font-size: 0.62rem;
  font-weight: 700;
  vertical-align: middle;
  letter-spacing: 0.02em;
}

.md-typeset .lv-core {
  background: color-mix(in srgb, var(--md-primary-fg-color) 16%, transparent);
  color: var(--md-primary-fg-color);
}

.md-typeset .lv-ext {
  background: color-mix(in srgb, var(--md-accent-fg-color) 16%, transparent);
  color: var(--md-accent-fg-color);
}

.md-typeset .lv-adv {
  background: color-mix(in srgb, var(--md-default-fg-color) 12%, transparent);
  color: var(--md-default-fg-color--light);
}
```

- [ ] **Step 2：构建校验**

Run: `.venv/Scripts/python.exe scripts/build_site_docs.py && .venv/Scripts/python.exe -m mkdocs build --strict`
Expected: 构建成功，无 WARNING（忽略 MkDocs 2.0 横幅）。

- [ ] **Step 3：提交**

```bash
git add assets/stylesheets/extra.css
git commit -m "style: add core/ext/adv level badge classes"
```

---

### Task 2：核心概念改写为编号定义盒 + 编号例题

**Files:**
- Modify: `chapters/01-foundations.md`（`## 核心概念` 与 `## 例题与推导` 两节）

**Interfaces:**
- Consumes: Task 1 的 `.lv-core` 徽标类。
- Produces: 编号块 `定义 1.1`—`定义 1.6`、`例 1.1`—`例 1.4`，供 Task 4 习题与 Task 5 知识结构引用。

- [ ] **Step 1：为 `## 核心概念` 标题加核心徽标，并将四个子概念改为定义盒**

将 `## 核心概念` 改为 `## 核心概念 <span class="lv-core">核心</span>`。保留每个概念现有的直觉叙述段落，在其概念陈述处插入对应定义盒（叙述正文不删除，仅在其前/内嵌入盒）：

```markdown
!!! abstract "定义 1.1（变量）"
    在一个问题中可以取不同数值的量，称为**变量**。一个量是不是变量，取决于当前讨论：在当前关系里它可能取不同值，就把它看作变量。

!!! abstract "定义 1.2（常量）"
    在当前讨论范围内保持固定不变的量，称为**常量**。常量并非「永远不变」，只是在当前这条关系中被暂时看作不变。

!!! abstract "定义 1.3（等式）"
    用等号 \(=\) 连接、表示左右两边相等的式子，称为**等式**。等式既可以表示一个确定的算术结果，也可以表示一种规则性的关系。

!!! abstract "定义 1.4（函数）"
    设对集合 \(D\) 中的每个输入 \(x\)，都按某个确定规则 \(f\) 对应到**唯一**的输出，记作 \(f(x)\)，则称 \(f\) 为定义在 \(D\) 上的**函数**。
```

- [ ] **Step 2：补 `定义 1.5`、`定义 1.6`（自变量/因变量、函数值）**

在「函数」概念叙述之后追加：

```markdown
!!! abstract "定义 1.5（自变量与因变量）"
    在 \(y = f(x)\) 中，可自由取值的 \(x\) 称为**自变量**，随 \(x\) 被确定下来的 \(y\) 称为**因变量**。

!!! abstract "定义 1.6（函数值）"
    当自变量取定某个 \(x_0\) 时，函数 \(f\) 给出的输出 \(f(x_0)\) 称为 \(f\) 在 \(x_0\) 处的**函数值**。
```

- [ ] **Step 3：将 `## 例题与推导` 三个现有例子改为编号 example 盒**

把现有「例 1 / 例 2 / 例 3」三段分别包进编号盒（保留原推导文字，仅改外壳与编号）：

```markdown
!!! example "例 1.1（读懂 \(y = 2x + 1\)）"
    <现有「例 1」正文与函数值表原样保留>

!!! example "例 1.2（用函数描述学习时间与成绩）"
    <现有「例 2」正文原样保留，含 y = 5x + 50>

!!! example "例 1.3（为什么 \(f(x)\) 和 \(y\) 经常一起出现）"
    <现有「例 3」正文原样保留>
```

- [ ] **Step 4：新增 `例 1.4`（读结构化加权和）**

在 `例 1.3` 之后追加：

```markdown
!!! example "例 1.4（读懂 \(z = w_1x_1 + w_2x_2 + b\) 的结构）"
    这条式子不必一次算出结果，先**读结构**：\(x_1, x_2\) 是两个输入，\(w_1, w_2\) 是它们各自的权重，\(b\) 是偏移。整体在说「把每个输入乘以自己的权重，加起来，再加上一个基础值」。例如 \(w_1 = 2, w_2 = 3, b = 1\)，输入 \(x_1 = 1, x_2 = 2\) 时，\(z = 2\times1 + 3\times2 + 1 = 9\)。后面线性模型、神经网络的一层，本质都是在重复这个「加权求和」的读法。
```

- [ ] **Step 5：构建校验 + 编号校验**

Run: `.venv/Scripts/python.exe scripts/build_site_docs.py && .venv/Scripts/python.exe -m mkdocs build --strict`
Run: `grep -c '!!! abstract "定义 1\.' chapters/01-foundations.md`（Expected: `6`）
Run: `grep -c '!!! example "例 1\.' chapters/01-foundations.md`（Expected: `4`）
Expected: 构建无 WARNING。

- [ ] **Step 6：提交**

```bash
git add chapters/01-foundations.md
git commit -m "docs(ch1): number core definitions and worked examples"
```

---

### Task 3：新增拓展层与进阶折叠块

**Files:**
- Modify: `chapters/01-foundations.md`（在 `## 核心概念` 之后、`## 例题与推导` 之前新增 `## 公式阅读拓展` 一节）

**Interfaces:**
- Consumes: Task 1 的 `.lv-ext`/`.lv-adv` 徽标类；定义 1.4（函数）。
- Produces: 「拓展」小节，第 3 章向量章可引用其下标记号铺垫。

- [ ] **Step 1：新增拓展小节（下标、求和、复合）**

在 `定义 1.6` 所在「核心概念」节末尾之后插入：

```markdown
## 公式阅读拓展 <span class="lv-ext">拓展</span>

本节只增加「读法」，不要求计算训练；第一次阅读可略读，后面用到时再回看。

### 1. 下标记号 \(x_i\)

当同一类量有很多个时，常用下标区分：\(x_1, x_2, \ldots, x_n\) 表示第 1 个、第 2 个一直到第 \(n\) 个 \(x\)。\(x_i\) 读作「第 \(i\) 个 \(x\)」，这里 \(i\) 是一个位置编号。第 3 章的向量，正是把这样一组带下标的数打包成一个对象。

### 2. 求和符号 \(\sum\)

把许多项加起来时，用求和符号缩写：

\[
\sum_{i=1}^{n} x_i = x_1 + x_2 + \cdots + x_n
\]

它读作「让 \(i\) 从 1 取到 \(n\)，把每个 \(x_i\) 加起来」。看到 \(\sum\) 不要紧张，它只是「连加」的简写。

### 3. 复合写法 \(f(g(x))\)

\(f(g(x))\) 表示**先**把 \(x\) 交给规则 \(g\) 得到 \(g(x)\)，**再**把这个结果交给规则 \(f\)。阅读顺序是「由内向外」。后面神经网络里「一层接一层」的结构，读法与此一致。
```

- [ ] **Step 2：新增进阶折叠块（函数良定义）**

紧接上面「复合写法」小节之后插入：

```markdown
??? note "进阶 · 可跳过：函数为什么要求「唯一输出」"
    定义 1.4 强调每个输入对应**唯一**输出。若同一个输入 \(x\) 能对应到两个不同的输出，那么这条对应关系就不是函数——因为「给定输入却不能确定输出」会让后面的预测、求导都失去意义。这一「单值 / 良定义」要求，是函数区别于一般「关系」的关键，但第一次阅读只需知道结论即可。
```

- [ ] **Step 3：构建校验 + 结构校验**

Run: `.venv/Scripts/python.exe scripts/build_site_docs.py && .venv/Scripts/python.exe -m mkdocs build --strict`
Run: `grep -c 'lv-ext\|lv-adv\|??? note "进阶' chapters/01-foundations.md`（Expected: ≥ `2`）
Expected: 构建无 WARNING。

- [ ] **Step 4：提交**

```bash
git add chapters/01-foundations.md
git commit -m "docs(ch1): add formula-reading extension and advanced foldout"
```

---

### Task 4：习题分层 + 分层参考答案

**Files:**
- Modify: `chapters/01-foundations.md`（`## 练习题` 节及其 `??? note "参考答案"` 块）

**Interfaces:**
- Consumes: 定义 1.1—1.6、拓展节的 \(\sum\) 读法。
- Produces: 连续编号 `习题 1.1`—`习题 1.8`，分三档。

- [ ] **Step 1：将 `## 练习题` 重写为三档结构**

替换现有练习题列表为：

```markdown
## 练习题

### 基础题

1. **习题 1.1** 在 \(y = 4x + 3\) 中，指出哪些是变量、哪些是常量。
2. **习题 1.2** 计算当 \(x = 0, 1, 2, 3\) 时，\(y = 3x + 2\) 的取值。
3. **习题 1.3** 设 \(f(x) = x + 7\)，求 \(f(1)\)、\(f(5)\)、\(f(10)\)。

### 提高题

4. **习题 1.4** 用自然语言解释 \(y = 5x + 10\) 表示什么样的变化关系。
5. **习题 1.5** 把「成绩 = 每多学 1 小时加 6 分，基础分 40」写成 \(y = ax + b\) 的形式，指出 \(a, b\)。
6. **习题 1.6** 读出 \(\sum_{i=1}^{3} x_i\) 的含义，并在 \(x_1 = 2, x_2 = 5, x_3 = 1\) 时求其值。

### 思考题（选做）

7. **习题 1.7** 举一个生活中的例子，写成「输出 = 某个关于输入的函数」的形式。
8. **习题 1.8** 解释为什么「同一个输入对应两个不同输出」就不能叫函数（可参考进阶折叠块）。
```

- [ ] **Step 2：更新 `参考答案` 折叠块为 8 题分层答案**

替换现有 `??? note "参考答案"` 内容为：

```markdown
??? note "参考答案"
    **基础题**

    1. 习题 1.1：变量是 \(x, y\)；常量是 \(4\) 和 \(3\)。
    2. 习题 1.2：\(x=0\to2\)，\(x=1\to5\)，\(x=2\to8\)，\(x=3\to11\)。
    3. 习题 1.3：\(f(1)=8\)，\(f(5)=12\)，\(f(10)=17\)。

    **提高题**

    4. 习题 1.4：每当输入 \(x\) 增加 1，输出 \(y\) 增加 5；\(x=0\) 时仍有基础值 10。
    5. 习题 1.5：\(a = 6\)，\(b = 40\)，即 \(y = 6x + 40\)。
    6. 习题 1.6：表示 \(x_1 + x_2 + x_3\)，即「把三个数加起来」；代入得 \(2 + 5 + 1 = 8\)。

    **思考题**

    7. 习题 1.7：开放题，答案不唯一。例如：每月话费 = 0.1 × 通话分钟数 + 20，写成 \(y = 0.1x + 20\)。
    8. 习题 1.8：函数要求每个输入对应唯一输出；若一个输入能得到两个不同输出，就无法由输入确定输出，预测与求导都失去依据，因此它只是「关系」而不是函数。
```

- [ ] **Step 3：构建校验 + 编号校验**

Run: `.venv/Scripts/python.exe scripts/build_site_docs.py && .venv/Scripts/python.exe -m mkdocs build --strict`
Run: `grep -c '习题 1\.' chapters/01-foundations.md`（Expected: `16`，正文 8 + 答案 8）
Expected: 三档标题 `### 基础题 / ### 提高题 / ### 思考题（选做）` 均存在；构建无 WARNING。

- [ ] **Step 4：提交**

```bash
git add chapters/01-foundations.md
git commit -m "docs(ch1): tier exercises into basic/advanced/thinking with answers"
```

---

### Task 5：新增「本章知识结构」+ 最终验收

**Files:**
- Modify: `chapters/01-foundations.md`（在 `## 本章小结` 之前新增 `## 本章知识结构`）

**Interfaces:**
- Consumes: 定义 1.1—1.6。
- Produces: 章末知识结构表 + 知识脉络。

- [ ] **Step 1：在 `## 本章小结` 之前插入知识结构节**

```markdown
## 本章知识结构

| 概念 | 一句话核心 | 在机器学习中的角色 |
| --- | --- | --- |
| 变量（定义 1.1） | 可取不同值的量 | 对应数据中的特征或模型输入 |
| 常量（定义 1.2） | 当前暂时固定的量 | 模型中固定的设定值 |
| 函数（定义 1.4） | 输入到输出的确定规则 | 模型本身就是一个函数 |
| 参数 \(w, b\) | 决定函数形状与位置的量 | 训练的本质就是调整参数 |

知识脉络：

- 用**字母**为量命名 → 区分**变量 / 常量**
- 把量之间的关系写成**等式** → 当它表达「输入定、输出定」时就是**函数**
- 函数中可调的量是**参数** → 后续模型与训练都建立在这条线索上
```

- [ ] **Step 2：最终全章结构校验**

Run: `.venv/Scripts/python.exe scripts/build_site_docs.py && .venv/Scripts/python.exe -m mkdocs build --strict`
Run: `grep -nE '^## ' chapters/01-foundations.md`
Expected: 依次包含 本章导读 / 学习目标 / 本章为什么重要 / 先修知识清单 / 直觉解释 / 核心概念 / 公式阅读拓展 / 例题与推导 / 图示理解 / Python 小实验 / 配图建议 / 与机器学习的联系 / 常见误区 / 练习题 / 本章知识结构 / 本章小结；构建无 WARNING。

- [ ] **Step 3：人工渲染抽查**

Run: `.venv/Scripts/python.exe -m mkdocs serve`（本地预览），逐项确认：定义/例盒正常渲染、`核心/拓展/进阶`徽标在浅/深色模式均清晰、进阶块默认收起、习题三档显示、LaTeX 正常。确认后停止预览。

- [ ] **Step 4：提交**

```bash
git add chapters/01-foundations.md
git commit -m "docs(ch1): add chapter knowledge-structure summary"
```

---

## Self-Review

- **Spec coverage**：A1 编号体系→Task 2/4；A2 分层加深（徽标+折叠）→Task 1/2/3；A3 习题分层→Task 4；A4 小结与知识结构→Task 5；A5 正式化措辞→Task 2/3 定义盒内措辞；B 第 1 章蓝图各项（核心定义、拓展三项、进阶折叠、习题分层、知识结构表）均有任务。第 7 节验收标准 1–6 分别由 Task 2/4、Task 1-3、Task 4、Task 5、各任务构建步、核心层保留约定覆盖。
- **Placeholder scan**：定义盒中 `<现有「例 N」正文…保留>` 是「保留既有文字」指令，非待填占位；其余均给出可直接粘贴的实际内容。
- **一致性**：徽标类 `.lv-core/.lv-ext/.lv-adv` 在 Task 1 定义、Task 2/3 使用，命名一致；编号「定义 1.x / 例 1.x / 习题 1.x」全程一致。

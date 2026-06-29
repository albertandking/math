# [OPEN] Debug Session: mathjax-first-load

## 问题概述
- 现象：首次打开网页时，部分公式没有渲染出来；刷新网页后，公式恢复正常渲染。
- 目标：确认首次加载阶段是 `MathJax` 初始化、事件触发时机、脚本加载顺序，还是局部页面替换流程导致首屏漏渲染。

## 当前假设
1. `DOMContentLoaded` 触发时 `MathJax.startup.promise` 尚未稳定，导致首次 `typesetPromise()` 没有真正覆盖到页面里的公式节点。
2. Material 的首屏/instant navigation 生命周期与现有 `document$` 订阅顺序不匹配，导致第一次进入页面时没有触发有效渲染，但刷新后走了另一条更完整的初始化路径。
3. `typesetClear()` 在首次加载阶段调用过早，清掉了还未完成初始化的数学节点状态，导致第一次渲染被跳过。
4. 页面中部分公式位于 admonition、HTML 容器或动态替换区域里，第一次 `typesetPromise()` 扫描范围不足，刷新后完整 DOM 稳定才被扫描到。
5. MathJax CDN 脚本首次加载完成前，页面已尝试执行渲染；刷新后因为缓存命中，脚本可更快就绪，所以看起来“刷新一次就好了”。

## 计划
1. 给 `assets/javascripts/mathjax.js` 添加最小化调试日志上报。
2. 本地启动站点并复现“首次打开未渲染，刷新后恢复”的过程。
3. 根据日志判断是脚本就绪时机、事件顺序还是扫描范围问题。
4. 在证据明确后再做最小修复。

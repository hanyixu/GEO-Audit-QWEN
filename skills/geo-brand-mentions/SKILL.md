---
name: geo-brand-mentions
description: CN brand authority scanner for AI visibility. Uses China platforms (Baike/WeChat/Douyin/XHS/etc.) and outputs zh-CN recommendations.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - WebFetch
  - Write
---

# Brand Mentions & Authority Signals (China-First)

## Goal

Evaluate a brand’s CN internet “discoverability + retrievability + verifiability + re-citable content” footprint, and produce an actionable fill-the-gaps plan. Focus areas:

- **Entity foundation**: Baidu Baike / authoritative directories as “baseline facts”
- **Long-form deposits**: WeChat Official Accounts (公众号) and WeChat Search (搜一搜)
- **High-interaction ecosystems**: Xiaohongshu, Douyin, Kuaishou, Bilibili, Zhihu, Weibo
- **Discussion & risk**: Baidu Zhidao, Tieba

> Note: Many CN platforms have strict anti-scraping controls. This skill prioritizes **search-based verification + recommendations** over brittle automated crawling.

---

## Suggested CN Platform Weighting Model

| 平台 | 权重 | 关注点 |
|---|---:|---|
| 百度百科 | 18% | 实体打底、基础事实一致性 |
| 微信公众号/搜一搜 | 18% | 长文沉淀、可引用内容块 |
| 小红书 | 14% | 种草/对比/避坑影响 |
| 抖音 | 12% | 短视频可发现性与社证 |
| 快手 | 8% | 场景化内容补充 |
| B站 | 10% | 深度测评/教程/对比 |
| 知乎 | 10% | 高意图问题占位与可引用回答 |
| 微博 | 5% | 媒体/大V提及与传播 |
| 百度知道/贴吧 | 5% | 基础问答与风险点管理 |

Total: `Brand_Authority_Score_CN = Σ(platform_score * platform_weight)`

Optional vertical add-ons (adjust weights per industry; keep total = 100%):
- Local life: 美团/大众点评, 高德/百度地图
- E-commerce: 淘宝/天猫, 京东, 拼多多, 1688
- B2B/entity validation: 企查查/天眼查, 1688, 行业协会名录
- Tech/knowledge: CSDN, 掘金, 博客园

---

## Procedure

### Step 1: Normalize brand identifiers (canonical “truth set”)

- Brand Chinese name / English name / common abbreviations / common misspellings
- Legal entity name (optional)
- Official website domain
- Industry/category
- Top 3 products/services (canonical naming)

### Step 2: Per-platform checks (Presence + Quality + Third-party)

For each platform, record:
- **Presence**: official account / profile / entry exists?
- **Quality**: does it contain “citable blocks” (definitions, FAQs, specs, comparisons, cases)?
- **Third-party**: independent reviews/discussions/media mentions exist?

Suggested queries (examples):
- Baidu: `[品牌名] 百度百科`, `[品牌名] 公众号`, `[品牌名] 小红书`, `[品牌名] 抖音`, `[品牌名] 快手`, `[品牌名] B站`, `[品牌名] 知乎`, `[品牌名] 微博`, `[品牌名] 百度知道`, `[品牌名] 贴吧`
- Optional: Sogou Weixin search for historical OA articles (环境允许时)

### Step 3: Sentiment & risk themes

For Q&A/discussion platforms and social, do a fast triage: Positive / Neutral / Negative. Extract “high-frequency negative themes” as must-fix items.

### Step 4: Platform-specific actions + 30-day plan

Prioritization:
- First: Baike + WeChat + website consistency (entity foundation)
- Second: high-intent Q&A occupancy (Zhihu / Xiaohongshu)
- Third: “citable info blocks” inside video ecosystems (Douyin / Bilibili)

---

## Output (MUST be in Simplified Chinese)

Generate `GEO-BRAND-MENTIONS.md` in **中文（简体）** using this template:

```markdown
# 品牌权威与提及报告（CN）：[品牌名]

**分析日期：** [Date]
**品牌：** [Brand Name]
**官网：** [URL]
**行业：** [Industry]

---

## 品牌权威分数： [X]/100（[强势/较强/一般/偏弱/很弱]）

### 平台分解

| 平台 | 分数 | 权重 | 加权 | 状态 |
|---|---:|---:|---:|---|
| 百度百科 | [X]/100 | 18% | [X] | [完整/一般/缺失] |
| 微信公众号 | [X]/100 | 18% | [X] | [活跃/一般/缺失] |
| 小红书 | [X]/100 | 14% | [X] | [活跃/一般/缺失] |
| 抖音 | [X]/100 | 12% | [X] | [活跃/一般/缺失] |
| 快手 | [X]/100 | 8% | [X] | [活跃/一般/缺失] |
| B站 | [X]/100 | 10% | [X] | [活跃/一般/缺失] |
| 知乎 | [X]/100 | 10% | [X] | [活跃/一般/缺失] |
| 微博 | [X]/100 | 5% | [X] | [活跃/一般/缺失] |
| 百度知道/贴吧 | [X]/100 | 5% | [X] | [健康/一般/风险] |
| **总分** | | | **[X]/100** | |

---

## 平台明细（每个平台至少给 3 条“可执行动作”）

### [平台名]（[X]/100）

**存在性：** [有/无]
**第三方内容：** [多/少/无]
**可引用内容块：** [强/一般/弱]
**关键发现：**
- ...

---

## 30 天行动计划

### 第 1 周（实体打底）
- [ ] 百度百科/官网信息一致性
- [ ] 官网补齐关于我们/资质/联系方式/更新时间
- [ ] Schema `sameAs` 补齐平台链接

### 第 2 周（高意图问题占位）
- [ ] 知乎/小红书：怎么选/对比/避坑/价格/售后

### 第 3 周（视频生态）
- [ ] 抖音/快手：短视频矩阵 + 字幕关键词
- [ ] B站：测评/教程/对比长视频

### 第 4 周（复盘与扩展）
- [ ] 舆情风险点复盘
- [ ] 迭代 FAQ 与可引用内容块
```


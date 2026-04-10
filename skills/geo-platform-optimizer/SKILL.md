---
name: geo-platform-optimizer
description: CN platform-specific AI optimization — focus on 元宝、豆包、千问 (with CN ecosystem signals)
version: 1.0.0
author: geo-seo-claude-cn
tags: [geo, ai-search, platform-optimization, china, yuanbao, doubao, qwen]
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Write
---

# GEO Platform Optimization (China-First)

## Core Insight

In the Chinese internet, AI assistants / AI search products differ significantly in **source preferences** and **distribution ecosystems**.
The same page can perform very differently across platforms. Platform-level GEO is not optional — it is foundational.

This skill provides checklists and scoring models for the major CN platforms:
- **元宝（腾讯生态）**
- **豆包（字节生态）**
- **千问（阿里生态）**

> Note: Platform crawling/indexing policies can change. This skill uses a robust baseline: **verifiable signals + citability + ecosystem consistency**.

**All final user-facing outputs MUST be in Simplified Chinese (zh-CN)**.

---

## How to Use

1. Collect target URL + industry/category + business type (ToC/ToB/Local Life/E-commerce/SaaS)
2. Evaluate site signals and off-site ecosystem signals per platform checklist
3. Produce per-platform scores (0-100) + gaps + concrete actions
4. Generate `GEO-PLATFORM-OPTIMIZATION.md` in Chinese

---

## Platform 1: 元宝（Tencent ecosystem）

### Source & ecosystem assumptions (practical)

Common verifiable signals in Tencent ecosystem:
- **微信公众号/视频号**（内容沉淀与可复用引用段落）
- **搜一搜**可检索性（标题、摘要、结构清晰度）
- **权威机构/媒体**的第三方背书（可验证性与信任）

### Optimization checklist

1. **WeChat long-form deposits**: Publish 10+ citable long articles covering brand/product definitions, FAQ, comparisons, cases, specs, and pricing positioning.
2. **Q&A structure**: Use question headings (H2/H3), then 1–2 sentence direct answers, then details.
3. **Citable blocks**: For each core topic, prepare 2–3 blocks of 100–180 Chinese characters, fact-dense and self-contained.
4. **Entity consistency**: Website, WeChat, Baike, social profiles share consistent naming, entity info, and contacts.
5. **sameAs completeness**: Add WeChat/Channels/Weibo/Zhihu/XHS/Douyin links into `Organization`/`LocalBusiness` schema `sameAs` where applicable.
6. **Freshness + authorship**: Show publish date, updated date, author/editor, credentials, and sources on key pages.

### Scoring (0-100)

| 维度 | 分值 | 评分方法 |
|---|---:|---|
| 公众号内容覆盖 | 25 | 10+篇=25，5-9篇=15，<5=5 |
| 可引用结构（问答+直接回答） | 20 | 多处稳定=20，部分=10，缺失=0 |
| 实体口径一致性 | 20 | 高一致=20，轻微偏差=10，混乱=0 |
| sameAs 与实体 Schema | 15 | 完整=15，部分=8，缺失=0 |
| 第三方背书可验证性 | 10 | 多来源=10，少量=5，无=0 |
| 更新/作者/来源 | 10 | 完整=10，部分=5，缺失=0 |

---

## Platform 2: 豆包（ByteDance ecosystem）

### Source & ecosystem assumptions (practical)

Strong signals in ByteDance ecosystem often come from:
- **抖音**（短视频：教程/对比/测评/清单）
- **图文与短内容分发**（标题与摘要的关键词覆盖）
- **讨论与复述**（第三方测评与用户口碑内容）

### Optimization checklist

1. **Video matrix**: Tutorials / comparisons / checklists / “pitfalls to avoid”. Titles include “category keyword + brand keyword”.
2. **Subtitles & spoken facts**: Explicit specs, conclusions, and use-cases (so content can be quoted).
3. **Bio / link card**: Standardize links to official site, customer support, core landing pages, and FAQ.
4. **UGC + third-party reviews**: Encourage real user experiences compliantly; prioritize comparison/review/case-style third-party content.
5. **Consistency**: Names, versions, and pricing positioning match the official site.
6. **Landing page citability**: Landing pages must have “direct answers + structured info (tables/lists)”.

### Scoring (0-100)

| 维度 | 分值 | 评分方法 |
|---|---:|---|
| 内容矩阵覆盖（4类） | 25 | 完整=25，部分=15，缺失=0 |
| 字幕/口播事实密度 | 20 | 高=20，中=10，低=0 |
| 简介与链接信息卡 | 15 | 完整=15，部分=8，缺失=0 |
| 第三方测评/UGC | 20 | 多=20，少=10，无=0 |
| 口径一致性 | 10 | 一致=10，部分=5，混乱=0 |
| 落地页可引用结构 | 10 | 强=10，中=5，弱=0 |

---

## Platform 3: 千问（Alibaba ecosystem）

### Source & ecosystem assumptions (practical)

Common verifiable signals in Alibaba ecosystem:
- **结构化与可验证事实**（参数、规格、对比表、FAQ、来源引用）
- **电商/产品信息一致性**（若是电商/品牌）
- **权威来源引用**（行业协会、标准、媒体、公开信息）

### Optimization checklist

1. **Structured product/service facts**: Put specs, pricing ranges, and use-cases into tables; use comparison tables for competitors.
2. **Definitions & terminology boxes**: Use definition sentences: `**术语**是...`.
3. **Verifiable data & sources**: Provide numbers/dates and cite public sources.
4. **FAQ coverage**: 10+ high-intent FAQs (how to choose, comparison, reliability, warranty, after-sales, price, compatibility).
5. **Entity consistency**: Website vs Baike/social is consistent (name, entity, contacts, product naming).
6. **Technical crawlability**: SSR/readable HTML, sane robots, sitemap, canonical correctness.

### Scoring (0-100)

| 维度 | 分值 | 评分方法 |
|---|---:|---|
| 表格/对比结构化 | 20 | 强=20，中=10，弱=0 |
| FAQ 覆盖 | 20 | 10+=20，5-9=10，<5=0 |
| 数据与来源可验证 | 20 | 多=20，少=10，无=0 |
| 定义与术语清晰 | 10 | 多处=10，少量=5，缺失=0 |
| 实体口径一致性 | 15 | 高=15，中=8，低=0 |
| 技术可抓取基础 | 15 | 强=15，中=8，弱=0 |

---

## Cross-platform actions (helpful everywhere)

1. **Entity foundation**: Baidu Baike + complete website “About / credentials / contacts / timeline”.
2. **sameAs**: Fill `sameAs` links for official social/content presences.
3. **Citable blocks**: 100–180 Chinese character fact-dense blocks per core topic.
4. **Structure**: tables, lists, FAQ, definition sentences.
5. **Consistency**: brand/product/version/pricing/after-sales messaging consistent.

---

## Output Format (Chinese required)

Generate `GEO-PLATFORM-OPTIMIZATION.md` in **中文（简体）**:

```markdown
# GEO 平台优化报告（CN）— [Domain]
Date: [Date]

## 平台得分
| 平台 | 得分 | 状态 |
|---|---:|---|
| 元宝（腾讯生态） | XX/100 | [强/中/弱] |
| 豆包（字节生态） | XX/100 | [强/中/弱] |
| 千问（阿里生态） | XX/100 | [强/中/弱] |

状态阈值：强=70+，中=40-69，弱=0-39

## 平台明细
### 元宝（腾讯生态）
- 得分：XX/100
- 关键缺口：
  - ...
- 优先动作（按影响排序）：
  1. ...

### 豆包（字节生态）
...

### 千问（阿里生态）
...

## 优先行动计划
### 本周（Quick Wins）
- ...

### 本月（Medium-Term）
- ...

### 本季度（Strategic）
- ...
```


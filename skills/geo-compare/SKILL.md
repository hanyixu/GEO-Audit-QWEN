---
name: geo-compare
description: >
  Monthly delta tracking and progress reporting for GEO clients. Compares two
  GEO audits (baseline vs. current), calculates score improvements across all
  categories, tracks action item completion, and generates a "here's your progress"
  client report. Use when user says "compare", "delta", "monthly report", "progress",
  "confronta", "progressi", "report mensile", or when running a monthly client check-in.
version: 1.0.0
tags: [geo, business, delta, monthly, reporting, client, progress]
allowedTools:
  - Read
  - Write
  - Bash
  - Glob
---

# GEO Monthly Delta Report Generator

## Purpose

The single most powerful retention tool for a GEO agency: show clients **exactly**
what improved since they started working with you. Every point gained on the GEO
score is proof of value. This skill generates the "here's your progress" report.

## China-First Requirements

- **Primary AI platforms (CN)**: 豆包、元宝、通义千问、Kimi、DeepSeek、百度 AI 搜索
- **Secondary/global platforms (lower weight, optional)**: ChatGPT, Claude, Gemini, Perplexity, Bing Copilot

**All final user-facing outputs MUST be in Simplified Chinese (zh-CN)**.

---

## Commands

```
/geo compare <domain>
/geo compare <baseline-file> <current-file>
/geo compare electron-srl.com --month march-2026
```

**Examples:**
```
/geo compare electron-srl.com
/geo compare ~/.geo-prospects/audits/electron-srl.com-2026-01-15.md ~/.geo-prospects/audits/electron-srl.com-2026-03-12.md
```

---

## Workflow

### Step 1: Find Audit Files

If only domain is provided:
1. Look in `~/.geo-prospects/audits/` for files matching `<domain>-*.md`
2. Sort by date
3. Use oldest as baseline, newest as current
4. If only one file exists: use it as baseline, run a fresh quick audit as current
5. If no files exist: suggest running `/geo prospect audit <domain>` first

### Step 2: Parse Both Audits

Extract from each audit file:
- Overall GEO Score
- Per-category scores (6 categories)
- Per-platform scores (5 platforms)
- AI crawler status (14 crawlers)
- Critical issues list
- Action items list with status

### Step 3: Calculate Deltas

For each metric:
- Delta = Current - Baseline
- Trend = ▲ (improved), ▼ (declined), ── (unchanged)
- Color coding in report: green (+), red (-), gray (=)

### Step 4: Generate Monthly Report

Output to `~/.geo-prospects/reports/<domain>-monthly-<date>.md`

---

## Report Template

Generate the following document:

```markdown
# GEO 月度进展报告（CN 优先）
## [公司/品牌名] — [月份 年份]

**报告周期：** [BASELINE DATE] → [CURRENT DATE]
**出品方：** [服务方/机构名]
**报告编号：** GEO-MONTHLY-[DOMAIN]-[YYMMDD]

---

## 执行摘要

[用 2-3 句话说明：本月提升点、总体趋势、下月优先聚焦。]

Example: "Electron Srl's GEO Score improved from 32 to 44 this month (+12 points),
placing the site firmly in the 'Below Average' tier and on track to reach 'Moderate'
by May. The biggest wins were AI crawler access (+3 crawlers now allowed) and schema
implementation (+Organization and LocalBusiness schemas live). Next month's focus is
content citability — the highest-weighted remaining gap."

---

## GEO 总分变化

```
总体 GEO 评分

  Baseline   [▓▓▓▓░░░░░░░░░░░░░░░░]  32/100  (Critical)
  Current    [▓▓▓▓▓▓▓▓░░░░░░░░░░░░]  44/100  (Below Average)
  Change     ▲ +12 points (+37.5%)

  目标：     第 6 个月达到 65/100（是否在轨：✓/✗）
```

---

## 分项分数：前后对比

| Category | Baseline | Current | Change | Trend |
|----------|---------|---------|--------|-------|
| AI Citability & Visibility | [X]/100 | [X]/100 | [+/-X] | [▲/▼/──] |
| Brand Authority Signals | [X]/100 | [X]/100 | [+/-X] | [▲/▼/──] |
| Content Quality & E-E-A-T | [X]/100 | [X]/100 | [+/-X] | [▲/▼/──] |
| Technical Foundations | [X]/100 | [X]/100 | [+/-X] | [▲/▼/──] |
| Structured Data | [X]/100 | [X]/100 | [+/-X] | [▲/▼/──] |
| Platform Optimization | [X]/100 | [X]/100 | [+/-X] | [▲/▼/──] |
| **TOTAL** | **[X]/100** | **[X]/100** | **[+/-X]** | **[▲/▼]** |

---

## 平台就绪度：前后对比（CN 优先）

| AI Platform | Baseline | Current | Change |
|-------------|---------|---------|--------|
| 豆包 | [X]/100 | [X]/100 | [+/-X] |
| 元宝 | [X]/100 | [X]/100 | [+/-X] |
| 通义千问 | [X]/100 | [X]/100 | [+/-X] |
| 百度 AI 搜索 | [X]/100 | [X]/100 | [+/-X] |
| Kimi / DeepSeek（如适用） | [X]/100 | [X]/100 | [+/-X] |

> 可选附录（如做出海/海外业务）：ChatGPT / Claude / Gemini / Perplexity / Bing Copilot

---

## AI 爬虫访问变化

| Crawler | Baseline | Current | Change |
|---------|---------|---------|--------|
| GPTBot (ChatGPT) | Blocked/Allowed | Blocked/Allowed | ✓ Fixed / No change |
| ClaudeBot (Anthropic) | Blocked/Allowed | Blocked/Allowed | ✓ Fixed / No change |
| PerplexityBot | Blocked/Allowed | Blocked/Allowed | ✓ Fixed / No change |
| Google-Extended (Gemini) | Blocked/Allowed | Blocked/Allowed | ✓ Fixed / No change |
| Bingbot | Blocked/Allowed | Blocked/Allowed | ✓ Fixed / No change |

[Show only crawlers that changed, or all if few crawlers.]

---

## 行动计划进展

### Quick Wins（速效项）— 进展

| # | Action | Assigned | Status | Impact |
|---|--------|---------|--------|--------|
| 1 | Allow all AI crawlers in robots.txt | Client dev | ✅ Done | +3 crawlers |
| 2 | Add Organization schema to homepage | Client dev | ✅ Done | Schema score +15 |
| 3 | Create llms.txt | Agency | ✅ Done | AI visibility +8 |
| 4 | Add author bylines to all articles | Client content | 🔄 In Progress | — |
| 5 | Fix meta descriptions (47 pages missing) | Client dev | ❌ Not started | — |

**Quick Wins 完成：** [X]/[Y]（[%]）

### 中期项（本月）— 进展

| # | Action | Target Month | Status |
|---|--------|-------------|--------|
| 1 | Rewrite top 10 pages with Q&A structure | Month 2 | 🔄 3/10 done |
| 2 | E-E-A-T: Create author pages | Month 2 | ❌ Not started |
| 3 | Register Bing Webmaster Tools | Month 1 | ✅ Done |
| 4 | Implement IndexNow | Month 2 | 🔄 In Progress |

### 战略项（本季度）— 进展

| # | Action | Target | Status |
|---|--------|--------|--------|
| 1 | Wikipedia entity creation | Month 4 | 📋 Planned |
| 2 | YouTube channel launch | Month 3 | 📋 Planned |
| 3 | Reddit presence (industry subs) | Month 3 | 📋 Planned |

---

## 本月成果（要写得“可感知、可验证”）

> Use this section to celebrate — clients need to see the value clearly.

✅ **[WIN 1]:** [Specific, tangible result — e.g., "GPTBot and ClaudeBot are now allowed. ChatGPT can now crawl and cite your content."]
✅ **[WIN 2]:** [e.g., "Organization schema implemented on homepage. Your brand entity is now machine-readable."]
✅ **[WIN 3]:** [e.g., "llms.txt created and deployed at electron-srl.com/llms.txt — one of only ~12% of sites in your industry to have this."]

---

## 本月新增问题/机会点

> Issues found in current audit that weren't in baseline.

⚠️ **[ISSUE 1]:** [What it is, what it means, how we'll fix it]
⚠️ **[ISSUE 2]:** [What it is, what it means, how we'll fix it]

---

## 下月重点

### Priority Actions for [NEXT MONTH]:

| Priority | Action | Owner | Expected Impact |
|----------|--------|-------|----------------|
| 1 | [Highest ROI action] | [Agency/Client] | +[X] GEO points |
| 2 | [Second priority] | [Agency/Client] | +[X] GEO points |
| 3 | [Third priority] | [Agency/Client] | +[X] GEO points |

**Target GEO Score next month:** [CURRENT + estimated gain]/100

---

## 6-Month Trajectory

| Month | Date | Score | Delta | Key Achievement |
|-------|------|-------|-------|----------------|
| Baseline | [Date] | [Score] | — | Initial audit |
| Month 1 | [Date] | [Score] | [+X] | Quick wins implemented |
| Month 2 | [Date] | [Score] | [+X] | *Current month* |
| Month 3 | [Date] | — | — | Content citability |
| Month 4 | — | — | — | Brand authority |
| Month 5 | — | — | — | Strategic initiatives |
| Month 6 | — | **Target: [X]** | — | Full review |

[Only fill rows that have happened. Show projected rows as "—"]

---

## 预估业务影响（保守口径）

Based on the [X]-point improvement this month:

- **AI citation likelihood:** Increased by approximately [X]%
- **Crawlers with access:** [X]/14 → [Y]/14 (better coverage on [platforms])
- **Estimated monthly AI-referred traffic improvement:** +[X]% (conservative)
- **Traffic value at current conversion rates:** +€[X]/month in organic value

*Note: Full traffic impact from GEO changes typically takes 4-8 weeks to materialize
as AI platforms re-index and update their knowledge bases.*

---

*GEO 月度报告 — [公司/品牌名] — [DATE]*
*如需沟通： [CONTACT EMAIL]*
```

---

## Delta Calculation Logic

When parsing two audit files, look for these patterns:

```
Score markers to extract:
- "GEO Score: XX/100"
- "Overall Score: XX"
- "AI Citability: XX/100"
- "Brand Authority: XX/100"
- "Technical: XX/100"
- "Schema: XX/100"
- "Platform: XX/100"
- "Content: XX/100"
- "GPTBot: Allowed/Blocked"
- "ClaudeBot: Allowed/Blocked"
```

If exact scores are not found in audit files, use contextual analysis of the
written findings to estimate approximate scores based on issues described.

---

## Trend Interpretation

| Delta | Trend Symbol | Meaning |
|-------|-------------|---------|
| +5 or more | ▲▲ | Strong improvement |
| +1 to +4 | ▲ | Improvement |
| 0 | ── | No change |
| -1 to -4 | ▼ | Slight decline |
| -5 or more | ▼▼ | Significant decline — needs discussion |

A decline is not necessarily bad — it can mean new issues were discovered in the
fresh audit that weren't visible before. Frame declines as "newly discovered opportunities."

---

## Output

1. Save report to `~/.geo-prospects/reports/<domain>-monthly-<YYYY-MM>.md`
2. Print confirmation with key stats:
   ```
   ✓ Monthly report generated: ~/.geo-prospects/reports/electron-srl.com-monthly-2026-03.md

   SUMMARY:
   GEO Score: 32 → 44 (+12 points) ▲
   Quick wins completed: 3/5 (60%)
   New issues found: 2 (minor)
   On track for Month 6 target: YES (65/100)
   ```
3. Suggest next action: "Share with client or run `/geo report-pdf` for a visual version"

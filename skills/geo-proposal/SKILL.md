---
name: geo-proposal
description: >
  Auto-generate a professional, client-ready GEO service proposal from audit data.
  Creates a full proposal in markdown and PDF including executive summary, findings,
  recommended service packages (Basic/Standard/Premium), pricing, timeline, and terms.
  Use when user says "proposal", "proposta", "offerta", "preventivo", "generate proposal",
  or after completing a GEO audit for a prospect.
version: 1.0.0
tags: [geo, business, proposal, sales, pricing, client]
allowedTools:
  - Read
  - Write
  - Bash
  - Glob
  - WebFetch
---

# GEO Proposal Generator

## Purpose

Generate a fully customized, client-ready GEO service proposal that:
1. Pulls findings directly from the prospect's GEO audit
2. Translates technical gaps into business pain points
3. Presents 3 service tiers with clear pricing
4. Includes a realistic ROI projection
5. Outputs a professional markdown document ready to send

## China-First Requirements

- **Output language**: The proposal MUST be written in Simplified Chinese (zh-CN).
- **Platforms**: Emphasize CN AI assistants and CN ecosystems (豆包/元宝/通义千问/百度 AI 搜索/Kimi/DeepSeek + 微信/小红书/抖音/B站/知乎等). Global platforms are optional add-ons.

---

## Command

```
/geo proposal <domain-or-audit-file> [--tier basic|standard|premium] [--client-name "Name"] [--monthly EUR]
```

**Examples:**
```
/geo proposal electron-srl.com
/geo proposal electron-srl.com --tier standard --client-name "Electron Srl"
/geo proposal ~/.geo-prospects/audits/electron-srl.com-2026-03-12.md
```

---

## Workflow

### Step 1: Load Audit Data

1. Check if `~/.geo-prospects/audits/<domain>*.md` exists
2. If not, suggest running `/geo quick <domain>` first
3. Extract from audit:
   - GEO Score (overall and per-category)
   - Top 3 critical findings
   - Quick wins list
   - Business type
   - Estimated organic traffic impact

### Step 2: Customize the Proposal

Auto-fill proposal template with:
- Company name (from domain or prospect record)
- GEO score and tier label
- 3 most critical pain points (translated to business language)
- Estimated revenue at risk from AI search shift
- Recommended service tier based on score:
  - Score 0-40 → Recommend Premium (critical issues need full attention)
  - Score 41-60 → Recommend Standard (significant gaps, needs monthly work)
  - Score 61-75 → Recommend Basic (solid base, needs monitoring)

### Step 3: Generate Proposal File

Output to `~/.geo-prospects/proposals/<domain>-proposal-<date>.md`
Also update prospect record if it exists in `~/.geo-prospects/prospects.json`

---

## Proposal Template

Generate the following document, filling all `[PLACEHOLDERS]` with real audit data:

---

```markdown
# GEO 优化服务方案（CN 优先）
## [公司/品牌名] — AI 搜索可见度与可引用性提升

**出品方：** [服务方/机构名]
**客户：** [联系人]，[公司/品牌名]
**日期：** [DATE]
**有效期至：** [DATE + 30 DAYS]
**编号：** GEO-PROP-[YYMMDD]-[DOMAIN]

---

## Executive Summary

[公司/品牌名] 所处行业为 [INDUSTRY]，主要服务 [GEOGRAPHY] 的客户。
我们在 [DATE] 对 [DOMAIN] 进行 GEO 审计后，得到综合评分 **[SCORE]/100（[档位]）**。

This means your website currently has [TIER DESCRIPTION — use score interpretation table].
随着 AI 搜索/AI 助手（豆包/元宝/通义千问/百度 AI 搜索等）在用户决策链路中的比重持续提升，这些缺口会直接影响品牌被推荐、被引用与被选择的概率，进而影响线索与成交。

The three most urgent issues are:
1. **[CRITICAL FINDING 1]** — [Business impact in one sentence]
2. **[CRITICAL FINDING 2]** — [Business impact in one sentence]
3. **[CRITICAL FINDING 3]** — [Business impact in one sentence]

我们建议采用 **[方案档位]**（**€[PRICE]/月**），目标是在 90 天内解决关键问题，并在 [INDUSTRY] 领域建立“可验证、可引用、可复述”的 AI 友好信息体系。

---

## 为什么现在必须做 GEO（对 [公司/品牌名] 的意义）

### AI 搜索迁移已经发生

| Metric | Value |
|--------|-------|
| AI-referred traffic growth (2025) | +527% YoY |
| AI traffic conversion vs. organic | 4.4x higher |
| ChatGPT weekly active users | 900M+ |
| Google AI Overviews monthly reach | 1.5B users, 200+ countries |
| Gartner: traditional search traffic drop by 2028 | -50% |
| Marketers investing in GEO today | Only 23% |

**First-mover advantage is real.** Companies that invest in GEO now will
capture the AI search channel before competitors do.

### 你当前的位置（基线）

| Metric | [COMPANY] | Industry Average | Top Performers |
|--------|-----------|------------------|----------------|
| GEO Score | [SCORE]/100 | 45/100 | 75+/100 |
| AI Crawlers Allowed | [X]/14 | 8/14 | 14/14 |
| Brand Mentions (AI platforms) | [STATUS] | Moderate | High |
| Schema Coverage | [STATUS] | Partial | Complete |
| llms.txt | [Yes/No] | 12% have it | 78% have it |

---

## Audit Findings Summary

### GEO Score Breakdown

| Category | Your Score | Weight | Weighted | Priority |
|----------|-----------|--------|---------|----------|
| AI Citability & Visibility | [SCORE]/100 | 25% | [WEIGHTED] | [HIGH/MED/LOW] |
| Brand Authority Signals | [SCORE]/100 | 20% | [WEIGHTED] | [HIGH/MED/LOW] |
| Content Quality & E-E-A-T | [SCORE]/100 | 20% | [WEIGHTED] | [HIGH/MED/LOW] |
| Technical Foundations | [SCORE]/100 | 15% | [WEIGHTED] | [HIGH/MED/LOW] |
| Structured Data | [SCORE]/100 | 10% | [WEIGHTED] | [HIGH/MED/LOW] |
| Platform Optimization | [SCORE]/100 | 10% | [WEIGHTED] | [HIGH/MED/LOW] |
| **TOTAL GEO SCORE** | | | **[SCORE]/100** | **[TIER]** |

### Critical Issues Found

[For each critical issue from audit:]

#### 🔴 [ISSUE TITLE]
**What we found:** [Technical finding in plain language]
**Business impact:** [What this means for their revenue/visibility]
**Our fix:** [What we will do to resolve it]
**Timeline:** [When they will see improvement]

---

## 我们的服务方案（分档交付）

We offer three engagement models based on the scope of optimization needed.

---

### BASIC — €2,500/month
*Best for: Sites with score 61-75 needing targeted improvements*

**What's included:**
- Quarterly full GEO audit (4x/year)
- Quarterly client report with score tracking
- Schema.org implementation (Organization + key page schemas)
- AI crawler access optimization (robots.txt)
- llms.txt creation and maintenance
- Email support (48-hour response)

**Estimated GEO score improvement:** +10-20 points in 6 months
**Contract:** Minimum 6 months

---

### STANDARD — €5,000/月 ⭐ 推荐给 [公司/品牌名]
*Best for: Sites with score 40-60 needing structured monthly work*

**Everything in Basic, plus:**
- Monthly full GEO audit + delta report
- Monthly strategy call (60 minutes)
- Content citability optimization (up to 10 pages/month)
- 品牌权威/实体信号建设（百度百科/公众号/小红书/知乎/B站等 + 垂直平台）
- 平台专项优化（豆包/元宝/通义千问/百度 AI 搜索；可选含海外平台）
- E-E-A-T improvements (author pages, credentials, freshness signals)
- Slack channel for fast communication (24-hour response)

**Estimated GEO score improvement:** +25-40 points in 6 months
**Contract:** Minimum 6 months

---

### PREMIUM — €9,500/月
*Best for: Sites with score 0-40 with critical issues, or competitive industries*

**Everything in Standard, plus:**
- Bi-weekly strategy calls
- Technical SEO implementation support (Core Web Vitals, SSR, speed)
- Full content strategy + production (4 optimized articles/month)
- 主动品牌建设（中文互联网生态 + 行业垂直平台的第三方背书/引用）
- Competitor monitoring and response
- Dedicated account manager
- Priority support (4-hour response)

**Estimated GEO score improvement:** +40-60 points in 6 months
**Contract:** Minimum 12 months

---

## ROI Projection for [COMPANY NAME]

Based on your current GEO score of [SCORE]/100 and industry benchmarks:

| Scenario | 6-Month Score | AI Traffic Increase | Est. Additional Value/Month |
|----------|--------------|--------------------|-----------------------------|
| No action | [SCORE + 2]/100 | +5% (organic growth) | €[LOW] |
| Basic package | [SCORE + 15]/100 | +30-40% | €[MED] |
| Standard package | [SCORE + 32]/100 | +60-90% | €[HIGH] |
| Premium package | [SCORE + 50]/100 | +100-150% | €[VERY HIGH] |

**Assumptions:**
- Based on estimated [X] monthly organic visitors to [DOMAIN]
- AI search is projected to drive 25-40% of organic discovery by end of 2026
- AI-referred traffic converts at 4.4x the rate of regular organic traffic
- Calculations use conservative estimates — actual results may vary

**Payback period (Standard package):** [X] months based on current traffic

---

## Engagement Timeline

### Month 1 — Foundation
- Kick-off call and onboarding (Week 1)
- Full technical audit + baseline metrics capture
- Quick wins implementation: robots.txt, schema, llms.txt, meta descriptions
- Expected score improvement: +5-10 points

### Month 2-3 — Optimization
- Content citability rewrites (top 10 pages)
- E-E-A-T improvements: author pages, credentials, dates
- Platform-specific optimization (Google AIO, ChatGPT, Perplexity)
- Brand presence: LinkedIn, Wikipedia/Wikidata groundwork
- Expected score improvement: +15-25 points cumulative

### Month 4-6 — Authority Building
- Brand mention campaigns (Reddit, industry sites, YouTube)
- Topical authority content strategy
- Monthly reports showing score improvements
- Expected score improvement: +30-45 points cumulative

### Month 6 — Review
- Full re-audit with before/after comparison
- ROI report
- Renewal discussion

---

## Why Us

- **GEO specialists**: We focus exclusively on AI search optimization, not traditional SEO agencies adapting to GEO
- **Transparent reporting**: Monthly reports show exactly what changed and why
- **No lock-in beyond minimum**: Month-to-month after initial commitment
- **Proven methodology**: 11-dimension GEO audit covering all major AI platforms
- **Fast results**: Quick wins visible within 30 days

---

## Investment Summary

| Package | Monthly | 6-Month | 12-Month |
|---------|---------|---------|----------|
| Basic | €2,500 | €15,000 | €30,000 |
| Standard | €5,000 | €30,000 | €60,000 |
| Premium | €9,500 | €57,000 | €114,000 |

*All prices exclude VAT. Payment terms: monthly, due within 15 days of invoice.*

---

## Next Steps

To move forward:

1. **Review this proposal** and share any questions
2. **Schedule a 30-minute call** to walk through findings together: [CALENDAR LINK]
3. **Sign the service agreement** (sent separately upon acceptance)
4. **Kick-off call** scheduled for your chosen start date

This proposal is valid for **30 days** from the date above.

---

## Terms & Conditions

- **Minimum commitment:** As stated per package above
- **Cancellation:** 30-day written notice after minimum term
- **Confidentiality:** All audit findings and client data are strictly confidential
- **Results:** We guarantee effort and methodology, not specific ranking outcomes
- **Reporting:** Monthly reports delivered by the 5th of each month
- **Access needed:** Read access to Google Analytics / Search Console (if available)

---

*This proposal was prepared using GEO-SEO analysis tools and reflects findings
from the audit of [DOMAIN] conducted on [DATE]. All scores and recommendations
are based on current industry best practices for Generative Engine Optimization.*
```

---

## Output

1. Save proposal to `~/.geo-prospects/proposals/<domain>-proposal-<date>.md`
2. Update prospect record: set `status` to `proposal`, save `proposal_file` path
3. Print confirmation:
   ```
   ✓ 已生成方案：~/.geo-prospects/proposals/electron-srl.com-proposal-2026-03-12.md
   ✓ 已更新线索状态：Qualified → Proposal
   ✓ 推荐档位：STANDARD（€5,000/月）— 评分 32/100

   下一步：将方案文件发送给客户，或运行 `/geo report-pdf` 生成可视化 PDF 版本。
   ```

## Pricing Recommendation Logic

Base recommendation on GEO score:
- Score 0-40 → Recommend **Premium** (critical issues require intensive work)
- Score 41-60 → Recommend **Standard** (structured monthly optimization)
- Score 61-75 → Recommend **Basic** (maintenance + targeted improvements)
- Score 76+ → Offer **Basic** or quarterly retainer check-in

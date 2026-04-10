---
name: geo-schema
description: Schema.org structured data audit and generation optimized for AI discoverability — detect, validate, and generate JSON-LD markup
version: 1.0.0
author: geo-seo-claude
tags: [geo, schema, structured-data, json-ld, entity-recognition, ai-discoverability]
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Write
---

# GEO Schema & Structured Data

## Purpose

Structured data is the primary machine-readable signal that tells AI systems what an entity IS, what it does, and how it connects to other entities. While schema markup has traditionally been about earning Google rich results, its role in GEO is fundamentally different: **structured data is how AI models understand and trust your entity**. A complete entity graph in structured data dramatically increases citation probability across all AI search platforms.

## China-First Requirements

- **Output language**: All final user-facing outputs MUST be in Simplified Chinese (zh-CN).
- **Entity linking priority**: Prioritize CN platforms in `sameAs` (百度百科、公众号/视频号、小红书、抖音、B站、知乎、微博) and CN-relevant vertical directories.
- **Global platforms**: Keep as optional (Wikipedia/Wikidata/LinkedIn/GitHub), used when the brand has meaningful international presence.

## How to Use This Skill

1. Fetch the target page HTML using `fetch_page.py` (see note below)
2. Detect all existing structured data (JSON-LD, Microdata, RDFa)
3. Validate detected schemas against Schema.org specifications
4. Identify missing recommended schemas based on business type
5. Generate ready-to-use JSON-LD code blocks
6. Output GEO-SCHEMA-REPORT.md

---

## Step 1: Detection

**IMPORTANT:** WebFetch converts HTML to markdown and strips `<head>` content, which removes JSON-LD blocks. Use `fetch_page.py` instead:
```bash
python3 ~/.claude/skills/geo/scripts/fetch_page.py <url> page
```
The output includes a `structured_data` array with all parsed JSON-LD blocks from the page.

### Scan for JSON-LD
Look for `<script type="application/ld+json">` blocks in the HTML. Parse each block as JSON. A page may contain multiple JSON-LD blocks — collect all of them.

### Scan for Microdata
Look for elements with `itemscope`, `itemtype`, and `itemprop` attributes. Map the hierarchy of nested items. Note: Microdata is harder for AI crawlers to parse than JSON-LD. Flag a recommendation to migrate to JSON-LD if Microdata is the only format found.

### Scan for RDFa
Look for elements with `typeof`, `property`, and `vocab` attributes. Similar to Microdata — recommend migration to JSON-LD.

### Priority Order
JSON-LD is the **strongly recommended format** for GEO. Google, Bing, and AI platforms all process JSON-LD most reliably. If the site uses Microdata or RDFa exclusively, flag this as a high-priority migration.

---

## Step 2: Validation

For each detected schema block, validate using a **CN-friendly strictness model**.

### Strictness Model (CN-Friendly)

This repo is often used in China network and for CN AI assistants. In practice, you do **not** need “perfect schema” everywhere. Use this rule:

- **Must-Fix (Blocking)**: Issues that cause parse failure, entity confusion, or obvious contradictions.
- **Should-Fix (High ROI)**: Issues that materially improve machine understanding/citability.
- **Nice-to-Have**: Completeness extras that rarely change outcomes.

When scoring or listing issues, do not punish sites for missing optional properties. Prioritize **stability, consistency, and machine readability**.

### Must-Fix (Blocking) checks

1. **Valid JSON**: Is the JSON-LD syntactically valid? (No trailing commas, malformed strings.)
2. **Valid `@type`**: Is `@type` a recognized Schema.org type?
3. **Core entity present**:
   - Business sites: at least one **Organization** (or subtype like LocalBusiness)
   - Content sites: **Article** + **publisher** (Organization) + **author**
   - Product pages: **Product** + **offers** (when pricing is shown)
4. **Entity consistency**: `name`, `url`, canonical domain, and contact fields do not conflict across schema blocks.
5. **No duplicates/conflicts**: Avoid multiple contradictory Organization blocks on the same page.

### Should-Fix (High ROI) checks

6. **sameAs links**: Provide `sameAs` to official presences (CN-focused: 百度百科、公众号、抖音、小红书、B站、知乎、微博等).
7. **Nesting**: Proper nesting (e.g., `author` inside Article; `address` inside Organization/LocalBusiness).
8. **URL validity**: URLs should resolve where feasible. In CN environments, if a platform is access-restricted, record as “unverifiable” instead of assuming 404.

### Nice-to-Have checks

9. **Recommended properties**: Enrich with additional properties that improve retrieval and grounding (e.g., `foundingDate`, `knowsAbout`, `contactPoint`, etc.).
10. **Rendering method**: Prefer server-rendered JSON-LD. If JSON-LD is injected via JS, flag as a *risk* (not always a failure), because processing may be delayed or inconsistent across crawlers.

> Note: The old “Required vs Recommended properties” framing is intentionally relaxed here. Treat “required” as *required for your business goal*, not as a theoretical completeness checklist.

---

## Step 3: Schema Types for GEO

### Organization (CRITICAL — every business site)
Essential for entity recognition across all AI platforms. This is how AI models identify WHAT the business is.

**Required properties:**
- `@type`: "Organization" (or subtype: Corporation, LocalBusiness, etc.)
- `name`: Official business name
- `url`: Official website URL
- `logo`: URL to logo image (ImageObject preferred)

**Recommended properties for GEO:**
- `sameAs`: Array of ALL platform URLs (see sameAs strategy below)
- `description`: 1-2 sentence description of the organization
- `foundingDate`: ISO 8601 date
- `founder`: Person schema
- `address`: PostalAddress schema
- `contactPoint`: ContactPoint with telephone, email, contactType
- `areaServed`: Geographic area
- `numberOfEmployees`: QuantitativeValue
- `industry`: Text or DefinedTerm
- `award`: Array of awards received
- `knowsAbout`: Array of topics the organization is expert in (strong GEO signal)

### LocalBusiness (for businesses with physical locations)
Extends Organization. Critical for local AI search results and Google Gemini.

**Additional required properties:**
- `address`: Full PostalAddress
- `telephone`: Phone number
- `openingHoursSpecification`: Operating hours

**Recommended for GEO:**
- `geo`: GeoCoordinates (latitude, longitude)
- `priceRange`: Price indicator
- `aggregateRating`: AggregateRating schema
- `review`: Array of Review schemas
- `hasMap`: URL to Google Maps

### Article + Author (CRITICAL for publishers)
The Author schema is one of the strongest E-E-A-T signals for AI platforms.

**Article required:**
- `@type`: "Article" (or NewsArticle, BlogPosting, TechArticle)
- `headline`: Article title
- `datePublished`: ISO 8601
- `dateModified`: ISO 8601 (critical for freshness signals)
- `author`: Person or Organization schema
- `publisher`: Organization schema with logo
- `image`: Representative image

**Author (Person) required for GEO:**
- `name`: Full name
- `url`: Author page URL on the site
- `sameAs`: LinkedIn, Twitter, personal site, Google Scholar, ORCID
- `jobTitle`: Professional title
- `worksFor`: Organization schema
- `knowsAbout`: Array of expertise areas
- `alumniOf`: Educational institutions
- `award`: Professional awards

### Product (for e-commerce)
**Required:**
- `name`, `description`, `image`
- `offers`: Offer with price, priceCurrency, availability
- `brand`: Brand schema
- `sku` or `gtin`/`mpn`

**Recommended for GEO:**
- `aggregateRating`: AggregateRating
- `review`: Array of individual reviews
- `category`: Product category
- `material`, `weight`, `width`, `height` (where applicable)

### FAQPage
**Status as of 2024**: Google restricts FAQ rich results to government and health sites. However, the FAQPage schema still serves GEO purposes — AI platforms parse FAQ structured data for question-answer extraction. Implement it for AI readability even though rich results may not appear.

**Structure:**
- `@type`: "FAQPage"
- `mainEntity`: Array of Question schemas, each with `acceptedAnswer` containing an Answer schema

### SoftwareApplication (for SaaS)
**Required:**
- `name`, `description`
- `applicationCategory`: e.g., "BusinessApplication"
- `operatingSystem`: Supported platforms
- `offers`: Pricing

**Recommended for GEO:**
- `aggregateRating`: User ratings
- `featureList`: Array of features (strong citation signal)
- `screenshot`: Screenshots
- `softwareVersion`: Current version
- `releaseNotes`: Link to changelog

### WebSite + SearchAction (for sitelinks search box)
**Structure:**
```json
{
  "@type": "WebSite",
  "name": "Site Name",
  "url": "https://example.com",
  "potentialAction": {
    "@type": "SearchAction",
    "target": {
      "@type": "EntryPoint",
      "urlTemplate": "https://example.com/search?q={search_term_string}"
    },
    "query-input": "required name=search_term_string"
  }
}
```

### Person (standalone — for personal brands, authors, thought leaders)
Use as a standalone schema on About/Bio pages. This builds the entity graph for individual expertise.

**Required:** `name`, `url`
**Recommended for GEO:** `sameAs`, `jobTitle`, `worksFor`, `knowsAbout`, `alumniOf`, `award`, `description`, `image`

### speakable Property (for voice/AI assistants)
The `speakable` property marks specific sections of content as particularly suitable for voice and AI assistant consumption. Add to Article or WebPage schemas.

```json
{
  "@type": "Article",
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelector": [".article-summary", ".key-takeaway"]
  }
}
```
This signals to AI assistants which passages are the best candidates for citation or reading aloud.

---

## Step 4: Deprecated/Changed Schemas to Flag

| Schema | Status | Note |
|---|---|---|
| HowTo | Rich results deprecated Aug 2023 | Still useful for AI parsing, but do not promise rich results |
| FAQPage | Restricted to govt/health Aug 2023 | Still useful for AI parsing (see above) |
| SpecialAnnouncement | Deprecated 2023 | Was for COVID; remove if still present |
| CourseInfo | Replaced by Course updates 2024 | Use updated Course schema properties |
| VideoObject `contentUrl` | Changed behavior 2024 | Must point to actual video file, not page URL |
| Review snippet | Stricter enforcement 2024 | Self-serving reviews on product pages may not display |

Flag any deprecated schemas found and recommend replacements.

---

## Step 5: sameAs Strategy (CRITICAL for Entity Recognition)

The `sameAs` property is the single most important structured data property for GEO. It tells AI systems: "This entity on my website is the SAME entity as these profiles elsewhere." This creates the entity graph that AI platforms use to verify, trust, and cite sources.

### Recommended sameAs Links (in priority order)

1. **百度百科** — strongest practical CN entity baseline for many categories
2. **微信公众号 / 视频号** — official long-form + distribution identity
3. **小红书** — high-intent product/service evaluation signals
4. **抖音 / 快手（如适用）** — short-video ecosystem identity
5. **B站** — long-form tutorials/reviews
6. **知乎** — high-intent Q&A occupancy
7. **微博** — media / KOL reference hub
8. **垂直平台**（按行业选择）— 美团/大众点评、高德/百度地图、天猫/京东/拼多多/1688、企查查/天眼查、行业协会名录等
9. **Wikipedia / Wikidata（可选）** — if the entity has a stable international footprint
10. **LinkedIn / GitHub（可选）** — for B2B/tech brands with active profiles

### sameAs Audit Process
1. Collect all known web presences for the entity
2. Check that each URL resolves (not 404 or redirected)
3. Verify the Organization/Person schema includes ALL of them
4. Check that the information on each platform is consistent (name, description, founding date, etc.)
5. Flag any platforms where the entity should have a presence but does not

---

## Step 6: JSON-LD Generation

Based on the detected business type, generate ready-to-paste JSON-LD blocks. Always generate:

1. **Organization or Person** (depending on entity type) — always
2. **WebSite with SearchAction** — always for the homepage
3. **Business-type-specific** — Article for publishers, Product for e-commerce, LocalBusiness for local, SoftwareApplication for SaaS
4. **BreadcrumbList** — for any page deeper than homepage

### Generation Rules
- Use the `@graph` pattern to include multiple schemas in one JSON-LD block
- All URLs must be absolute (not relative)
- Include `@id` properties for cross-referencing between schemas
- Use ISO 8601 for all dates
- Include `speakable` on Article schemas with CSS selectors pointing to key content sections
- Place JSON-LD in `<head>` section — NOT injected via JavaScript

### Template: Organization with Full GEO Signals
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://example.com/#organization",
  "name": "Company Name",
  "url": "https://example.com",
  "logo": {
    "@type": "ImageObject",
    "url": "https://example.com/logo.png",
    "width": 600,
    "height": 60
  },
  "description": "Concise description of what the company does.",
  "foundingDate": "2020-01-15",
  "founder": {
    "@type": "Person",
    "name": "Founder Name",
    "sameAs": "https://www.linkedin.com/in/founder"
  },
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "123 Main St",
    "addressLocality": "City",
    "addressRegion": "State",
    "postalCode": "12345",
    "addressCountry": "US"
  },
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+1-555-555-5555",
    "contactType": "customer service",
    "email": "support@example.com"
  },
  "sameAs": [
    "https://en.wikipedia.org/wiki/Company_Name",
    "https://www.wikidata.org/wiki/Q12345",
    "https://www.linkedin.com/company/company-name",
    "https://www.youtube.com/@companyname",
    "https://twitter.com/companyname",
    "https://github.com/companyname",
    "https://www.crunchbase.com/organization/company-name"
  ],
  "knowsAbout": [
    "Topic 1",
    "Topic 2",
    "Topic 3"
  ]
}
```

---

## Scoring Rubric (0-100)

| Criterion | Points | How to Score |
|---|---|---|
| Organization/Person schema present and complete | 15 | 15 if full, 10 if basic, 0 if none |
| sameAs links (5+ platforms) | 15 | 3 per valid sameAs link, max 15 |
| Article schema with author details | 10 | 10 if full author schema, 5 if name only, 0 if none |
| Business-type-specific schema present | 10 | 10 if complete, 5 if partial, 0 if missing |
| WebSite + SearchAction | 5 | 5 if present, 0 if not |
| BreadcrumbList on inner pages | 5 | 5 if present, 0 if not |
| JSON-LD format (not Microdata/RDFa) | 5 | 5 if JSON-LD, 3 if mixed, 0 if only Microdata/RDFa |
| Server-rendered (not JS-injected) | 10 | 10 if in HTML source, 5 if JS but in head, 0 if dynamic JS |
| speakable property on articles | 5 | 5 if present, 0 if not |
| Valid JSON + valid Schema.org types | 10 | 10 if no errors, 5 if minor issues, 0 if major errors |
| knowsAbout property on Organization/Person | 5 | 5 if present with 3+ topics, 0 if missing |
| No deprecated schemas present | 5 | 5 if clean, 0 if deprecated schemas found |

---

## Output Format

Generate **GEO-SCHEMA-REPORT.md** with:

```markdown
# GEO Schema 与结构化数据报告（CN 优先）— [Domain]
日期： [Date]

## Schema 评分： XX/100

## 检测到的结构化数据
| Page | Schema Type | Format | Status | Issues |
|---|---|---|---|---|
| / | Organization | JSON-LD | Valid | Missing sameAs |
| /blog/post-1 | Article | JSON-LD | Valid | No author schema |

## 校验结果
[按 schema 块逐项列出：通过/失败、错误原因、修复建议]

## 缺失的推荐 Schema
[根据业务类型列出应补齐的 schema（含优先级）]

## sameAs 实体链接清单（CN 优先）
| Platform | URL | Status |
|---|---|---|
| 百度百科 | [URL or "未找到"] | 已有/缺失 |
| 微信公众号/视频号 | [URL or "未找到"] | 已有/缺失 |
| 小红书 | [URL or "未找到"] | 已有/缺失 |
| 抖音 | [URL or "未找到"] | 已有/缺失 |
| B站 | [URL or "未找到"] | 已有/缺失 |
| 知乎 | [URL or "未找到"] | 已有/缺失 |
| 微博 | [URL or "未找到"] | 已有/缺失 |
| 垂直平台（按行业） | [URL or "未找到"] | 已有/缺失 |
[Continue for all recommended platforms]

## 生成的 JSON-LD 代码（可直接上线）
[Ready-to-paste JSON-LD blocks for each missing or incomplete schema]

## 实施说明
- 放置位置（推荐：原始 HTML 的 `<head>`，避免仅用 JS 注入）
- SSR/可抓取要求（AI 爬虫通常不执行 JS）
- 验证方式（结构化数据测试工具 + 线上抓取自检）
```

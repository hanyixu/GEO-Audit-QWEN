---
name: geo-llmstxt
description: Analyzes and generates llms.txt files -- the emerging standard for helping AI systems understand website structure and content. Can validate existing llms.txt files or generate new ones from scratch by crawling the site.
allowedTools:
  - Read
  - Grep
  - Glob
  - Bash
  - WebFetch
  - Write
---

# llms.txt Standard Analysis and Generation Skill

## Purpose

This skill handles everything related to the `llms.txt` standard -- an emerging convention (proposed by Jeremy Howard in September 2024, gaining adoption through 2025-2026) that allows websites to provide structured guidance to AI systems about their content, structure, and key information. It is analogous to `robots.txt` (which tells crawlers what NOT to access) but instead tells AI systems what IS most useful to understand about the site.

## China-First Requirements

- **Output language**: All final user-facing outputs MUST be in Simplified Chinese (zh-CN).
- **Content selection**: Prefer pages that match CN search intent patterns (对比/避坑/价格/售后/参数/案例/资质/合规) and CN distribution channels.
- **Section naming**: Use CN-friendly sections when generating llms.txt (e.g., `## 产品/服务`, `## 价格`, `## 解决方案`, `## 案例`, `## 指南/教程`, `## FAQ`, `## 关于我们`, `## 联系方式`, `## 合规/资质`).

## Why llms.txt Matters

AI language models face a fundamental challenge when processing websites: they must determine which pages are most important, what the site is about, and how content is organized -- typically by crawling many pages and inferring structure. `llms.txt` solves this by providing an explicit, machine-readable (and human-readable) summary.

**Benefits of having a well-crafted llms.txt:**

1. **Faster AI comprehension:** AI systems can understand your site's purpose and structure from a single file rather than crawling dozens of pages.
2. **Controlled narrative:** You choose which pages and facts AI systems see first, shaping how they represent your brand.
3. **Higher citation accuracy:** AI systems that consult llms.txt can cite the correct, authoritative page for each topic.
4. **Reduced misrepresentation:** Key facts (pricing, features, locations) are stated explicitly, reducing AI hallucination about your business.
5. **Early adopter advantage:** As of early 2026, fewer than 5% of websites have an llms.txt file, making it a differentiator.

---

## The llms.txt Specification

### File Location

The file MUST be located at the root of the domain:
```
https://example.com/llms.txt
```

### Format Specification

The file uses Markdown formatting with specific conventions:

```markdown
# [网站/品牌名称]

> [一句话说明你是谁、做什么、服务谁。尽量控制在 200 个中文字符以内，事实表达，少口号。]

## 产品/服务

- [核心产品页](https://example.com/product): 说明这页包含哪些核心信息（功能/适用场景/价格口径/参数等）。

## 指南/教程

- [入门指南](https://example.com/guide): 覆盖的关键问题、步骤、注意事项。

## FAQ

- [常见问题](https://example.com/faq): 价格、售后、保修、对比、适配等高意图问题的答案集合。
```

### Detailed Format Rules

**1. Title (Required)**
```markdown
# Site Name
```
- Must be the first line of the file.
- Should be the official business/site name.
- Use the H1 heading format (single `#`).

**2. Description (Required)**
```markdown
> Brief description of the site/business
```
- Must appear immediately after the title.
- Use Markdown blockquote format (`>`).
- Keep under 200 characters.
- Should clearly state what the business does and who it serves.
- Avoid marketing fluff -- be factual and specific.

**3. Main Sections (Required -- at least one)**

Use H2 headings (`##`) to organize pages by category. Common section names:

| Section Name | Purpose | Example Content |
|---|---|---|
| `## Docs` | Primary documentation or key pages | Product pages, service descriptions, core content |
| `## Optional` | Secondary pages worth knowing about | Blog posts, supplementary resources |
| `## API` | API documentation | API reference, authentication guides |
| `## Blog` | Blog or news content | Recent/popular articles |
| `## Products` | Product catalog | Product pages, pricing |
| `## Services` | Service offerings | Service descriptions, process pages |
| `## About` | Company information | About page, team, mission |
| `## Resources` | Educational/reference content | Guides, tutorials, whitepapers |
| `## Legal` | Legal documents | Terms of service, privacy policy |
| `## Contact` | Contact information | Contact page, support channels |

**4. Page Entries (Required)**

Each entry follows the format:
```markdown
- [Page Title](URL): Description of page content
```

Rules for page entries:
- **Title:** Use the actual page title or a clear descriptive title.
- **URL:** Must be a full, absolute URL (not relative paths).
- **Description:** 10-30 words describing what the page covers. Be specific about the information available.
- **Order:** List pages in order of importance within each section.
- **Limit:** Include 10-30 page entries total. Prioritize your most authoritative and useful pages.

**5. Key Facts Section (Recommended)**

```markdown
## Key Facts
- Founded in [year] by [founder(s)]
- Headquarters: [City, Country]
- [X] customers/users in [Y] countries
- Key products: [Product A], [Product B], [Product C]
- Industry: [Industry classification]
```

This section provides quick reference data that AI systems frequently need to answer user queries about your business.

**6. Contact Section (Recommended)**

```markdown
## Contact
- Website: https://example.com
- Email: hello@example.com
- Support: support@example.com
- Phone: +1-555-123-4567
- Address: 123 Main St, City, State, ZIP, Country
```

---

## llms-full.txt (Extended Version)

In addition to `llms.txt`, sites can provide `/llms-full.txt` -- an extended version with more detail.

**Differences from llms.txt:**

| Feature | llms.txt | llms-full.txt |
|---|---|---|
| **Length** | Concise (50-150 lines) | Comprehensive (150-500+ lines) |
| **Page entries** | 10-30 key pages | 30-100+ pages |
| **Descriptions** | 10-30 words per entry | 30-100 words per entry, may include key facts from each page |
| **Audience** | Quick AI comprehension | Deep AI analysis |
| **Sections** | 3-6 sections | 8-15 sections |
| **Key facts** | Business-level facts | Page-level facts and data points |

Both files can coexist. AI systems check for `llms.txt` first, then may optionally load `llms-full.txt` for deeper understanding.

---

## Analysis Mode

When checking an existing llms.txt file:

### Step 1: Fetch the File

1. Use WebFetch to retrieve `[domain]/llms.txt`.
2. Also check for `[domain]/llms-full.txt`.
3. Record HTTP status code:
   - **200:** File exists -- proceed to validation.
   - **404:** File does not exist -- recommend generation.
   - **403:** File exists but is blocked -- flag as misconfiguration.
   - **301/302:** Redirect -- follow and note the redirect.

### Step 2: Validate Format

Check each structural element:

| Element | Check | Severity if Missing |
|---|---|---|
| H1 Title | Present, matches business name | Critical |
| Blockquote description | Present, under 200 chars, factual | High |
| At least one H2 section | Present | Critical |
| Page entries with URLs | At least 5 entries present | High |
| URLs are absolute | All URLs use full https:// paths | High |
| URLs are valid | All URLs return 200 status | Medium |
| Descriptions present | Every entry has a description after the colon | Medium |
| Key Facts section | Present with business information | Medium |
| Contact section | Present with at least email | Low |
| Reasonable length | 30-200 lines | Low |
| No broken Markdown | Proper formatting throughout | Medium |

### Step 3: Assess Content Quality

Rate the llms.txt on these dimensions:

**Completeness (0-100):**
- Does it cover all major site sections visible in the navigation?
- Are the most important/highest-traffic pages included?
- Is the Key Facts section present with accurate business data?
- Does it include recent/updated content?

**Accuracy (0-100):**
- Do descriptions accurately reflect page content?
- Are URLs valid and pointing to the correct pages?
- Are Key Facts verifiable and current?
- Is the business description accurate?

**Usefulness (0-100):**
- Would an AI system understand the site's purpose from this file alone?
- Are descriptions specific enough to differentiate pages?
- Are the most citation-worthy pages highlighted?
- Is the organization logical and intuitive?

**Overall llms.txt Score** = (Completeness * 0.40) + (Accuracy * 0.35) + (Usefulness * 0.25)

### Step 4: Compare Against Site Content

1. Crawl the site's main navigation and sitemap.
2. Identify important pages NOT listed in llms.txt.
3. Check if any listed URLs are broken or redirected.
4. Verify that the business description matches current homepage messaging.
5. Flag stale entries (pages that have been significantly updated since the llms.txt was written).

---

## Generation Mode

When creating a new llms.txt file from scratch:

### Step 1: Site Discovery

1. Fetch the homepage and extract:
   - Site name (from `<title>`, `<meta property="og:site_name">`, or H1)
   - Business description (from meta description or hero section)
   - Main navigation links
   - Footer links
2. Fetch `/sitemap.xml` to discover all public pages.
3. Identify the site's primary business type (SaaS, E-commerce, Local, Publisher, Agency).

### Step 2: Page Prioritization

Categorize all discovered pages and select the most important ones:

**Always Include:**
- Homepage
- About / Company page
- Pricing page (if exists)
- Primary product/service pages (top 3-5)
- Contact page
- Documentation landing page (if exists)

**Include if High Quality:**
- Top blog posts (by apparent importance, recency, or comprehensiveness)
- Case studies or customer stories
- Key resource/guide pages
- FAQ page
- Careers page (for large companies)

**Skip:**
- Thin category/tag pages
- Pagination pages
- Login/signup pages
- Legal boilerplate (unless specifically relevant)
- Duplicate or near-duplicate content
- Pages with minimal unique content

### Step 3: Write Descriptions

For each selected page:

1. Fetch the page content using WebFetch.
2. Read the H1, meta description, and first 2-3 paragraphs.
3. Write a description that:
   - Is 10-30 words long
   - States what information is on the page
   - Mentions specific topics, data, or features covered
   - Avoids marketing language ("best," "leading," "revolutionary")
   - Uses factual, informative language

**Good description examples:**
- `Explains the three pricing tiers (Free, Pro, Enterprise) with feature comparison and annual/monthly costs.`
- `Details the company's founding in 2018, team of 45 employees, and office locations in Austin and London.`
- `Covers integration setup for Slack, Salesforce, and HubSpot with step-by-step guides and API endpoints.`

**Bad description examples:**
- `Our amazing pricing page!` (marketing language, no specifics)
- `Learn more about our company.` (too vague)
- `Click here for details.` (not descriptive)

### Step 4: Compile Key Facts

Gather key business facts from the site:

- Year founded
- Founder name(s)
- Headquarters location
- Number of employees (if public)
- Number of customers/users (if public)
- Key products or services (list top 3-5)
- Industry classification
- Notable clients or partnerships (if public)
- Key differentiators (what makes this business unique)
- Recent milestones or achievements (last 12 months)

### Step 5: Assemble the File

Construct the llms.txt following this template:

```markdown
# [Site Name]

> [One clear sentence: what the business does, who it serves, and its primary value proposition. Under 200 characters.]

## Docs

- [Most Important Page](https://example.com/page): Description covering the key content on this page.
- [Second Page](https://example.com/page-2): Description of this page's content and value.
- [Third Page](https://example.com/page-3): What users and AI systems will find here.

## Products

- [Product A](https://example.com/product-a): Core features, target users, and pricing model for Product A.
- [Product B](https://example.com/product-b): What Product B does and how it differs from Product A.

## Resources

- [Guide Title](https://example.com/guide): Comprehensive guide covering [topic] with [X] sections and practical examples.
- [Blog Post](https://example.com/blog/post): Analysis of [topic] with original data from [source].

## Key Facts

- Founded in [year] by [name(s)]
- Headquartered in [City, Country]
- [Specific metric: e.g., "Serves 10,000+ businesses in 40 countries"]
- [Key differentiator: e.g., "Only platform offering real-time X and Y integration"]
- Industry: [Classification]

## Contact

- Website: https://example.com
- Email: [primary contact email]
- Support: [support URL or email]
```

### Step 6: Validate the Generated File

Before outputting:
1. Verify all URLs are reachable (200 status).
2. Confirm total entry count is between 10-30.
3. Check that no description exceeds 50 words.
4. Verify the overall file length is 50-150 lines.
5. Ensure Markdown formatting is clean and consistent.

---

## Output Format

### For Analysis Mode

Generate `GEO-LLMSTXT-ANALYSIS.md`:

```markdown
# llms.txt 分析报告（CN 优先）：[Domain]

**分析日期：** [Date]
**llms.txt 状态：** [Found at URL / Not Found / Error]
**llms-full.txt 状态：** [Found / Not Found]

---

## llms.txt 总分： [X]/100

| Dimension | Score |
|---|---|
| Completeness | [X]/100 |
| Accuracy | [X]/100 |
| Usefulness | [X]/100 |

---

## 格式校验

| Element | Status | Notes |
|---|---|---|
| H1 Title | [Pass/Fail] | [Notes] |
| Description blockquote | [Pass/Fail] | [Notes] |
| H2 Sections | [Pass/Fail] | [X sections found] |
| Page entries | [Pass/Fail] | [X entries found] |
| URL validity | [Pass/Fail] | [X broken URLs] |
| Entry descriptions | [Pass/Fail] | [X missing descriptions] |
| Key Facts | [Pass/Fail] | [Notes] |
| Contact section | [Pass/Fail] | [Notes] |

---

## 重要页面缺失清单

These important pages were found on the site but not in llms.txt:

1. [Page Title](URL) -- [Why it should be included]
2. [Page Title](URL) -- [Why it should be included]

## 优化建议（按优先级）

1. [Specific recommendation]
2. [Specific recommendation]
3. [Specific recommendation]

## 建议的 llms.txt（可直接替换上线）

[Complete rewritten llms.txt file if significant improvements are needed]
```

### For Generation Mode

Output the complete `llms.txt` file content (in Chinese), ready to be saved to the site's root directory. Also output a brief `GEO-LLMSTXT-GENERATION.md` report (Chinese) explaining:
- 发现了多少页面、最终选择了多少页面
- 选择与排序依据（为什么这些页最值得 AI 先读）
- 边界页面（可后续补充）
- 推荐更新频率（内容站可按月；稳定官网可按季度或版本发布后更新）

---

## Best Practices Reference

1. **Update regularly.** If your site publishes weekly blog posts, update llms.txt monthly. If your product changes quarterly, update after each release.
2. **Lead with your strongest content.** The first entries in each section should be your most authoritative, comprehensive pages.
3. **Be specific in descriptions.** "Comprehensive 3,000-word guide to React Server Components with code examples" is far more useful than "React guide."
4. **Include your differentiators.** If your site has unique data, original research, or exclusive features, highlight these in descriptions and Key Facts.
5. **Keep it concise.** The llms.txt should be scannable in under 60 seconds. Save detail for llms-full.txt.
6. **Use absolute URLs.** Always include the full `https://` URL, never relative paths.
7. **Test after deployment.** After uploading, verify the file is accessible at `https://yourdomain.com/llms.txt` with no redirects.
8. **Coordinate with robots.txt.** Ensure pages listed in llms.txt are not blocked in robots.txt for AI crawlers.
9. **Mirror your site structure.** Section names in llms.txt should roughly correspond to your main navigation categories.
10. **Avoid sensitive pages.** Do not include internal tools, admin panels, or pages with sensitive information.

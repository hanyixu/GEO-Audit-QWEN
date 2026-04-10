<p align="center">
  <img src="assets/banner.svg" alt="GEO-SEO Claude Code 技能" width="900"/>
</p>

<p align="center">
  <strong>GEO 优先，SEO 支撑。</strong> 为 AI 驱动的搜索引擎优化网站<br/>
  （豆包、元宝、通义千问、Kimi、DeepSeek、百度 AI 搜索）同时巩固传统 SEO 基础。
</p>

<p align="center">
  AI 搜索正在蚕食传统搜索流量。这个工具帮你优化流量的去向，而不是它曾经的来源。
</p>

---

## 为什么 GEO 在 2026 年至关重要

| 指标 | 数值 |
|--------|-------|
| GEO 服务市场规模 | 850亿+（预计2031年达730亿美元） |
| AI 引荐流量增长率 | 同比增长 +527% |
| AI 流量转化率 vs 自然搜索 | 高出 4.4 倍 |
| Gartner 预测：2028年搜索流量下降 | -50% |
| 品牌提及 vs 外链对 AI 的影响 | 强相关性高 3 倍 |
| 已投资 GEO 的营销人员占比 | 仅 23% |

---

## 快速开始

### 一键安装（macOS / Linux）

> **提示：** 如果你已经把本仓库 clone 到本地（或下载了 zip），推荐直接在仓库根目录运行 `./install.sh`（确保安装的是当前仓库版本）。只有在你确认下面的仓库地址后，再使用 curl 一键安装。

```bash
curl -fsSL https://raw.githubusercontent.com/<YOUR_GITHUB_OWNER>/<YOUR_REPO>/v1.0.0/install.sh | bash
```

### 手动安装

```bash
git clone https://github.com/<YOUR_GITHUB_OWNER>/<YOUR_REPO>.git
cd <YOUR_REPO>
git checkout v1.0.0
./install.sh
```

### Windows（Git Bash）

需要安装 [Git for Windows](https://git-scm.com/downloads)，其中包含 Git Bash。

> **提示：** 如果你已经把本仓库 clone 到本地（或下载了 zip），推荐直接在仓库根目录运行 `./install-win.sh`（确保安装的是当前仓库版本）。只有在你确认下面的仓库地址后，再使用 curl 一键安装。

```bash
# 方式一：一键安装（在 Git Bash 中运行，不要用 PowerShell 或 CMD）
curl -fsSL https://raw.githubusercontent.com/<YOUR_GITHUB_OWNER>/<YOUR_REPO>/v1.0.0/install-win.sh | bash

# 方式二：手动安装
git clone https://github.com/<YOUR_GITHUB_OWNER>/<YOUR_REPO>.git
cd <YOUR_REPO>
git checkout v1.0.0
./install-win.sh
```

> **注意：** 右键点击文件夹并选择"在此处打开 Git Bash"，或打开 Git Bash 后导航到目录。请勿使用 PowerShell 或命令提示符。

### 环境要求

- Python 3.8+
- Claude Code CLI
- Git
- 可选：Playwright（用于截图）

---

## 命令列表

打开 Claude Code 并使用以下命令：

| 命令 | 功能说明 |
|---------|-------------|
| `/geo audit <url>` | 使用并行子智能体执行完整 GEO + SEO 审计 |
| `/geo quick <url>` | 60 秒 GEO 可见度快速诊断 |
| `/geo citability <url>` | 评估内容被 AI 引用的准备度得分 |
| `/geo crawlers <url>` | 检查 AI 爬虫访问权限（robots.txt） |
| `/geo llmstxt <url>` | 分析或生成 llms.txt 文件 |
| `/geo brands <url>` | 扫描 AI 引用平台上的品牌提及 |
| `/geo platforms <url>` | 针对各平台的专项优化 |
| `/geo schema <url>` | 结构化数据分析与生成 |
| `/geo technical <url>` | 技术 SEO 审计 |
| `/geo content <url>` | 内容质量与 E-E-A-T 评估 |
| `/geo report <url>` | 生成可交付客户的 GEO 报告 |
| `/geo report-pdf` | 生成带图表和可视化内容的专业 PDF 报告 |

---

## 项目架构

```
geo-seo-claude/
├── geo/                          # 主技能编排器
│   └── SKILL.md                  # 主技能文件，含命令路由
├── skills/                       # 13 个专项子技能
│   ├── geo-audit/                # 完整审计编排与评分
│   ├── geo-citability/           # AI 引用准备度评分
│   ├── geo-crawlers/             # AI 爬虫访问分析
│   ├── geo-llmstxt/              # llms.txt 标准分析与生成
│   ├── geo-brand-mentions/       # AI 引用平台品牌存在感
│   ├── geo-platform-optimizer/   # 各平台 AI 搜索专项优化
│   ├── geo-schema/               # AI 可发现性结构化数据
│   ├── geo-technical/            # 技术 SEO 基础
│   ├── geo-content/              # 内容质量与 E-E-A-T
│   ├── geo-report/               # 可交付客户的 Markdown 报告生成
│   ├── geo-report-pdf/           # 带图表的专业 PDF 报告
│   ├── geo-prospect/             # 轻量 CRM 客户管道管理
│   ├── geo-proposal/             # 自动生成客户提案
│   └── geo-compare/              # 月度变化追踪与进度报告
├── agents/                       # 5 个并行子智能体
│   ├── geo-ai-visibility.md      # GEO 审计、引用度、爬虫、品牌
│   ├── geo-platform-analysis.md  # 平台专项优化
│   ├── geo-technical.md          # 技术 SEO 分析
│   ├── geo-content.md            # 内容与 E-E-A-T 分析
│   └── geo-schema.md             # Schema 结构化数据分析
├── scripts/                      # Python 工具脚本
│   ├── fetch_page.py             # 页面抓取与解析
│   ├── citability_scorer.py      # AI 引用度评分引擎
│   ├── brand_scanner.py          # 品牌提及检测
│   ├── llmstxt_generator.py      # llms.txt 验证与生成
│   └── generate_pdf_report.py    # PDF 报告生成器（ReportLab）
├── schema/                       # JSON-LD 模板
│   ├── organization.json         # 机构 Schema（含 sameAs）
│   ├── local-business.json       # 本地商家 Schema
│   ├── article-author.json       # 文章 + 作者 Schema（E-E-A-T）
│   ├── software-saas.json        # 软件应用 Schema
│   ├── product-ecommerce.json    # 含报价的商品 Schema
│   └── website-searchaction.json # 网站 + 搜索动作 Schema
├── install.sh                    # 一键安装脚本
├── uninstall.sh                  # 卸载脚本
├── requirements.txt              # Python 依赖
└── README.md                     # 本文件
```

---

## 数据存储

CRM 和报告技能（`/geo prospect`、`/geo proposal`、`/geo compare`）会在 Claude Code 目录外存储运行数据：

```
~/.geo-prospects/
├── prospects.json              # 客户/潜在客户管道数据
├── proposals/                  # 生成的提案文档
│   └── <domain>-proposal-<date>.md
└── reports/                    # 月度对比报告
    └── <domain>-monthly-<YYYY-MM>.md
```

该目录**不会**被卸载脚本删除——如果不再需要客户数据，请手动删除。

---

## 工作原理

### 完整审计流程

运行 `/geo audit https://example.com` 时：

1. **发现阶段** — 抓取首页，识别业务类型，爬取站点地图
2. **并行分析** — 同时启动 5 个子智能体：
   - AI 可见度（引用度、爬虫权限、llms.txt、品牌提及）
   - 平台分析（豆包、通义千问、百度 AI 搜索就绪度）
   - 技术 SEO（Core Web Vitals、SSR、安全性、移动端）
   - 内容质量（E-E-A-T、可读性、内容新鲜度）
   - Schema 结构化数据（检测、验证、生成）
3. **综合评估** — 汇总各维度得分，生成综合 GEO 评分（0-100）
4. **报告输出** — 输出优先级排序的行动计划及速效优化项

### 评分方法论

| 评估维度 | 权重 |
|----------|--------|
| AI 引用度与可见度 | 25% |
| 品牌权威信号 | 20% |
| 内容质量与 E-E-A-T | 20% |
| 技术基础 | 15% |
| 结构化数据 | 10% |
| 平台优化 | 10% |

---

## 核心功能

### 引用度评分
分析内容块被 AI 引用的准备程度。最易被 AI 引用的段落通常为 134-167 字，自成体系、富含事实，且能直接回答问题。

### AI 爬虫分析
检查 robots.txt 对 14+ 种 AI 爬虫（豆包爬虫、百度 Spider、ClaudeBot、GPTBot 等）的配置，并提供具体的允许/屏蔽建议。

### 品牌提及扫描
品牌提及与 AI 可见度的相关性比外链高 3 倍。扫描 B 站、知乎、百度百科、微博、小红书、抖音及其他 7+ 个平台。

### 平台专项优化
仅有 11% 的域名能同时被豆包和百度 AI 搜索针对同一查询引用。提供各平台的差异化优化建议。

### llms.txt 生成
生成新兴的 llms.txt 标准文件，帮助 AI 爬虫理解你的网站结构。

### 可交付客户的报告
生成专业 GEO 报告（Markdown 或 PDF 格式）。PDF 报告包含分数仪表盘、条形图、平台就绪度可视化、颜色编码表格及优先级行动计划——可直接交付给客户。

---

## 适用场景

- **GEO 服务机构** — 执行客户审计并生成交付物
- **营销团队** — 监控并提升 AI 搜索可见度
- **内容创作者** — 优化内容以获得 AI 引用
- **本地商家** — 被 AI 助手精准收录
- **SaaS 公司** — 提升在各 AI 平台的实体识别度
- **电商** — 优化商品页面以获得 AI 购物推荐

---

## 卸载

```bash
./uninstall.sh
```

或手动删除：
```bash
rm -rf ~/.claude/skills/geo ~/.claude/skills/geo-* ~/.claude/agents/geo-*.md
```

---

## 想把这个工具变成一门生意？

工具本身免费。如何将其变现，欢迎加入社群一起探讨。

**[加入 AI 营销交流社群 →](https://skool.com/aiworkshop)**

社群内你将获得：
- **视频教程** — 手把手讲解安装、运行审计、解读报告
- **客户获取手册** — 如何寻找潜在客户、推销 GEO 服务、完成签单
- **直播答疑** — 带上你的审计结果，获得一对一指导
- **GEO 服务定价与模板** — 提案文档、冷启动外发脚本、客户入驻流程

GEO 服务机构的月收费区间为 1.4 万–8.4 万人民币。这个工具负责审计，社群教你如何销售。

---

## 开源协议

MIT License

---

## 参与贡献

欢迎提交贡献！

---

为 AI 搜索时代而生。

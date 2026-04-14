# 千问GEO审计Skills

**GEO 优先，SEO 支撑。** 为 AI 驱动的搜索引擎优化网站  
（豆包、元宝、通义千问、Kimi、DeepSeek、百度 AI 搜索）同时巩固传统 SEO 基础。

专为中文互联网生态设计，同时兼容全球 AI 平台

---

### 快速上手

**这个项目做什么：** 一键审计网站在中文AI搜索引擎（豆包/元宝/千问/Kimi/DeepSeek/百度）中的可见度，同时优化传统SEO基础。14个专业子技能覆盖AI引用度、品牌提及、技术SEO、内容质量、结构化数据等维度，生成0-100的综合GEO评分和可交付客户的优化报告。



**安装：** 

```bash
curl -fsSL https://raw.githubusercontent.com/hanyixu/GEO-Audit-QWEN/main/install.sh | bash
```

或手动安装：`git clone https://github.com/hanyixu/GEO-Audit-QWEN.git && cd GEO-Audit-QWEN && chmod +x install.sh && ./install.sh`



**运行第一次audit：** 安装完成后，打开 Qwen Code，输入 `/geo audit https://你的网站.com` 即可执行完整审计，5个并行子智能体会自动分析并生成GEO-AUDIT-REPORT.md报告文件。

---

## 🌟 项目简介

**GEO（Generative Engine Optimization，智能引擎优化）** 是一套针对 AI 驱动搜索引擎的优化方法论。与传统 SEO 不同，GEO 的目标是让 AI 系统（豆包、元宝、通义千问、Kimi、DeepSeek 等）能够：

- **发现** 你的网站内容
- **理解** 你的品牌和产品信息
- **验证** 内容的可信度
- **引用** 你的数据到 AI 生成的回答中
- **推荐** 你的产品给用户

研究表明，GEO 评分高的网站在 AI 生成回答中的可见度提升 **30-115%**（佐治亚理工学院/普林斯顿/IIT 德里 2024 年研究）。

### 为什么选择本项目？


| 特性                | 说明                                      |
| ----------------- | --------------------------------------- |
| 📋 适配中文互联网环境      | 专为中文互联网生态设计，覆盖豆包/元宝/千问/Kimi/DeepSeek/百度 |
| 🔍 **实际搜索验证**     | 所有品牌提及检查均通过实际中文互联网搜索验证，非猜测推断            |
| 📊 **科学评分**       | 6 维度评分体系，加权计算综合 GEO 分数（0-100）           |
| 🛠️ **14 个专业子技能** | 覆盖审计、引用度、爬虫、品牌、平台优化、结构化数据等              |
| 📄 **可交付报告**      | 生成 Markdown/PDF 格式的专业报告，可直接交付客户         |
| 🤖 **千问原生支持**     | 完美适配 Qwen Code，本地化部署，数据不出境              |


---

## 🚀 安装运行

### 方式一：一键安装（推荐）

> **适用系统：** macOS / Linux

```bash
curl -fsSL https://raw.githubusercontent.com/hanyixu/GEO-Audit-QWEN/main/install.sh | bash
```

### 方式二：手动安装

```bash
# 克隆仓库
git clone https://github.com/hanyixu/GEO-Audit-QWEN.git
cd GEO-Audit-QWEN

# 执行安装脚本
chmod +x install.sh
./install.sh
```

### Windows（Git Bash）

> **注意：** 请使用 Git Bash 运行，不要使用 PowerShell 或 CMD。

```bash
# 方式一：一键安装
curl -fsSL https://raw.githubusercontent.com/hanyixu/GEO-Audit-QWEN/main/install-win.sh | bash

# 方式二：手动安装
git clone https://github.com/hanyixu/GEO-Audit-QWEN.git
cd GEO-Audit-QWEN
chmod +x install-win.sh
./install-win.sh
```

### 环境要求

- **Python 3.8+**
- **Qwen Code CLI**（通义千问代码工具）
- **Git**
- **可选：** Playwright（用于截图功能）

---

## 🤖 千问（Qwen Code）使用方法

> **💡 重要提示：** 本工具完美支持 Qwen Code（通义千问代码助手），所有功能均可在千问本地运行，**数据不出境**

### 安装到千问

本项目的安装脚本会自动将 14 个 GEO 技能安装到 Qwen Code 的技能目录：

- **macOS/Linux:** `~/.qwen/skills/`
- **Windows:** `%USERPROFILE%\.qwen\skills\`

安装完成后，打开 Qwen Code 即可直接使用。

### 千问中的使用命令

在 Qwen Code 中，使用 `/geo` 前缀调用各项功能：


| 命令                      | 功能说明                          |
| ----------------------- | ----------------------------- |
| `/geo audit <url>`      | 完整 GEO + SEO 审计（含中文互联网实际搜索验证） |
| `/geo citability <url>` | 评估内容被 AI 引用的准备度得分             |
| `/geo crawlers <url>`   | 检查 AI 爬虫访问权限（robots.txt）      |
| `/geo llmstxt <url>`    | 分析或生成 llms.txt 文件             |
| `/geo brands <url>`     | 扫描中文 AI 引用平台上的品牌提及（实际搜索验证）    |
| `/geo platforms <url>`  | 针对各平台的专项优化                    |
| `/geo schema <url>`     | 结构化数据分析与生成                    |
| `/geo technical <url>`  | 技术 SEO 审计                     |
| `/geo content <url>`    | 内容质量与 E-E-A-T 评估              |
| `/geo report <url>`     | 生成可交付客户的 GEO 报告               |
| `/geo report-pdf`       | 生成带图表和可视化内容的专业 PDF 报告         |
| `/geo compare <url>`    | 月度变化追踪与进度报告                   |


### 使用示例

```
# 执行完整审计
/geo audit https://www.example.com

# 快速诊断 AI 可见度
/geo audit https://www.teknodas.cn

# 检查品牌在中文互联网的 presence
/geo brands https://www.apple.com.cn

# 生成 PDF 报告
/geo report-pdf
```

### 本地化优势


| 特性            | 说明                      |
| ------------- | ----------------------- |
| 🔒 **数据不出境**  | 所有分析在本地运行，不上传任何数据       |
| 🇨🇳 **中文优化** | 覆盖百度百科/微信/知乎/小红书等       |
| 🔍 **实际搜索验证** | 所有品牌提及检查均通过真实中文互联网搜索验证  |
| 📊 **符合国标**   | 支持中国 ICP 备案检测、HTTPS 要求等 |
| 🛠️ **开箱即用**  | 安装即用，无需额外配置             |


---

## 📦 技能包架构

### 14 个专业子技能


| 技能                         | 功能                           |
| -------------------------- | ---------------------------- |
| **geo-audit**              | 完整 GEO + SEO 审计，并行 5 个子智能体分析 |
| **geo-citability**         | AI 引用准备度评分（0-100）            |
| **geo-crawlers**           | AI 爬虫访问权限分析（14+ 爬虫）          |
| **geo-llmstxt**            | llms.txt 分析与生成               |
| **geo-brand-mentions**     | 中文互联网品牌提及扫描（实际搜索验证）          |
| **geo-platform-optimizer** | 平台专项优化（豆包/元宝/千问等）            |
| **geo-schema**             | Schema.org 结构化数据分析与生成        |
| **geo-technical**          | 技术 SEO 审计（性能、安全、SSR）         |
| **geo-content**            | 内容质量与 E-E-A-T 评估             |
| **geo-report**             | Markdown 格式可交付报告生成           |
| **geo-report-pdf**         | PDF 格式专业报告（含图表可视化）           |
| **geo-prospect**           | 轻量 CRM 客户管道管理                |
| **geo-proposal**           | 自动生成客户提案                     |
| **geo-compare**            | 月度变化追踪与进度对比                  |


### 5 个并行子智能体

审计时自动启动：


| 子智能体      | 职责                          |
| --------- | --------------------------- |
| AI 可见度分析  | 引用度、爬虫权限、llms.txt、品牌提及      |
| 平台分析      | 豆包/元宝/千问/百度 AI 搜索就绪度        |
| 技术 SEO    | Core Web Vitals、SSR、安全性、移动端 |
| 内容质量      | E-E-A-T、可读性、内容新鲜度           |
| Schema 分析 | 结构化数据检测、验证、生成               |


---

## 📊 评分方法论

### 综合 GEO 评分（0-100）


| 评估维度          | 权重  | 说明                     |
| ------------- | --- | ---------------------- |
| AI 引用度与可见度    | 25% | 内容被 AI 引用的准备程度         |
| 品牌权威信号        | 20% | 第三方平台提及、实体识别信号         |
| 内容质量与 E-E-A-T | 20% | 经验、专业性、权威性、可信度         |
| 技术基础          | 15% | AI 爬虫访问、llms.txt、渲染、速度 |
| 结构化数据         | 10% | Schema.org 标记质量和完整性    |
| 平台优化          | 10% | 在豆包/元宝/千问等平台的 presence |


### 评分等级


| 分数范围   | 等级  | 解读                       |
| ------ | --- | ------------------------ |
| 90-100 | 优秀  | 顶级 GEO 优化，极有可能被 AI 引用    |
| 75-89  | 良好  | 强大的 GEO 基础，有改进空间         |
| 60-74  | 一般  | 中等 GEO presence，存在显著优化机会 |
| 40-59  | 较差  | GEO 信号弱，AI 系统可能难以引用      |
| 0-39   | 严重  | 极少 GEO 优化，网站对 AI 系统基本不可见 |


---

## 🔍 中文互联网实际搜索验证

> **💡 本项目核心特色：** 所有品牌提及检查均通过**真实中文互联网搜索验证**，而非猜测或推断。

### 覆盖的中文平台


| 平台        | 权重  | 验证方式              |
| --------- | --- | ----------------- |
| 百度百科      | 18% | 实际搜索验证品牌词条存在性与完整性 |
| 微信公众号/搜一搜 | 18% | 实际搜索验证官方账号与内容     |
| 小红书       | 14% | 实际搜索验证品牌内容与用户讨论   |
| 抖音        | 12% | 实际搜索验证官方账号与视频内容   |
| 快手        | 8%  | 实际搜索验证短视频内容       |
| B站        | 10% | 实际搜索验证测评/教程/对比内容  |
| 知乎        | 10% | 实际搜索验证话题热度与官方回答   |
| 微博        | 5%  | 实际搜索验证官方账号与大 V 提及 |
| 百度知道/贴吧   | 5%  | 实际搜索验证基础问答与风险点    |
| 企查查/天眼查   | 附加  | 实际搜索验证企业实体与资质     |


### 验证标准


| 搜索结果        | 状态  | 分数      |
| ----------- | --- | ------- |
| 0 条相关       | 缺失  | 0/100   |
| 1-3 条但不相关   | 缺失  | 0/100   |
| 1-3 条且相关    | 极少  | 20/100  |
| 4-10 条      | 存在  | 50/100  |
| 10+ 条       | 活跃  | 80/100  |
| 10+ 条且有官方认证 | 强势  | 100/100 |


---

## 🌐 项目架构

```
geo-seo-claude-CN/
├── skills/                       # 14 个专项子技能
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
├── install.sh                    # 一键安装脚本（macOS/Linux）
├── install-win.sh                # 一键安装脚本（Windows Git Bash）
├── uninstall.sh                  # 卸载脚本
├── requirements.txt              # Python 依赖
└── README.md                     # 本文件
```

---

## 📁 数据存储

CRM 和报告技能（`/geo prospect`、`/geo proposal`、`/geo compare`）会在本地存储运行数据：

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

## 🛠️ 工作原理

### 完整审计流程

运行 `/geo audit https://example.com` 时：

1. **发现阶段** — 抓取首页，识别业务类型，爬取站点地图
2. **并行分析** — 同时启动 5 个子智能体：
  - AI 可见度（引用度、爬虫权限、llms.txt、**实际搜索验证品牌提及**）
  - 平台分析（豆包、通义千问、百度 AI 搜索就绪度）
  - 技术 SEO（Core Web Vitals、SSR、安全性、移动端）
  - 内容质量（E-E-A-T、可读性、内容新鲜度）
  - Schema 结构化数据（检测、验证、生成）
3. **综合评估** — 汇总各维度得分，生成综合 GEO 评分（0-100）
4. **报告输出** — 输出优先级排序的行动计划及速效优化项

---

## 💼 适用场景


| 场景           | 说明                       |
| ------------ | ------------------------ |
| **GEO 服务机构** | 执行客户审计并生成交付物             |
| **营销团队**     | 监控并提升 AI 搜索可见度           |
| **内容创作者**    | 优化内容以获得 AI 引用            |
| **本地商家**     | 被 AI 助手精准收录              |
| **SaaS 公司**  | 提升在各 AI 平台的实体识别度         |
| **电商**       | 优化商品页面以获得 AI 购物推荐        |
| **企业安全合规**   | 本地化部署，数据不出境，符合中国企业数据安全要求 |


---

## 🗑️ 卸载

```bash
./uninstall.sh
```

或手动删除：

```bash
# Qwen Code
rm -rf ~/.qwen/skills/geo ~/.qwen/skills/geo-* ~/.qwen/agents/geo-*.md

# Claude Code
rm -rf ~/.claude/skills/geo ~/.claude/skills/geo-* ~/.claude/agents/geo-*.md
```

---

## 📝 开源协议

MIT License

---

## 📞 联系

- GitHub: [https://github.com/hanyixu/GEO-Audit-QWEN](https://github.com/hanyixu/GEO-Audit-QWEN)
- 问题反馈: [新建 Issue](https://github.com/hanyixu/GEO-Audit-QWEN/issues)
- 代码贡献: [Fork 并提交 PR](https://github.com/hanyixu/GEO-Audit-QWEN/pulls)
- 开发者：Hanyi


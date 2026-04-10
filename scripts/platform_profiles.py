#!/usr/bin/env python3
"""
Platform profiles used by GEO scanners and skills.

This repo was originally designed around Western platforms (YouTube/Reddit/Wikipedia).
For China deployments, we centralize a CN profile here to keep brand/platform scoring
consistent across scripts and skill prompts.
"""

from __future__ import annotations

from dataclasses import dataclass
from urllib.parse import quote_plus


@dataclass(frozen=True)
class PlatformCheck:
    key: str
    name_zh: str
    name_en: str
    weight: float  # 0..1
    search_urls: tuple[str, ...]
    check_points_zh: tuple[str, ...]
    quick_wins_zh: tuple[str, ...]


def _baidu_web_search(q: str) -> str:
    return f"https://www.baidu.com/s?wd={quote_plus(q)}"


def _sogou_weixin_search(q: str) -> str:
    return f"https://weixin.sogou.com/weixin?type=2&query={quote_plus(q)}"


def get_cn_brand_platform_checks(brand_name: str, domain: str | None = None) -> tuple[PlatformCheck, ...]:
    """
    CN-centric brand authority/mention checks.

    Note: many CN platforms have anti-bot measures. We intentionally provide search URLs
    and human-verifiable checkpoints rather than brittle scraping.
    """
    brand = brand_name.strip()
    domain_hint = f" {domain}" if domain else ""

    checks: list[PlatformCheck] = [
        PlatformCheck(
            key="baike",
            name_zh="百度百科",
            name_en="Baidu Baike",
            weight=0.18,
            search_urls=(
                _baidu_web_search(f"{brand} 百度百科"),
                f"https://baike.baidu.com/search/word?word={quote_plus(brand)}",
            ),
            check_points_zh=(
                "是否存在品牌/公司/产品的百科词条（标题与主体一致）",
                "词条信息是否完整：成立时间、所在地、主营业务、官网、产品/服务、品牌别名",
                "是否有权威来源引用（新闻、协会、媒体、公开资料）",
            ),
            quick_wins_zh=(
                "准备可公开引用的权威材料（媒体报道/备案信息/工商公开信息/白皮书）",
                "统一品牌中文名/英文名/简称，确保与官网一致（含 Logo、介绍、联系方式）",
                "在官网 Schema `sameAs` 中补齐百科/社媒链接（若已有）",
            ),
        ),
        PlatformCheck(
            key="weixin_mp",
            name_zh="微信公众号/搜一搜",
            name_en="WeChat Official Accounts",
            weight=0.18,
            search_urls=(
                _sogou_weixin_search(f"{brand}{domain_hint}"),
                _baidu_web_search(f"{brand} 公众号"),
            ),
            check_points_zh=(
                "是否有官方公众号（认证/主体一致）",
                "是否有“品牌故事/关于我们/产品说明/常见问题/案例”类长文沉淀",
                "是否能被搜一搜/第三方搜索稳定检索到（标题、摘要、关键词覆盖）",
            ),
            quick_wins_zh=(
                "用“问答式小标题 + 直接回答 + 细节补充”的结构重写关键文章（利于引用）",
                "为每篇文章补齐：发布日期/更新日期/作者/参考来源",
                "在官网增加“媒体/公众号文章合集”入口，形成可抓取的聚合页",
            ),
        ),
        PlatformCheck(
            key="xiaohongshu",
            name_zh="小红书",
            name_en="Xiaohongshu",
            weight=0.14,
            search_urls=(
                _baidu_web_search(f"{brand} 小红书"),
            ),
            check_points_zh=(
                "是否有官方账号/品牌号/门店（若适用）",
                "是否有高互动笔记提及品牌（测评、对比、教程、避坑）",
                "是否出现稳定的“品类词 + 品牌词”组合（例如“XX怎么选 + 品牌”）",
            ),
            quick_wins_zh=(
                "建立“教程/对比/清单/避坑”四类内容矩阵，标题包含品类词+品牌词",
                "准备可复用的核心卖点段落（100-180字），便于被二次引用/转述",
                "引导真实用户 UGC（注意合规），沉淀常见问题与统一回应口径",
            ),
        ),
        PlatformCheck(
            key="douyin",
            name_zh="抖音",
            name_en="Douyin",
            weight=0.12,
            search_urls=(
                _baidu_web_search(f"{brand} 抖音"),
            ),
            check_points_zh=(
                "是否有官方账号/蓝V（若适用）",
                "是否有第三方测评/对比/教程视频提及品牌",
                "视频标题/字幕/口播是否清晰包含品牌词与核心品类词",
            ),
            quick_wins_zh=(
                "制作“问题-答案-步骤/对比-结论”结构短视频，字幕包含关键事实点",
                "在简介/置顶视频/合集里补齐：官网、客服、核心产品页链接",
                "统一品牌词写法（中文/英文/简称），避免同义分裂",
            ),
        ),
        PlatformCheck(
            key="kuaishou",
            name_zh="快手",
            name_en="Kuaishou",
            weight=0.08,
            search_urls=(
                _baidu_web_search(f"{brand} 快手"),
            ),
            check_points_zh=(
                "是否有官方账号（若适用）",
                "是否有真实场景内容/用户讨论提及品牌",
            ),
            quick_wins_zh=(
                "用真实场景演示+对比方式表达卖点（更贴近快手生态）",
                "沉淀可复用的口播脚本与字幕关键词列表",
            ),
        ),
        PlatformCheck(
            key="bilibili",
            name_zh="B站",
            name_en="Bilibili",
            weight=0.10,
            search_urls=(
                _baidu_web_search(f"{brand} B站"),
                _baidu_web_search(f"{brand} bilibili"),
            ),
            check_points_zh=(
                "是否有深度测评/教程/对比视频提及品牌（标题/简介/字幕）",
                "是否有关键视频被收藏/投币/评论（代表讨论与认可）",
            ),
            quick_wins_zh=(
                "优先做长内容：测评/对比/教程，简介补齐参数/链接/FAQ",
                "把可引用的关键结论做成“总结段落/时间轴章节”",
            ),
        ),
        PlatformCheck(
            key="zhihu",
            name_zh="知乎",
            name_en="Zhihu",
            weight=0.10,
            search_urls=(
                _baidu_web_search(f"{brand} 知乎"),
                _baidu_web_search(f"{brand} 怎么样 知乎"),
            ),
            check_points_zh=(
                "是否在高相关问题下被提及（品类词/对比/推荐）",
                "回答是否包含清晰的可引用结论（定义、优缺点、场景建议、数据/参数）",
            ),
            quick_wins_zh=(
                "占位 10-20 个高意图问题（“怎么选/哪个好/避坑/对比”），统一品牌事实口径",
                "为回答加入结构化信息：小标题、列表、表格、参数与来源",
            ),
        ),
        PlatformCheck(
            key="weibo",
            name_zh="微博",
            name_en="Weibo",
            weight=0.05,
            search_urls=(
                _baidu_web_search(f"{brand} 微博"),
            ),
            check_points_zh=(
                "是否有认证账号（若适用）",
                "是否有媒体/大V提及品牌（非自说自话）",
            ),
            quick_wins_zh=(
                "把“品牌事实信息卡”（成立时间/主营/官网/联系方式）固定在置顶内容",
                "与行业媒体/账号做联合内容，争取第三方引用",
            ),
        ),
        PlatformCheck(
            key="baidu_qa_forums",
            name_zh="百度知道/贴吧",
            name_en="Baidu Zhidao/Tieba",
            weight=0.05,
            search_urls=(
                _baidu_web_search(f"{brand} 百度知道"),
                _baidu_web_search(f"{brand} 贴吧"),
            ),
            check_points_zh=(
                "是否有“品牌+品类词”相关问答/讨论能被检索到",
                "讨论内容是否存在明显负面风险点（售后/质量/欺诈等）",
            ),
            quick_wins_zh=(
                "整理官方 FAQ 与统一回应口径，减少信息噪音与误解",
                "对负面风险点建立处理流程（客服、声明、整改进度可公开）",
            ),
        ),
    ]

    total = sum(c.weight for c in checks) or 1.0
    if abs(total - 1.0) > 1e-6:
        checks = [
            PlatformCheck(
                key=c.key,
                name_zh=c.name_zh,
                name_en=c.name_en,
                weight=c.weight / total,
                search_urls=c.search_urls,
                check_points_zh=c.check_points_zh,
                quick_wins_zh=c.quick_wins_zh,
            )
            for c in checks
        ]

    return tuple(checks)


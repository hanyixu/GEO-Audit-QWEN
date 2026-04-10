#!/usr/bin/env python3
"""
Brand Mention Scanner (CN) — Checks brand presence across China platforms that
influence AI assistants’ entity recognition and recommendations.

Western sources like Wikipedia/Reddit/YouTube are often unreliable in China networks.
This script outputs a CN platform checklist + weights + actions (no brittle scraping).
"""

import sys
import json
from datetime import datetime

from platform_profiles import get_cn_brand_platform_checks


def generate_brand_report(brand_name: str, domain: str = None) -> dict:
    """Generate a CN-centric brand mention plan (no fragile scraping)."""
    platforms = []
    for c in get_cn_brand_platform_checks(brand_name=brand_name, domain=domain):
        platforms.append(
            {
                "key": c.key,
                "platform_zh": c.name_zh,
                "platform_en": c.name_en,
                "weight": round(c.weight, 4),
                "search_urls": list(c.search_urls),
                "check_points_zh": list(c.check_points_zh),
                "quick_wins_zh": list(c.quick_wins_zh),
            }
        )

    report = {
        "mode": "CN",
        "brand_name": brand_name,
        "domain": domain,
        "analysis_date": datetime.now().strftime("%Y-%m-%d"),
        "key_insight_zh": "在 AI 推荐与引用场景中，跨平台品牌提及（尤其是百科/内容平台/问答讨论）通常比单纯外链更能影响实体识别与信任。",
        "brand_authority_model": {
            "note_zh": "该脚本输出的是“检查清单 + 权重模型”。由于多数平台反爬严格，默认不做自动抓取，避免不稳定与账号风险。",
            "weights_sum": round(sum(p["weight"] for p in platforms), 4),
        },
        "platforms": platforms,
        "overall_recommendations_zh": [
            "先做实体打底：统一品牌名称口径（中文/英文/简称）+ 官网“关于我们/资质/联系方式/时间线”完善 + Schema sameAs 补齐。",
            "用“可引用内容块”重写核心介绍：100-180 字一段，事实密度高、可独立理解（适合被 AI 摘录）。",
            "建立内容矩阵：教程/对比/清单/避坑 + FAQ，覆盖高意图问题（怎么选/哪个好/靠谱吗/价格/售后）。",
            "优先打通三大生态：腾讯（公众号/视频号/搜一搜）、字节（抖音/头条系）、阿里（千问相关内容分发与站内外一致性）。",
        ],
    }
    return report


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python brand_scanner.py <brand_name> [domain]")
        print("Example: python brand_scanner.py '某某品牌' example.com")
        sys.exit(1)

    brand = sys.argv[1]
    domain = sys.argv[2] if len(sys.argv) > 2 else None

    result = generate_brand_report(brand, domain)
    print(json.dumps(result, indent=2, default=str))

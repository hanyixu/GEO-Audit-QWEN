import os

from dotenv import load_dotenv
from openai import OpenAI


class QwenClient:
    def __init__(self) -> None:
        load_dotenv()
        api_key = os.getenv("DASHSCOPE_API_KEY", "").strip()
        if not api_key:
            raise ValueError("DASHSCOPE_API_KEY is required")

        base_url = os.getenv(
            "DASHSCOPE_BASE_URL",
            "https://dashscope.aliyuncs.com/compatible-mode/v1",
        ).strip()
        model = os.getenv("QWEN_MODEL", "qwen-plus").strip()

        self.model = model
        self.client = OpenAI(api_key=api_key, base_url=base_url)

    def audit_content(self, content: str, system_prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            temperature=0.2,
            messages=[
                {"role": "system", "content": system_prompt},
                {
                    "role": "user",
                    "content": (
                        "Audit the following content based on GEO skill logic.\n\n"
                        f"{content}"
                    ),
                },
            ],
        )
        result = response.choices[0].message.content
        return result.strip() if result else ""

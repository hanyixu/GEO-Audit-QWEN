from pathlib import Path
from typing import List, Optional, Tuple


def _skills_root() -> Path:
    return Path(__file__).resolve().parents[2] / "skills"


def available_skills() -> List[str]:
    skills_dir = _skills_root()
    if not skills_dir.exists():
        return []

    names: List[str] = []
    for entry in skills_dir.iterdir():
        if entry.is_dir() and (entry / "SKILL.md").exists():
            names.append(entry.name)
    return sorted(names)


def _normalize_name(value: str) -> str:
    return value.strip().lower().replace("_", "-")


def load_skills_as_system_prompt(
    focus_areas: Optional[List[str]] = None,
) -> Tuple[str, List[str]]:
    skills_dir = _skills_root()
    if not skills_dir.exists():
        raise ValueError("Skills directory is missing")

    all_skills = available_skills()
    selected = all_skills

    if focus_areas:
        available_map = {_normalize_name(name): name for name in all_skills}
        selected = []
        missing = []
        for item in focus_areas:
            key = _normalize_name(item)
            if key in available_map:
                selected.append(available_map[key])
            else:
                missing.append(item)
        if missing:
            raise ValueError(
                f"Unknown focus_areas: {', '.join(missing)}. "
                f"Available: {', '.join(all_skills)}"
            )

    sections: List[str] = []
    for skill_name in selected:
        skill_path = skills_dir / skill_name / "SKILL.md"
        if not skill_path.exists():
            continue
        content = skill_path.read_text(encoding="utf-8").strip()
        sections.append(f"## Skill: {skill_name}\n{content}")

    system_prompt = (
        "You are a GEO audit specialist.\n"
        "You must follow the skill instructions below when auditing content.\n"
        "If instructions conflict, prefer the most relevant skill to the request.\n\n"
        + "\n\n".join(sections)
    )

    return system_prompt, selected

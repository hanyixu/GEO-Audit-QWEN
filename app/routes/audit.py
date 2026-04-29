from fastapi import APIRouter, HTTPException

from app.models.schemas import AuditRequest, AuditResponse
from app.services.qwen_client import QwenClient
from app.services.skills_loader import load_skills_as_system_prompt

router = APIRouter(prefix="/v1", tags=["audit"])


@router.post("/audit", response_model=AuditResponse)
async def create_audit(request: AuditRequest) -> AuditResponse:
    try:
        system_prompt, used_focus_areas = load_skills_as_system_prompt(
            request.focus_areas
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    try:
        client = QwenClient()
        result = client.audit_content(request.content, system_prompt)
    except ValueError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail=f"QWEN API request failed: {exc}",
        ) from exc

    return AuditResponse(result=result, used_focus_areas=used_focus_areas)

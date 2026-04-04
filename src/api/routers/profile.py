from fastapi import APIRouter
from src.schemas.profile import ProfilePublicResponse
from src.schemas.resume import ProfileResumeResponse

from src.services.mock_profile import get_profile_public
from src.services.mock_resume import get_profile_resume

router = APIRouter(prefix = "/profiles", tags=["profiles"])

@router.get("/{username}", response_model=ProfilePublicResponse)
def get_public_profile(username: str):
    return get_profile_public(username)

@router.get("/{username}/resume", response_model=ProfileResumeResponse)
def get_resume_profile(username: str):
    return get_profile_resume(username)
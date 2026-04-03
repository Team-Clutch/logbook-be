from fastapi import APIRouter
from src.schemas.profile import ProfilePublicResponse
from src.services.mock_profile import get_profile_public

router = APIRouter(prefix = "/profiles", tags=["profiles"])

@router.get("/{username}", response_model=ProfilePublicResponse)
def get_public_profile(username: str):
    return get_profile_public(username)
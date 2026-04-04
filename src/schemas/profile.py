from pydantic import BaseModel


class Award(BaseModel):
    title: str
    description: str
    awardedAt: str


class Career(BaseModel):
    title: str
    organization: str
    description: str
    startedAt: str
    endedAt: str


class PublicUser(BaseModel):
    username: str
    displayName: str
    profileImg: str
    headline: str
    keywords: list[str]
    skills: list[str]
    links: dict[str, str]
    awards: list[Award]
    careers: list[Career]


class FeaturedPost(BaseModel):
    projectId: str
    finalPostId: str
    slug: str
    title: str
    summary: str
    tags: list[str]


class ProfilePublicResponse(BaseModel):
    user: PublicUser
    featuredPosts: list[FeaturedPost]

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


class Contact(BaseModel):
    email: str
    phone: str
    address: dict[str, str]


class Personal(BaseModel):
    born: str
    militaryService: str


class Education(BaseModel):
    title: str
    organization: str
    major: str
    startedAt: str
    endedAt: str


class Qualification(BaseModel):
    title: str
    awardedAt: str


class ResumeUser(BaseModel):
    username: str
    displayName: str
    profileImg: str
    headline: str


class FeaturedPostRef(BaseModel):
    projectId: str
    finalPostId: str


class ProfileResumeResponse(BaseModel):
    user: ResumeUser
    contact: Contact
    personal: Personal
    educations: list[Education]
    careers: list[Career]
    qualifications: list[Qualification]
    skills: list[str]
    links: dict[str, str]
    featuredPostRefs: list[FeaturedPostRef]

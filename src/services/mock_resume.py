from src.schemas.resume import ProfileResumeResponse

PROFILE_RESUME_MOCK = {
  "user": {
    "username": "honggildong",
    "displayName": "홍길동",
    "profileImg": "https://example.com/images/profile-honggildong.png",
    "headline": "Full-stack developer building clean, reliable systems"
  },
  "contact": {
    "email": "hong@example.com",
    "phone": "010-0000-0000",
    "address": {
      "zipcode": "12345",
      "baseAddress": "Seoul",
      "detailAddress": "101-202",
      "extraAddress": "Gangnam-gu"
    }
  },
  "personal": {
    "born": "1999-01-01",
    "militaryService": "completed"
  },
  "educations": [
    {
      "title": "B.S. in Computer Science",
      "organization": "Kangwon National University",
      "major": "Computer Science",
      "startedAt": "2015-03-01T00:00:00Z",
      "endedAt": "2019-02-28T00:00:00Z"
    }
  ],
  "careers": [
    {
      "title": "Backend Engineer",
      "organization": "Naver",
      "description": "Built internal tools and API services for content operations.",
      "startedAt": "2019-01-01T00:00:00Z",
      "endedAt": "2022-12-31T00:00:00Z"
    }
  ],
  "qualifications": [
    {
      "title": "정보처리기사",
      "awardedAt": "2020-08-01T00:00:00Z"
    },
    {
      "title": "정보보안기사",
      "awardedAt": "2021-06-01T00:00:00Z"
    }
  ],
  "skills": [
    "React",
    "TypeScript",
    "Node.js",
    "AWS"
  ],
  "links": {
    "github": "https://github.com/honggildong",
    "tistory": "https://honggildong.tistory.com"
  },
  "featuredPostRefs": [
    {
      "projectId": "projectTelegramSummarizer",
      "finalPostId": "postTelegramSummarizerFinal"
    },
    {
      "projectId": "projectExamReportAutomation",
      "finalPostId": "postExamReportAutomationFinal"
    }
  ]
}

def get_profile_resume(username: str) -> dict:
    # mock 단계라 username 검증 작없 없이 그대로 반환해도 됨
    return PROFILE_RESUME_MOCK
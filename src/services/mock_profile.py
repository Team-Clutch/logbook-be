from src.schemas.profile import ProfilePublicResponse

PROFILE_PUBLIC_MOCK = {
    "user": {
        "username": "honggildong",
        "displayName": "홍길동",
        "profileImg": "https://example.com/images/profile-honggildong.png",
        "headline": "Full-stack developer building clean, reliable systems",
        "keywords": ["efficiency", "scalability", "empathy"],
        "skills": ["React", "TypeScript", "Node.js", "AWS"],
        "links": {
            "github": "https://github.com/honggildong",
            "tistory": "https://honggildong.tistory.com"
        },
        "awards": [
            {
                "title": "1st Place Global",
                "description": "Project: EcoStream AI",
                "awardedAt": "2025-11-01T00:00:00Z"
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
        ]
    },
    "featuredPosts": [
        {
            "projectId": "projectTelegramSummarizer",
            "finalPostId": "postTelegramSummarizerFinal",
            "slug": "telegram-summarizer-bot",
            "title": "Telegram Summarizer Bot",
            "summary": "텔레그램 채팅을 요약하고 핵심 맥락을 정리하는 자동화 봇 프로젝트",
            "tags": ["python", "AWS", "LLM(Google Gemini)"]
        }
    ]
}

def get_profile_public(username: str) -> dict:
    # mock 단계라 username 검증 작업없이 그대로 반환해도 됨.
    return PROFILE_PUBLIC_MOCK
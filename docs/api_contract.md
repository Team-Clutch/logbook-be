# API Contract

## Purpose
- LOGbook MVP의 mock API 계약을 정의한다.
- 프론트엔드와 백엔드가 동일한 request/response shape를 공유한다.

## Common Rules
- JSON field naming은 camelCase를 사용한다.
- public 식별자는 username, postId, projectId를 사용한다.
- slug는 URL/SEO용 보조 식별자다.
- 기간 데이터는 YYYY-MM 형식을 사용한다.
- 이벤트 시각은 UTC ISO 8601 형식을 사용한다.
- 댓글 수 대신 reactionCount를 사용한다.
- DTO reference base path: `docs/dto_drafts/`


## Endpoints

### GET /health
- 설명: 서버 상태를 확인하는 API
- response:
    - `200 OK`
    - body:
    ```json
    {
        "status": "ok"
    }
    ```
- notes:
    - health check의 1차 판단 기준은 HTTP status code.
    - json body는 개발자와 디버깅을 위한 보조 정보.

### GET /profiles/{username}
- 설명: 등록된 유저명을 인자로하여 프로필을 반환하는 API
- path params: `username`
- response DTO: `profile-public-dto.json`

### GET /profiles/{username}/resume
- 설명: 등록된 유저명을 인자로하여 프로필에 기반한 이력서를 반환하는 API
- path params: `username`
    - `username`: (`string`)
- response DTO: `profile-resume-dto.json`

### GET /posts/{postId}/{slug}
- 설명: 게시글의 아이디와 슬러그를 이용해서 해당 게시글의 내용을 반환하는 API
- path params: `postId`, `slug`
    - `postId`: (`string`) 백엔드에서 자동으로 생성되어 할당된 암호화 코드 형태를 갖는다.
    - `slug`: (`string`) 자연어 기반의 인간이나 봇에게 식별가능한 SEO 친화적 형태를 갖는다. 
- response DTO: `post-detail-dto.json`
- notes:

### GET /board
- 설명: 게시판의 내용을 반환하는 API
- query params:
    - `sort`: `publishedAtDesc(default) | publishedAtAsc | viewCountDesc | viewCountAsc | reactionCountDesc | reactionCountAsc`
    - `tab`: `projects(default) | posts | all`
    - `cursor`: pagination cursor string (optional)
    - `limit`: `number` - `12(default) | 50(max) | 8(min)`
- response DTO: `board-list-dto.json`
- notes:
    - `projects` 탭은 `type = projectFinal`만 반환한다.
    - `posts` 탭은 `type = devlog`만 반환한다.
    - `all` 탭은 두 타입을 모두 반환할 수 있다.

## DTO References
- profile-public-dto.json
- profile-resume-dto.json
- post-detail-dto.json
- board-list-dto.json

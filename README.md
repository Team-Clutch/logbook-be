# logbook-be

LOGbook MVP 백엔드 레포지토리.

## Requirements

- Python 3.11
- Poetry

## Setup

프로젝트 루트에서 아래 명령을 실행.

```powershell
poetry install
```

Poetry가 어떤 Python 버전을 선택했는지 확인하는 법:

```powershell
poetry env info
```

## Run

반드시 **프로젝트 루트**에서 실행.

```powershell
cd .\logbook-be
poetry run uvicorn src.main:app --reload
```

## Important

이 프로젝트는 `src` 레이아웃을 사용.

따라서 아래처럼 `src` 디렉터리 안으로 들어가서 실행하면 import 에러가 날 수 있음.

```powershell
cd .\logbook-be\src
poetry run uvicorn main:app --reload
```

*위 방식은 사용하지 않음.*

## API Docs

서버 실행 후 아래 경로에서 OpenAPI 문서를 확인할 수 있음.

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- OpenAPI JSON: [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json)

## Contract Documents

- API 계약 문서: [docs/api_contract.md](docs/api_contract.md)
- DTO 초안: [docs/dto_drafts](docs/dto_drafts)

현재 구현은 계약 문서를 기준으로 진행, 브랜치에 따라 mock API 구현 상태가 일부 다를 수 있음.

## Project Structure

```text
src/
  api/
    routers/      # FastAPI 라우터
  core/           # 설정 / 환경 관련 코드
  models/         # 추후 DB 모델
  schemas/        # Pydantic request/response schema
  services/       # mock data / business logic
  main.py         # FastAPI 앱 진입점
docs/
  api_contract.md
  dto_drafts/
```

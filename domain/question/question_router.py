from fastapi import APIRouter
from domain.question.question_schema import Question

# /api/question 경로의 엔드포인트를 그룹화하는 라우터 생성
router = APIRouter(
    prefix="/api/question",
    tags=["question"],  # Swagger UI에서 카테고리 태그로 표시됩니다.
)


@router.get("/list", response_model=list[Question])
def question_list():
    """질문 목록을 조회하는 API 엔드포인트"""
    # 더미 데이터 반환 (추후 DB 연결 단계에서 SQLAlchemy 데이터로 대체됩니다)
    sample_data = [
        {"id": 1, "subject": "FastAPI 질문입니다", "content": "FastAPI 질문 내용입니다."},
        {"id": 2, "subject": "점프 투 FastAPI 질문", "content": "교재 실습 진행 중입니다."},
    ]
    return sample_data
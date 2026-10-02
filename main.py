from fastapi import FastAPI
from domain.question import question_router

app = FastAPI(
    title="Jump to FastAPI API",
    description="점프 투 FastAPI 교재 실습 프로젝트",
    version="0.1.0",
)


@app.get("/")
def index():
    return {"message": "Jump to FastAPI backend server is running!"}


# 분리한 question 라우터를 메인 앱에 포함
app.include_router(question_router.router)
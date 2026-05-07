from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

import shutil
import os

from parser import parse_resume

from generate_questions import generate_questions
from follow_up import generate_follow_up_question
from analyze_interview import analyze_interview

app = FastAPI()

# =========================
# CORS
# =========================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# REQUEST MODEL
# =========================

class QuestionRequest(BaseModel):

    skills: list

    company: str

# ========================
# FOLLOW-UP QUESTION REQUEST MODEL
# ========================

class FollowUpRequest(BaseModel):

    previous_question: str

    user_answer: str

    skills: list

    company: str


# =========================
# ANALYTICS
# =========================

class AnalysisRequest(BaseModel):

    questions: list

    answers: list

# =========================
# UPLOAD FOLDER
# =========================

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# =========================
# HOME API
# =========================

@app.get("/")
def home():

    return {
        "message": "API Running"
    }

# =========================
# RESUME PARSER API
# =========================

@app.post("/parse-resume")
async def parse_resume_api(
        file: UploadFile = File(...)
):

    file_path = f"{UPLOAD_FOLDER}/{file.filename}"

    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(file.file, buffer)

    result = parse_resume(file_path)

    return {

        "status": "success",

        "data": result
    }

# =========================
# QUESTION GENERATOR API
# =========================

@app.post("/generate-questions")
def generate_questions_api(
        request: QuestionRequest
):

    questions = generate_questions(

        request.skills,

        request.company

    )

    return {

        "status": "success",

        "questions": questions

    }


# =========================
# FOLLOW-UP QUESTION API
# =========================

@app.post("/generate-followup")
def generate_followup_api(
        request: FollowUpRequest
):

    followup_question = generate_follow_up_question(

        request.previous_question,

        request.user_answer,

        request.skills,

        request.company
    )

    return {

        "status": "success",

        "followup_question": followup_question

    }

@app.post("/analyze-interview")
def analyze_interview_api(
        request: AnalysisRequest
):

    result = analyze_interview(

        request.questions,

        request.answers

    )

    return {

        "status": "success",

        "analysis": result

    }
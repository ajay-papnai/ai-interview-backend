from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

import shutil
import os

from parser import parse_resume

app = FastAPI(
    title="AI Interview Resume Parser API"
)

# =========================
# CORS CONFIG
# =========================

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],

)

# =========================
# UPLOAD FOLDER
# =========================

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# =========================
# HOME ROUTE
# =========================

@app.get("/")
def home():

    return {

        "status": "success",

        "message": "Resume Parser API Running"

    }

# =========================
# RESUME PARSER API
# =========================

@app.post("/parse-resume")
async def parse_resume_api(
        file: UploadFile = File(...)
):

    try:

        # Validate PDF

        if not file.filename.endswith(".pdf"):

            return {

                "status": "error",

                "message": "Only PDF files allowed"

            }

        # Save file

        file_path = os.path.join(
            UPLOAD_FOLDER,
            file.filename
        )

        with open(file_path, "wb") as buffer:

            shutil.copyfileobj(file.file, buffer)

        # Parse Resume

        result = parse_resume(file_path)

        # Delete uploaded file after parsing

        if os.path.exists(file_path):
            os.remove(file_path)

        return {

            "status": "success",

            "data": result

        }

    except Exception as e:

        return {

            "status": "error",

            "message": str(e)

        }
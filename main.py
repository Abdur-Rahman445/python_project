from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# ----------- DATA STORE -----------
students = {}
courses = {}

# ----------- MODELS -----------
class Student(BaseModel):
    roll: str
    name: str

class Course(BaseModel):
    course_id: str
    title: str
    credits: int

class Enrollment(BaseModel):
    roll: str
    course_id: str


# ----------- FUNCTIONS -----------
def calculate_total_credits(course_ids):
    total = 0
    for cid in course_ids:
        total += courses[cid]["credits"]
    return total


# ----------- API ROUTES -----------

@app.get("/")
def home():
    return {"message": "Course Enrollment System API Running!"}


# 1. Add Student
@app.post("/add-student")
def add_student(data: Student):
    if data.roll in students:
        raise HTTPException(status_code=400, detail="Student already exists")

    students[data.roll] = {
        "name": data.name,
        "courses": [],
        "total_credits": 0
    }
    return {"message": "Student added successfully", "student": students[data.roll]}


# 2. Add Course
@app.post("/add-course")
def add_course(data: Course):
    if data.course_id in courses:
        raise HTTPException(status_code=400, detail="Course already exists")

    courses[data.course_id] = {
        "title": data.title,
        "credits": data.credits
    }
    return {"message": "Course added successfully", "course": courses[data.course_id]}


# 3. Enroll Student in Course
@app.post("/enroll")
def enroll_student(data: Enrollment):
    if data.roll not in students:
        raise HTTPException(status_code=404, detail="Student not found")

    if data.course_id not in courses:
        raise HTTPException(status_code=404, detail="Course not found")

    if data.course_id in students[data.roll]["courses"]:
        raise HTTPException(status_code=400, detail="Student already enrolled in this course")

    students[data.roll]["courses"].append(data.course_id)
    students[data.roll]["total_credits"] = calculate_total_credits(
        students[data.roll]["courses"]
    )

    return {
        "message": "Enrollment successful",
        "student": students[data.roll]
    }


# 4. View a Student
@app.get("/student/{roll}")
def get_student(roll: str):
    if roll not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return students[roll]


# 5. View All Students
@app.get("/all-students")
def all_students():
    return students


# 6. View All Courses
@app.get("/all-courses")
def all_courses():
    return courses

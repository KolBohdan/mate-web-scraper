from dataclasses import dataclass, fields
from app.enums import CourseType


@dataclass
class Course:
    name: str
    short_description: str
    course_type: CourseType
    num_of_modules: int
    num_of_topics: int
    duration: str


COURSE_FIELDS = [field.name for field in fields(Course)]

from abc import ABC, abstractmethod
from typing import List,Dict
from datetime import datetime
import logging
import json

logging.basicConfig(level=logging.INFO,format="%(asctime)s-%(levelname)s-%(messages)s")
logger=logging.getLogger(__name__)

#---------EXCEPTIONS-----------------

class StudentNotFoundException(Exception):
    pass
class CourseNotFoundException(Exception):
    pass
class GradeNotFoundException(Exception):
    pass
class GradeAlreadyExistsException(Exception):
    pass
class StudentAlreadyExistsException(Exception):
    pass
class CourseAlreadyExistsException(Exception):
    pass

#---------DOMAIN MODELS---------
class Student:
    def __init__(self,student_id:str,student_name:str,student_email:str,student_year:int):
        self.student_id=student_id
        self.student_name=student_name
        self.student_email=student_email
        self.student_year=student_year
        
        
class Course:
    def __init__(self,course_id:str,course_name:str,course_credits:int):
        self.course_id=course_id
        self.course_name=course_name
        self.course_credits=course_credits
            
    
class Grade:
    def __init__(self,student:Student,course:Course,grade_value:float):
        self.student=student
        self.course=course
        self.grade_value=grade_value
        
        
    def weighted_score(self)->float:
        return self.grade_value * self.course.course_credits
    
   


class StudentRepository(ABC):
    @abstractmethod
    def add_student(self,student:Student):
        pass
    
    @abstractmethod
    def get_student(self,student_id:str)->Student:
        pass    
    
    def get_all_students(self)->List[Student]:
        pass
    
class CourseRepository(ABC):
    @abstractmethod
    def add_course(self,course:Course):
        pass
    
    @abstractmethod
    def get_course(self,course_id:str)->Course:
        pass    
    
    def get_all_courses(self)->List[Course]:
        pass

class GradeRepository(ABC):
    @abstractmethod
    def add_grade(self,grade:Grade):
        pass
    
    @abstractmethod
    def get_grade(self,student_id:str,course_id:str)->Grade:
        pass    
    
    def get_all_grades(self)->List[Grade]:
        pass
    

    
#--------IN MEMORY REPOSITORIES-----------------

class InMemoryStudentRepository(StudentRepository):
    def __init__(self):
        self.students:Dict[str,Student]={}
        
    def add_student(self,student:Student)->None:
        if student.student_id in self.students:
            logger.error(f"Student with id {student.student_id} already exists.")
            raise StudentAlreadyExistsException(f"Student with id {student.student_id} already exists.")
        self.students[student.student_id]=student
        logger.info(f"Student with id {student.student_id} added successfully.")

    def get_student(self,student_id)->Student:
        if student_id not in self.students:
            logger.error(f"Student with id {student_id} not found.")
            raise StudentNotFoundException(f"Student with id {student_id} not found.")
        return self.students[student_id]
    
    def get_all_students(self)->List[Student]:
        return list(self.students.values())

        
        
class InMemoryCourseRepository(CourseRepository):
    def __init__(self):
        self.course:Dict[str,Course]={}
    
    def add_course(self,course:Course)->None:
        if course.course_id in self.course:
            logger.error(f"Course with ID :{course.course_id}already exists.")
            raise CourseAlreadyExistsException(f"Course with ID :{course.course_id}already exists.")
        self.course[course.course_id]=course
        logger.info(f"Course with ID:{course.course_id}added successfully.")
        
    def get_course(self,course_id:str)->Course:
        if course_id not in self.course:
            logger.error(f"Course with ID:{course_id}not found.")
            raise CourseNotFoundException(f"Course with ID:{course_id}not found.")
        return self.course[course_id]
    def get_all_courses(self)->List[Course]:
        return list(self.course.values())
    
    
class InMemoryGradeRepository(GradeRepository):
    def __init__(self):
        self.grades:Dict[str,Grade]={}
        
    def add_grade(self,grade:Grade)->None:
        key=f"{grade.student.student_id}_{grade.course.course_id}"
        if key in self.grades:
            logger.error(f"Grade for student {grade.student.student_id} in course {grade.course.course_id} already exists.")
            raise GradeAlreadyExistsException(f"Grade for student {grade.student.student_id} in course {grade.course.course_id} already exists.")
        self.grades[key]=grade
        logger.info(f"Grade for student {grade.student.student_id} in course {grade.course.course_id} added successfully.")
        
    def get_grade(self,student_id:str,course_id:str)->Grade:
        key=f"{student_id}_{course_id}"
        if key not in self.grades:
            logger.error(f"Grade for student {student_id} in course {course_id} not found.")
            raise GradeNotFoundException(f"Grade for student {student_id} in course {course_id} not found.")
        return self.grades[key]
    
    def get_all_grades(self)->List[Grade]:
        return list(self.grades.values())
    
    
#--------GRADING SYSTEM SERVICE-----------------
class GradingSystemManager:
    def __init__(self,student_repo:StudentRepository,course_repo:CourseRepository,grade_repo:GradeRepository):
        self.student_repo=student_repo
        self.course_repo=course_repo
        self.grade_repo=grade_repo
        
    def register_student(self,student_id:str,student_name:str,student_email:str,student_year:int):
        student=Student(student_id,student_name,student_email,student_year)
        self.student_repo.add_students(student)
        
    def register_course(self,course_id:str,course_name:str,course_credits:int):
        course=Course(course_id,course_name,course_credits)
        self.course_repo.add_course(course)

    def assign_grade(self):
        pass
    
    def send_grade_report(self):
        pass
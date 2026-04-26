#This exercise illustrates the difference between shallow copy and deep copy. Deep copy separates booth student 1 and student 3
#whilst shallow copy , makes changes to both student 1 and student 2

import copy 

class Student:
  def __init__(self,name,student_id,grade,courses):
    self.name=name
    self.student_id=student_id
    self.grade=grade
    self.courses=courses


  def __repr__(self):
    return f"Student:Name:{self.name},ID:{self.student_id},grade:{self.grade},courses:{self.courses}"



student1=Student("Martha",113608,6,["Maths","Physics","Geography"])
student2=copy.copy(student1)
student2.courses.append("Computers")
print(student1)
print(student2)


student3=copy.deepcopy(student1)
student3.courses.append("Biology")

print(student1)
print(student3)
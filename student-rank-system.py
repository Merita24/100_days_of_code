import json

    

def rank_students(student_list):
    try:
        if not isinstance(student_list,list):
            raise TypeError("Input must be a list of dictionaries")
        for student in student_list:
            if not isinstance(student,dict):
                raise TypeError("Student must be a dictionary")
            if "name" not in student or "score" not in student:
                raise KeyError("Each student must have 'name' and 'score'")
            if not isinstance(student["score"],(int,float)):
                raise ValueError("Student score must be a numeric value")
            
            ranked_students=sorted(student_list,key=lambda x:x["score"],reverse=True)
            ranked_json=json.dumps(ranked_students,indent=4)
            return ranked_json
    except (TypeError,KeyError,ValueError) as e:
        return f"Exception thrown:{e}"
    
    
if __name__=="__main__":
    students=[
    {"name":"Alice","score":89},
    {"name":"Mary","score":64},
    {"name":"Kate","score":95},
    {"name":"Simon","score":82},
    {"name":"Rachel","score":88},
    {"name":"Eugene","score":21},
    {"name":"Trevor","score":24},
    {"name":"Natasha","score":62},
    {"name":"Pete","score":75},
    {"name":"Mercy","score":88},
    {"name":"Brian","score":59},
    {"name":"Tina","score":99},
        ]
    results=rank_students(students)
    print(results)
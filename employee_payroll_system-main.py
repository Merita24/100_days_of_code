import json
class EmployeeContextManager:
    def __init__(self,filename,mode):
        self.filename=filename
        self.mode=mode
        self.file=None
        
    def __enter__(self):
        try:
            self.file=open(self.filename,self.mode)
            return self.file
        except FileNotFoundError:
            print("file not found.....creating a new one")
            if 'w' in self.mode:
                self.file=open(self.filename,self.mode)
                return self.file
            
    def __exit__(self,exc_type,exc_value,traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print(f"An error occurred:{exc_value}")
            return True 
        
        
    
class Employee:
    def __init__(self,name,employee_id,dept):
        self.name=name
        self.employee_id=employee_id
        self.dept=dept
        
    def get_employee_info(self):
        return f"Name:{self.name}, ID:{self.employee_id},Department:{self.dept}"
    
    def to_dict(self):
        return {
            "name":self.name,
            "employee_id":self.employee_id,
            "dept":self.dept
            
        }
    @classmethod   
    def from_dict(cls,data):
        return cls(
            name=data["name"],
            employee_id=data["employee_id"],
            dept=data["dept"]
        )
        
        
class EmployeePayroll:
    def __init__(self):
        self.employees={}
        
        
    def add_employee(self,employee):
        self.employees[employee.employee_id]=employee
        
    def remove_employee(self,employee_id):
        if employee_id in self.employees:
            del self.employees[employee_id]
        else:
            raise ValueError("Employee ID not found")
        
    def calculate_total_compensation(self,salary,tax,benefits):
        tax_amount=salary*tax
        total_compensation=salary - tax_amount + benefits
        return total_compensation
    
    def get_payroll_info(self):
        return f"Employee:{self.employee.get_employee_info()}, Salary:{self.salary},Benefits:{self.benefits}"
    
    def save_to_file(self,filename):
        
        with EmployeeContextManager(filename,'w')as file:
            data={
                 "employees":[emp.to_dict()for emp in self.employees.values()]
                    
            }
                
            json.dump(data,file,indent=4)
            print("Data saved successfully.")
       
    def load_from_file(self,filename):
        try:
            with EmployeeContextManager(filename,'r')as file:
                data=json.load(file)
                for emp_data in data.get("employees",[]):
                    emp=Employee.from_dict(emp_data)
                    self.employees[emp.employee_id]=emp
                print("Data loaded successfully.")
        except FileNotFoundError:
            print("File not found. No data loaded.")
            

if __name__=="__main__":
    payroll_system=EmployeePayroll()
    
    emp1=Employee("Alice",101,"HR")
    emp2=Employee("Bob",102,"IT")
    
    payroll_system.add_employee(emp1)
    payroll_system.add_employee(emp2)
    
    payroll_system.save_to_file("employee_data.json")
    
    new_payroll_system=EmployeePayroll()
    new_payroll_system.load_from_file("employee_data.json")
    
    for emp in new_payroll_system.employees.values():
        print(emp.get_employee_info())
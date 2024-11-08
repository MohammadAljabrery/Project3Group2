import secrets

class SecuritySystem:
    def __init__(self):
        self.security_code = 0000
        self.employee_code = {"emp123" : None, "emp456" : None, "emp789" : None }
           
    def validate_employee_code(self, employee_code):
        return employee_code == self.employee_code
     
    def get_security_code(self, employee_code):
        min_value = 1000
        max_value = 9999        
        security_code = secrets.randbelow(max_value - min_value + 1) + min_value     #self
        self.employee_code[employee_code] = security_code
        return self.security_code
    
    def validate_security_code(self, employee_code, entered_code):
        return self.employee_code.get(employee_code) == entered_code
        

            
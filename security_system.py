import secrets
import os

class SecuritySystem:
    def __init__(self, file_path="employee_codes.txt"):
        self.file_path = file_path
        self.employee_code = self.load_employee_codes()

    def load_employee_codes(self):
        """Load employee codes and their security codes from the file."""
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"The file '{self.file_path}' does not exist.")

        with open(self.file_path, "r") as file:
            lines = file.readlines()

        employee_data = {}
        for line in lines:
            emp_id, code = line.strip().split(":")
            employee_data[emp_id] = int(code) if code != "None" else None

        return employee_data

    def save_employee_codes(self):
        """Save employee codes and their security codes back to the file."""
        with open(self.file_path, "w") as file:
            for emp_id, code in self.employee_code.items():
                code_str = str(code) if code is not None else "None"
                file.write(f"{emp_id}:{code_str}\n")

    def validate_employee_code(self, employee_code):
        """Check if the employee ID exists in the system."""
        return employee_code in self.employee_code

    def get_security_code(self, employee_code):
        """Generate a security code if none exists and return it."""
        if not self.validate_employee_code(employee_code):
            raise ValueError(f"Employee ID '{employee_code}' does not exist.")

        if self.employee_code[employee_code] is None:  # Generate a new code if it doesn't exist
            min_value = 1000
            max_value = 9999
            security_code = secrets.randbelow(max_value - min_value + 1) + min_value
            self.employee_code[employee_code] = security_code
            self.save_employee_codes()  # Save updated codes to the file

        return self.employee_code[employee_code]

    def validate_security_code(self, employee_code, entered_code):
        """Validate the entered security code for the given employee ID."""
        if not self.validate_employee_code(employee_code):
            raise ValueError(f"Employee ID '{employee_code}' does not exist.")

        return self.employee_code.get(employee_code) == entered_code

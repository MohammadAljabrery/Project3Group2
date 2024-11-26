import unittest
from security_system import SecuritySystem

class TestSecuritySystem(unittest.TestCase):

    def test_security_system_init(self):
        # Test with the actual file path containing data
        system = SecuritySystem(file_path="employee_codes.txt")
        self.assertEqual(system.employee_code, {
            "henil": 9999,
            "meera": 8661,
            "nikhil": 8773,
            "mohammad": 5712,
            "gurpreet": 9656
        })

    def test_validate_employee_code_exists(self):
        system = SecuritySystem(file_path="employee_codes.txt")
        result = system.validate_employee_code("henil")
        self.assertTrue(result)

    def test_validate_employee_code_not_exists(self):
        system = SecuritySystem(file_path="employee_codes.txt")
        result = system.validate_employee_code("emp0")
        self.assertFalse(result)

    def test_get_security_code_valid(self):
        system = SecuritySystem(file_path="employee_codes.txt")
        security_code = system.get_security_code("henil")
        self.assertEqual(security_code, 9999)

    def test_get_security_code_invalid(self):
        system = SecuritySystem(file_path="employee_codes.txt")
        with self.assertRaises(ValueError):
            system.get_security_code("emp0")
        
    def test_validate_security_code_correct(self):
        system = SecuritySystem(file_path="employee_codes.txt")
        result = system.validate_security_code("henil", 9999)
        self.assertTrue(result)
    
    def test_validate_security_code_incorrect(self):
        system = SecuritySystem(file_path="employee_codes.txt")
        result = system.validate_security_code("henil", 1425)
        self.assertFalse(result)

    def test_read_data_from_valid_file(self):
        system = SecuritySystem(file_path="employee_codes.txt")
        self.assertEqual(system.employee_code, {
            "henil": 9999,
            "meera": 8661,
            "nikhil": 8773,
            "mohammad": 5712,
            "gurpreet": 9656
        })


    def test_save_employee_codes(self):
        system = SecuritySystem(file_path="employee_codes.txt")
        system.employee_code["henil"] = 9999  # Update security code
        system.save_employee_codes()

        system = SecuritySystem(file_path="employee_codes.txt")
        self.assertEqual(system.employee_code, {
            "henil": 9999,
            "meera": 8661,
            "nikhil": 8773,
            "mohammad": 5712,
            "gurpreet": 9656
        })

if __name__ == "__main__":
    unittest.main()
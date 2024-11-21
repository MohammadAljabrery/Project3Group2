import tkinter as tk
from tkinter import messagebox
from security_system import SecuritySystem


class SecuritySystemGUI:
    def __init__(self, root, security_system):
        self.root = root
        self.security_system = security_system

        root.configure(bg="black")

        # Title and heading
        root.title("Sumbarine Security")
        tk.Label(root, text="Sumbarine Security", font=("Arial", 24), bg="black", fg="green").pack(pady=10)

        # Employee ID Input
        tk.Label(root, text="Enter Employee ID:", font=("Arial", 14), bg="black", fg="green").pack()
        self.employee_id_entry = tk.Entry(root, font=("Arial", 14))
        self.employee_id_entry.pack(pady=5)

        # Generate Code Button
        self.generate_button = tk.Button(root, text="Generate Code", font=("Arial", 14), bg="black", fg="green",
                                         command=self.generate_code)
        self.generate_button.pack(pady=10)

        # Display Generated Code
        self.code_label = tk.Label(root, text="", font=("Arial", 14), bg="black", fg="green")
        self.code_label.pack()

        # Security Code Input
        tk.Label(root, text="Enter Security Code:", font=("Arial", 14), bg="black", fg="green").pack()
        self.security_code_entry = tk.Entry(root, font=("Arial", 14))
        self.security_code_entry.pack(pady=5)

        # Submit Button
        self.submit_button = tk.Button(root, text="Submit", font=("Arial", 14), bg="black", fg="green",
                                       command=self.validate_code)
        self.submit_button.pack(pady=10)

    def generate_code(self):
        """
        Use SecuritySystem to validate the employee ID and generate a security code.
        If the ID is valid, display the code. Otherwise, show an error message.
        """
        employee_id = self.employee_id_entry.get().strip()
        if not employee_id:
            messagebox.showerror("Error", "Please enter an Employee ID.")
            return

        if self.security_system.validate_employee_code(employee_id):
            generated_code = self.security_system.get_security_code(employee_id)
            self.code_label.config(text=f"Generated Code: {generated_code}")
        else:
            messagebox.showerror("Error", "Invalid Employee ID.")

    def validate_code(self):
        """
        Validate the entered security code using SecuritySystem.
        If the code is valid for the entered employee ID, grant access.
        Otherwise, show an error message.
        """
        employee_id = self.employee_id_entry.get().strip()
        entered_code = self.security_code_entry.get().strip()

        if not employee_id:
            messagebox.showerror("Error", "Please enter an Employee ID.")
            return

        if not entered_code.isdigit():
            messagebox.showerror("Error", "Please enter a valid 4-digit code.")
            return

        if self.security_system.validate_security_code(employee_id, int(entered_code)):
            messagebox.showinfo("Success", "Access Granted!")
        else:
            messagebox.showerror("Error", "Invalid Security Code.")

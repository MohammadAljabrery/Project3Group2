import tkinter as tk
from tkinter import messagebox
from security_system import SecuritySystem


class SecuritySystemGUI:
    def __init__(self, root, security_system, callback):
        self.root = root
        self.security_system = security_system
        self.callback = callback  # Callback to pass result to main
        root.configure(bg="SkyBlue3")
        self.root.title("Security System")
        root.geometry("1920x1080")

        # Employee ID Input
        tk.Label(root, text="Enter Employee ID:", font=("Arial", 20), bg="Skyblue3", fg="black").pack(pady=(50, 0))
        self.employee_id_entry = tk.Entry(root, font=("Arial", 20), width=30)
        self.employee_id_entry.pack(pady=5)

        # Generate Code Button
        self.generate_button = tk.Button(root, text="Generate Code", font=("Arial", 20), bg="Skyblue3", fg="black", width=15,
                                         command=self.generate_code)
        self.generate_button.pack(pady=10)      

        # Security Code Input
        tk.Label(root, text="Enter Security Code:", font=("Arial", 20), bg="Skyblue3", fg="black").pack()
        self.security_code_entry = tk.Entry(root, font=("Arial", 20))
        self.security_code_entry.pack(pady=5)

        # Submit Button
        self.submit_button = tk.Button(root, text="Submit", font=("Arial", 14), bg="Skyblue3", fg="black",
                                       command=self.validate_code)
        self.submit_button.pack(pady=10)
        
        # Display Generated Code
        self.code_label = tk.Label(root, text="", font=("Arial", 20), bg="Skyblue3", fg="black")
        self.code_label.pack(pady=30)

    def generate_code(self):
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
        employee_id = self.employee_id_entry.get().strip()
        entered_code = self.security_code_entry.get().strip()

        if not employee_id:
            messagebox.showerror("Error", "Please enter an Employee ID.")
            self.callback(False, self.root)  # Pass False to the callback
            return

        if not entered_code.isdigit():
            messagebox.showerror("Error", "Please enter a valid 4-digit code.")
            self.callback(False, self.root)  # Pass False to the callback
            return

        if self.security_system.validate_security_code(employee_id, int(entered_code)):
            messagebox.showinfo("Success", "Access Granted!")
            self.callback(True, self.root)  # Pass True to the callback
        else:
            messagebox.showerror("Error", "Invalid Security Code.")
            self.callback(False, self.root)  # Pass False to the callback
        

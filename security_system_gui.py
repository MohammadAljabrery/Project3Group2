import customtkinter as ctk
from tkinter import messagebox
from security_system import SecuritySystem


class SecuritySystemGUI(ctk.CTkFrame):
    def __init__(self, root, security_system, callback):
        super().__init__(root)
        self.security_system = security_system
        self.callback = callback  # Callback to pass result to main
        self.pack(fill="both", expand=True)
        self.configure(fg_color="gray15")  # Background color
        root.title("Security System")
        # Header
        # self.header_label = ctk.CTkLabel(
        #     self, text="Security System", font=ctk.CTkFont("Arial", 40, "bold"), fg_color="gray15", text_color="white"
        # )
        # self.header_label.pack(pady=(50, 20))

        # Employee ID Input Section
        self.employee_id_label = ctk.CTkLabel(
            self, text="Enter Employee ID:", font=ctk.CTkFont("Arial", 20), text_color="white"
        )
        self.employee_id_label.pack(pady=(200, 10))

        self.employee_id_entry = ctk.CTkEntry(self, font=ctk.CTkFont("Arial", 20), width=400, height=50)
        self.employee_id_entry.pack(pady=5)

        # Generate Code Button
        self.generate_button = ctk.CTkButton(
            self,
            text="Generate Code",
            font=ctk.CTkFont("Arial", 20),
            width=200,
            height=50,
            fg_color="teal",
            hover_color="darkslategray",
            command=self.generate_code,
        )
        self.generate_button.pack(pady=20)

        # Security Code Input Section
        self.security_code_label = ctk.CTkLabel(
            self, text="Enter Security Code:", font=ctk.CTkFont("Arial", 20), text_color="white"
        )
        self.security_code_label.pack(pady=(20, 10))

        self.security_code_entry = ctk.CTkEntry(self, font=ctk.CTkFont("Arial", 20), width=400, height=50)
        self.security_code_entry.pack(pady=5)

        # Submit Button
        self.submit_button = ctk.CTkButton(
            self,
            text="Submit",
            font=ctk.CTkFont("Arial", 20),
            width=200,
            height=50,
            fg_color="green",
            hover_color="darkgreen",
            command=self.validate_code,
        )
        self.submit_button.pack(pady=20)

        # Display Generated Code Section
        self.code_label = ctk.CTkLabel(
            self, text="", font=ctk.CTkFont("Arial", 20), text_color="yellow"
        )
        self.code_label.pack(pady=(30, 0))

    def generate_code(self):
        employee_id = self.employee_id_entry.get().strip()
        if not employee_id:
            messagebox.showerror("Error", "Please enter an Employee ID.")
            return

        if self.security_system.validate_employee_code(employee_id):
            generated_code = self.security_system.get_security_code(employee_id)
            self.code_label.configure(text=f"Generated Code: {generated_code}")
        else:
            messagebox.showerror("Error", "Invalid Employee ID.")

    def validate_code(self):
        employee_id = self.employee_id_entry.get().strip()
        entered_code = self.security_code_entry.get().strip()

        if not employee_id:
            messagebox.showerror("Error", "Please enter an Employee ID.")
            self.callback(False, self)  # Pass False to the callback
            return

        if not entered_code.isdigit():
            messagebox.showerror("Error", "Please enter a valid 4-digit code.")
            self.callback(False, self)  # Pass False to the callback
            return

        if self.security_system.validate_security_code(employee_id, int(entered_code)):
            messagebox.showinfo("Success", "Access Granted!")
            self.callback(True, self)  # Pass True to the callback
        else:
            messagebox.showerror("Error", "Invalid Security Code.")
            self.callback(False, self)  # Pass False to the callback


# Main Application
def main():
    root = ctk.CTk()
    root.geometry("1920x1080")
    root.title("Security System")

    security_system = SecuritySystem()  # Assuming this is defined elsewhere

    def callback(success, frame):
        if success:
            print("Access Granted")
        else:
            print("Access Denied")

    app = SecuritySystemGUI(root, security_system, callback)
    root.mainloop()


if __name__ == "__main__":
    main()

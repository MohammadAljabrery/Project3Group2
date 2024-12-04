import customtkinter as ctk
from tkinter import messagebox
from ballast_system import BallastSystem


class BallastSystemGUI(ctk.CTkFrame):
    def __init__(self, parent, on_back):
        super().__init__(parent)
        self.parent = parent
        self.on_back = on_back
        self.system = BallastSystem()
        
        # Configure the appearance mode and theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Title
        # ctk.CTkLabel(
        #     self, text="Ballast System", font=ctk.CTkFont("Arial", 60, "bold")
        # ).pack(pady=40)

        # Volume slider and input box
        ctk.CTkLabel(self, text="Enter the volume (L)", font=ctk.CTkFont("Arial", 35)).pack(pady=20)
        self.volume_var = ctk.IntVar(value=0)
        self.volume_slider = ctk.CTkSlider(
            self, from_=0, to=1000, variable=self.volume_var, command=self.update_input,
            width=800, height=20
        )
        self.volume_slider.pack(pady=20)
        self.volume_entry = ctk.CTkEntry(self, textvariable=self.volume_var, width=200, font=("Arial", 30))
        self.volume_entry.pack(pady=20)

        # Fill and Drain Buttons
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.pack(pady=40)
        ctk.CTkButton(
            button_frame, text="Fill", font=ctk.CTkFont("Arial", 25), width=250, height=50,
            command=self.fill_ballast, fg_color="green", hover_color="darkgreen"
        ).grid(row=0, column=0, padx=40)
        ctk.CTkButton(
            button_frame, text="Drain", font=ctk.CTkFont("Arial", 25), width=250, height=50,
            command=self.drain_ballast, fg_color="red", hover_color="darkred"
        ).grid(row=0, column=1, padx=40)

        # Tanks and Depth
        tank_frame = ctk.CTkFrame(self, fg_color="transparent")
        tank_frame.pack(pady=30)

        # Tank 1
        self.tank1_label = ctk.CTkLabel(
            tank_frame, text="Tank 1\n0L", font=ctk.CTkFont("Arial", 20, "bold"),
            width=180, height=180, fg_color="lightblue", text_color="black", corner_radius=10
        )
        self.tank1_label.grid(row=0, column=0, padx=40)

        # Tank 2
        self.tank2_label = ctk.CTkLabel(
            tank_frame, text="Tank 2\n0L", font=ctk.CTkFont("Arial", 20, "bold"),
            width=180, height=180, fg_color="lightblue", text_color="black", corner_radius=10
        )
        self.tank2_label.grid(row=0, column=1, padx=40)

        self.depth_label = ctk.CTkLabel(
            self, text="Depth: 0m", font=ctk.CTkFont("Arial", 30, "bold"), text_color="white"
        )
        self.depth_label.pack(pady=40)

        # Back Button
        ctk.CTkButton(
            self, text="Back", font=ctk.CTkFont("Arial", 18), width=150, height=30,
            fg_color="gray", hover_color="darkgray", command=self.on_back
        ).pack(side="bottom", pady="20")

        # Initial update
        self.update_status()

    def update_input(self, _):
        self.volume_var.set(self.volume_slider.get())

    def fill_ballast(self):
        volume = self.volume_var.get()
        success, message = self.system.fill_ballast(volume)
        if not success:
            messagebox.showwarning("Warning", message)
        self.update_status()

    def drain_ballast(self):
        volume = self.volume_var.get()
        success, message = self.system.drain_ballast(volume)
        if not success:
            messagebox.showwarning("Warning", message)
        self.update_status()

    def update_status(self):
        tank1_volume = self.system.tank1_volume
        tank2_volume = self.system.tank2_volume
        depth = self.system.depth

        self.tank1_label.configure(text=f"Tank 1\n{tank1_volume:.1f}L")
        self.tank2_label.configure(text=f"Tank 2\n{tank2_volume:.1f}L")
        self.depth_label.configure(text=f"Depth: {depth:.1f}m")


# Example usage
if __name__ == "__main__":
    def go_back():
        print("Back button clicked!")  # Replace this with frame-switching logic.

    root = ctk.CTk()
    root.geometry("1920x1080")  # Set the window to 1920x1080
    BallastSystemGUI(root, go_back).pack(fill="both", expand=True)
    root.mainloop()

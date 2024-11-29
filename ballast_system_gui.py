import tkinter as tk
from tkinter import messagebox
from ballast_system import BallastSystem


class BallastSystemGUI(tk.Frame):
    def __init__(self, parent, on_back):
        super().__init__(parent, bg="Skyblue3")
        self.parent = parent
        self.on_back = on_back  # Callback for the back button
        self.system = BallastSystem()
        
        self.configure(bg="Skyblue3")

        # Title
        tk.Label(self, text="Ballast System", font=("Arial", 50, "bold"), fg="black", bg="Skyblue3").pack(pady=10)

        # Volume slider and input box
        volume_frame = tk.Frame(self, bg="Skyblue3")
        volume_frame.pack(pady=50)
        tk.Label(volume_frame, text="Enter the volume (L)", font=("Arial", 30, "bold"), fg="black", bg="Skyblue3").pack()
        self.volume_var = tk.IntVar(value=0)
        self.volume_slider = tk.Scale(
            volume_frame, from_=0, to=1000, orient="horizontal", variable=self.volume_var,
            bg="dodgerblue", fg="black", length=1000, command=self.update_input
        )
        self.volume_slider.pack()
        self.volume_entry = tk.Entry(volume_frame, textvariable=self.volume_var, width=5, font=("Arial", 20))
        self.volume_entry.pack(pady=5)

        # Fill and Drain Buttons
        button_frame = tk.Frame(self, bg="Skyblue3")
        button_frame.pack(pady=10)
        tk.Button(
            button_frame, text="Fill", font=("Arial", 15, "bold"), bg="green", fg="Skyblue3", width=50, height=1,
            command=self.fill_ballast
        ).grid(row=0, column=0, padx=5)
        tk.Button(
            button_frame, text="Drain", font=("Arial", 15, "bold"), bg="red", fg="Skyblue3", width=50, height=1,
            command=self.drain_ballast
        ).grid(row=0, column=1, padx=5)

        # Tanks and Depth
        tank_frame = tk.Frame(self, bg="Skyblue3")
        tank_frame.pack(pady=10)

        # Tank 1 Label with Border
        tank1_border = tk.Frame(tank_frame, bg="black", bd=5)
        tank1_border.grid(row=0, column=0, padx=5)
        self.tank1_label = tk.Label(
            tank1_border, text="Tank 1\n0L", font=("Arial", 12, "bold"), fg="black", bg="SkyBlue2",
            width=20, height=10
        )
        self.tank1_label.pack()

        # Tank 2 Label with Border
        tank2_border = tk.Frame(tank_frame, bg="black", bd=5)
        tank2_border.grid(row=0, column=1, padx=5)
        self.tank2_label = tk.Label(
            tank2_border, text="Tank 2\n0L", font=("Arial", 12, "bold"), fg="black", bg="SkyBlue2",
            width=20, height=10
        )
        self.tank2_label.pack()

        self.depth_label = tk.Label(self, text="Depth: 0m", font=("Arial", 20, "bold"), fg="black", bg="Skyblue3")
        self.depth_label.pack(pady=10)

        # Back Button
        back_button = tk.Button(
            self, text="Back", font=("Arial", 15, "bold"), bg="gray", fg="white", command=self.on_back
        )
        back_button.pack(pady=10)

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

        self.tank1_label.config(text=f"Tank 1\n{tank1_volume:.1f}L")
        self.tank2_label.config(text=f"Tank 2\n{tank2_volume:.1f}L")
        self.depth_label.config(text=f"Depth: {depth:.1f}m")


# Example usage
if __name__ == "__main__":
    def go_back():
        print("Back button clicked!")  # Replace this with frame-switching logic.

    root = tk.Tk()
    BallastSystemGUI(root, go_back).pack(fill="both", expand=True)
    root.mainloop()

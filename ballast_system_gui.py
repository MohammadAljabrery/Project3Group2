import tkinter as tk
from tkinter import messagebox
from ballast_system import BallastSystem

class BallastSystemGUI:
    def __init__(self, root):
        # Create an instance of BallastSystem
        self.system = BallastSystem()

        # Set up the root window
        self.root = root
        self.root.title("Ballast System")
        self.root.geometry("1920x1080")
        self.root.configure(bg="Skyblue3")
        

        # Title
        # title_label = tk.Label(
        #     root, text="Ballast System", font=("Arial", 50, "bold"), fg="black", bg="Skyblue3"
        # )
        # title_label.pack(pady=10)

        # Volume slider and input box
        volume_frame = tk.Frame(root, bg="Skyblue3")
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
        button_frame = tk.Frame(root, bg="Skyblue3")
        button_frame.pack(pady=10)
        self.fill_button = tk.Button(
            button_frame, text="Fill", font=("Arial", 15, "bold"), bg="green", fg="Skyblue3", width=50,height=1,
            command=self.fill_ballast
        )
        self.fill_button.grid(row=0, column=0, padx=5)
        self.drain_button = tk.Button(
            button_frame, text="Drain", font=("Arial", 15, "bold"), bg="red", fg="Skyblue3", width=50,height=1,
            command=self.drain_ballast
        )
        self.drain_button.grid(row=0, column=1, padx=5)

        # Tanks and Depth
        tank_frame = tk.Frame(root, bg="Skyblue3")
        tank_frame.pack(pady=10)
        tank_frame = tk.Frame(root, bg="Skyblue3")
        tank_frame.pack(pady=10)

        # Tank 1 Label with Border
        tank1_border = tk.Frame(tank_frame, bg="black", bd=5)  # Border color and thickness
        tank1_border.grid(row=0, column=0, padx=5)
        self.tank1_label = tk.Label(
            tank1_border, text="Tank 1\n0L", font=("Arial", 12, "bold"), fg="black", bg="SkyBlue2",
            width=20, height=10
        )
        self.tank1_label.pack()

        # Tank 2 Label with Border
        tank2_border = tk.Frame(tank_frame, bg="black", bd=0)  # Border color and thickness
        tank2_border.grid(row=0, column=1, padx=5, pady=5)
        self.tank2_label = tk.Label(
            tank2_border, text="Tank 2\n0L", font=("Arial", 12, "bold"), fg="black", bg="SkyBlue2",
            width=20, height=10
        )
        self.tank2_label.pack()

        self.tank2_label.grid(row=0, column=1, padx=5, pady=5)
        self.depth_label = tk.Label(root, text="Depth: 0m", font=("Arial", 20, "bold"), fg="black", bg="Skyblue3")
        self.depth_label.pack(pady=10)

        # Initial update
        self.update_status()

    def update_input(self, _):
        #Synchronize the slider and input box.
        self.volume_var.set(self.volume_slider.get())

    def fill_ballast(self):
        #Fill the ballast tanks with the specified volume.
        volume = self.volume_var.get()
        success, message = self.system.fill_ballast(volume)
        if not success:
            messagebox.showwarning("Warning", message)
        self.update_status()

    def drain_ballast(self):
        #Drain the ballast tanks by the specified volume.
        volume = self.volume_var.get()
        success, message = self.system.drain_ballast(volume)
        if not success:
            messagebox.showwarning("Warning", message)
        self.update_status()

    def update_status(self):
        #Update the GUI to reflect the current state of the system.
        tank1_volume = self.system.tank1_volume
        tank2_volume = self.system.tank2_volume
        depth = self.system.depth

        self.tank1_label.config(text=f"Tank 1\n{tank1_volume:.1f}L")
        self.tank2_label.config(text=f"Tank 2\n{tank2_volume:.1f}L")
        self.depth_label.config(text=f"Depth: {depth:.1f}m")

#((self.system.max_tank1_volume+self.system.max_tank2_volume)-(self.system.tank1_volume+self.system.tank2_volume))

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
        self.root.geometry("400x500")
        self.root.configure(bg="black")

        # Title
        title_label = tk.Label(
            root, text="Ballast System", font=("Arial", 16, "bold"), fg="lime", bg="black"
        )
        title_label.pack(pady=10)

        # Volume slider and input box
        volume_frame = tk.Frame(root, bg="black")
        volume_frame.pack(pady=10)
        tk.Label(volume_frame, text="Enter the volume (L)", font=("Arial", 12, "bold"), fg="lime", bg="black").pack()
        self.volume_var = tk.IntVar(value=0)
        self.volume_slider = tk.Scale(
            volume_frame, from_=0, to=1000, orient="horizontal", variable=self.volume_var,
            bg="dodgerblue", fg="black", length=300, command=self.update_input
        )
        self.volume_slider.pack()
        self.volume_entry = tk.Entry(volume_frame, textvariable=self.volume_var, width=5, font=("Arial", 14))
        self.volume_entry.pack(pady=5)

        # Fill and Drain Buttons
        button_frame = tk.Frame(root, bg="black")
        button_frame.pack(pady=10)
        self.fill_button = tk.Button(
            button_frame, text="Fill", font=("Arial", 12, "bold"), bg="green", fg="black", width=10, 
            command=self.fill_ballast
        )
        self.fill_button.grid(row=0, column=0, padx=5)
        self.drain_button = tk.Button(
            button_frame, text="Drain", font=("Arial", 12, "bold"), bg="red", fg="black", width=10,
            command=self.drain_ballast
        )
        self.drain_button.grid(row=0, column=1, padx=5)

        # Tanks and Depth
        tank_frame = tk.Frame(root, bg="black")
        tank_frame.pack(pady=10)
        self.tank1_label = tk.Label(
            tank_frame, text="Tank 1\n0L", font=("Arial", 12, "bold"), fg="black", bg="dodgerblue", width=10, height=5
        )
        self.tank1_label.grid(row=0, column=0, padx=5)
        self.tank2_label = tk.Label(
            tank_frame, text="Tank 2\n0L", font=("Arial", 12, "bold"), fg="black", bg="dodgerblue", width=10, height=5
        )
        self.tank2_label.grid(row=0, column=1, padx=5)
        self.depth_label = tk.Label(root, text="Depth: 0m", font=("Arial", 16, "bold"), fg="lime", bg="black")
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

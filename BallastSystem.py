import tkinter as tk
from tkinter import messagebox,  simpledialog
from tkinter import ttk

class BallastSystem:
    def __init__(self, root):
        # Initialize submarine properties
        self.ballast_tank_volume = 0  # in liters
        self.max_ballast_volume = 1000  # maximum capacity in liters
        self.depth = 0  # in meters

        # Set up the GUI
        self.root = root    
        self.root.title("Submarine Ballast System")
        self.root.geometry("400x400")
        self.root.configure(bg="#2E3B4E")


        # Title label
        title_label = tk.Label(
            root, text="Submarine Ballast Control", font=("Times New Roman", 16, "bold"), fg="white", bg="#2E3B4E"
        )
        title_label.pack(pady=10)

        # Volume slider with label
        volume_frame = tk.Frame(root, bg="#2E3B4E")
        volume_frame.pack(pady=10)
        volume_label = tk.Label(volume_frame, text="Adjust Volume (L):", font=("Times New Roman", 12), fg="white", bg="#2E3B4E")
        volume_label.pack(side="left", padx=5)
        self.volume_slider = tk.Scale(volume_frame, from_=0, to=500, orient="horizontal", bg="#2E3B4E", 
                                      font=("Arial", 10), length=200)
        self.volume_slider.pack(side="left")

        # Fill and Drain Buttons
        button_frame = tk.Frame(root, bg="#2E3B4E")
        button_frame.pack(pady=10)
        self.fill_button = tk.Button(
            button_frame, text="Fill Ballast", font=("Times New Roman", 12, "bold"), bg="#4CAF50", fg="white", width=10,
            command=self.fill_ballast
        )
        self.fill_button.grid(row=0, column=0, padx=5)
        self.drain_button = tk.Button(
            button_frame, text="Drain Ballast", font=("Times New Roman", 12, "bold"), bg="#F44336", fg="white", width=10,
            command=self.drain_ballast
        )
        self.drain_button.grid(row=0, column=1, padx=5)

        # Progress bars for ballast volume and depth
        tk.Label(root, text="Ballast Volume", font=("Times New Roman", 10, "bold"), fg="white", bg="#2E3B4E").pack(pady=5)
        self.volume_progress = ttk.Progressbar(root, length=300, maximum=self.max_ballast_volume)
        self.volume_progress.pack(pady=5)
        
        tk.Label(root, text="Depth", font=("Arial", 10, "bold"), fg="white", bg="#2E3B4E").pack(pady=5)
        self.depth_progress = ttk.Progressbar(root, length=300, maximum=self.max_ballast_volume / 10)
        self.depth_progress.pack(pady=5)

        # Status display
        self.status_label = tk.Label(root, text="", font=("Arial", 12), fg="white", bg="#2E3B4E")
        self.status_label.pack(pady=10)
       
        # Initial status update
        self.update_status()
   
    def fill_ballast(self):
        volume = self.volume_slider.get()
        if self.ballast_tank_volume + volume > self.max_ballast_volume:
            messagebox.showwarning("Warning", "Tank is full! Can't add more water.")
            self.ballast_tank_volume = self.max_ballast_volume
        else:
            self.ballast_tank_volume += volume
            self.update_depth()
        self.update_status()

        
    def drain_ballast(self):
        volume = self.volume_slider.get()
        if self.ballast_tank_volume - volume < 0:
            messagebox.showwarning("Warning", "Tank is empty! Can't drain more water.")
            self.ballast_tank_volume = 0
        else:
            self.ballast_tank_volume -= volume
            self.update_depth()
        self.update_status()

    def update_depth(self):
        # Simple model for depth
        self.depth = self.ballast_tank_volume / 10

    def update_status(self):
        # Update status label and progress bars
        status = f"Ballast volume: {self.ballast_tank_volume} liters\nDepth: {self.depth} meters"
        self.status_label.config(text=status)
        self.volume_progress['value'] = self.ballast_tank_volume
        self.depth_progress['value'] = self.depth

# Main function
def main():
    root = tk.Tk()
    app = BallastSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()

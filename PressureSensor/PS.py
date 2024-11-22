import customtkinter as ctk
import random


class PressureSensor:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x300")
        self.root.title("Pressure Sensor Module")

        # Initialize pressure value
        self.pressure = 0.0  # Pressure in units like PSI (pounds per square inch)

        # Create the label to display pressure data
        self.pressure_label = ctk.CTkLabel(self.root, text="Pressure: -", font=("Arial", 16))
        self.pressure_label.pack(pady=10)

        # Start updating the pressure data
        self.update_pressure_data()

    def simulate_pressure_data(self):
        """Simulate reading pressure value from a sensor."""
        self.pressure = round(random.uniform(800, 1200), 2)  # Random pressure between 800 and 1200 PSI

    def update_pressure_data(self):
        """Update the pressure data displayed on the GUI."""
        # Simulate new pressure data
        self.simulate_pressure_data()

        # Update the label with the new data
        self.pressure_label.configure(text=f"Pressure: {self.pressure} PSI")

        # Schedule the next update
        self.root.after(2000, self.update_pressure_data)

    def get_pressure(self):
        """Return the current pressure value for other modules to access."""
        return self.pressure


# Main application for testing
if __name__ == "__main__":
    root = ctk.CTk()
    pressure_sensor = PressureSensor(root)
    root.mainloop()

import customtkinter as ctk
import random


class WaterQualitySensor:
    def __init__(self, root):
        self.root = root

        # Initialize sensor readings
        self.ph_level = 0.0
        self.ppm_level = 0.0

        # Create the labels to display sensor data
        # self.ph_label = ctk.CTkLabel(self.root, text="pH Level: -", font=("Arial", 16))
        # self.ph_label.pack(pady=10)
        #
        # self.ppm_label = ctk.CTkLabel(self.root, text="PPM: -", font=("Arial", 16))
        # self.ppm_label.pack(pady=10)

        # Start updating the sensor data
        self.update_sensor_data()

    def simulate_sensor_data(self):
        """Simulate reading pH and ppm values from a sensor."""
        self.ph_level = round(random.uniform(6.5, 8.5), 2)  # Random pH between 6.5 and 8.5
        self.ppm_level = round(random.uniform(200, 800), 2)  # Random ppm between 200 and 800

    def update_sensor_data(self):
        """Update the sensor data displayed on the GUI."""
        # Simulate new data
        self.simulate_sensor_data()

        # Update labels with new data
        # self.ph_label.configure(text=f"pH Level: {self.ph_level}")
        # self.ppm_label.configure(text=f"PPM: {self.ppm_level}")

        # Schedule the next update
        self.root.after(2000, self.update_sensor_data)


# Main application
if __name__ == "__main__":
    root = ctk.CTk()
    water_quality_sensor = WaterQualitySensor(root)
    root.mainloop()

import tkinter as tk
from tkinter import *
from PropulsionSystem import PropulsionSystem  # Import Propulsion System GUI
from enviornmentControlSystem import SubmarineEnvironmentalControlSystem  # Import Environmental Control System GUI
from ballast_system_gui import BallastSystemGUI  # Import Ballast System GUI
from security_system import SecuritySystem
from security_system_gui import SecuritySystemGUI
from PressureSensor.PS import *  # Import the PressureSensor class
from WaterQualitySensor.WQS import *
from sonar import run_sonar_frame, SonarFrame
from navigation import NavigationFrame
from logger import LoggerSystem, run_logger_frame
from security_system import SecuritySystem
from ballast_system import BallastSystem
import customtkinter as ctk

logger = LoggerSystem()


def open_navigation_menu(root):
    """Opens the navigation menu after successful security validation."""
    # Destroy the security window
    root.destroy()

    # Create a new window for the navigation menu
    nav_root = tk.Tk()
    nav_root.title("Submarine Systems Navigation")
    nav_root.geometry("1920x1080")
    nav_root.configure(bg="gray15")

    ctk.CTkLabel(
        nav_root, text="Select a Submarine System", font=("Arial", 25), text_color="white", 
    ).pack(pady=20)

    # Pressure sensor and label
    pressure_sensor = PressureSensor(nav_root)
    pressure_label = ctk.CTkLabel(
        nav_root, text="Current Pressure: -", font=("Arial", 19), text_color="white", 
    )
    pressure_label.place(relx=1.0, rely=0.05, anchor="ne")

    def update_pressure_label():
        """Update the pressure label with the current pressure."""
        pressure = pressure_sensor.get_pressure()  # Get the current pressure value
        pressure_label.configure(text=f"Pressure: {pressure} PSI")  # Update the label
        nav_root.after(1000, update_pressure_label)  # Update every second

    # Start updating the pressure label
    update_pressure_label()

    # Create the WaterQualitySensor object to display water quality readings
    water_quality_sensor = WaterQualitySensor(nav_root)  # Water quality sensor displays below pressure readings

    # Create the water quality labels (these labels will be updated by the WaterQualitySensor)
    ph_label = ctk.CTkLabel(nav_root, text="pH Level: -", font=("Arial", 19), text_color="white")
    ph_label.place(relx=1.0, rely=0.15, anchor='ne')  # Position below pressure readings on the right side

    ppm_label = ctk.CTkLabel(nav_root, text="PPM: -", font=("Arial", 19), text_color="white")
    ppm_label.place(relx=1.0, rely=0.20, anchor='ne')  # Position below pH level label on the right side

    def update_water_quality_data():
        """Update the water quality sensor labels with the current data."""
        ph = water_quality_sensor.ph_level
        ppm = water_quality_sensor.ppm_level
        ph_label.configure(text=f"pH Level: {ph}")
        ppm_label.configure(text=f"PPM: {ppm}")
        nav_root.after(2000, update_water_quality_data)  # Update every 2 seconds

    # Start updating water quality labels
    nav_root.after(2000, update_water_quality_data)

    # Buttons to navigate to different systems
    ctk.CTkButton(
        nav_root,
        text="Propulsion System",
        font=("Arial", 19),
        command=lambda: open_propulsion_system(nav_root),
         width=270, height= 70
    ).pack(pady=10)

    ctk.CTkButton(
        nav_root,
        text="Environmental Control System",
        font=("Arial", 19),
        command=lambda: open_environmental_control_system(nav_root),
         width=270, height= 70
    ).pack(pady=10)

    ctk.CTkButton(
        nav_root,
        text="Ballast System",
        font=("Arial", 19),
        command=lambda: open_ballast_system(nav_root),
        width=270, height= 70
    ).pack(pady=10)

    ctk.CTkButton(
        nav_root,
        text="Light Control System",
        font=("Arial", 19),
        command=lambda: open_lcs(nav_root),
         width=270, height= 70
    ).pack(pady=10)

    ctk.CTkButton(
        nav_root,
        text="Sonar System",
        font=("Arial", 19),
        command=lambda: open_sonar_system(nav_root),
         width=270, height= 70
    ).pack(pady=10)

    ctk.CTkButton(
    nav_root,
    text="Navigation System",
    font=("Arial", 19),
    command=lambda: open_navigation_system(nav_root),
     width=270, height= 70
    ).pack(pady=10)

    
    ctk.CTkButton(
        nav_root,
        text="Logger System",
        font=("Arial", 19),
        command=lambda: open_logger_system(nav_root),
        width=270, height= 70
    ).pack(pady=10)

    nav_root.mainloop()


def open_logger_system(nav_root):
    nav_root.withdraw()  # Hide the navigation menu
    logger_root = tk.Tk()
    logger_root.title("Logger System")
    logger_root.geometry("1920x1080")
    run_logger_frame(logger_root, nav_root, logger)  # Pass logger system instance
    logger_root.mainloop()

    
def open_sonar_system(nav_root):
    nav_root.withdraw()  # Hide the navigation menu window
    sonar_root = tk.Tk()  # Create a new root window for the Sonar System
    sonar_root.title("Sonar System")
    sonar_root.geometry("1920x1080")
    sonar_frame = SonarFrame(sonar_root, nav_root)  # Pass the navigation menu window as a reference
    sonar_frame.pack(fill=tk.BOTH, expand=True)
    sonar_root.mainloop()
    


    
def open_navigation_system(nav_root):
    nav_root.withdraw()  # Hide the navigation menu window
    navigation_root = tk.Tk()  # Create a new root window for the Navigation System
    navigation_root.title("Navigation System")
    navigation_root.geometry("1920x1080")
    navigation_frame = NavigationFrame(navigation_root, nav_root)  # Pass the navigation menu window as a reference
    navigation_frame.pack(fill=tk.BOTH, expand=True)
    navigation_root.mainloop()

    
def open_lcs(nav_root):
    """Launches the Light Control System GUI."""
    from LightControlSystem.tk import main_frame  # Import LCS main_window function
    nav_root.destroy()  # Close the navigation menu
    main_frame.mainloop()  # Correctly invoke the LCS GUI function


def open_propulsion_system(nav_root):
    """Launches the Propulsion System GUI."""
    nav_root.destroy()  # Close the navigation menu
    propulsion_root = tk.Tk()
    app = PropulsionSystem(propulsion_root)  # Pass the root window
    propulsion_root.mainloop()


def open_environmental_control_system(nav_root):
    """Launches the Environmental Control System GUI."""
    nav_root.destroy()  # Close the navigation menu
    environmental_root = tk.Tk()
    app = SubmarineEnvironmentalControlSystem()  # Initialize the Environmental System
    app.run()  # Start the main loop


def open_ballast_system(nav_root):
    """Launches the Ballast System GUI."""
    # Hide the navigation root instead of destroying it
    nav_root.withdraw()

    # Create a new window for the Ballast System GUI
    ballast_window = tk.Toplevel(nav_root)
    ballast_window.title("Ballast System")
    ballast_window.geometry("1920x1080")

    def go_back():
        # Close the Ballast System window and show the navigation menu
        ballast_window.destroy()
        nav_root.deiconify()

    BallastSystemGUI(ballast_window, go_back).pack(fill="both", expand=True)


def validation_callback(result, root):
    """Callback function to handle security system validation."""
    if result:
        open_navigation_menu(root)      
        
        
    else:
        print("Invalid code or Access Denied.")  # Handle invalid access


def main():
    security_system = SecuritySystem()
    root = ctk.CTk()
    root.geometry("1920x1080")
    app = SecuritySystemGUI(root, security_system, validation_callback)
    root.mainloop()

if __name__ == "__main__":
    main()

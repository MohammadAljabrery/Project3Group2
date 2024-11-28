import tkinter as tk
from PropulsionSystem import PropulsionSystem  # Import Propulsion System GUI
from enviornmentControlSystem import SubmarineEnvironmentalControlSystem  # Import Environmental Control System GUI
from ballast_system_gui import BallastSystemGUI  # Import Ballast System GUI
from security_system import SecuritySystem
from security_system_gui import SecuritySystemGUI

def open_navigation_menu(root):
    """Opens the navigation menu after successful security validation."""
    # Destroy the security window
    root.destroy()

    # Create a new window for the navigation menu
    nav_root = tk.Tk()
    nav_root.title("Submarine Systems Navigation")
    nav_root.geometry("800x600")

    # Title label
    tk.Label(nav_root, text="Select a Submarine System", font=("Arial", 18)).pack(pady=20)

    # Buttons to navigate to different systems
    tk.Button(
        nav_root,
        text="Propulsion System",
        font=("Arial", 14),
        command=lambda: open_propulsion_system(nav_root),
        width=30,
    ).pack(pady=10)

    tk.Button(
        nav_root,
        text="Environmental Control System",
        font=("Arial", 14),
        command=lambda: open_environmental_control_system(nav_root),
        width=30,
    ).pack(pady=10)

    tk.Button(
        nav_root,
        text="Ballast System",
        font=("Arial", 14),
        command=lambda: open_ballast_system(nav_root),
        width=30,
    ).pack(pady=10)

    nav_root.mainloop()


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
    nav_root.destroy()  # Close the navigation menu
    ballast_root = tk.Tk()
    app = BallastSystemGUI(ballast_root)  # Pass the root window
    ballast_root.mainloop()


def validation_callback(result, root):
    """Callback function to handle security system validation."""
    if result:
        open_navigation_menu(root)  # Proceed to the navigation menu
    else:
        print("Invalid code or Access Denied.")  # Handle invalid access


def main():
    """Main function to start the application."""
    security_system = SecuritySystem()  # Initialize the security system
    root = tk.Tk()  # Main Tkinter window for the security system
    app = SecuritySystemGUI(root, security_system, validation_callback)  # Pass the callback with root

    # Start the GUI loop
    root.mainloop()


if __name__ == "__main__":
    main()

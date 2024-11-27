import customtkinter as ctk
from datetime import datetime
import random
import json


class SubmarineEnvironmentalControlSystem:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Submarine Environmental Control System")
        self.root.geometry("1200x800")

        # Set theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # System configuration
        self.config = {
            'temperature': {
                'current': 22,
                'target': 22,
                'min': 18,
                'max': 28,
                'critical_high': 30,
                'critical_low': 15,
                'unit': '°C',
                'color': '#FF6B6B'
            },
            'humidity': {
                'current': 50,
                'target': 50,
                'min': 40,
                'max': 60,
                'critical_high': 70,
                'critical_low': 35,
                'unit': '%',
                'color': '#4ECDC4'
            },
            'air_quality': {
                'current': 80,
                'target': 80,
                'min': 60,
                'max': 100,
                'critical_low': 50,
                'unit': 'AQI',
                'color': '#95A5A6'
            },
            'oxygen_level': {
                'current': 21,
                'target': 21,
                'min': 19,
                'max': 23,
                'critical_high': 25,
                'critical_low': 18,
                'unit': '%',
                'color': '#45B7D1'
            },
            'co2_level': {
                'current': 400,
                'target': 400,
                'min': 350,
                'max': 1000,
                'critical_high': 1500,
                'critical_low': 300,
                'unit': 'ppm',
                'color': '#D35400'
            }
        }

        self.create_gui()

    def create_gui(self):
        # Main container
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Tabview
        self.tabview = ctk.CTkTabview(self.main_frame)
        self.tabview.pack(fill="both", expand=True, padx=5, pady=5)

        # Tabs
        self.tab_control = self.tabview.add("Control Panel")
        self.tab_monitor = self.tabview.add("Monitoring")
        self.create_control_panel()
        self.create_monitoring_panel()

    def create_control_panel(self):
        controls_frame = ctk.CTkFrame(self.tab_control)
        controls_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.control_widgets = {}
        for i, (param, details) in enumerate(self.config.items()):
            frame = ctk.CTkFrame(controls_frame)
            frame.pack(fill="x", padx=5, pady=10)

            # Parameter name
            ctk.CTkLabel(
                frame, text=param.replace("_", " ").title(), width=120
            ).pack(side="left", padx=5)

            # Slider to control current value
            slider = ctk.CTkSlider(
                frame,
                from_=details["min"],
                to=details["max"],
                number_of_steps=100,
                command=lambda value, p=param: self.update_current_value(p, value),
            )
            slider.set(details["current"])
            slider.pack(side="left", padx=5, fill="x", expand=True)

            # Current value display
            value_label = ctk.CTkLabel(
                frame, text=f"{details['current']}{details['unit']}", width=80
            )
            value_label.pack(side="left", padx=5)

            # Reset button to reset to target
            reset_button = ctk.CTkButton(
                frame,
                text="Reset",
                command=lambda p=param: self.reset_to_target(p),
            )
            reset_button.pack(side="left", padx=5)

            self.control_widgets[param] = {
                "slider": slider,
                "value_label": value_label,
            }

    def create_monitoring_panel(self):
        monitor_frame = ctk.CTkFrame(self.tab_monitor)
        monitor_frame.pack(fill="both", expand=True, padx=10, pady=10)

        ctk.CTkLabel(
            monitor_frame, text="Monitoring Panel: Real-Time Values", font=("Arial", 16)
        ).pack(pady=10)

        for param, details in self.config.items():
            frame = ctk.CTkFrame(monitor_frame)
            frame.pack(fill="x", padx=5, pady=5)

            ctk.CTkLabel(
                frame,
                text=f"{param.replace('_', ' ').title()}: {details['current']}{details['unit']}",
            ).pack(side="left", padx=10)

    def update_current_value(self, param, value):
        # Update current value from slider
        value = round(float(value), 1)
        self.config[param]["current"] = value
        self.control_widgets[param]["value_label"].configure(
            text=f"{value}{self.config[param]['unit']}"
        )

    def reset_to_target(self, param):
        # Reset current value to target value
        target = self.config[param]["target"]
        self.config[param]["current"] = target
        self.control_widgets[param]["slider"].set(target)
        self.control_widgets[param]["value_label"].configure(
            text=f"{target}{self.config[param]['unit']}"
        )

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = SubmarineEnvironmentalControlSystem()
    app.run()

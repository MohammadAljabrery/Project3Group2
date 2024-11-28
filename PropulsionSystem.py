#skyblue
import customtkinter as ctk
import time

class PropulsionSystem:
    def __init__(self, root: ctk.CTk):
        self.root = root
        self.root.title("Submarine Propulsion System")
        self.root.geometry("1920x1080")
        self.root.minsize(900, 900)

        # System parameters
        self.current_speed = 0.0
        self.target_speed = 0.0
        self.fuel_level = 100.0
        self.engine_status = False
        self._current_direction = "Stopped"  # Private variable to hold current direction
        self.latitude = 0.0  # Starting latitude (provided by sensor)
        self.longitude = 0.0  # Starting longitude (provided by sensor)
        self.step_size = 0.1  # Step size for movement (if manually adjusted)
        self.system_logs = []

        self.last_update_time = time.time()

        # RPM parameters
        self.rpm = 0  # RPM of the engine
        self.rpm_factor = 100  # Factor to convert speed to RPM (adjust based on system)

        # UI setup
        self.setup_ui()
        self.update_system()

        # Gradual speed increase rate (controls how fast speed increases)
        self.speed_increase_rate = 0.2  # Speed increase rate (km/h per update)

    # Getter for current direction
    def get_current_direction(self):
        return self._current_direction

    # Setter for current direction
    def set_current_direction(self, direction):
        # Only update direction if the engine is on
        if self.engine_status:
            self._current_direction = direction
            self.update_coordinates_based_on_direction(direction)
            self.log_event(f"Direction changed to {self._current_direction}.")
        else:
            self.log_event("Cannot change direction — engine is OFF.")

    def setup_ui(self):
        """Setup all UI elements."""
        # Target controls
        target_frame = ctk.CTkFrame(self.root)
        target_frame.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(target_frame, text="Target Speed (km/h):", font=("Arial", 14)).grid(
            row=0, column=0, padx=10, pady=5, sticky="w"
        )
        self.target_speed_input = ctk.CTkEntry(target_frame, width=100)
        self.target_speed_input.grid(row=0, column=1, padx=10, pady=5)
        self.target_speed_input.insert(0, "0")

        set_speed_button = ctk.CTkButton(
            target_frame, text="Set Speed", command=self.set_speed
        )
        set_speed_button.grid(row=0, column=2, padx=10, pady=5)

        # Engine controls
        engine_frame = ctk.CTkFrame(self.root)
        engine_frame.pack(fill="x", padx=20, pady=10)

        self.engine_status_label = ctk.CTkLabel(
            engine_frame, text="Engine Status: OFF", font=("Arial", 14)
        )
        self.engine_status_label.pack(side="left", padx=10)

        self.toggle_engine_button = ctk.CTkButton(
            engine_frame, text="Start Engine", command=self.toggle_engine
        )
        self.toggle_engine_button.pack(side="left", padx=10)

        # Fuel display
        fuel_frame = ctk.CTkFrame(self.root)
        fuel_frame.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(fuel_frame, text="Fuel Level:", font=("Arial", 14)).pack(
            side="left", padx=10
        )
        self.fuel_bar = ctk.CTkProgressBar(fuel_frame, width=400)
        self.fuel_bar.pack(side="left", padx=10)
        self.fuel_bar.set(self.fuel_level / 100)

        refuel_button = ctk.CTkButton(
            fuel_frame, text="Refuel", command=self.refuel, fg_color="green"
        )
        refuel_button.pack(side="left", padx=10)

        # Speed display
        speed_frame = ctk.CTkFrame(self.root)
        speed_frame.pack(fill="x", padx=20, pady=10)

        self.speed_label = ctk.CTkLabel(
            speed_frame, text=f"Current Speed: {self.current_speed:.2f} km/h"
        )
        self.speed_label.pack(side="left", padx=10)

        # RPM display
        self.rpm_label = ctk.CTkLabel(
            speed_frame, text=f"Current RPM: {self.rpm}"
        )
        self.rpm_label.pack(side="left", padx=10)

        # Direction controls
        direction_frame = ctk.CTkFrame(self.root)
        direction_frame.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(
            direction_frame, text="Control Direction:", font=("Arial", 14)
        ).grid(row=0, column=0, padx=10, pady=5)

        directions = [
            ("Forward", "Forward"),
            ("Reverse", "Reverse"),
            ("Left", "Left"),
            ("Right", "Right"),
            ("Stop", "Stopped"),
        ]
        for i, (text, direction) in enumerate(directions):
            button = ctk.CTkButton(
                direction_frame,
                text=text,
                command=lambda d=direction: self.set_current_direction(d),
                width=100,
            )
            button.grid(row=0, column=i + 1, padx=5, pady=5)

        # Coordinate and Direction display
        self.direction_label = ctk.CTkLabel(
            direction_frame, text=f"Current Direction: {self.get_current_direction()}"
        )
        self.direction_label.grid(row=1, column=0, columnspan=6, pady=10)

        self.coordinates_label = ctk.CTkLabel(
            direction_frame, text=f"Latitude: {self.latitude}, Longitude: {self.longitude}"
        )
        self.coordinates_label.grid(row=2, column=0, columnspan=6, pady=10)

        # Logs
        log_frame = ctk.CTkFrame(self.root)
        log_frame.pack(fill="both", expand=True, padx=20, pady=10)

        ctk.CTkLabel(
            log_frame, text="System Logs", font=("Arial", 14, "bold")
        ).pack(pady=10)

        self.log_textbox = ctk.CTkTextbox(log_frame, state="disabled", wrap="word")
        self.log_textbox.pack(fill="both", expand=True, padx=10, pady=10)

    def log_event(self, message):
        """Log events to the system log display."""
        timestamp = time.strftime("[%H:%M:%S]", time.localtime())
        self.system_logs.append(f"{timestamp} {message}")
        self.update_logs()

    def update_logs(self):
        """Update the logs textbox."""
        self.log_textbox.configure(state="normal")
        self.log_textbox.delete(1.0, "end")
        self.log_textbox.insert("end", "\n".join(self.system_logs))
        self.log_textbox.configure(state="disabled")

    def toggle_engine(self):
        """Start or stop the engine."""
        self.engine_status = not self.engine_status
        if self.engine_status:
            self.engine_status_label.configure(text="Engine Status: ON")
            self.toggle_engine_button.configure(text="Stop Engine")
            self.log_event("Engine started.")
        else:
            self.engine_status_label.configure(text="Engine Status: OFF")
            self.toggle_engine_button.configure(text="Start Engine")
            self.log_event("Engine stopped.")
            self.current_speed = 0  # Reset speed when engine is off

    def update_coordinates_based_on_direction(self, direction):
        """Update coordinates based on direction."""
        if direction == "Forward":
            self.latitude += self.step_size  # Latitude increases as it moves forward
        elif direction == "Reverse":
            self.latitude -= self.step_size  # Latitude decreases as it moves in reverse
        elif direction == "Left":
            self.longitude -= self.step_size  # Longitude decreases as it turns left
        elif direction == "Right":
            self.longitude += self.step_size  # Longitude increases as it turns right
        elif direction == "Stopped":
            pass  # Do nothing for stop, just keep current position

        # Update coordinate display
        self.coordinates_label.configure(
            text=f"Latitude: {self.latitude:.2f}, Longitude: {self.longitude:.2f}"
        )

    def refuel(self):
        """Refuel the submarine."""
        self.fuel_level = 100.0  # Refuel to full
        self.fuel_bar.set(self.fuel_level / 100)
        self.log_event("Submarine refueled.")

    def set_speed(self):
        """Set the target speed."""
        try:
            self.target_speed = float(self.target_speed_input.get())
            print(f"Target speed set to {self.target_speed} km/h.")  # Debug print
            self.log_event(f"Target speed set to {self.target_speed} km/h.")
        except ValueError:
            self.log_event("Invalid speed value entered.")
            print("Invalid speed value entered.")  # Debug print
            return  # Return if the value is invalid to prevent errors in the system

    def update_system(self):
        """Update system status and simulate real-time changes."""
        # Update the current speed gradually towards target speed
        if self.engine_status and self.current_speed < self.target_speed:
            self.current_speed += self.speed_increase_rate  # Gradual speed increase
            if self.current_speed > self.target_speed:
                self.current_speed = self.target_speed  # Prevent overshooting

        # Update RPM
        self.rpm = int(self.current_speed * self.rpm_factor)

        # Update fuel based on current speed (consumption increases with speed)
        fuel_consumption_rate = self.current_speed * 0.05  # Example rate of fuel consumption
        if self.engine_status and self.fuel_level > 0:
            self.fuel_level -= fuel_consumption_rate
            if self.fuel_level < 0:
                self.fuel_level = 0  # Prevent negative fuel
            self.fuel_bar.set(self.fuel_level / 100)  # Update fuel bar

        # Check for fuel level and alert if it is 50% or lower
        if self.fuel_level <= 50.0:
            self.show_fuel_alert()

        # Update UI labels
        self.speed_label.configure(text=f"Current Speed: {self.current_speed:.2f} km/h")
        self.rpm_label.configure(text=f"Current RPM: {self.rpm}")

        # Schedule the next update
        self.root.after(1000, self.update_system)

    def show_fuel_alert(self):
        """Show a fuel alert when the fuel level is below 50%."""
        self.log_event("Warning: Fuel level is below 50%! Consider refueling.")
        ctk.CTkMessagebox(title="Fuel Warning", message="Fuel level is below 50%! Consider refueling.", icon="warning")


# Create the application window and run the program
if __name__ == "__main__":
    root = ctk.CTk()
    app = PropulsionSystem(root)
    root.mainloop()

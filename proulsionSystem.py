import sys
import random
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QProgressBar, QHBoxLayout, QPushButton, QLineEdit, QFormLayout, QGroupBox, QMessageBox
from math import radians, sin, cos, sqrt, atan2

class PropulsionSystem(QWidget):
    def __init__(self):
        super().__init__()

        # Initial system state
        self.current_speed = 0
        self.target_speed = 0
        self.engine_status = False
        self.fuel_level = 100
        self.speed_threshold = 100
        self.fuel_alert = False
        self.speed_threshold_alert = False

        # Latitude and Longitude for Direction
        self.latitude = 0.0
        self.longitude = 0.0
        self.target_latitude = 0.0
        self.target_longitude = 0.0

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Propulsion System')
        self.setGeometry(100, 100, 500, 500)

        # Layout
        layout = QVBoxLayout()

        # Target Settings GroupBox
        target_group = QGroupBox("Target Settings:")
        target_layout = QFormLayout()

        # Target Speed Input
        self.target_speed_input = QLineEdit(self)
        self.target_speed_input.setPlaceholderText("Enter Target Speed (km/h)")
        target_layout.addRow("Target Speed:", self.target_speed_input)

        # Latitude and Longitude Inputs
        self.latitude_input = QLineEdit(self)
        self.latitude_input.setPlaceholderText("Enter Latitude")
        target_layout.addRow("Latitude:", self.latitude_input)

        self.longitude_input = QLineEdit(self)
        self.longitude_input.setPlaceholderText("Enter Longitude")
        target_layout.addRow("Longitude:", self.longitude_input)

        # Target Latitude and Longitude Inputs
        self.target_latitude_input = QLineEdit(self)
        self.target_latitude_input.setPlaceholderText("Enter Target Latitude")
        target_layout.addRow("Target Latitude:", self.target_latitude_input)

        self.target_longitude_input = QLineEdit(self)
        self.target_longitude_input.setPlaceholderText("Enter Target Longitude")
        target_layout.addRow("Target Longitude:", self.target_longitude_input)

        target_group.setLayout(target_layout)

        # Fuel & Engine Status GroupBox
        fuel_group = QGroupBox("Fuel & Engine Status:")
        fuel_layout = QFormLayout()

        # Fuel Level Display
        self.fuel_label = QLabel(f'Fuel Level: {self.fuel_level}%')
        self.fuel_bar = QProgressBar(self)
        self.fuel_bar.setRange(0, 100)
        fuel_layout.addRow(self.fuel_label, self.fuel_bar)

        # Engine Status Display
        self.engine_label = QLabel('Engine Status: OFF')
        self.engine_button = QPushButton('Toggle Engine', self)
        self.engine_button.clicked.connect(self.toggle_engine)
        fuel_layout.addRow(self.engine_label, self.engine_button)

        # Fill Fuel Button
        self.fill_fuel_button = QPushButton('Fill Fuel', self)
        self.fill_fuel_button.clicked.connect(self.fill_fuel)
        fuel_layout.addRow(self.fill_fuel_button)

        fuel_group.setLayout(fuel_layout)

        # Current Readings GroupBox
        readings_group = QGroupBox("Current Readings:")
        readings_layout = QFormLayout()

        # Current Speed Display
        self.current_speed_label = QLabel(f'Current Speed: {self.current_speed} km/h')
        readings_layout.addRow(self.current_speed_label)

        # Current Latitude and Longitude Display
        self.current_latitude_label = QLabel(f'Current Latitude: {self.latitude}')
        self.current_longitude_label = QLabel(f'Current Longitude: {self.longitude}')
        readings_layout.addRow(self.current_latitude_label, self.current_longitude_label)

        # Direction Display
        self.current_direction_label = QLabel("Direction: Calculating...")
        readings_layout.addRow(self.current_direction_label)

        # Speed Threshold Alert
        self.threshold_label = QLabel(f'Speed Threshold Alert: {"Alert" if self.speed_threshold_alert else "Normal"}')
        readings_layout.addRow(self.threshold_label)

        readings_group.setLayout(readings_layout)

        # Buttons
        self.set_speed_button = QPushButton('Set Speed', self)
        self.set_speed_button.clicked.connect(self.set_speed)
        self.set_direction_button = QPushButton('Set Direction', self)
        self.set_direction_button.clicked.connect(self.set_direction)

        layout.addWidget(target_group)
        layout.addWidget(fuel_group)
        layout.addWidget(readings_group)
        layout.addWidget(self.set_speed_button)
        layout.addWidget(self.set_direction_button)

        self.setLayout(layout)

        # Set timer for updating system states
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_system)
        self.timer.start(1000)

    def toggle_engine(self):
        self.engine_status = not self.engine_status
        self.update_engine_indicator()

    def set_speed(self):
        try:
            self.target_speed = float(self.target_speed_input.text())
            self.adjust_speed(self.target_speed)
        except ValueError:
            self.current_speed_label.setText('Invalid input for speed')

    def adjust_speed(self, target_speed):
        self.current_speed = target_speed
        self.fuel_bar.setValue(self.fuel_level)
        self.current_speed_label.setText(f'Current Speed: {self.current_speed} km/h')

        if self.current_speed > self.speed_threshold:
            self.speed_threshold_alert = True
            self.threshold_label.setText(f'Speed Threshold Alert: Alert')
        else:
            self.speed_threshold_alert = False
            self.threshold_label.setText(f'Speed Threshold Alert: Normal')

    def set_direction(self):
        try:
            # Get user input for current and target coordinates
            self.latitude = float(self.latitude_input.text())
            self.longitude = float(self.longitude_input.text())
            self.target_latitude = float(self.target_latitude_input.text())
            self.target_longitude = float(self.target_longitude_input.text())

            # Calculate the direction from current coordinates to target coordinates
            direction = self.calculate_direction(self.latitude, self.longitude, self.target_latitude, self.target_longitude)
            self.current_direction_label.setText(f'Direction: {direction}')
            self.current_latitude_label.setText(f'Current Latitude: {self.latitude}')
            self.current_longitude_label.setText(f'Current Longitude: {self.longitude}')
        except ValueError:
            self.current_direction_label.setText('Invalid input for coordinates')

    def calculate_direction(self, lat1, lon1, lat2, lon2):
        # Convert latitude and longitude from degrees to radians
        lat1 = radians(lat1)
        lon1 = radians(lon1)
        lat2 = radians(lat2)
        lon2 = radians(lon2)

        # Haversine formula to calculate the bearing
        dlon = lon2 - lon1
        dlat = lat2 - lat1

        x = sin(dlat) * cos(lat2)
        y = cos(lat1) * sin(lat2) - sin(lat1) * cos(lat2) * cos(dlon)

        # Calculate the bearing angle
        initial_bearing = atan2(x, y)
        initial_bearing = radians(initial_bearing)  # Convert to degrees

        # Normalize the bearing to 0-360 degrees
        compass_bearing = (initial_bearing + 360) % 360

        # Determine the direction (N, S, E, W)
        if 0 <= compass_bearing < 45 or 315 <= compass_bearing < 360:
            return 'North'
        elif 45 <= compass_bearing < 135:
            return 'East'
        elif 135 <= compass_bearing < 225:
            return 'South'
        elif 225 <= compass_bearing < 315:
            return 'West'

    def update_engine_indicator(self):
        if self.engine_status:
            self.engine_label.setText('Engine Status: ON')
        else:
            self.engine_label.setText('Engine Status: OFF')

    def fill_fuel(self):
        self.fuel_level = 100
        self.fuel_bar.setValue(self.fuel_level)
        self.fuel_label.setText(f'Fuel Level: {self.fuel_level}%')

    def update_system(self):
        # If engine is on, decrease fuel by 5 units every second
        if self.engine_status:
            if self.fuel_level > 0:
                self.fuel_level -= 5
            else:
                self.fuel_level = 0  # Ensure fuel doesn't go negative
        
        # Randomize speed and coordinates every second
        self.current_speed = random.randint(0, 120)  # Random speed between 0 and 120 km/h
        self.latitude = random.uniform(-90.0, 90.0)  # Random latitude between -90 and 90
        self.longitude = random.uniform(-180.0, 180.0)  # Random longitude between -180 and 180

        # Update progress bar and labels
        self.fuel_bar.setValue(self.fuel_level)
        self.fuel_label.setText(f'Fuel Level: {self.fuel_level}%')
        self.current_speed_label.setText(f'Current Speed: {self.current_speed} km/h')

        # Simulate the direction change
        self.current_latitude_label.setText(f'Current Latitude: {self.latitude}')
        self.current_longitude_label.setText(f'Current Longitude: {self.longitude}')

        # Fuel alert if the fuel level drops below 50
        if self.fuel_level < 50 and not self.fuel_alert:
            self.fuel_alert = True
            self.show_fuel_alert()

    def show_fuel_alert(self):
        alert_msg = "Fuel Level Below 50%! Please Refill Fuel."
        QMessageBox.warning(self, "Fuel Alert", alert_msg)  # GUI pop-up message box
        self.fuel_alert = False  # Reset the alert after showing


if __name__ == '__main__':
    app = QApplication(sys.argv)
    system = PropulsionSystem()
    system.show()
    sys.exit(app.exec_())

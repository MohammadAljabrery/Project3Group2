import sys
import random
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QProgressBar, QHBoxLayout, QPushButton, QLineEdit, QFormLayout, QGroupBox, QMessageBox

class EnvironmentalControlSystem(QWidget):
    def __init__(self):
        super().__init__()

        # Initial system state
        self.current_temperature = 22  # Starting temperature in Celsius
        self.target_temperature = 22
        self.current_humidity = 50  # Starting humidity in percentage
        self.target_humidity = 50
        self.temp_threshold = 30  # High temperature alert
        self.humidity_threshold = 40  # Low humidity alert
        self.temp_alert = False
        self.humidity_alert = False

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Environmental Control System')
        self.setGeometry(100, 100, 500, 500)

        # Layout
        layout = QVBoxLayout()

        # Target Settings GroupBox
        target_group = QGroupBox("Target Settings:")
        target_layout = QFormLayout()

        # Target Temperature Input
        self.target_temperature_input = QLineEdit(self)
        self.target_temperature_input.setPlaceholderText("Enter Target Temperature (°C)")
        target_layout.addRow("Target Temperature:", self.target_temperature_input)

        # Target Humidity Input
        self.target_humidity_input = QLineEdit(self)
        self.target_humidity_input.setPlaceholderText("Enter Target Humidity (%)")
        target_layout.addRow("Target Humidity:", self.target_humidity_input)

        target_group.setLayout(target_layout)

        # Temperature & Humidity Status GroupBox
        status_group = QGroupBox("Temperature & Humidity Status:")
        status_layout = QFormLayout()

        # Temperature Display
        self.temperature_label = QLabel(f'Temperature: {self.current_temperature}°C')
        self.temperature_bar = QProgressBar(self)
        self.temperature_bar.setRange(0, 50)  # Temperature range (0-50°C)
        status_layout.addRow(self.temperature_label, self.temperature_bar)

        # Humidity Display
        self.humidity_label = QLabel(f'Humidity: {self.current_humidity}%')
        self.humidity_bar = QProgressBar(self)
        self.humidity_bar.setRange(0, 100)  # Humidity range (0-100%)
        status_layout.addRow(self.humidity_label, self.humidity_bar)

        status_group.setLayout(status_layout)

        # Buttons
        self.set_temperature_button = QPushButton('Set Temperature', self)
        self.set_temperature_button.clicked.connect(self.set_temperature)
        self.set_humidity_button = QPushButton('Set Humidity', self)
        self.set_humidity_button.clicked.connect(self.set_humidity)

        layout.addWidget(target_group)
        layout.addWidget(status_group)
        layout.addWidget(self.set_temperature_button)
        layout.addWidget(self.set_humidity_button)

        self.setLayout(layout)

        # Set timer for updating system states
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_system)
        self.timer.start(1000)

    def set_temperature(self):
        try:
            self.target_temperature = float(self.target_temperature_input.text())
            self.adjust_temperature(self.target_temperature)
        except ValueError:
            self.temperature_label.setText('Invalid input for temperature')

    def adjust_temperature(self, target_temperature):
        self.current_temperature = target_temperature
        self.temperature_bar.setValue(self.current_temperature)
        self.temperature_label.setText(f'Temperature: {self.current_temperature}°C')

        if self.current_temperature > self.temp_threshold:
            self.temp_alert = True
            self.show_temperature_alert()
        else:
            self.temp_alert = False

    def set_humidity(self):
        try:
            self.target_humidity = float(self.target_humidity_input.text())
            self.adjust_humidity(self.target_humidity)
        except ValueError:
            self.humidity_label.setText('Invalid input for humidity')

    def adjust_humidity(self, target_humidity):
        self.current_humidity = target_humidity
        self.humidity_bar.setValue(self.current_humidity)
        self.humidity_label.setText(f'Humidity: {self.current_humidity}%')

        if self.current_humidity < self.humidity_threshold:
            self.humidity_alert = True
            self.show_humidity_alert()
        else:
            self.humidity_alert = False

    def update_system(self):
        # Randomize temperature and humidity every second
        self.current_temperature = random.randint(18, 30)  # Random temperature between 18 and 30°C
        self.current_humidity = random.randint(30, 60)  # Random humidity between 30 and 60%

        # Update progress bars and labels
        self.temperature_bar.setValue(self.current_temperature)
        self.temperature_label.setText(f'Temperature: {self.current_temperature}°C')

        self.humidity_bar.setValue(self.current_humidity)
        self.humidity_label.setText(f'Humidity: {self.current_humidity}%')

        # Check if any alert conditions are met
        if self.current_temperature > self.temp_threshold and not self.temp_alert:
            self.temp_alert = True
            self.show_temperature_alert()

        if self.current_humidity < self.humidity_threshold and not self.humidity_alert:
            self.humidity_alert = True
            self.show_humidity_alert()

    def show_temperature_alert(self):
        alert_msg = "Temperature Above Threshold! Please Adjust Temperature."
        QMessageBox.warning(self, "Temperature Alert", alert_msg)  # GUI pop-up message box

    def show_humidity_alert(self):
        alert_msg = "Humidity Below Threshold! Please Adjust Humidity."
        QMessageBox.warning(self, "Humidity Alert", alert_msg)  # GUI pop-up message box


if __name__ == '__main__':
    app = QApplication(sys.argv)
    system = EnvironmentalControlSystem()
    system.show()
    sys.exit(app.exec_())

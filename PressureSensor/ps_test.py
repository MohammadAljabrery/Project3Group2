import unittest
from PressureSensor.PS import *
from unittest.mock import patch
import customtkinter as ctk
import time

class TestPressureSensor(unittest.TestCase):
    def setUp(self):

        self.root = ctk.CTk()
        self.pressure_sensor = PressureSensor(self.root)

    def tearDown(self):

        self.root.destroy()

    def test_pressure_within_range(self):

        for _ in range(100):
            self.pressure_sensor.simulate_pressure_data()
            pressure = self.pressure_sensor.get_pressure()
            self.assertGreaterEqual(pressure, 800, "Pressure is below 800 PSI")
            self.assertLessEqual(pressure, 1200, "Pressure is above 1200 PSI")

class TestPressureSensorRealTimeUpdate(unittest.TestCase):

    def setUp(self):

        self.root = ctk.CTk()
        self.pressure_sensor = PressureSensor(self.root)

    def tearDown(self):

        self.root.destroy()

    @patch.object(PressureSensor, 'simulate_pressure_data')
    def test_pressure_real_time_update(self, mock_simulate):

        start_time = time.time()
        update_times = []

        for _ in range(5):
            self.pressure_sensor.update_pressure_data()
            update_times.append(time.time() - start_time)
            time.sleep(1)  # Wait for the interval to mimic real-time updates

        for i in range(1, len(update_times)):
            self.assertAlmostEqual(update_times[i], update_times[i-1] + 1, delta=0.1, msg="Update interval deviates from 1 second.")


if __name__ == '__main__':
    unittest.main()


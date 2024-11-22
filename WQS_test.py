import unittest
from WQS import *
import customtkinter as ctk

class TestWaterQualitySensor(unittest.TestCase):

    def setUp(self):
        self.root = ctk.CTk()
        self.water_quality_sensor = WaterQualitySensor(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_ph_within_range(self):
        for _ in range(100):
            self.water_quality_sensor.simulate_sensor_data()
            ph_value = self.water_quality_sensor.ph_level
            self.assertGreaterEqual(ph_value, 6.5)
            self.assertLessEqual(ph_value, 8.5)

class TestWaterQualitySensor02(unittest.TestCase):

    def setUp(self):
        self.root = ctk.CTk()
        self.water_quality_sensor = WaterQualitySensor(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_ppm_within_range(self):
        for _ in range(100):
            self.water_quality_sensor.simulate_sensor_data()
            ppm_value = self.water_quality_sensor.ppm_level
            self.assertGreaterEqual(ppm_value, 200)
            self.assertLessEqual(ppm_value, 800)


if __name__ == '__main__':
    unittest.main()

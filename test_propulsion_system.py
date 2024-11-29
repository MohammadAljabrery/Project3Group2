import unittest
from PropulsionSystem import PropulsionSystem
from unittest.mock import MagicMock
import customtkinter as ctk
import time

class TestPropulsionSystem(unittest.TestCase):
    
    def setUp(self):
        """Setup for each test case."""
        # Create a mock for the Tkinter root window
        self.root_mock = MagicMock(spec=ctk.CTk)
        self.system = PropulsionSystem(self.root_mock)

    def test_initial_state(self):
        """Test the initial state of the system."""
        self.assertEqual(self.system.current_speed, 0.0)
        self.assertEqual(self.system.target_speed, 0.0)
        self.assertEqual(self.system.fuel_level, 100.0)
        self.assertEqual(self.system.engine_status, False)
        self.assertEqual(self.system.get_current_direction(), "Stopped")

    def test_set_current_direction_engine_off(self):
        """Test direction change when engine is off."""
        self.system.set_current_direction("Forward")
        self.assertEqual(self.system.get_current_direction(), "Stopped")
        self.assertIn("Cannot change direction", self.system.system_logs)

    def test_set_current_direction_engine_on(self):
        """Test direction change when engine is on."""
        self.system.toggle_engine()  # Turn engine on
        self.system.set_current_direction("Forward")
        self.assertEqual(self.system.get_current_direction(), "Forward")
        self.assertIn("Direction changed to Forward", self.system.system_logs)

    def test_toggle_engine_on(self):
        """Test toggling the engine to ON."""
        self.system.toggle_engine()
        self.assertEqual(self.system.engine_status, True)
        self.assertIn("Engine started", self.system.system_logs)

    def test_toggle_engine_off(self):
        """Test toggling the engine to OFF."""
        self.system.toggle_engine()  # Turn engine on first
        self.system.toggle_engine()  # Then turn it off
        self.assertEqual(self.system.engine_status, False)
        self.assertIn("Engine stopped", self.system.system_logs)

    def test_set_speed_valid(self):
        """Test setting a valid target speed."""
        self.system.target_speed_input.set("50")
        self.system.set_speed()
        self.assertEqual(self.system.target_speed, 50.0)
        self.assertIn("Target speed set to 50.0 km/h", self.system.system_logs)

    def test_set_speed_invalid(self):
        """Test setting an invalid target speed."""
        self.system.target_speed_input.set("invalid")
        self.system.set_speed()
        self.assertEqual(self.system.target_speed, 0.0)  # No speed change on error
        self.assertIn("Invalid speed value entered", self.system.system_logs)

    def test_update_coordinates_forward(self):
        """Test coordinate update when moving forward."""
        self.system.set_current_direction("Forward")
        self.assertEqual(self.system.latitude, 0.1)  # Step size is 0.1
        self.assertEqual(self.system.longitude, 0.0)
    
    def test_update_coordinates_reverse(self):
        """Test coordinate update when moving in reverse."""
        self.system.set_current_direction("Reverse")
        self.assertEqual(self.system.latitude, -0.1)  # Step size is -0.1
        self.assertEqual(self.system.longitude, 0.0)

    def test_update_coordinates_left(self):
        """Test coordinate update when turning left."""
        self.system.set_current_direction("Left")
        self.assertEqual(self.system.latitude, 0.0)
        self.assertEqual(self.system.longitude, -0.1)  # Step size is -0.1

    def test_update_coordinates_right(self):
        """Test coordinate update when turning right."""
        self.system.set_current_direction("Right")
        self.assertEqual(self.system.latitude, 0.0)
        self.assertEqual(self.system.longitude, 0.1)  # Step size is 0.1

    def test_refuel(self):
        """Test refueling the submarine."""
        self.system.fuel_level = 50.0  # Set fuel to 50%
        self.system.refuel()
        self.assertEqual(self.system.fuel_level, 100.0)
        self.assertIn("Submarine refueled.", self.system.system_logs)

    def test_update_system_speed_increase(self):
        """Test the gradual speed increase towards the target speed."""
        self.system.target_speed = 10.0
        self.system.current_speed = 5.0
        self.system.update_system()
        self.assertGreater(self.system.current_speed, 5.0)  # Speed should increase

    def test_update_system_fuel_consumption(self):
        """Test fuel consumption based on current speed."""
        initial_fuel = self.system.fuel_level
        self.system.current_speed = 20.0  # Simulate some speed
        self.system.update_system()
        self.assertLess(self.system.fuel_level, initial_fuel)  # Fuel should decrease

    def test_show_fuel_alert(self):
        """Test the fuel alert when fuel level is low."""
        self.system.fuel_level = 40.0  # Below 50% threshold
        self.system.show_fuel_alert()
        self.assertIn("Warning: Fuel level is below 50%!", self.system.system_logs)

if __name__ == "__main__":
    unittest.main()

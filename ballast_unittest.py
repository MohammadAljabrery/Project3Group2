import unittest
from ballast_system import BallastSystem

class TestBallastSystem(unittest.TestCase):
    def setUp(self):
        self.ballast_system = BallastSystem()

    # Test Case ID: Ballast_Init_001
    def test_initialization(self):
        self.assertEqual(self.ballast_system.tank1_volume, 0.0)
        self.assertEqual(self.ballast_system.tank2_volume, 0.0)
        self.assertEqual(self.ballast_system.max_tank1_volume, 500.0)
        self.assertEqual(self.ballast_system.max_tank2_volume, 500.0)
        self.assertEqual(self.ballast_system.depth, 0.0)

    # Test Case ID: Ballast_Fill_Valid_002
    def test_fill_valid(self):
        success, message = self.ballast_system.fill_ballast(500.0)
        self.assertTrue(success)
        self.assertEqual(self.ballast_system.tank1_volume, 250.0)
        self.assertEqual(self.ballast_system.tank2_volume, 250.0)

    # Test Case ID: Ballast_Fill_OverCapacity_003
    def test_fill_over_capacity(self):
        success, message = self.ballast_system.fill_ballast(1200.0)
        self.assertFalse(success)
        self.assertEqual(message, "Tank can only fill 1000L!")
        self.assertEqual(self.ballast_system.tank1_volume, 0.0)
        self.assertEqual(self.ballast_system.tank2_volume, 0.0)

    # Test Case ID: Ballast_Drain_Valid_004
    def test_drain_valid(self):
        self.ballast_system.fill_ballast(500.0)
        success, message = self.ballast_system.drain_ballast(200.0)
        self.assertTrue(success)
        self.assertEqual(self.ballast_system.tank1_volume, 150.0)
        self.assertEqual(self.ballast_system.tank2_volume, 150.0)

    # Test Case ID: Ballast_Drain_ExceedsVolume_005
    def test_drain_exceeds_volume(self):
        self.ballast_system.fill_ballast(300.0)
        success, message = self.ballast_system.drain_ballast(400.0)
        self.assertFalse(success)
        self.assertEqual(message, "Tank can only Drain 300.0L!")
        self.assertEqual(self.ballast_system.tank1_volume, 150.0)
        self.assertEqual(self.ballast_system.tank2_volume, 150.0)

    # Test Case ID: Ballast_Depth_Calculation_006
    def test_depth_calculation(self):
        self.ballast_system.fill_ballast(300.0)
        self.assertEqual(self.ballast_system.depth, 30.0)

    # Test Case ID: Ballast_Negative_Input_007
    def test_negative_input(self):
        success_fill, message_fill = self.ballast_system.fill_ballast(-100.0)
        success_drain, message_drain = self.ballast_system.drain_ballast(-50.0)
        
        self.assertFalse(success_fill)  # Check if the function returns False
        self.assertEqual(message_fill, "No Negative value Accepted")  # Check for the expected message
        
        self.assertFalse(success_drain)  # Similarly, check for the drain method
        self.assertEqual(message_drain, "No Negative value Accepted")  # Check for the expected message
        
        # Ensure that the volumes remain unchanged
        self.assertEqual(self.ballast_system.tank1_volume, 0.0)
        self.assertEqual(self.ballast_system.tank2_volume, 0.0)



    # Test Case ID: Ballast_Fill_Partial_008
    def test_fill_partial(self):
        self.ballast_system.fill_ballast(900.0)
        success, message = self.ballast_system.fill_ballast(200.0)
        self.assertFalse(success)
        self.assertEqual(message, "Tank can only fill 100.0L!")
        self.assertEqual(self.ballast_system.tank1_volume, 450.0)
        self.assertEqual(self.ballast_system.tank2_volume, 450.0)

    # Test Case ID: Ballast_Drain_Empty_009
    def test_drain_empty(self):
        success, message = self.ballast_system.drain_ballast(100.0)
        self.assertFalse(success)
        self.assertEqual(message, "Tank is empty! Can't drain more water.")
        self.assertEqual(self.ballast_system.tank1_volume, 0.0)
        self.assertEqual(self.ballast_system.tank2_volume, 0.0)

    # Test Case ID: Ballast_Boundary_010
    def test_boundary_conditions(self):
        # Fill exactly to capacity
        success, message = self.ballast_system.fill_ballast(1000.0)
        self.assertTrue(success)
        self.assertEqual(self.ballast_system.tank1_volume, 500.0)
        self.assertEqual(self.ballast_system.tank2_volume, 500.0)
        
        # Drain exact volume from full capacity
        success, message = self.ballast_system.drain_ballast(1000.0)
        self.assertTrue(success)
        self.assertEqual(self.ballast_system.tank1_volume, 0.0)
        self.assertEqual(self.ballast_system.tank2_volume, 0.0)

    # Test Case ID: Ballast_Zero_Input_011
    def test_zero_volume_input(self):
        success_fill, message_fill = self.ballast_system.fill_ballast(0.0)
        success_drain, message_drain = self.ballast_system.drain_ballast(0.0)
        self.assertTrue(success_fill)
        self.assertEqual(message_fill, "")
        self.assertEqual(self.ballast_system.tank1_volume, 0.0)
        self.assertEqual(self.ballast_system.tank2_volume, 0.0)
        self.assertTrue(success_drain)
        self.assertEqual(message_drain, "")

if __name__ == "__main__":
    unittest.main()

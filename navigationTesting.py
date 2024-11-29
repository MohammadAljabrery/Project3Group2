import unittest
import math
from navigation import NavigationSystem  # Assuming your NavigationSystem is in navigation.py


class TestNavigationSystem(unittest.TestCase):

    def test_NAV_TC1_set_waypoint(self):
        # NAV_TC1: Verify setWaypoint sets the waypoint correctly
        nav = NavigationSystem(0.0, 0.0, 0)
        nav.setWaypoint(45.0, -75.0)
        self.assertEqual(nav.getWaypoint(), (45.0, -75.0), "Waypoint not set correctly.")

    def test_NAV_TC2_invalid_waypoint(self):
        # NAV_TC2: Verify setWaypoint rejects invalid latitude/longitude
        nav = NavigationSystem(0.0, 0.0, 0)
        nav.setWaypoint(45.0, -75.0)  # Set a valid waypoint first
        nav.setWaypoint(100.0, -200.0)  # Invalid waypoint
        self.assertEqual(nav.getWaypoint(), (45.0, -75.0), "Invalid waypoint accepted.")

    def test_NAV_TC3_set_course(self):
        # NAV_TC3: Verify setDirection sets the direction correctly
        nav = NavigationSystem(0.0, 0.0, 0)
        nav.setDirection(90)
        self.assertEqual(nav.getDirection(), 90, "Direction not set correctly.")

    def test_NAV_TC4_boundary_direction(self):
        # NAV_TC4: Verify setDirection handles 0 and 360 correctly
        nav = NavigationSystem(0.0, 0.0, 0)
        nav.setDirection(0)
        self.assertEqual(nav.getDirection(), 0, "Direction 0 not handled correctly.")
        nav.setDirection(360)
        self.assertEqual(nav.getDirection(), 360, "Direction 360 not handled correctly.")

    def test_NAV_TC5_calculate_distance(self):
        # NAV_TC5: Verify calculateDistanceToWaypoint computes correct distance
        nav = NavigationSystem(44.0, -76.0, 0)
        nav.setWaypoint(45.0, -75.0)
        distance = nav.calculateDistanceToWaypoint()
        expected_distance = 157.2  # Close to this value in km
        self.assertAlmostEqual(distance, expected_distance, delta=0.5, msg="Distance calculation incorrect.")


if __name__ == '__main__':
    unittest.main()

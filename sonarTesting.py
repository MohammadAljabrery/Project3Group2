import unittest
from sonar import SonarSystem

class TestSonarSystem(unittest.TestCase):
    def setUp(self):
        self.sonar = SonarSystem()

    def test_adjustFrequency_valid(self):
        self.assertTrue(self.sonar.adjustFrequency(2000))
        self.assertEqual(self.sonar.getFrequency(), 2000)

    def test_adjustFrequency_invalid(self):
        self.sonar.adjustFrequency(2000)
        self.assertFalse(self.sonar.adjustFrequency(-100))
        self.assertEqual(self.sonar.getFrequency(), 2000)

    def test_adjustRange_valid(self):
        self.assertTrue(self.sonar.adjustRange(500))
        self.assertEqual(self.sonar.getRange(), 500)

    def test_adjustRange_max(self):
        self.assertTrue(self.sonar.adjustRange(1000))
        self.assertEqual(self.sonar.getRange(), 1000)

    def test_adjustPulseDuration_valid(self):
        self.assertTrue(self.sonar.adjustPulseDuration(0.5))
        self.assertEqual(self.sonar.getPulseDuration(), 0.5)

    def test_adjustPulseDuration_zero(self):
        self.sonar.adjustPulseDuration(1)
        self.assertFalse(self.sonar.adjustPulseDuration(0))
        self.assertEqual(self.sonar.getPulseDuration(), 1)

    def test_adjustBeamWidth_valid(self):
        self.assertTrue(self.sonar.adjustBeamWidth(30))
        self.assertEqual(self.sonar.getBeamWidth(), 30)

if __name__ == '__main__':
    unittest.main()

import unittest
import os
from logger import LoggerSystem
import datetime

class TestLoggerSystem(unittest.TestCase):

    def setUp(self):
        """Set up a LoggerSystem instance and clean the test log file."""
        self.log_file = "test_logs.txt"
        self.logger = LoggerSystem(self.log_file)

        # Ensure the log file is empty before each test
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

    def tearDown(self):
        """Clean up the test log file."""
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

    def test_LOG_TC1_valid_log_entry(self):
        """Test that logAction correctly logs an entry with valid input."""
        self.logger.logAction("user123", "User logged in")
        logs = self.logger.getLogs()
        self.assertIn("User logged in", logs)
        self.assertIn("user123", logs)
        self.assertTrue("USER: user123 | ACTION: User logged in" in logs, "Log entry not correctly formatted.")

    def test_LOG_TC2_empty_action(self):
        """Test that logAction handles an empty action description."""
        self.logger.logAction("user123", "")
        logs = self.logger.getLogs()
        self.assertIn("user123", logs)
        self.assertIn("ACTION: ", logs, "Empty action description not logged correctly.")

    def test_LOG_TC3_log_saved_to_file(self):
        """Test that logs are saved to the external file."""
        self.logger.logAction("user456", "User action saved")
        self.logger.saveLogs()

        # Read the file and check the saved log
        with open(self.log_file, "r") as file:
            file_contents = file.read()

        self.assertIn("User action saved", file_contents)
        self.assertIn("user456", file_contents)
        self.assertTrue("USER: user456 | ACTION: User action saved" in file_contents, "Log not correctly saved to file.")


if __name__ == "__main__":
    unittest.main()

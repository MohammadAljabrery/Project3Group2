import unittest
import customtkinter as ctk
from LightControlSystem.classes import Sliders
from LightControlSystem.classes import OptionBox

class TestBrightnessSlider(unittest.TestCase):
    def setUp(self):
        # Create a root window for testing as the master for CTkFrame
        self.root = ctk.CTk()
        self.slider_app = Sliders()
        self.test_frame = ctk.CTkFrame(master=self.root)  # specify root as master
        self.test_label = ctk.CTkLabel(self.test_frame, text="0%")  # test label simulating the slider's display

    def tearDown(self):
        # Destroy the root window after each test to clean up
        self.root.destroy()

    def test_brightness_slider_zero(self):
        self.slider_app.update_label(self.test_label, 0)
        self.assertEqual(self.test_label.cget("text"), "0%")

    def test_brightness_slider_middle(self):
        self.slider_app.update_label(self.test_label, 50)
        self.assertEqual(self.test_label.cget("text"), "50%")

    def test_brightness_slider_full(self):
        self.slider_app.update_label(self.test_label, 100)
        self.assertEqual(self.test_label.cget("text"), "100%")

class TestColorSelection(unittest.TestCase):
    def setUp(self):
        # Set up a root window and frame for testing
        self.root = ctk.CTk()
        self.option_box_app = OptionBox()
        self.test_frame = ctk.CTkFrame(master=self.root)
        # Create option box with color options
        self.color_options = ["Red", "Blue", "Green"]
        self.color_box = self.option_box_app.create_option_box(self.test_frame, values=self.color_options, row=0, column=0, padx=5, pady=5)

    def tearDown(self):
        # Clean up the root window after each test
        self.root.destroy()

    def test_color_selection_red(self):
        # Select "Red" from the color list box
        self.color_box.set("Red")
        self.assertEqual(self.color_box.get(), "Red")

    def test_color_selection_blue(self):
        # Select "Blue" from the color list box
        self.color_box.set("Blue")
        self.assertEqual(self.color_box.get(), "Blue")

    def test_color_selection_green(self):
        # Select "Green" from the color list box
        self.color_box.set("Green")
        self.assertEqual(self.color_box.get(), "Green")


if __name__ == '__main__':
    unittest.main()

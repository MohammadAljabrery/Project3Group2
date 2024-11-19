import tkinter as tk
from ballast_system_gui import BallastSystemGUI  # Import the BallastSystemGUI class

# Main function
def main():
    root = tk.Tk()
    app = BallastSystemGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()


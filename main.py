import tkinter as tk
from security_system import SecuritySystem
from security_system_gui import SecuritySystemGUI
from ballast_system_gui import BallastSystemGUI

def validation_callback(result, root):
    if result:       
        
        new_window = tk.Toplevel(root)
         
        app = BallastSystemGUI(new_window) 
        new_window.mainloop()  
        root.destroy()          
       
    else:
        print("Invalid code or Access Denied.")

def main():
    security_system = SecuritySystem()
    root = tk.Tk()  # Main Tkinter window for the entire application
    app = SecuritySystemGUI(root, security_system, validation_callback)  # Pass the callback with root
    
    # Start the GUI loop
    root.mainloop()

if __name__ == "__main__":
    main()


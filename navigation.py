import random
import math
from tkinter import *
from tkinter import messagebox

class NavigationSystem:
    def __init__(self, currentLatitude, currentLongitude, currentDirection):
        self.Latitude = currentLatitude
        self.Longitude = currentLongitude
        self.Direction = currentDirection
        self.waypoints = []
    
    # GETTERS
    def getLatitude(self):
        return self.Latitude
    
    def getLongitude(self):
        return self.Longitude
    
    def getDirection(self):
        return self.Direction
    
    def getWaypoint(self):
        if self.waypoints:
            return self.waypoints[0]  # Return the first waypoint tuple
        return None  # No waypoints are set

        
        
    # SETTERS
    def setWaypoint(self, newLatitude, newLongitude):
        """Sets or updates the current waypoint."""
        if self.waypoints:
            self.waypoints[0] = (newLatitude, newLongitude)  # Update the first waypoint
        else:
            self.waypoints.append((newLatitude, newLongitude))  # Add the first waypoint
        print(f"New waypoint set: {newLatitude}°N, {newLongitude}°E")

        
    def setDirection(self, newDirection):
        self.Direction = newDirection
        print(f"Course adjusted to {newDirection} degrees.")

    def calculateDistanceToWaypoint(self):
        """Calculates and returns the distance to the next waypoint."""
        if not self.waypoints:
            return None

        nextWaypoint = self.waypoints[0]

        # Correctly use the attribute names
        lat1 = math.radians(self.Latitude)
        lon1 = math.radians(self.Longitude)

        lat2 = math.radians(nextWaypoint[0])  # latitude of next waypoint
        lon2 = math.radians(nextWaypoint[1])  # longitude of next waypoint

        # Haversine formula to calculate the distance between two points on the Earth
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = 6371 * c  # Earth radius in kilometers

        return distance

    
    def displayStatus(self):
        """Displays the current position, direction, and distance to the next waypoint."""
        print(f"Current position: {self.currentLatitude}° N, {self.currentLongitude}° E")
        print(f"Current direction: {self.currentDirection} degrees")
        
        if self.waypoints:
            distance = self.calculateDistanceToWaypoint()
            print(f"Distance to next waypoint: {distance:.2f} km")
        else:
            print("No destination waypoints set.")

def navigation_gui():
    navigation = NavigationSystem(88.00, -172.00, 70)
    
    def updateStatus():
        # Update the position label
        positionLabel.config(text=f"{navigation.getLatitude()}°N, {navigation.getLongitude()}°E")

        # Update the direction label
        directionLabel.config(text=f"{navigation.getDirection()}°")

        # Update the waypoint and distance labels
        waypoint = navigation.getWaypoint()
        if waypoint:
            distance = navigation.calculateDistanceToWaypoint()
            if distance is not None:
                waypointLabel.config(text=f"Next Waypoint: {waypoint[0]}°N, {waypoint[1]}°E")
                distanceLabel.config(text=f"Distance To Waypoint: {distance:.2f} km")
            else:
                distanceLabel.config(text="N/A")
        else:
            waypointLabel.config(text="No Waypoint Set.")
            distanceLabel.config(text="N/A")




        
    def setWaypoint():
        try:
            lat = float(latitudeEntry.get())
            if not (-90 <= lat <= 90):
                messagebox.showerror("Error", "Please enter valid latitude (-90 to 90).")
                return
            lon = float(longitudeEntry.get())
            if not (-180 <= lon <= 180):
                messagebox.showerror("Error", "Please enter valid longitude (-180 to 180).")
                return
            navigation.setWaypoint(lat, lon)
            messagebox.showinfo("Waypoint Set", f"Waypoint set to: {lat}°N, {lon}°E")
            updateStatus()  # Update the GUI labels
        except ValueError:
            messagebox.showerror("Error", "Please enter valid latitude and longitude values.")



    
    def setCourse():
        try:
            direction = float(directionEntry.get())
            if not (0 <= direction <= 360):
                messagebox.showerror("Error", "Please enter valid direction (0 to 360).")
                return
            navigation.setDirection(direction)
            messagebox.showinfo("Course Set", f"Course adjusted to: {direction}°")
            updateStatus()  # Update the GUI labels
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid direction (in degrees).")


    
    window = Tk()
    window.title("Navigation System Control")
    window.geometry("1920x1080")
    window.configure(bg="lightblue")

    # Main layout
    mainFrame = Frame(window, bg="lightblue")
    mainFrame.pack(expand=True, fill="both", padx=20, pady=20)

    # Current Position
    positionFrame = Frame(mainFrame, bg="lightgrey", padx=10, pady=10, borderwidth=2, relief="solid")
    positionFrame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    Label(positionFrame, text="Current Position", font=("Consolas", 14), bg="lightgrey").pack(anchor="center")
    positionLabel = Label(positionFrame, text="0.0°N, 0.0°E", font=("Consolas", 12), bg="lightgrey")
    positionLabel.pack(anchor="center")

    # Current Direction
    directionFrame = Frame(mainFrame, bg="lightgrey", padx=10, pady=10, borderwidth=2, relief="solid")
    directionFrame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
    Label(directionFrame, text="Current Direction", font=("Consolas", 14), bg="lightgrey").pack(anchor="center")
    directionLabel = Label(directionFrame, text="0.0°", font=("Consolas", 12), bg="lightgrey")
    directionLabel.pack(anchor="center")

    # Set Course
    setCourseFrame = Frame(mainFrame, bg="lightgrey", padx=10, pady=10, borderwidth=2, relief="solid")
    setCourseFrame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
    Label(setCourseFrame, text="Set Course", font=("Consolas", 14), bg="lightgrey").grid(row=0, column=0, columnspan=2)
    Label(setCourseFrame, text="Direction (°):", bg="lightgrey").grid(row=1, column=0, sticky="e")
    directionEntry = Entry(setCourseFrame, font=("Consolas", 12))
    directionEntry.grid(row=1, column=1, pady=5)
    Button(setCourseFrame, text="Set Course", font=("Consolas", 12), command=setCourse).grid(row=2, column=0, columnspan=2, pady=10)

    # Waypoint
    waypointFrame = Frame(mainFrame, bg="lightgrey", padx=10, pady=10, borderwidth=2, relief="solid")
    waypointFrame.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
    Label(waypointFrame, text="Waypoint", font=("Consolas", 14), bg="lightgrey").pack(anchor="center")
    waypointLabel = Label(waypointFrame, text="No Waypoint Set.", font=("Consolas", 12), bg="lightgrey")
    waypointLabel.pack(anchor="center")

    # Distance to Waypoint
    distanceFrame = Frame(mainFrame, bg="lightgrey", padx=10, pady=10, borderwidth=2, relief="solid")
    distanceFrame.grid(row=2, column=2, sticky="nsew", padx=10, pady=10)
    Label(distanceFrame, text="Distance to Waypoint", font=("Consolas", 14), bg="lightgrey").pack(anchor="center")
    distanceLabel = Label(distanceFrame, text="N/A", font=("Consolas", 12), bg="lightgrey")
    distanceLabel.pack(anchor="center")

    # Set Waypoint
    setWaypointFrame = Frame(mainFrame, bg="lightgrey", padx=10, pady=10, borderwidth=2, relief="solid")
    setWaypointFrame.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)
    Label(setWaypointFrame, text="Set Waypoint", font=("Consolas", 14), bg="lightgrey").grid(row=0, column=0, columnspan=2)
    Label(setWaypointFrame, text="Latitude:", bg="lightgrey").grid(row=1, column=0, sticky="e")
    Label(setWaypointFrame, text="Longitude:", bg="lightgrey").grid(row=2, column=0, sticky="e")
    latitudeEntry = Entry(setWaypointFrame, font=("Consolas", 12))
    longitudeEntry = Entry(setWaypointFrame, font=("Consolas", 12))
    latitudeEntry.grid(row=1, column=1, pady=5)
    longitudeEntry.grid(row=2, column=1, pady=5)
    Button(setWaypointFrame, text="Set Waypoint", font=("Consolas", 12), command=setWaypoint).grid(row=3, column=0, columnspan=2, pady=10)

    # Make the grid cells expand evenly
    mainFrame.columnconfigure(0, weight=1)
    mainFrame.columnconfigure(1, weight=1)
    mainFrame.columnconfigure(2, weight=1)
    mainFrame.rowconfigure(0, weight=1)
    mainFrame.rowconfigure(1, weight=1)
    mainFrame.rowconfigure(2, weight=1)

    updateStatus()
    window.mainloop()
    
navigation_gui()
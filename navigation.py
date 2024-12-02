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

class NavigationFrame(Frame):
    def __init__(self, parent, previous_window):
        super().__init__(parent, bg="lightblue")
        self.parent = parent
        self.previous_window = previous_window  # Reference to the previous window

        # Navigation System initialization
        self.navigation = NavigationSystem(88.00, -172.00, 70)

        # Main layout
        mainFrame = Frame(self, bg="lightblue")
        mainFrame.pack(expand=True, fill="both", padx=20, pady=20)

        # Current Position
        positionFrame = Frame(mainFrame, bg="lightgrey", padx=10, pady=10, borderwidth=2, relief="solid")
        positionFrame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        Label(positionFrame, text="Current Position", font=("Consolas", 14), bg="lightgrey").pack(anchor="center")
        self.positionLabel = Label(positionFrame, text="0.0°N, 0.0°E", font=("Consolas", 12), bg="lightgrey")
        self.positionLabel.pack(anchor="center")

        # Current Direction
        directionFrame = Frame(mainFrame, bg="lightgrey", padx=10, pady=10, borderwidth=2, relief="solid")
        directionFrame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        Label(directionFrame, text="Current Direction", font=("Consolas", 14), bg="lightgrey").pack(anchor="center")
        self.directionLabel = Label(directionFrame, text="0.0°", font=("Consolas", 12), bg="lightgrey")
        self.directionLabel.pack(anchor="center")

        # Set Course
        setCourseFrame = Frame(mainFrame, bg="lightgrey", padx=10, pady=10, borderwidth=2, relief="solid")
        setCourseFrame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
        Label(setCourseFrame, text="Set Course", font=("Consolas", 14), bg="lightgrey").grid(row=0, column=0, columnspan=2)
        Label(setCourseFrame, text="Direction (°):", bg="lightgrey").grid(row=1, column=0, sticky="e")
        self.directionEntry = Entry(setCourseFrame, font=("Consolas", 12))
        self.directionEntry.grid(row=1, column=1, pady=5)
        Button(setCourseFrame, text="Set Course", font=("Consolas", 12), command=self.setCourse).grid(row=2, column=0, columnspan=2, pady=10)

        # Waypoint
        waypointFrame = Frame(mainFrame, bg="lightgrey", padx=10, pady=10, borderwidth=2, relief="solid")
        waypointFrame.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
        Label(waypointFrame, text="Waypoint", font=("Consolas", 14), bg="lightgrey").pack(anchor="center")
        self.waypointLabel = Label(waypointFrame, text="No Waypoint Set.", font=("Consolas", 12), bg="lightgrey")
        self.waypointLabel.pack(anchor="center")

        # Distance to Waypoint
        distanceFrame = Frame(mainFrame, bg="lightgrey", padx=10, pady=10, borderwidth=2, relief="solid")
        distanceFrame.grid(row=2, column=2, sticky="nsew", padx=10, pady=10)
        Label(distanceFrame, text="Distance to Waypoint", font=("Consolas", 14), bg="lightgrey").pack(anchor="center")
        self.distanceLabel = Label(distanceFrame, text="N/A", font=("Consolas", 12), bg="lightgrey")
        self.distanceLabel.pack(anchor="center")

        # Set Waypoint
        setWaypointFrame = Frame(mainFrame, bg="lightgrey", padx=10, pady=10, borderwidth=2, relief="solid")
        setWaypointFrame.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)
        Label(setWaypointFrame, text="Set Waypoint", font=("Consolas", 14), bg="lightgrey").grid(row=0, column=0, columnspan=2)
        Label(setWaypointFrame, text="Latitude:", bg="lightgrey").grid(row=1, column=0, sticky="e")
        Label(setWaypointFrame, text="Longitude:", bg="lightgrey").grid(row=2, column=0, sticky="e")
        self.latitudeEntry = Entry(setWaypointFrame, font=("Consolas", 12))
        self.longitudeEntry = Entry(setWaypointFrame, font=("Consolas", 12))
        self.latitudeEntry.grid(row=1, column=1, pady=5)
        self.longitudeEntry.grid(row=2, column=1, pady=5)
        Button(setWaypointFrame, text="Set Waypoint", font=("Consolas", 12), command=self.setWaypoint).grid(row=3, column=0, columnspan=2, pady=10)

        # Back Button
        Button(mainFrame, text="Back", font=("Consolas", 12), command=self.goBack).grid(row=3, column=1, pady=20)

        # Make the grid cells expand evenly
        mainFrame.columnconfigure(0, weight=1)
        mainFrame.columnconfigure(1, weight=1)
        mainFrame.columnconfigure(2, weight=1)
        mainFrame.rowconfigure(0, weight=1)
        mainFrame.rowconfigure(1, weight=1)
        mainFrame.rowconfigure(2, weight=1)

        self.updateStatus()

    def updateStatus(self):
        # Update the position label
        self.positionLabel.config(text=f"{self.navigation.getLatitude()}°N, {self.navigation.getLongitude()}°E")
        self.directionLabel.config(text=f"{self.navigation.getDirection()}°")
        waypoint = self.navigation.getWaypoint()
        if waypoint:
            distance = self.navigation.calculateDistanceToWaypoint()
            if distance is not None:
                self.waypointLabel.config(text=f"Next Waypoint: {waypoint[0]}°N, {waypoint[1]}°E")
                self.distanceLabel.config(text=f"Distance To Waypoint: {distance:.2f} km")
            else:
                self.distanceLabel.config(text="N/A")
        else:
            self.waypointLabel.config(text="No Waypoint Set.")
            self.distanceLabel.config(text="N/A")

    def setWaypoint(self):
        try:
            lat = float(self.latitudeEntry.get())
            lon = float(self.longitudeEntry.get())
            if not (-90 <= lat <= 90) or not (-180 <= lon <= 180):
                messagebox.showerror("Error", "Please enter valid coordinates.")
                return
            self.navigation.setWaypoint(lat, lon)
            self.updateStatus()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")

    def setCourse(self):
        try:
            direction = float(self.directionEntry.get())
            if not (0 <= direction <= 360):
                messagebox.showerror("Error", "Please enter a valid direction (0-360).")
                return
            self.navigation.setDirection(direction)
            self.updateStatus()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def goBack(self):
        self.parent.destroy()
        self.previous_window.deiconify()


def run_navigation_frame(parent, previous_window):
    frame = NavigationFrame(parent, previous_window)
    frame.pack(fill=BOTH, expand=True)
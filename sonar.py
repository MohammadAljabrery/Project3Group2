import random 
from logger import LoggerSystem
from time import sleep
from tkinter import *
from tkinter import ttk

class SonarSystem:
    def __init__(self, frequency: float = 0.0, range: float = 0.0, pulseDuration: float = 0.0, beamWidth: float = 0.0):
        self.frequency = frequency
        self.range = range
        self.pulseDuration = pulseDuration
        self.beamWidth = beamWidth

    # GETTERS      
    def getFrequency(self):
        return self.frequency
    
    def getRange(self):
        return self.range
    
    def getPulseDuration(self):
        return self.pulseDuration
    
    def getBeamWidth(self):
        return self.beamWidth
    #SETTERS
    def adjustFrequency(self, newFrequency: float):
        if (1000 <= newFrequency <= 10000):
            self.frequency = newFrequency
            print(f"Frequency set to: {self.frequency} Hz")
            return True # so it will return true if everything is aiit
        else:
            print("Frequency out of range!")
            return False # it return false if everything is mid
    
    def adjustRange(self, newRange: float):
        if (1 <= newRange <= 1000):
            self.range = newRange
            return True # so it will return true if everything is aiit
        else:
            print("Range out of range!")
            return False # it return false if everything is mid
    
    def adjustPulseDuration(self, newPulseDuration: float):
        if (newPulseDuration > 0):
            self.pulseDuration = newPulseDuration
            return True # so it will return true if everything is aiit
        else:
            print("Pulse duration must be more than 0 seconds!")
            return False # it return false if everything is mid
        
    def adjustBeamWidth(self, newBeamWidth: float):
        if (0 < newBeamWidth <= 360):
            self.beamWidth = newBeamWidth
            return True # so it will return true if everything is aiit
        else:
            print("Beam width must be a real angle!")
            return False # it return false if everything is mid
    
    def detectObjects(self):
        currentFrequency = int(self.getFrequency())
        currentRange = int(self.getRange())
        currentPulseDuration = int(self.getPulseDuration())
        currentBeamWidth = int(self.getBeamWidth())
        print(f"Starting object detection with frequency: {currentFrequency} Hz, range: {currentRange} m, pulse duration: {currentPulseDuration} s, beam width: {currentBeamWidth} degrees")
    
        detectedObjects = []
        objectCount = 1
        detection_probability = min(0.1 + (currentFrequency - 1000) / 10000, 0.9)
        max_range = min(currentRange, 1000 - (currentFrequency - 1000) / 10)
    
        for second in range(currentPulseDuration):
            if random.random() < detection_probability:
                distance = random.uniform(1, max_range)
                angle = random.uniform(0, currentBeamWidth)
                detectedObjects.append({
                    "Object Number": objectCount,
                    "Distance (m)": round(distance, 2),
                    "Angle (degrees)": round(angle, 2)
                })
                print(f"Second {second + 1}: Detected object #{objectCount} at distance {distance:.2f} m, angle {angle:.2f} degrees")
                objectCount += 1
            else:
                print(f"Second {second + 1}: No object detected")
            #sleep(1)
        print("Object detection complete!")
        return detectedObjects


class SonarFrame(Frame):
    def __init__(self, parent, previous_window):
        super().__init__(parent, bg="lightblue")
        self.parent = parent
        self.previous_window = previous_window  # Store the reference to the previous window

        # Create an instance of SonarSystem
        self.sonar = SonarSystem()

        # Frequency Frame
        frequencyFrame = Frame(self)
        frequencyFrame.pack(anchor='w', pady=10)
        self.frequencySlider = Scale(frequencyFrame,
                                     from_=1000,
                                     to=10000,
                                     length=1000,
                                     orient=HORIZONTAL,
                                     font=('Consolas', 13),
                                     tickinterval=3000,
                                     label="Frequency (Hz)",
                                     command=self.onFrequencyChange,
                                     bg="lightgrey")
        self.frequencySlider.pack(anchor='center', pady=2)
        self.frequencyLabel = Label(frequencyFrame, text=f"Frequency set to: {self.sonar.getFrequency()} Hz",
                                     font=('Consolas', 12), bg="lightgrey")
        self.frequencyLabel.pack(anchor='center', pady=2)
        self.frequencyEntry = Entry(frequencyFrame,
                                     font=('Consolas', 12),
                                     fg="black",
                                     bg="lightgrey")
        self.frequencyEntry.pack(anchor='center', pady=2)
        self.frequencyApplyButton = Button(frequencyFrame,
                                           text="Apply Frequency Setting",
                                           command=lambda: self.onFrequencyChange(None))
        self.frequencyApplyButton.pack(anchor='center', pady=2)

        # Range Frame
        rangeFrame = Frame(self)
        rangeFrame.pack(anchor='w', pady=10)
        self.rangeSlider = Scale(rangeFrame,
                                 from_=1,
                                 to=1000,
                                 length=1000,
                                 orient=HORIZONTAL,
                                 font=('Consolas', 13),
                                 tickinterval=100,
                                 label="Range (meters)",
                                 command=self.onRangeChange,
                                 bg="lightgrey")
        self.rangeSlider.pack(anchor='center', pady=2)
        self.rangeLabel = Label(rangeFrame, text=f"Range set to: {self.sonar.getRange()} meters",
                                font=('Consolas', 12), bg="lightgrey")
        self.rangeLabel.pack(anchor='center', pady=2)
        self.rangeEntry = Entry(rangeFrame, font=('Consolas', 12), fg="black", bg="lightgrey")
        self.rangeEntry.pack(anchor='center', pady=2)
        self.rangeApplyButton = Button(rangeFrame, text="Apply Range Setting", command=lambda: self.onRangeChange(None))
        self.rangeApplyButton.pack(anchor='center', pady=2)

        # Pulse Duration Frame
        pulseDurationFrame = Frame(self)
        pulseDurationFrame.pack(anchor='w', pady=10)
        self.pulseDurationSlider = Scale(pulseDurationFrame,
                                         from_=0,
                                         length=1000,
                                         orient=HORIZONTAL,
                                         font=('Consolas', 13),
                                         tickinterval=100,
                                         label="Pulse duration (seconds)",
                                         command=self.onPulseDurationChange,
                                         bg="lightgrey")
        self.pulseDurationSlider.pack(anchor='center', pady=2)
        self.pulseDurationLabel = Label(pulseDurationFrame, text=f"Pulse duration set to: {self.sonar.getRange()} meters",
                                        font=('Consolas', 12), bg="lightgrey")
        self.pulseDurationLabel.pack(anchor='center', pady=2)
        self.pulseDurationEntry = Entry(pulseDurationFrame, font=('Consolas', 12), fg="black", bg="lightgrey")
        self.pulseDurationEntry.pack(anchor='center', pady=2)
        self.pulseDurationApplyButton = Button(pulseDurationFrame, text="Apply Pulse duration Setting",
                                               command=lambda: self.onPulseDurationChange(None))
        self.pulseDurationApplyButton.pack(anchor='center', pady=2)

        # Beam Width Frame
        beamWidthFrame = Frame(self)
        beamWidthFrame.pack(anchor='w', pady=10)
        self.beamWidthSlider = Scale(beamWidthFrame,
                                     from_=0,
                                     to=360,
                                     length=1000,
                                     orient=HORIZONTAL,
                                     font=('Consolas', 13),
                                     tickinterval=100,
                                     label="beam width (degrees)",
                                     command=self.onBeamWidthChange,
                                     bg="lightgrey")
        self.beamWidthSlider.pack(anchor='center', pady=2)
        self.beamWidthLabel = Label(beamWidthFrame, text=f"Beam width set to: {self.sonar.getBeamWidth()} meters",
                                    font=('Consolas', 12), bg="lightgrey")
        self.beamWidthLabel.pack(anchor='center', pady=2)
        self.beamWidthEntry = Entry(beamWidthFrame, font=('Consolas', 12), fg="black", bg="lightgrey")
        self.beamWidthEntry.pack(anchor='center', pady=2)
        self.beamWidthApplyButton = Button(beamWidthFrame, text="Apply Beam width Setting",
                                           command=lambda: self.onBeamWidthChange(None))
        self.beamWidthApplyButton.pack(anchor='center', pady=2)

        # Object Detection Frame
        objectDetectionFrame = Frame(self, bg="lightgrey")
        objectDetectionFrame.place(relx=0.98, rely=0.01, anchor='ne', width=600, height=400)
        self.objectDetectionTitleLabel = Label(objectDetectionFrame,
                                               text="Detected Objects:",
                                               font=('Consolas', 14),
                                               bg="white",
                                               fg="black")
        self.objectDetectionTitleLabel.pack(anchor='w', pady=5, padx=10)
        self.detectButton = Button(self, text="Start Detection",
                                   command=lambda: self.updateObjectDetectionTable(self.sonar.detectObjects()))
        self.detectButton.pack(anchor='center', pady=20)
        self.style = ttk.Style()
        self.style.configure("Treeview", font=("Consolas", 12))
        self.style.configure("Treeview.Heading", font=("Consolas", 14, "bold"))
        self.objectDetectionTable = ttk.Treeview(objectDetectionFrame,
                                                 columns=("objectNumber", "distance", "angle"),
                                                 show="headings",
                                                 height=15)
        self.objectDetectionTable.pack(fill="both", expand=True, padx=10, pady=10)
        self.objectDetectionTable.heading("objectNumber", text="Object Number")
        self.objectDetectionTable.heading("distance", text="Distance (meters)")
        self.objectDetectionTable.heading("angle", text="Angle (degrees)")
        self.objectDetectionTable.column("objectNumber", anchor="center", width=150)
        self.objectDetectionTable.column("distance", anchor="center", width=150)
        self.objectDetectionTable.column("angle", anchor="center", width=150)
        self.objectDetectionTable.tag_configure("odd", background="lightgrey")
        self.objectDetectionTable.tag_configure("even", background="white")


        back_button = Button(self, text="Back", font=('Consolas', 12), command=self.go_back)
        back_button.pack(anchor='center', pady=20)

    def go_back(self):
        """Go back to the previous window."""
        self.parent.destroy()  # Close the current Sonar window
        self.previous_window.deiconify()  # Show the navigation menu again
    #FREQUENCY
    def onFrequencyChange(self, value=None):
        # If a value is provided by the slider, use it; otherwise, get it from the entry box
        if value is not None:
            frequency = float(value)  # Value from slider
        else:
            try:
                frequency = float(self.frequencyEntry.get())  # Value from entry box
            except ValueError:
                self.frequencyLabel.config(text="Invalid input!")
                return

        # Set frequency and update feedback label
        if self.sonar.adjustFrequency(frequency):
            self.frequencyLabel.config(text=f"Frequency set to: {self.sonar.getFrequency()} Hz")
            # Synchronize the slider if the value came from the entry box
            if value is None:
                self.frequencySlider.set(frequency)
        else:
            self.frequencyLabel.config(text="Frequency out of range!")
    
    #RANGE    
    def onRangeChange(self, value=None):
        if value is not None:
            range_value = float(value)  # Value from slider
        else:
            try:
                range_value = float(self.rangeEntry.get())  # Value from entry box
            except ValueError:
                self.rangeLabel.config(text="Invalid input!")
                return

        if self.sonar.adjustRange(range_value):
            self.rangeLabel.config(text=f"Range set to: {self.sonar.getRange()} meters")
            if value is None:
                self.rangeSlider.set(range_value)
        else:
            self.rangeLabel.config(text="Range out of range!")
    
    #PULSE DURATION
    def onPulseDurationChange(self, value=None):
        if value is not None:
            pulse_duration = float(value)  # Value from slider
        else:
            try:
                pulse_duration = float(self.pulseDurationEntry.get())  # Value from entry box
            except ValueError:
                self.pulseDurationLabel.config(text="Invalid input!")
                return

        if self.sonar.adjustPulseDuration(pulse_duration):
            self.pulseDurationLabel.config(text=f"Pulse duration set to: {self.sonar.getPulseDuration()} s")
            if value is None:
                self.pulseDurationSlider.set(pulse_duration)
        else:
            self.pulseDurationLabel.config(text="Pulse duration must be > 0!")  
            
     #BEAM WIDTH       
    def onBeamWidthChange(self, value=None):
        if value is not None:
            beam_width = float(value)  # Value from slider
        else:
            try:
                beam_width = float(self.beamWidthEntry.get())  # Value from entry box
            except ValueError:
                self.beamWidthLabel.config(text="Invalid input!")
                return

        if self.sonar.adjustBeamWidth(beam_width):
            self.beamWidthLabel.config(text=f"Beam width set to: {self.sonar.getBeamWidth()} degrees")
            if value is None:
                self.beamWidthSlider.set(beam_width)
        else:
            self.beamWidthLabel.config(text="Beam width must be a real angle!")     
    
    #OBJECT DETECTION
    def updateObjectDetectionTable(self, detectedObjects):
        # Clear the table before adding new data
        self.objectDetectionTable.delete(*self.objectDetectionTable.get_children())
    
        def display_object(index=0):
            # Check if we have more objects to display
            if index < len(detectedObjects):
                obj = detectedObjects[index]
                # Determine the row tag for alternating colors
                row_tag = "odd" if index % 2 == 0 else "even"
                # Insert object data into the Treeview table with the appropriate tag
                self.objectDetectionTable.insert("", "end", values=(obj['Object Number'], obj['Distance (m)'], obj['Angle (degrees)']), tags=(row_tag,))
                # Schedule the next object to be displayed after 1 second
                self.master.after(1000, display_object, index + 1)
    
        # Start displaying objects
        display_object()



# Run the GUI setup function
def run_sonar_frame(parent):
    frame = SonarFrame(parent)
    frame.pack(fill=BOTH, expand=True)


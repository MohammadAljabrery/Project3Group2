import random 
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


def setup_gui():
    sonar = SonarSystem()

    #FREQUENCY
    def onFrequencyChange(value=None):
        # If a value is provided by the slider, use it; otherwise, get it from the entry box
        if value is not None:
            frequency = float(value)  # Value from slider
        else:
            try:
                frequency = float(frequencyEntry.get())  # Value from entry box
            except ValueError:
                frequencyLabel.config(text="Invalid input!")
                return

        # Set frequency and update feedback label
        if sonar.adjustFrequency(frequency):
            frequencyLabel.config(text=f"Frequency set to: {sonar.getFrequency()} Hz")
            # Synchronize the slider if the value came from the entry box
            if value is None:
                frequencySlider.set(frequency)
        else:
            frequencyLabel.config(text="Frequency out of range!")
    
    #RANGE    
    def onRangeChange(value=None):
        if value is not None:
            range_value = float(value)  # Value from slider
        else:
            try:
                range_value = float(rangeEntry.get())  # Value from entry box
            except ValueError:
                rangeLabel.config(text="Invalid input!")
                return

        if sonar.adjustRange(range_value):
            rangeLabel.config(text=f"Range set to: {sonar.getRange()} meters")
            if value is None:
                rangeSlider.set(range_value)
        else:
            rangeLabel.config(text="Range out of range!")
    
    #PULSE DURATION
    def onPulseDurationChange(value=None):
        if value is not None:
            pulse_duration = float(value)  # Value from slider
        else:
            try:
                pulse_duration = float(pulseDurationEntry.get())  # Value from entry box
            except ValueError:
                pulseDurationLabel.config(text="Invalid input!")
                return

        if sonar.adjustPulseDuration(pulse_duration):
            pulseDurationLabel.config(text=f"Pulse duration set to: {sonar.getPulseDuration()} s")
            if value is None:
                pulseDurationSlider.set(pulse_duration)
        else:
            pulseDurationLabel.config(text="Pulse duration must be > 0!")  
            
     #BEAM WIDTH       
    def onBeamWidthChange(value=None):
        if value is not None:
            beam_width = float(value)  # Value from slider
        else:
            try:
                beam_width = float(beamWidthEntry.get())  # Value from entry box
            except ValueError:
                beamWidthLabel.config(text="Invalid input!")
                return

        if sonar.adjustBeamWidth(beam_width):
            beamWidthLabel.config(text=f"Beam width set to: {sonar.getBeamWidth()} degrees")
            if value is None:
                beamWidthSlider.set(beam_width)
        else:
            beamWidthLabel.config(text="Beam width must be a real angle!")     
    
    #OBJECT DETECTION
    def updateObjectDetectionTable(detectedObjects):
        # Clear the table before adding new data
        objectDetectionTable.delete(*objectDetectionTable.get_children())
    
        def display_object(index=0):
            # Check if we have more objects to display
            if index < len(detectedObjects):
                obj = detectedObjects[index]
                # Determine the row tag for alternating colors
                row_tag = "odd" if index % 2 == 0 else "even"
                # Insert object data into the Treeview table with the appropriate tag
                objectDetectionTable.insert("", "end", values=(obj['Object Number'], obj['Distance (m)'], obj['Angle (degrees)']), tags=(row_tag,))
                # Schedule the next object to be displayed after 1 second
                window.after(1000, display_object, index + 1)
    
        # Start displaying objects
        display_object()


    window = Tk()
    window.title("Sonar System Control")
    window.geometry("1920x1080")
    window.configure(bg="lightblue")
    frequencyFrame = Frame(window)
    frequencyFrame.pack(anchor='w',pady=10)
    rangeFrame = Frame(window)
    rangeFrame.pack(anchor='w',pady=10)
    pulseDurationFrame = Frame(window)
    pulseDurationFrame.pack(anchor='w',pady=10)
    beamWidthFrame = Frame(window)
    beamWidthFrame.pack(anchor='w',pady=10)
    objectDetectionFrame = Frame(window, bg="lightgrey")
    objectDetectionFrame.place(relx=0.98,rely=0.01,anchor='ne', width=600,height=400)
    
    # FREQUENCY
    frequencySlider = Scale(frequencyFrame,
                            from_=1000,
                            to=10000,
                            length=1000,    # Reduced length to make it more compact
                            orient=HORIZONTAL,
                            font=('Consolas', 13),
                            tickinterval=3000, # Keep tick interval for every 2000 Hz
                            label="Frequency (Hz)",
                            command=onFrequencyChange,
                            bg="lightgrey")
    frequencySlider.pack(anchor='center',pady=2)
    frequencyLabel = Label(frequencyFrame, text=f"Frequency set to: {sonar.getFrequency()} Hz", font=('Consolas', 12), bg="lightgrey")
    frequencyLabel.pack(anchor='center',pady=2)
    frequencyEntry = Entry(frequencyFrame,
                           font=('Consolas', 12),
                            fg="black",
                            bg="lightgrey"
                            )                           
    frequencyEntry.pack(anchor='center',pady=2)
    frequencyApplyButton = Button(frequencyFrame,
                                  text="Apply Frequency Setting",
                                  command=lambda: onFrequencyChange(None),
                                  )
    frequencyApplyButton.pack(anchor='center',pady=2)

    #RANGE
    rangeSlider = Scale(rangeFrame,
                            from_=1,
                            to=1000,
                            length=1000,    # Reduced length to make it more compact
                            orient=HORIZONTAL,
                            font=('Consolas', 13),
                            tickinterval=100, # Keep tick interval for every 2000 Hz
                            label="Range (meters)",
                            command=onRangeChange,
                            bg="lightgrey")
    rangeSlider.pack(anchor='center',pady=2)
    rangeLabel = Label(rangeFrame, text=f"Range set to: {sonar.getRange()} meters", font=('Consolas', 12), bg="lightgrey")
    rangeLabel.pack(anchor='center',pady=2)
    rangeEntry = Entry(rangeFrame, font=('Consolas', 12), fg="black", bg="lightgrey")                           
    rangeEntry.pack(anchor='center',pady=2)
    rangeApplyButton = Button(rangeFrame, text="Apply Range Setting", command=lambda: onRangeChange(None))
    rangeApplyButton.pack(anchor='center',pady=2)
    #PULSE DURATION
    pulseDurationSlider = Scale(pulseDurationFrame,
                            from_=0,
                            #to=1000,
                            length=1000,    # Reduced length to make it more compact
                            orient=HORIZONTAL,
                            font=('Consolas', 13),
                            tickinterval=100, # Keep tick interval for every 2000 Hz
                            label="Pulse duration (seconds)",
                            command=onPulseDurationChange,
                            bg="lightgrey")
    pulseDurationSlider.pack(anchor='center',pady=2)
    pulseDurationLabel = Label(pulseDurationFrame, text=f"Pulse duration set to: {sonar.getRange()} meters", font=('Consolas', 12), bg="lightgrey")
    pulseDurationLabel.pack(anchor='center',pady=2)
    pulseDurationEntry = Entry(pulseDurationFrame, font=('Consolas', 12), fg="black", bg="lightgrey")                           
    pulseDurationEntry.pack(anchor='center',pady=2)
    pulseDurationApplyButton = Button(pulseDurationFrame, text="Apply Pulse duration Setting", command=lambda: onPulseDurationChange(None))
    pulseDurationApplyButton.pack(anchor='center',pady=2)
    
    #BEAM WIDTH
    beamWidthSlider = Scale(beamWidthFrame,
                            from_=0,
                            to=360,
                            length=1000,    # Reduced length to make it more compact
                            orient=HORIZONTAL,
                            font=('Consolas', 13),
                            tickinterval=100, # Keep tick interval for every 2000 Hz
                            label="beam width (degrees)",
                            command=onBeamWidthChange,
                            bg="lightgrey")
    beamWidthSlider.pack(anchor='center',pady=2)
    beamWidthLabel = Label(beamWidthFrame, text=f"Beam width set to: {sonar.getBeamWidth()} meters", font=('Consolas', 12), bg="lightgrey")
    beamWidthLabel.pack(anchor='center',pady=2)
    beamWidthEntry = Entry(beamWidthFrame, font=('Consolas', 12), fg="black", bg="lightgrey")                           
    beamWidthEntry.pack(anchor='center',pady=2)
    beamWidthApplyButton = Button(beamWidthFrame, text="Apply Beam width Setting", command=lambda: onBeamWidthChange(None))
    beamWidthApplyButton.pack(anchor='center',pady=2)
    
    #DETECTION TABLE NAME
    objectDetectionTitleLabel = Label(objectDetectionFrame,
                                      text="Detected Objects:",
                                      font=('Consolas', 14),
                                          bg="white",
                                          fg="black"
                                    )
    objectDetectionTitleLabel.pack(anchor='w', pady=5, padx=10)
    
    #DETECTION BUTTON
    detectButton = Button(window, text="Start Detection", command=lambda: updateObjectDetectionTable(sonar.detectObjects()))
    detectButton.pack(anchor='center', pady=20)
    # DETECTION TABLE
    style = ttk.Style()
    style.configure("Treeview", font=("Consolas", 12))
    style.configure("Treeview.Heading", font=("Consolas", 14, "bold"))
    objectDetectionTable = ttk.Treeview(objectDetectionFrame,
                                        columns=("objectNumber", "distance", "angle"),
                                        show="headings",
                                        height=15)
    objectDetectionTable.pack(fill="both", expand=True, padx=10, pady=10)
    objectDetectionTable.heading("objectNumber", text="Object Number")
    objectDetectionTable.heading("distance", text="Distance (meters)")
    objectDetectionTable.heading("angle", text="Angle (degrees)")
    objectDetectionTable.column("objectNumber", anchor="center", width=150)
    objectDetectionTable.column("distance", anchor="center", width=150)
    objectDetectionTable.column("angle", anchor="center", width=150)
    
    # DETECTION TABLE ALTERNATING COLOURS
    objectDetectionTable.tag_configure("odd", background="lightgrey")
    objectDetectionTable.tag_configure("even", background="white")

    window.mainloop()

# Run the GUI setup function
def run_sonar_gui():
    setup_gui()
    

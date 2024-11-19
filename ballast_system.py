class BallastSystem:
    def __init__(self):
        self.tank1_volume = 0
        self.tank2_volume = 0
        self.max_tank1_volume = 500
        self.max_tank2_volume = 500
        self.depth = 0  # in meters

    def fill_ballast(self, volume):
        if self.tank1_volume + self.tank2_volume + volume > self.max_tank1_volume+ self.max_tank2_volume:
            total_volume_left = (self.max_tank1_volume+ self.max_tank2_volume) - (self.tank1_volume + self.tank2_volume)
            if(total_volume_left == 1000):
                return False, "Tank is Full"
            else:
                return False, f"Tank can only fill {total_volume_left}L!"
        else:
            self.tank1_volume += volume/2
            self.tank2_volume += volume/2
            self.update_depth()
            return True, ""

    def drain_ballast(self, volume):
        if self.tank1_volume + self.tank2_volume - volume < 0:
            total_volume = (self.tank1_volume+self.tank2_volume)
            
            if (total_volume == 0):
                return False, "Tank is empty! Can't drain more water."
            else:
                return False, f"Tank can only Drain {total_volume}L!"
                
        else:
            self.tank1_volume -= volume/2
            self.tank2_volume -= volume/2
            self.update_depth()
            return True, ""

    def update_depth(self):
        self.depth = (self.tank1_volume+self.tank2_volume) / 10  # Simple depth model

def main():
    system = BallastSystem()
    
    while True:
        print("\n--- Submarine Ballast System ---")
        print(f"Current Tank 1 Volume: {system.tank1_volume:.2f}L")
        print(f"Current Tank 2 Volume: {system.tank2_volume:.2f}L")
        print(f"Total Volume: {system.tank1_volume + system.tank2_volume:.2f}L")
        print(f"Current Depth: {system.depth:.2f}m")
        
        action = input("Enter 'f' to fill ballast or 'q' to quit: ").strip().lower()
        if action == 'q':
            print("Exiting the Ballast System.")
            break
        elif action == 'f':
            try:
                volume = float(input("Enter the volume to fill (in liters): "))
                success, message = system.fill_ballast(volume)
                if not success:
                    print(f"Warning: {message}")
                else:
                    print("Ballast filled successfully!")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        else:
            print("Invalid action. Please enter 'f' or 'q'.")

# Run the main function
if __name__ == "__main__":
    main()

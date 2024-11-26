class BallastSystem:
    def __init__(self):
        self.tank1_volume = 0
        self.tank2_volume = 0
        self.max_tank1_volume = 500
        self.max_tank2_volume = 500
        self.depth = 0  # in meters

    def fill_ballast(self, volume):
        if volume < 0:
            return False, "No Negative value Accepted"
        
        if self.tank1_volume + self.tank2_volume + volume > self.max_tank1_volume + self.max_tank2_volume:
            total_volume_left = (self.max_tank1_volume + self.max_tank2_volume) - (self.tank1_volume + self.tank2_volume)
            return False, f"Tank can only fill {total_volume_left}L!"
        
        self.tank1_volume += volume / 2
        self.tank2_volume += volume / 2
        self.update_depth()
        return True, ""


    def drain_ballast(self, volume):
        
        if volume < 0:
            return False,"No Negative value Accepted"
        
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


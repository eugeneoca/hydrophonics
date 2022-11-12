

class PHController:
    
    def __init__(self):
        self.current_value = 0
        self.target_value = 0

    def read(self):
        return self.current_value

    def readTarget(self):
        return self.target_value

    def increase(self):
        self.current_value+=1

    def decrease(self):
        self.current_value-=1

    def increaseTarget(self):
        self.target_value+=1

    def decreaseTarget(self):
        self.target_value-=1
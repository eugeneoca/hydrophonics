

class SupplyController:
    
    def __init__(self):
        self.current_value = 0

    def read(self):
        return self.current_value
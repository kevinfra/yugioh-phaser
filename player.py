class Player:

    def __init__(self):
        self.lp = 8000
        self.triggers = [[],[],[],[],[],[]]

    def update_lp(self, lp):
        self.lp = lp
    
    def add_trigger(self, phase_number, card_name):
        self.triggers[phase_number].append(card_name)

    def triggers_in_phase(self, phase_number):
        return self.triggers[phase_number]
    
    def clear_triggers(self, phase_number):
        self.triggers[phase_number].clear()

class Game:

    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.current_player = 0
        self.TOTAL_PHASES = 6 
        self.PHASES = ['Draw', 'Stand by', 'Main1', 'Battle', 'Main2', 'End']

    def start(self):
        while self.players[0].lp > 0 or self.players[1].lp > 0:
            print(f'Starting turn for Player: {"0" if self.current_player == 0 else "1"}')
            for phase_number in range(self.TOTAL_PHASES):
                print(f'Entring {self.PHASES[phase_number]} Phase')
                
                # Check Triggers
                current_player_triggers = self.players[self.current_player].triggers_in_phase(phase_number)
                self.check_triggers(current_player_triggers, 'Current')
                self.players[self.current_player].clear_triggers(phase_number)
                second_player_triggers = self.players[(self.current_player + 1) % 2].triggers_in_phase(phase_number)
                self.check_triggers(second_player_triggers, 'Other')
                self.players[(self.current_player + 1) % 2].clear_triggers(phase_number)

                # Wait for adding new triggers
                card_name_trigger = input('Name of card for next trigger (leave blank if none)')
                while card_name_trigger != '':
                    phase_to_trigger = input(f"When should this card trigger? ({', '.join(self.PHASES)})")
                    phase_number_to_activate = self.PHASES.index(phase_to_trigger)
                    player = int(input('Which player has this trigger? (0 for starting player, 1 otherwise)'))
                    self.players[player].add_trigger(phase_number_to_activate, card_name_trigger)
                    card_name_trigger = input('Name of card for next trigger (leave blank if none)')

                update = input('Update LPs for current player?')
                if update != '':
                    self.players[self.current_player].update_lp(int(update))
                update = input('Update LPs for other player?')
                if update != '':
                    self.players[(self.current_player + 1) % 2].update_lp(int(update))


            self.current_player = (self.current_player + 1) % 2
    
    def check_triggers(self, player_triggers, player_name):
        if len(player_triggers) > 0:
            print(f'{player_name} player has triggers on this phase: ')
            print(", ".join(player_triggers))
            input('ok?')

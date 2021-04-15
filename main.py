from player import Player
from game import Game

def main():
    print('Welcome to Yu-Gi-Oh Phaser')
    print()
    input('Press any key to start a duel')
    p1 = Player()
    p2 = Player()
    game = Game(p1,p2)
    game.start()
    print('GG WP')

main()
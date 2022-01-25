'''
Starting point of the BowlingAlley
'''
from Game import Game
if __name__ == "__main__":
    totalPlayers = int(input("Enter toltal number of players"))
    strike = 10
    spare = 5
    obj = Game(totalPlayers, strike, spare)
    score1 = obj.startPlaying()
    score1 = obj.startPlaying()


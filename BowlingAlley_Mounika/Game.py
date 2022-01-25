import operator

'''
BonusMethod:
1. Taking the input
if input is 'X' BonusMethod(chances-1)
else:
'''
class Game:
    '''
    Initializing values
    totalSet => Fixed to 10 sets
    totalPlayers => total number of players playing the game
    strike => bonus score for the strike
    spare => bonus score for the spare
    playersHavingStrikeOrSpare => Traking the players having strike/ spare
    scores => dictionary of player and his score
    '''
    def __init__(self, totalPlayers, strike, spare):
        self.totalSets = 2
        self.chancesForEachSet = 2
        self.totalPlayers = totalPlayers
        self.strike = strike
        self.spare = spare
        self.playersHavingStrikeOrSpare = []
        self.scores = {}

    # Initially scores will be zero
    def scoreInitialization(self):
        for i in range(self.totalPlayers):
            self.scores["player" + str(i)] = 0

    # Here calculating score for the each player with 3 chances
    def playForSinglePlayer(self, playerNum):
        playerScore = 0
        remBalls = 10
        for i in range(self.chancesForEachSet):
            score = input("Enter score for Player "+str(playerNum) + " : ")

            # If strike happens other than first attemt or spare happend other than 2 attemp
            if(i==0 and score == '/') or (i ==1 and score == 'x'):
                print("Invalid Input Please give other than " + score)
                score = input("Enter score for Player "+str(playerNum) + " : ") # taking correct input

            # If the it is a strike
            if(score == 'X' or score == 'x' and i == 0):
                if(playerNum not in self.playersHavingStrikeOrSpare):
                    self.playersHavingStrikeOrSpare.append(playerNum) #Storing this player to give bonus chance
                # if(i == 9 and score == 'X'):
                #     self.CallBonusMethod();
                return playerScore + self.strike + remBalls

            # If it is a spare
            elif(score == '/' and i == 1):
                if (playerNum not in self.playersHavingStrikeOrSpare):
                    self.playersHavingStrikeOrSpare.append(playerNum) #Storing this player to give bonus chance

                return playerScore + self.spare + remBalls

            # If it is spare/strike but not 2nd/1st attempt, consider this as normal score
            else:
                if(score == 'x' or score == '/' or score == 'X'):
                    score = remBalls
                playerScore += int(score)
                if(playerScore >10):
                    playerScore = 10
                    remBalls = 0
                else:
                    remBalls -= int(score)

            # If we have three chances and at 3rd chance we strike down all the 10 pins
            if(remBalls == 0):
                return playerScore

        return playerScore

    '''
    Calling each player in a set
    '''
    def playForSet(self):
        for i in range(self.totalPlayers):
            score = self.playForSinglePlayer(i)
            self.scores["player" + str(i)] += score
            self.ScoreBoard()

    '''
    Calling the players who are having bonuns set
    '''
    def playForBonusSet(self):
        for i in self.playersHavingStrikeOrSpare:
            print("Bonus set for the player" + str(i))
            score = self.playForSinglePlayer(i)
            self.scores["player" + str(i)] += score
            self.ScoreBoard()

    '''
    Printing the score board 
    '''
    def ScoreBoard(self):
        for i in range(self.totalPlayers):
            print("Player" + str(i) + " => " + str(self.scores["player" + str(i)]))

    '''
    Leader Board after completing all the set and bonus sets by all the players
    '''
    def printLeaderBoard(self):
        print("LeaderBoard")
        self.scores = dict( sorted(self.scores.items(), key=operator.itemgetter(1),reverse=True)) # Sort the dictionary based on scores in descending Order
        maxScore = 0
        for key in self.scores:
            print(key + " => " + str(self.scores[key]))
            if(self.scores[key] > maxScore):
                maxScore = self.scores[key]
        for key in self.scores:
            if(self.scores[key] == maxScore):
                print(key +" is the winner with " + str(self.scores[key]) + " score")
            else:
                break;

    ''' 
    Game is starting from here
    '''
    def startPlaying(self):
        self.scoreInitialization()
        for i in range(self.totalSets):
            print("Set :" + str(i+1))
            self.playForSet()
        self.playForBonusSet() # allowing players to play bonus set
        self.printLeaderBoard() # Displaying the leaderBoard
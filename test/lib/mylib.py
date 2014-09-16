#!/usr/bin/python
from random import randrange

# Constant variables
DIVIDOR 		= '========================================================'
HINTS_DIVIDOR 	= '++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
PLAYER_O 		= 1
PLAYER_X 		= 2
DRAW_GAME 		= 10
QUIT_GAME 		= 20
PLAYER_O_WIN	= PLAYER_O*3
PLAYER_X_WIN	= PLAYER_X*3

# The player class
class player:
	def __init__(self, player):
		self.player = player

	def getPlayer(self):
		return self.player

class human(player):
	def nextStep(self):
		player_input = -1
		while player_input == -1:
			value = raw_input('Input your next step (quit for stop game, h for hints): ')

			if value.lower() == 'q' :
				player_input = 0
			elif value.lower() == 'w' :
				player_input = 1
			elif value.lower() == 'e' :
				player_input = 2
			elif value.lower() == 'a' :
				player_input = 3
			elif value.lower() == 's' :
				player_input = 4
			elif value.lower() == 'd' :
				player_input = 5
			elif value.lower() == 'z' :
				player_input = 6
			elif value.lower() == 'x' :
				player_input = 7
			elif value.lower() == 'c' :
				player_input = 8
			elif value.lower() == 'quit':
				player_input = 10;
			elif value.lower() == 'h':
				player_input = 20;
			else:
				player_input = -1

		return player_input
		

class computer(player):
	def nextStep(self):
		self.step = randrange(9)
		print 'Computer input next step: %d' % self.step
		return int(self.step)

class tictactoe:
	def __init__(self):
		self.round 			= 0
		self.winner 		= 0
		self.playerA 		= human(PLAYER_O)
		self.playerB 		= computer(PLAYER_X)
		self.gameContinue 	= True
		self.list			= [int(9) for item in xrange(9)]

	def checkDrawGame(self):
		for item in self.list:
			if item == 9:
				return False
		return True

	def checkWinGame(self):
		if ((self.list[0]+self.list[1]+self.list[2]) == PLAYER_O_WIN):
			self.winner = PLAYER_O
			return True
		elif ((self.list[0]+self.list[1]+self.list[2]) == PLAYER_X_WIN):
			self.winner = PLAYER_X
			return True
		elif ((self.list[3]+self.list[4]+self.list[5]) == PLAYER_O_WIN):
			self.winner = PLAYER_O
			return True
		elif ((self.list[3]+self.list[4]+self.list[5]) == PLAYER_X_WIN):
			self.winner = PLAYER_X
			return True
		elif ((self.list[6]+self.list[7]+self.list[8]) == PLAYER_O_WIN):
			self.winner = PLAYER_O
			return True
		elif ((self.list[6]+self.list[7]+self.list[8]) == PLAYER_X_WIN):
			self.winner = PLAYER_X
			return True
		elif ((self.list[0]+self.list[3]+self.list[6]) == PLAYER_O_WIN):
			self.winner = PLAYER_O
			return True
		elif ((self.list[0]+self.list[3]+self.list[6]) == PLAYER_X_WIN):
			self.winner = PLAYER_X
			return True
		elif ((self.list[1]+self.list[4]+self.list[7]) == PLAYER_O_WIN):
			self.winner = PLAYER_O
			return True
		elif ((self.list[1]+self.list[4]+self.list[7]) == PLAYER_X_WIN):
			self.winner = PLAYER_X
			return True
		elif ((self.list[2]+self.list[5]+self.list[8]) == PLAYER_O_WIN):
			self.winner = PLAYER_O
			return True
		elif ((self.list[2]+self.list[5]+self.list[8]) == PLAYER_X_WIN):
			self.winner = PLAYER_X
			return True
		elif ((self.list[0]+self.list[4]+self.list[8]) == PLAYER_O_WIN):
			self.winner = PLAYER_O
			return True
		elif ((self.list[0]+self.list[4]+self.list[8]) == PLAYER_X_WIN):
			self.winner = PLAYER_X
			return True
		elif ((self.list[2]+self.list[4]+self.list[6]) == PLAYER_O_WIN):
			self.winner = PLAYER_O
			return True
		elif ((self.list[2]+self.list[4]+self.list[6]) == PLAYER_X_WIN):
			self.winner = PLAYER_X
			return True
		elif self.checkDrawGame():
			self.winner = DRAW_GAME
			return True
		else:
			return False


	def getRound(self):
		return self.round

	def update(self):
		while self.checkWinGame() == False:
			self.printGameBoard()
			step = -1
			while step == -1:
				step = self.playerB.nextStep() if self.round % 2 == 0 else self.playerA.nextStep()
				if step == 10:
					break
				if step == 20:
					self.printGameBoardHints()
					step = -1
				if self.list[step] != 9:
					print 'Position %d is already input' % int(step+1)
					step = -1
				pass
			if (step == 10):
				self.winner = QUIT_GAME
				break
			self.list[step] = self.playerB.getPlayer() if self.round % 2 == 0 else self.playerA.getPlayer()
		if self.winner != QUIT_GAME:
			self.printGameBoard()
			self.printWinnerInfo()
		else:
			print 'Game Over!'


	def printGamePlayer(self, item):
		if item == PLAYER_O:
			return 'O'
		elif item == PLAYER_X:
			return 'X'
		else:
			return ' '
		
	def printGameBoard(self):
		self.round+=1
		if self.round == 1:
			self.printHeaderInfo()
		print 'Round %d' % (self.round)
		# print '\t',
		# print ('\n\t-----------\n\t'.join(['|'.join([' {:1} '.format(self.printGamePlayer(item)) for item in row]) for row in self.list]))
		print '\t %s | %s | %s ' % (self.printGamePlayer(self.list[0]), self.printGamePlayer(self.list[1]), self.printGamePlayer(self.list[2]))
		print '\t-----------'
		print '\t %s | %s | %s ' % (self.printGamePlayer(self.list[3]), self.printGamePlayer(self.list[4]), self.printGamePlayer(self.list[5]))
		print '\t-----------'
		print '\t %s | %s | %s ' % (self.printGamePlayer(self.list[6]), self.printGamePlayer(self.list[7]), self.printGamePlayer(self.list[8]))

	def printGameBoardHints(self):
		print HINTS_DIVIDOR
		print 'Input the corresponding key to choose your step:'
		print 
		print '\t q | w | e '
		print '\t-----------'
		print '\t a | s | d '
		print '\t-----------'
		print '\t z | x | c '
		print
		print HINTS_DIVIDOR

	def printHeaderInfo(self):
		print DIVIDOR
		print 'Tic Tac Toe'
		print 'human: %s, computer: %s\n' % (self.playerA.getPlayer(), self.playerB.getPlayer())
		print DIVIDOR
		print 'Game Start:'

	def printWinnerInfo(self):
		if self.winner == DRAW_GAME:
			print DIVIDOR
			print 'Draw Game!'
			print DIVIDOR
		else:
			winner = 'O' if self.winner == PLAYER_O else 'X'
			print DIVIDOR
			print 'Congratulations!'
			print 'The Winner is %s' % winner
			print DIVIDOR

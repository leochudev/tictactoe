#!/usr/bin/python
from random import randrange
from player import gameplayer

# Constant variables
DIVIDOR 		= '========================================================'
HINTS_DIVIDOR 	= '++++++++++++++++++++++++++++++++++++++++++++++++++++++++'

class gameinfo:
	def printHeaderInfo(self, playerA, playerB):
		print DIVIDOR
		print 'Tic Tac Toe'
		print 'human: %s, computer: %s\n' % (self.printGamePlayer(playerA.getPlayer()), self.printGamePlayer(playerB.getPlayer()))
		print DIVIDOR
		print 'Game Start:'

	def printGamePlayer(self, item):
		if item == gameplayer.PLAYER_O:
			return 'O'
		elif item == gameplayer.PLAYER_X:
			return 'X'
		else:
			return ' '

	def printWinnerInfo(self, winner):
		if winner == gamelogic.DRAW_GAME:
			print DIVIDOR
			print 'Draw Game!'
			print DIVIDOR
		else:
			winner = 'O' if winner == gameplayer.PLAYER_O else 'X'
			print DIVIDOR
			print 'Congratulations!'
			print 'The Winner is %s' % winner
			print DIVIDOR

class gamelogic:
	# Game State
	CONT_GAME 		= 10
	DRAW_GAME 		= 20
	QUIT_GAME 		= 30

	PLAYER_O_WIN	= gameplayer.PLAYER_O*3
	PLAYER_X_WIN	= gameplayer.PLAYER_X*3
	
	def checkDrawGame(self, board):
		return True if sum(board)%10 == 9 else False
		
	def checkWinGame(self, board):
		if ((board[0]+board[1]+board[2]) == self.PLAYER_O_WIN):
			return gameplayer.PLAYER_O
		elif ((board[0]+board[1]+board[2]) == self.PLAYER_X_WIN):
			return gameplayer.PLAYER_X
		elif ((board[3]+board[4]+board[5]) == self.PLAYER_O_WIN):
			return gameplayer.PLAYER_O
		elif ((board[3]+board[4]+board[5]) == self.PLAYER_X_WIN):
			return gameplayer.PLAYER_X
		elif ((board[6]+board[7]+board[8]) == self.PLAYER_O_WIN):
			return gameplayer.PLAYER_O
		elif ((board[6]+board[7]+board[8]) == self.PLAYER_X_WIN):
			return gameplayer.PLAYER_X
		elif ((board[0]+board[3]+board[6]) == self.PLAYER_O_WIN):
			return gameplayer.PLAYER_O
		elif ((board[0]+board[3]+board[6]) == self.PLAYER_X_WIN):
			return gameplayer.PLAYER_X
		elif ((board[1]+board[4]+board[7]) == self.PLAYER_O_WIN):
			return gameplayer.PLAYER_O
		elif ((board[1]+board[4]+board[7]) == self.PLAYER_X_WIN):
			return gameplayer.PLAYER_X
		elif ((board[2]+board[5]+board[8]) == self.PLAYER_O_WIN):
			return gameplayer.PLAYER_O
		elif ((board[2]+board[5]+board[8]) == self.PLAYER_X_WIN):
			return gameplayer.PLAYER_X
		elif ((board[0]+board[4]+board[8]) == self.PLAYER_O_WIN):
			return gameplayer.PLAYER_O
		elif ((board[0]+board[4]+board[8]) == self.PLAYER_X_WIN):
			return gameplayer.PLAYER_X
		elif ((board[2]+board[4]+board[6]) == self.PLAYER_O_WIN):
			return gameplayer.PLAYER_O
		elif ((board[2]+board[4]+board[6]) == self.PLAYER_X_WIN):
			return gameplayer.PLAYER_X
		elif self.checkDrawGame(board):
			return self.DRAW_GAME
		else:
			return self.CONT_GAME

class gameboard(gameinfo):
	def __init__(self):
		self.list = [int(gameplayer.BLANK) for i in xrange(9)]
	
	def checkAvailable(self, step):
		return True if self.list[step] == gameplayer.BLANK else False

	def getGameBoard(self):
		return self.list

	def printGameBoard(self, playerA, playerB):
		self.round+=1
		if self.round == 1:
			self.printHeaderInfo(playerA, playerB)
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

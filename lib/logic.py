#!/usr/bin/python
from random import randrange

class gamelogic:
	BLANK			= 10
	PLAYER_O 		= 11
	PLAYER_X 		= 21

	# Game State
	CONT_GAME 		= 10
	DRAW_GAME 		= 20
	QUIT_GAME 		= 30

	PLAYER_O_WIN	= PLAYER_O*3
	PLAYER_X_WIN	= PLAYER_X*3
	
	def checkDrawGame(self, board):
		return True if sum(board)%10 == 9 else False
		
	def checkWinGame(self, board):
		if ((board[0]+board[1]+board[2]) == self.PLAYER_O_WIN):
			return self.PLAYER_O
		elif ((board[0]+board[1]+board[2]) == self.PLAYER_X_WIN):
			return self.PLAYER_X
		elif ((board[3]+board[4]+board[5]) == self.PLAYER_O_WIN):
			return self.PLAYER_O
		elif ((board[3]+board[4]+board[5]) == self.PLAYER_X_WIN):
			return self.PLAYER_X
		elif ((board[6]+board[7]+board[8]) == self.PLAYER_O_WIN):
			return self.PLAYER_O
		elif ((board[6]+board[7]+board[8]) == self.PLAYER_X_WIN):
			return self.PLAYER_X
		elif ((board[0]+board[3]+board[6]) == self.PLAYER_O_WIN):
			return self.PLAYER_O
		elif ((board[0]+board[3]+board[6]) == self.PLAYER_X_WIN):
			return self.PLAYER_X
		elif ((board[1]+board[4]+board[7]) == self.PLAYER_O_WIN):
			return self.PLAYER_O
		elif ((board[1]+board[4]+board[7]) == self.PLAYER_X_WIN):
			return self.PLAYER_X
		elif ((board[2]+board[5]+board[8]) == self.PLAYER_O_WIN):
			return self.PLAYER_O
		elif ((board[2]+board[5]+board[8]) == self.PLAYER_X_WIN):
			return self.PLAYER_X
		elif ((board[0]+board[4]+board[8]) == self.PLAYER_O_WIN):
			return self.PLAYER_O
		elif ((board[0]+board[4]+board[8]) == self.PLAYER_X_WIN):
			return self.PLAYER_X
		elif ((board[2]+board[4]+board[6]) == self.PLAYER_O_WIN):
			return self.PLAYER_O
		elif ((board[2]+board[4]+board[6]) == self.PLAYER_X_WIN):
			return self.PLAYER_X
		elif self.checkDrawGame(board):
			return self.DRAW_GAME
		else:
			return self.CONT_GAME

class gameinfo(gamelogic):
	DIVIDOR 		= '========================================================'
	HINTS_DIVIDOR 	= '++++++++++++++++++++++++++++++++++++++++++++++++++++++++'

	def printHeaderInfo(self, playerA, playerB):
		print self.DIVIDOR
		print 'Tic Tac Toe'
		print 'human: %s, computer: %s\n' % (self.printGamePlayer(playerA.getPlayer()), self.printGamePlayer(playerB.getPlayer()))
		print self.DIVIDOR
		print 'Game Start:'

	def printGamePlayer(self, item):
		if item == gamelogic.PLAYER_O:
			return 'O'
		elif item == gamelogic.PLAYER_X:
			return 'X'
		else:
			return ' '

	def printWinnerInfo(self, winner):
		if winner == gamelogic.DRAW_GAME:
			print self.DIVIDOR
			print 'Draw Game!'
			print self.DIVIDOR
		else:
			winner = 'O' if winner == gamelogic.PLAYER_O else 'X'
			print self.DIVIDOR
			print 'Congratulations!'
			print 'The Winner is %s' % winner
			print self.DIVIDOR

class gameboard(gameinfo):
	def __init__(self):
		self.list = [int(gamelogic.BLANK) for i in xrange(9)]
	
	def checkAvailable(self, step):
		return True if self.list[step] == gamelogic.BLANK else False

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
		print gameinfo.HINTS_DIVIDOR
		print 'Input the corresponding key to choose your step:'
		print 
		print '\t q | w | e '
		print '\t-----------'
		print '\t a | s | d '
		print '\t-----------'
		print '\t z | x | c '
		print
		print gameinfo.HINTS_DIVIDOR

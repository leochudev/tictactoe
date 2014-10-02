#!/usr/bin/python
from random import randrange

# Constant variables
DIVIDOR 		= '========================================================'
HINTS_DIVIDOR 	= '++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
BLANK			= 10
PLAYER_O 		= 11
PLAYER_X 		= 21
CONT_GAME 		= 10
DRAW_GAME 		= 20
QUIT_GAME 		= 30
SHOW_HINT		= 40
EXCEPTION		= -1
PLAYER_O_WIN	= PLAYER_O*3
PLAYER_X_WIN	= PLAYER_X*3

class gameinfo:
	def printHeaderInfo(self, playerA, playerB):
		print DIVIDOR
		print 'Tic Tac Toe'
		print 'human: %s, computer: %s\n' % (self.printGamePlayer(playerA.getPlayer()), self.printGamePlayer(playerB.getPlayer()))
		print DIVIDOR
		print 'Game Start:'

	def printGamePlayer(self, item):
		if item == PLAYER_O:
			return 'O'
		elif item == PLAYER_X:
			return 'X'
		else:
			return ' '

	def printWinnerInfo(self, winner):
		if winner == DRAW_GAME:
			print DIVIDOR
			print 'Draw Game!'
			print DIVIDOR
		else:
			winner = 'O' if winner == PLAYER_O else 'X'
			print DIVIDOR
			print 'Congratulations!'
			print 'The Winner is %s' % winner
			print DIVIDOR

class gamelogic:
	def checkDrawGame(self, board):
		return True if sum(board)%10 == 9 else False
		
	def checkWinGame(self, board):
		if ((board[0]+board[1]+board[2]) == PLAYER_O_WIN):
			return PLAYER_O
		elif ((board[0]+board[1]+board[2]) == PLAYER_X_WIN):
			return PLAYER_X
		elif ((board[3]+board[4]+board[5]) == PLAYER_O_WIN):
			return PLAYER_O
		elif ((board[3]+board[4]+board[5]) == PLAYER_X_WIN):
			return PLAYER_X
		elif ((board[6]+board[7]+board[8]) == PLAYER_O_WIN):
			return PLAYER_O
		elif ((board[6]+board[7]+board[8]) == PLAYER_X_WIN):
			return PLAYER_X
		elif ((board[0]+board[3]+board[6]) == PLAYER_O_WIN):
			return PLAYER_O
		elif ((board[0]+board[3]+board[6]) == PLAYER_X_WIN):
			return PLAYER_X
		elif ((board[1]+board[4]+board[7]) == PLAYER_O_WIN):
			return PLAYER_O
		elif ((board[1]+board[4]+board[7]) == PLAYER_X_WIN):
			return PLAYER_X
		elif ((board[2]+board[5]+board[8]) == PLAYER_O_WIN):
			return PLAYER_O
		elif ((board[2]+board[5]+board[8]) == PLAYER_X_WIN):
			return PLAYER_X
		elif ((board[0]+board[4]+board[8]) == PLAYER_O_WIN):
			return PLAYER_O
		elif ((board[0]+board[4]+board[8]) == PLAYER_X_WIN):
			return PLAYER_X
		elif ((board[2]+board[4]+board[6]) == PLAYER_O_WIN):
			return PLAYER_O
		elif ((board[2]+board[4]+board[6]) == PLAYER_X_WIN):
			return PLAYER_X
		elif self.checkDrawGame(board):
			return DRAW_GAME
		else:
			return CONT_GAME

class gameboard(gameinfo):
	def __init__(self):
		self.list = [int(BLANK) for i in xrange(9)]
	
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

# The player class
class player:
	def __init__(self, player):
		self.player 	= player
		self.oppnent 	= PLAYER_O if self.player == PLAYER_O else PLAYER_X
		self.choice		= 0

	def getPlayer(self):
		return self.player

	def getOpponent(self):
		return self.oppnent

class human(player):
	def nextStep(self, board):
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
				player_input = QUIT_GAME;
			elif value.lower() == 'h':
				player_input = SHOW_HINT;
			else:
				player_input = EXCEPTION

		return player_input
		

class computer(player, gamelogic):
	def nextStep(self, board):
		temp_board = list(board)
		step = self.minimax(temp_board, 0)

		print 'Computer input next step: %d' % self.choice
		return int(self.choice)

	def unitScore(self, winner, depth):
		print winner

		if winner == DRAW_GAME:
			return 0
		else:
			return 10-depth if winner == self.player else depth-10

	def getAvailableStep(self, board):
		steps = []
		for i in xrange(9):
			if board[i] == BLANK:
				steps.append(i)
		return steps

	def getNewState(self, board, depth, step):
		tmp_board = list(board)
		tmp_board[step] = self.player if depth%2==1 else self.oppnent
		return tmp_board

	def minimax(self, board, depth):
		result = self.checkWinGame(board)
		if result != CONT_GAME:
			# print 'unitScore: %d' % self.unitScore(result, depth)
			return self.unitScore(result, depth)
		depth += 1
		scores = []
		steps  = []

		# print 'depth: %d' % depth
		# print 'be4 scores: ',
		# print ''.join(str(scores))

		for step in self.getAvailableStep(board):
			score = self.minimax(self.getNewState(board, depth, step), depth)
			# print 'score: %d' % score
			scores.append(score)
			steps.append(step)

		# print 'scores: ',
		# print ''.join(str(scores))
		# print 'steps: ',
		# print ''.join(str(steps))
		# print 'size of scores: %d, steps: %d' % (len(scores), len(steps))

		if depth%2 == 1:
			max_value_pos = scores.index(max(scores))
			self.choice = steps[max_value_pos]
			return max(scores)
		else:
			min_value_pos = scores.index(min(scores))
			self.choice = steps[min_value_pos]
			return min(scores)


class tictactoe(gamelogic, gameboard):
	def __init__(self):
		gameboard.__init__(self)
		self.round 			= 0
		self.winner 		= CONT_GAME
		self.playerA 		= human(PLAYER_O)
		self.playerB 		= computer(PLAYER_X)
		
	def update(self):
		while self.winner == CONT_GAME:
			self.printGameBoard(self.playerA, self.playerB)
			step = EXCEPTION
			while step == EXCEPTION:
				step = self.playerB.nextStep(self.list) if self.round % 2 == 0 else self.playerA.nextStep(self.list)
				if step == QUIT_GAME:
					break
				if step == SHOW_HINT:
					self.printGameBoardHints()
					step = EXCEPTION
				if self.list[step] != BLANK:
					print 'Position %d is already input' % int(step+1)
					step = EXCEPTION
				pass
			if (step == QUIT_GAME):
				self.winner = QUIT_GAME
				break
			self.list[step] = self.playerB.getPlayer() if self.round % 2 == 0 else self.playerA.getPlayer()
			self.winner = self.checkWinGame(self.list)
			pass
		if self.winner != QUIT_GAME:
			self.printGameBoard(self.playerA, self.playerB)
			self.printWinnerInfo(self.winner)
		else:
			print 'Game Over!'

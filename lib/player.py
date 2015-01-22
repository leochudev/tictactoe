#!/usr/bin/python
from logic import gamelogic
from logic import gameboard

# The player class
class gameplayer(gamelogic):
	# user input
	SHOW_HINT		= 40
	EXCEPTION		= -1

	def __init__(self, player):
		self.player 	= player
		self.oppnent 	= gamelogic.PLAYER_O if self.player != gamelogic.PLAYER_O else gamelogic.PLAYER_X
		self.choice		= 0
		
	def getPlayer(self):
		return self.player

	def getOpponent(self):
		return self.oppnent

class human(gameplayer):
	def __init__(self, player):
		gameplayer.__init__(self, player)

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
				player_input = gamelogic.QUIT_GAME
			elif value.lower() == 'h':
				player_input = self.SHOW_HINT
			else:
				player_input = self.EXCEPTION

		return player_input
		

class computer(gameplayer, gamelogic, gameboard):
	def __init__(self, player):
		gameplayer.__init__(self, player)
		self.level = 0

	def nextStep(self, board):
		temp_board = list(board)
		step = self.minimax(temp_board, 0)

		print 'Computer input next step: %d' % self.choice
		return int(self.choice)

	def unitScore(self, winner, depth):
		if winner == gamelogic.DRAW_GAME:
			return 0
		else:
			return 10-depth if winner == self.player else depth-10

	def getAvailableStep(self, board):
		steps = []
		for i in xrange(9):
			if board[i] == self.BLANK:
				steps.append(i)
		return steps

	def getNewState(self, board, depth, step):
		tmp_board = list(board)
		tmp_board[step] = self.player if depth%2==1 else self.oppnent
		
		return tmp_board

	def minimax(self, board, depth):
		result = self.checkWinGame(board)
		if result != gamelogic.CONT_GAME:
			return self.unitScore(result, depth)
		depth += 1
		scores = []
		steps  = []

		for step in self.getAvailableStep(board):
			score = self.minimax(self.getNewState(board, depth, step), depth)
			scores.append(score)
			steps.append(step)

		if depth%2 == 1:
			max_value_pos = scores.index(max(scores))
			self.choice = steps[max_value_pos]
			return max(scores)
		else:
			min_value_pos = scores.index(min(scores))
			self.choice = steps[min_value_pos]
			return min(scores)
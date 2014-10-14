#!/usr/bin/python
from player import gamelogic
from player import gameboard

from player import human
from player import computer


# value in the game board
BLANK			= 10
PLAYER_O 		= 11
PLAYER_X 		= 21

class tictactoe(gamelogic, gameboard):
	def __init__(self):
		gameboard.__init__(self)
		self.round 			= 0
		self.state 			= gamelogic.CONT_GAME
		self.playerA 		= human(PLAYER_O)
		self.playerB 		= computer(PLAYER_X)
		
	def update(self):
		while self.state == gamelogic.CONT_GAME:
			self.printGameBoard(self.playerA, self.playerB)
			step = human.EXCEPTION
			while step == human.EXCEPTION:
				step = self.playerB.nextStep(self.list) if self.round % 2 == 0 else self.playerA.nextStep(self.list)
				if step == gamelogic.QUIT_GAME:
					break
				if step == human.SHOW_HINT:
					self.printGameBoardHints()
					step = human.EXCEPTION
				if self.checkAvailable(step) == False:
					print 'Position %d is already input' % int(step+1)
					step = human.EXCEPTION
				pass
			if (step == gamelogic.QUIT_GAME):
				self.state = gamelogic.QUIT_GAME
				break
			self.list[step] = self.playerB.getPlayer() if self.round % 2 == 0 else self.playerA.getPlayer()
			self.state = self.checkWinGame(self.list)
			pass
		if self.state != gamelogic.QUIT_GAME:
			self.printGameBoard(self.playerA, self.playerB)
			self.printWinnerInfo(self.state)
		else:
			print 'Game Over!'
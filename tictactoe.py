#!/usr/bin/python3

from operator import itemgetter 
import random

def clear_screen():
	print(chr(27) + "[2J")

def choose_a_letter():
	print("\nWelcome To Tic-Tac-Toe!\n")
	choice = ''
	while not (choice == 'X' or choice == 'O'):
		choice = input("Please Choose X or O: \n").upper()
	if choice == "X":
		return ['X', 'O']
	else:
		return ['O', 'X']

def draw_board(board):
	print("     |     |")
	print("  {}  |  {}  |  {}".format(board[1], board[2], board[3]))
	print("     |     |")
	print("-----------------")
	print("     |     |")
	print("  {}  |  {}  |  {}".format(board[4], board[5], board[6]))
	print("     |     |")
	print("-----------------")
	print("     |     |")
	print("  {}  |  {}  |  {}".format(board[7], board[8], board[9]))
	print("     |     |")

def explain_board():
	print("\nWhen making moves, you will enter the follling numbers to select a box\n")
	print("     |     |")
	print("  1  |  2  |  3")
	print("     |     |")
	print("-----------------")
	print("     |     |")
	print("  4  |  5  |  6")
	print("     |     |")
	print("-----------------")
	print("     |     |")
	print("  7  |  8  |  9")
	print("     |     |")
	input("\nPress Enter to continue...")

def who_goes_first():
	random_num = random.randint(0, 1)
	if random_num == 0:
		return "Player"
	else:
		return "Computer"

def player_go(open_moves, board):
	clear_screen()
	draw_board(board)
	choice = ""
	while choice not in open_moves:
		choice = input("Please choose a square: ")
		try:
			int(choice)
		except ValueError:
			print("You didn't enter an integer")
		else:
			choice = int(choice)
	return choice

def computer_go(open_moves):
	choice = random.choice(open_moves)
	return choice

def check_if_winner(board):
	# horizontal
	if board[1:4] == ['X', 'X', 'X'] or board[1:4] == ['O', 'O', 'O']:
		return True
	elif board[4:7] == ['X', 'X', 'X'] or board[4:7] == ['O', 'O', 'O']:
		return True
	elif board[7:] == ['X', 'X', 'X'] or board[7:] == ['O', 'O', 'O']:
		return True
	# veritcal
	elif list(itemgetter(*[1,4,7])(board)) == ['X', 'X', 'X'] or list(itemgetter(*[1,4,7])(board)) == ['O', 'O', 'O']:
		return True
	elif list(itemgetter(*[2,5,8])(board)) == ['X', 'X', 'X'] or list(itemgetter(*[2,5,8])(board)) == ['O', 'O', 'O']:
		return True
	elif list(itemgetter(*[3,6,9])(board)) == ['X', 'X', 'X'] or list(itemgetter(*[3,6,9])(board)) == ['O', 'O', 'O']:
		return True
	# diagonal
	elif list(itemgetter(*[1,5,9])(board)) == ['X', 'X', 'X'] or list(itemgetter(*[1,5,9])(board)) == ['O', 'O', 'O']:
		return True
	elif list(itemgetter(*[3,5,7])(board)) == ['X', 'X', 'X'] or list(itemgetter(*[3,5,7])(board)) == ['O', 'O', 'O']:
		return True
	else:
		return False

while True:
	open_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	board = [' '] * 10
	clear_screen()
	player_letter, computer_letter = choose_a_letter()
	clear_screen()
	explain_board()
	clear_screen()
	turn = who_goes_first()
	game = True
	while game:
		if (turn == 'Player' or turn == 'Computer') and open_moves == []:
			print("\nCat Game! Please try again!\n")
			game = False
		elif turn == 'Player' and open_moves != []: # Player's turn
			player_choice = player_go(open_moves, board)
			open_moves.remove(player_choice)
			board[player_choice] = player_letter
			if check_if_winner(board):
				print("\nYou won the game! Congratulations!\n")
				break
			turn = 'Computer' # This is ending the Player's turn
		else: # Computer's Turn
			computer_choice = computer_go(open_moves)
			print("Computer moved and selected " + str(computer_choice))
			open_moves.remove(computer_choice)
			board[computer_choice] = computer_letter
			draw_board(board)
			if check_if_winner(board):
				print("\nYou have lost the game! Better luck next time!\n")
				break
			turn = 'Player' # This is ending the Computer's turn
	break

import gnubg

board = gnubg.board_from_position_id("4HPwATDgc/ABMA")

keystring = "4HPhQUAzTvABMA:MAEAAAAAAAAE"
board = gnubg.board_from_position_id(keystring)

print(board)

moves = gnubg.best_move(pos=board, dice1=3, dice2=5, n=2, s=b"O", b=False, r=False, list=True, reduced=False) 
print(moves) 

legal_moves = gnubg.moves(board, 3, 5, True)

gnubg.probabilities(board, gnubg.p_prune)

win, wing, winbg, loseg, losebg = gnubg.probabilities(board, 0)
lose = 1 - win 
equity = win + wing + winbg - lose - loseg - losebg

print(f"Win:        {win:>6.3f}\n"
      f"Win gammon: {wing:>6.3f}\n"
      f"Win bg:     {winbg:>6.3f}\n"
      f"Lose:       {lose:>6.3f}\n"
      f"Lose gammon:{loseg:>6.3f}\n"
      f"Lose bg:    {losebg:>6.3f}\n"
      f"Equity:     {equity:>6.3f}")

gnubg.key_of_board(board)

ro = gnubg.cubeful_rollout(pos = gnubg.key_of_board(board))

print(ro)
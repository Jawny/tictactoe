import copy
import tictactoe

# Sample Board
board = ["O",'-',"X",
        "X",'O' ,"X", 
        '-',"O","-"]

huPlayer = 'O'
aiPlayer = 'X'

# Nathan's personal game state monitor cuz Johnny's suck ass
# jk i had trouble trying to use yours lmao
def winning(board, player):
  if board[0] == player and board[1] == player and board[2] == player or board[3] == player and board[4] == player and board[5] == player or board[6] == player and board[7] == player and board[8] == player or board[0] == player and board[3] == player and board[6] == player or board[1] == player and board[4] == player and board[7] == player or board[2] == player and board[5] == player and board[8] == player or board[0] == player and board[4] == player and board[8] == player or board[2] == player and board[4] == player and board[6] == player:
    return 'true'
  else:
    return 'false'

def getAvailableSpots(board):
  availSpots = []
  for i in range(len(board)):
    if board[i] == "-":
      availSpots.append(i)
  return availSpots

def minimax(newBoard, player):

  # Available spots
  availSpots = getAvailableSpots(newBoard)

  # Check for game end
  # TODO: check if huPlayer or aiPlayer wins
  if winning(newBoard, huPlayer) == 'true': return {'score': -10}
  elif winning(newBoard, aiPlayer) == 'true': return {'score': 10}
  elif len(availSpots) == 0: return {'score': 0}

  # Array to collect all the goodies
  moves = []

  # Loop through available spots
  for i in range(len(availSpots)):
    move = {}
    move['index'] = availSpots[i]

    # Set empty spot to current player
    newBoard[availSpots[i]] = player

    if player == aiPlayer:
      result = minimax(newBoard, huPlayer)
      move['score'] = result['score']
    else:
      result = minimax(newBoard, aiPlayer)
      move['score'] = result['score']
    
    # Reset spot to empty
    newBoard[availSpots[i]] = '-'

    # Push the object to the array
    moves.append(move)
    print(moves)


  if player == aiPlayer:
    bestScore = -10000
    for i in range(len(moves)):
      if moves[i]['score'] > bestScore:
        bestScore = moves[i]['score']
        bestMove = i
  else: 
    bestScore = 10000
    for i in range(len(moves)):
      if moves[i]['score'] < bestScore:
        bestScore = moves[i]['score']
        bestMove = i

  return moves[bestMove]

bestSpot = minimax(board, aiPlayer)
print('best spot:', bestSpot)
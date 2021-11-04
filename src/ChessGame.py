import chess

class ChessGame(object):
    def __init__(self):
        self.board = chess.Board()
        self.whiteID = 0
        self.blackID = 0


    def __init__(self,board, whiteID, blackID):
        self.board = board
        self.whiteID = whiteID
        self.blackID = blackID
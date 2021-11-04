import chess

from ChessGame import ChessGame

class ChessBot():
    def __init__(self):
        self.chessGames = {}  # gameID to index and object of ChessGame(chess.Board(), whiteID, blackID)
        self.playingUsers = {}  # userID to index gameIDs

    def challenge(self, user1ID, user2ID):
        board = chess.Board()
        self.chessGames[id(board)] = ChessGame(board, user2ID, user1ID)
        self.playingUsers[user2ID] = id(board)  #players point to the game they are playing in #WHITE
        self.playingUsers[user1ID] = id(board)    #BLACK

    def matchup(self, user1, user2):
        if (user1.id not in self.playingUsers) and (user2.id not in self.playingUsers): #if neither of them are playing
            self.challenge(user1.id, user2.id)
            return self.representation(user1.id)


    def listLegalMoves(self, userID):
        if userID in self.playingUsers:
            return str(self.chessGames[self.playingUsers[userID]].board.legal_moves)[37:-1]
        else:
            return "You must be in a game to ask for legal moves"


    def movePush(self, game, algebraicMove):
        try:
            game.board.push(game.board.parse_san(algebraicMove))
            return ""
        except ValueError as moveError:
            return "Invalid or illegal move, for legal moves: !legal. The bot expects valid algebraic notation to be used in moves, for example: Nh6, Nh3, h6"


    def move(self, userID, algebraicMove):
        if userID in self.playingUsers:
            game = self.chessGames[self.playingUsers[userID]]
        else:
            return 'Not in an active game.'

        if (game.board.turn == chess.WHITE):
            if (userID == game.whiteID):
                return self.movePush(game, algebraicMove)
            else:
                return "Not your turn."
        else:
            if (userID == game.blackID):
                return self.movePush(game, algebraicMove)
            else:
                return "Not your turn."

    def representation(self, userID): #TODO REPLACE IT WITH A GENERATED IMAGE
        game = self.chessGames[self.playingUsers[userID]]
        boardRepresentation = "`" + str(game.board) + "`"

        return boardRepresentation

    def internalCleaner(self, game):
        try:
            self.chessGames.pop(self.playingUsers[game.whiteID])
            self.chessGames.pop(self.playingUsers[game.blackID])
        except KeyError as error:
            print("Cleanup going well.")
        self.playingUsers.pop(game.whiteID)
        self.playingUsers.pop(game.blackID)
        del game

    def overCleanup(self, userID): #cleans up the game once it's over
        game = self.chessGames[self.playingUsers[userID]]
        if game.board.is_game_over():
            result = "\nGame over" + game.board.result()
            self.internalCleaner(game)
            return result
        return ''

    def resign(self, user):
        if user.id not in self.playingUsers:
            return "You cannot resign if you are not in a match"
        else:
            game = self.chessGames[self.playingUsers[user.id]]
            self.internalCleaner(game)
            return str(user) + " has fortfeited their game, shame."
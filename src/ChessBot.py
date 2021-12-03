import chess
import chess.svg
import imgkit

from ChessGame import ChessGame
import dbman



class ChessBot():
    def __init__(self):
        self.chessGames = {}  # gameID to index and object of ChessGame(chess.Board(), whiteID, blackID)
        self.playingUsers = {}  # userID to index gameIDs

    def challenge(self, user1ID, user2ID):
        board = chess.Board()
        self.chessGames[id(board)] = ChessGame(board, user2ID, user1ID)
        self.playingUsers[user2ID] = id(board)  # players point to the game they are playing in #WHITE
        self.playingUsers[user1ID] = id(board)  # BLACK

    def matchup(self, user1, user2):
        if (user1.id not in self.playingUsers) and (
                user2.id not in self.playingUsers):  # if neither of them are playing
            self.challenge(user1.id, user2.id)
            return self.representation(user1.id)
        else:
            return "One of the users is already in a game."

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

    def representation(self, userID):
        game = self.chessGames[self.playingUsers[userID]]
        boardRepresentation = str(userID) + ".png"
        imgkit.from_string(chess.svg.board(game.board,size=600),boardRepresentation,
            options={
                'width' : 605,
                'height' : 615
            })

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

    def overCleanup(self, userID):  # cleans up the game once it's over
        game = self.chessGames[self.playingUsers[userID]]
        if game.board.is_stalemate():
            result = "\nGame over, stalemate."
            dbman.database_handler(game.whiteID, "Chess", 2)
            dbman.dBase.database_handler(game.blackID, "Chess", 2)
            self.internalCleaner(game)
            return result

        elif game.board.is_game_over():
            result = "\nGame over" + game.board.result()

            dbman.database_handler(userID, "Chess", 1)

            if (game.whiteID == userID):
                dbman.database_handler(game.blackID, "Chess", 0)
            else:
                dbman.database_handler(game.whiteID, "Chess", 0)
            self.internalCleaner(game)
            return result
        return ''

    def resign(self, user):
        if user.id not in self.playingUsers:
            return "You cannot resign if you are not in a match"
        else:
            game = self.chessGames[self.playingUsers[user.id]]
            self.internalCleaner(game)
            dbman.database_handler(user.id, "Chess", 0)
            if (game.whiteID == user.id):
                dbman.database_handler(game.blackID, "Chess", 1)
            else:
                dbman.database_handler(game.whiteID, "Chess", 1)
            return str(user) + " has fortfeited their game, shame."

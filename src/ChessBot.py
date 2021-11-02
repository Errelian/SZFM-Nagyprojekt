import chess
import random

class ChessBot():
    def __init__(self):
        self.chessGames = {}  # {gameID->(board,white,black)} where board is a chess.Board(), and white and black are userIDs
        self.playingUsers = {}  # {userID->gameID}, represents active players. Used to prevent users being in multiple games, and to interpret commands
        self.user_names = {}  # {userID->userName}Maintains dictionary of userids and usernames
        self.match_queue = []

    def createMatch(self) -> bool: #TODO MAKE IT SO YOU CAN JUST CHALLENGE SOMEONE
        if len(self.match_queue) >= 2:
            board = chess.Board()
            if random.randint(0, 1):
                white = self.match_queue.pop(0)
                black = self.match_queue.pop(0)
            else:
                black = self.match_queue.pop(0)
                white = self.match_queue.pop(0)
            self.chessGames[id(board)] = (board, white, black)
            self.playingUsers[white] = id(board)  # each player points to the gameID they're playing on
            self.playingUsers[black] = id(board)
            return True
        else:
            return False

    # returns true if a game starts, else false
    def queue(self, userID, userName) -> str:
        if userID not in self.playingUsers and userID not in self.match_queue:  # TODO: searches array which is slow
            self.user_names[userID] = userName
            self.match_queue.append(userID)
            self.user_names[userID] = userName
            if self.createMatch():
                return self.representation(userID)
            else:
                return f'{userName} has been added to the queue.'


    def listLegalMoves(self, userID):
        return str(self.chessGames[self.playingUsers[userID]][0].legal_moves)[37:-1]

    def move(self, userID, san_move):
        if userID in self.playingUsers:
            game = self.chessGames[self.playingUsers[userID]]
        else:
            return 'No active game. Join the queue with `!chess`'

        if game[0].is_game_over():
            return None
        elif (game[0].turn == chess.WHITE and game[1] == userID) or (game[0].turn == chess.BLACK and game[2] == userID): #if the player tries to move om the correct turn
            try:
                move = game[0].parse_san(san_move)  # try for parsing error
                game[0].push(move)
            except ValueError as error:
                if 'invalid' in str(error):
                    return 'Move expects valid algebraic notation. ie; Ne3, e4, Qxe2, etc.'
                elif 'illegal' in str(error):
                    return 'Illegal move. For a list of legal moves try !legal'
            return None
        elif (game[0].turn == chess.WHITE and game[2] == userID) or (game[0].turn == chess.BLACK and game[1] == userID): #if the player tries to move on the wrong turn
            return "Player not to move"
        else:
            return 'Unknown error'

    def representation(self, userID): #generates basic ascii representation
        game = self.chessGames[self.playingUsers[userID]]
        boardRepresentation = f'`{game[0]}`'

        if game[0].turn:
            boardRepresentation += f'\nWhite ({self.user_names[game[1]]}) to move.'
        else:
            boardRepresentation += f'\nBlack ({self.user_names[game[2]]}) to move.'

        return boardRepresentation

    def overCleanup(self, userID): #deletes game if it's over and displays a message
        game = self.chessGames[self.playingUsers[userID]]
        if game[0].is_game_over():
            # cleanup game
            result = f'\nGame over {game[0].result()}'
            del self.playingUsers[game[1]]
            if game[2] in self.playingUsers:
                del self.playingUsers[game[2]]
            del game
            return result

    def resign(self, userID):
        if userID not in self.playingUsers:
            return "You cannot resign if you are not in a match"
        else:
            game = self.chessGames[self.playingUsers[userID]]
            user_name = self.user_names[userID]
            # cleanup game:
            del self.playingUsers[game[1]]
            if game[2] in self.playingUsers:
                del self.playingUsers[game[2]]
            del game
            return f"{user_name} has resigned."
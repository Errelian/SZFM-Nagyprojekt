import chess

class ChessBot():
    def __init__(self): #TODO REFRACTOR THESE 3 INTO MORE OO WITH SEPARATE CLASSES ALL FANCY AND STUFF
        self.chessGames = {}  # gameID to index (chess.Board(), white, black) #TODO make into a class with 3 members: board, white, black. Needs to have a full arg contructor too.
        self.playingUsers = {}  # userID to index gameIDs
        self.usernameDict = {}  # userID to index Usernames

    def challenge(self, user1ID, user2ID):
        board = chess.Board()
        black = user1ID
        white = user2ID
        self.chessGames[id(board)] = (board, white, black)
        self.playingUsers[white] = id(board)  #players point to the game they are playing in
        self.playingUsers[black] = id(board)

    def matchup(self, user1, user2):
        if (user1.id not in self.playingUsers) and (user2.id not in self.playingUsers):
            self.usernameDict[user1.id] = user1
            self.usernameDict[user2.id] = user2
            self.challenge(user1.id, user2.id)
            return self.representation(user1.id)


    def listLegalMoves(self, userID):
        if userID in self.playingUsers:
            return str(self.chessGames[self.playingUsers[userID]][0].legal_moves)[37:-1]
        else:
            return "You must be in a game to ask for legal moves"

    def move(self, userID, algebraicMove): #TODO REFRACTOR
        if userID in self.playingUsers:
            game = self.chessGames[self.playingUsers[userID]]
        else:
            return 'No active game. Join the queue with `!chess`'

        if game[0].is_game_over():
            return "Game over."
        elif (game[0].turn == chess.WHITE and game[1] == userID) or (game[0].turn == chess.BLACK and game[2] == userID): #if the player tries to move om the correct turn
            try:
                move = game[0].parse_san(algebraicMove)
                game[0].push(move)
            except ValueError as error:
                if 'invalid' in str(error):
                    return 'Move expects valid algebraic notation. For example; Ne3, e4, Qxe2, etc.'
                elif 'illegal' in str(error):
                    return 'Move not legal, for a list of legal moves: !legal'
            return None
        elif (game[0].turn == chess.WHITE and game[2] == userID) or (game[0].turn == chess.BLACK and game[1] == userID): #if the player tries to move on the wrong turn
            return "Not this player's turn."
        else:
            return 'Unknown error'

    def representation(self, userID): #TODO REPLACE IT WITH A GENERATED IMAGE
        game = self.chessGames[self.playingUsers[userID]]
        boardRepresentation = f'`{game[0]}`'

        if game[0].turn:
            boardRepresentation += "\nWhite player's turn (" + str(self.usernameDict[game[1]]) + ") to move."
        else:
            boardRepresentation += "\nBlack player's turn (" + str(self.usernameDict[game[2]]) + ") to move."

        return boardRepresentation

    def overCleanup(self, userID): #cleans up the game once it's over
        game = self.chessGames[self.playingUsers[userID]]
        if game[0].is_game_over():

            result = "\nGame over" + game[0].result()
            del self.playingUsers[game[1]]
            if game[2] in self.playingUsers:
                del self.playingUsers[game[2]]
            del game
            return result
        return ''

    def resign(self, userID):
        if userID not in self.playingUsers:
            return "You cannot resign if you are not in a match"
        else:
            game = self.chessGames[self.playingUsers[userID]]
            user_name = self.usernameDict[userID]

            del self.playingUsers[game[1]]
            if game[2] in self.playingUsers:
                del self.playingUsers[game[2]]
            del game
            return f"{user_name} has fortfeited their game, shame."
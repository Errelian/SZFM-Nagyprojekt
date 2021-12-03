import sqlite3
import os.path
import sys

class DBSetup:
    def __init__(self):
        self.database_exists = os.path.isfile("scores.db")

        self.conn = sqlite3.connect('scores.db')
        self.c = self.conn.cursor()

    class Result:

        user_id = ""
        game_type = ""
        victory = ""

    def create_database(self):

        self.c.execute("""CREATE TABLE results (
        id integer not null primary key,
        player_id text,
        chess_games integer,
        chess_win integer,
        chess_draw integer,
        chess_lose integer,
        ttt_games integer,
        ttt_win integer,
        ttt_draw integer,
        ttt_lose integer
        )""")


    def get_next_id(self):

        self.c.execute("SELECT id FROM results ORDER BY ID DESC LIMIT 1")
        try:
            current_id = self.c.fetchone()[0]
        except Exception as e:
            return 0
        else:
            return current_id + 1



    def create_new_user(self):

        self.c.execute("INSERT INTO results VALUES (?, ?, '0', '0','0','0','0','0','0','0')", (self.get_next_id(),self.Result.user_id,) )


    def update_current_user_chess(self):

        if self.Result.victory == 1:
            self.c.execute("""
            UPDATE results
            SET chess_games = chess_games + 1,
            chess_win = chess_win + 1
            WHERE player_id = ?;
            """, (self.Result.user_id,))
        elif self.Result.victory == 0:
            self.c.execute("""
            UPDATE results
            SET chess_games = chess_games + 1,
            chess_lose = chess_lose + 1
            WHERE player_id = ?;
            """, (self.Result.user_id,))
        else:
            self.c.execute("""
            UPDATE results
            SET chess_games = chess_games + 1,
            chess_draw = chess_draw + 1
            WHERE player_id = ?;
            """, (self.Result.user_id,))



    def update_current_user_ttt(self):

            if self.Result.victory == 1:
                self.c.execute("""
                UPDATE results
                SET ttt_games = ttt_games + 1,
                ttt_win = ttt_win + 1
                WHERE player_id = ?;
                """, (self.Result.user_id,))
            elif self.Result.victory == 0:
                self.c.execute("""
                UPDATE results
                SET ttt_games = ttt_games + 1,
                ttt_lose = ttt_lose + 1
                WHERE player_id = ?;
                """, (self.Result.user_id,))
            else:
                self.c.execute("""
                UPDATE results
                SET ttt_games = ttt_games + 1,
                ttt_draw = ttt_draw + 1
                WHERE player_id = ?;
                """, (self.Result.user_id,))


    def database_handler(self,user_id,game_type,victory):


        if self.database_exists == False:
            self.create_database()


        self.Result.user_id = user_id
        self.Result.game_type = game_type
        self.Result.victory = int(victory)

        self.c.execute("SELECT id FROM results WHERE player_id = ?", (user_id,))
        try:
            self.c.fetchone()[0] == int
        except Exception as e:
            self.create_new_user()

        if game_type == "Chess":
            self.update_current_user_chess()
        elif game_type == "Tic-Tac-Toe":
            self.update_current_user_ttt()
        else:
            sys.exit("Game type doesn't exist")

        #DEBUG write contents to console
        self.c.execute("SELECT * FROM results")
        print(self.c.fetchall())

        self.conn.commit()
        self.conn.close()

#dbs = DBSetup()

#dbs.database_handler("Ace33","Chess","1")

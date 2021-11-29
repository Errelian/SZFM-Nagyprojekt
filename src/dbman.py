import sqlite3
import ChessBot
import os.path
import sys

database_exists = os.path.isfile("scores.db")

conn = sqlite3.connect('scores.db')
c = conn.cursor()

class Result:

    user_id = ""
    game_type = ""
    victory = ""

def create_database():

    c.execute("""CREATE TABLE results (
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


def get_next_id():

    c.execute("SELECT id FROM results ORDER BY ID DESC LIMIT 1")
    try:
        current_id = c.fetchone()[0]
    except Exception as e:
        return 0
    else:
        return current_id + 1



def create_new_user():

    c.execute("INSERT INTO results VALUES (?, ?, '0', '0','0','0','0','0','0','0')", (get_next_id(),Result.user_id,) )


def update_current_user_chess():

    if Result.victory == 1:
        c.execute("""
        UPDATE results
        SET chess_games = chess_games + 1,
        chess_win = chess_win + 1
        WHERE player_id = ?;
        """, (Result.user_id,))
    elif Result.victory == 0:
        c.execute("""
        UPDATE results
        SET chess_games = chess_games + 1,
        chess_lose = chess_lose + 1
        WHERE player_id = ?;
        """, (Result.user_id,))
    else:
        c.execute("""
        UPDATE results
        SET chess_games = chess_games + 1,
        chess_draw = chess_draw + 1
        WHERE player_id = ?;
        """, (Result.user_id,))



def update_current_user_ttt():

        if Result.victory == 1:
            c.execute("""
            UPDATE results
            SET ttt_games = ttt_games + 1,
            ttt_win = ttt_win + 1
            WHERE player_id = ?;
            """, (Result.user_id,))
        elif Result.victory == 0:
            c.execute("""
            UPDATE results
            SET ttt_games = ttt_games + 1,
            ttt_lose = ttt_lose + 1
            WHERE player_id = ?;
            """, (Result.user_id,))
        else:
            c.execute("""
            UPDATE results
            SET ttt_games = ttt_games + 1,
            ttt_draw = ttt_draw + 1
            WHERE player_id = ?;
            """, (Result.user_id,))


def database_handler(user_id,game_type,victory):

    if database_exists == False:
        create_database()


    Result.user_id = user_id
    Result.game_type = game_type
    Result.victory = int(victory)

    c.execute("SELECT id FROM results WHERE player_id = ?", (user_id,))
    try:
        c.fetchone()[0] == int
    except Exception as e:
        create_new_user()

    if game_type == "Chess":
        update_current_user_chess()
    elif game_type == "Tic-Tac-Toe":
        update_current_user_ttt()
    else:
        sys.exit("Game type doesn't exist")

    #DEBUG write contents to console
    c.execute("SELECT * FROM results")
    print(c.fetchall())

    conn.commit()
    conn.close()

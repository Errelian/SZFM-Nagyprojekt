#!/usr/bin/env python3

import sqlite3
import ChessBot
import os.path
import sys

database_exists = os.path.isfile("scores.db")


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
        print("Empty database")
        return 0
    else:
        return current_id + 1



def create_new_user():

    c.execute("INSERT INTO results VALUES (?, ?, '0', '0','0','0','0','0','0','0')", (get_next_id(),user_id,) )


def update_current_user_chess():

    if victory == 1:
        c.execute("""
        UPDATE results
        SET chess_games = chess_games + 1,
        chess_win = chess_win + 1
        WHERE player_id = ?;
        """, (user_id,))
    elif victory == 0:
        c.execute("""
        UPDATE results
        SET chess_games = chess_games + 1,
        chess_lose = chess_lose + 1
        WHERE player_id = ?;
        """, (user_id,))
    else:
        c.execute("""
        UPDATE results
        SET chess_games = chess_games + 1,
        chess_draw = chess_draw + 1
        WHERE player_id = ?;
        """, (user_id,))



def update_current_user_ttt():

        if victory == 1:
            c.execute("""
            UPDATE results
            SET ttt_games = ttt_games + 1,
            ttt_win = ttt_win + 1
            WHERE player_id = ?;
            """, (user_id,))
        elif victory == 0:
            c.execute("""
            UPDATE results
            SET ttt_games = ttt_games + 1,
            ttt_lose = ttt_lose + 1
            WHERE player_id = ?;
            """, (user_id,))
        else:
            c.execute("""
            UPDATE results
            SET ttt_games = ttt_games + 1,
            ttt_draw = ttt_draw + 1
            WHERE player_id = ?;
            """, (user_id,))



conn = sqlite3.connect('scores.db')
c = conn.cursor()

if database_exists == False:
    create_database()


print(get_next_id())

#user_id, type_of_game, win=1 lose=0 draw=2
recieved_array = ["AcesHigh37","Tic-Tac-Toe","0"]
user_id = recieved_array[0]
game_type = recieved_array[1]
victory = int(recieved_array[2])


c.execute("SELECT id FROM results WHERE player_id = ?", (user_id,))
try:
    c.fetchone()[0] == int
except Exception as e:
    print("Not found")
    create_new_user()

print("Found")
if game_type == "Chess":
    update_current_user_chess()
elif game_type == "Tic-Tac-Toe":
    update_current_user_ttt()
else:
    sys.exit("Game type doesn't exist")




c.execute("SELECT * FROM results")
print(c.fetchall())

#print(id)

conn.commit()
conn.close()

########################################################################################

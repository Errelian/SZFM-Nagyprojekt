import sqlite3

conn = sqlite3.connect('scores.db')

c = conn.cursor()

c.execute("""CREATE TABLE results (
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

c.execute("INSERT INTO results VALUES ('AcesHigh37', '15', '7','3','5','30','5','20','5')")

c.execute("SELECT * FROM results")
print(c.fetchall())

conn.commit()
conn.close()

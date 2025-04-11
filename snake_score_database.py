import sqlite3
from datetime import datetime

connect = sqlite3.connect("scores.db")
cursor = connect.cursor()


# creating the scores table
cursor.execute('''
CREATE TABLE IF NOT EXISTS scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    game_name TEXT NOT NULL,
    score INTEGER NOT NULL,
    timestamp TEXT NOT NULL
)
''')

connect.commit()




# Save a new score
def save_score(username, game_name, score):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('''
        INSERT INTO scores (username, game_name, score, timestamp)
        VALUES (?,?,?,?)
    ''', (username, game_name, score, timestamp))
    connect.commit()

# Get highest score for user in snake game
def get_user_high_score(username, game_name):
    cursor.execute('''
        SELECT MAX(score) FROM scores
        WHERE username = ? AND game_name = ?
    ''', (username, game_name))
    result = cursor.fetchone()
    return result[0] if result[0] is not None else 0

# Get top scores for snake game (easy & hard mode)

def get_top_scores(game_name, limit=5):
    cursor.execute('''
        SELECT username, score, timestamp
        FROM scores
        WHERE game_name = ?
        ORDER BY score DESC
        LIMIT ?
    ''', (game_name, limit))
    return cursor.fetchall()

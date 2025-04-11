from flask import Flask, render_template
import subprocess
import sys
app = Flask(__name__)




@app.route('/')
def index():
    return render_template('index.html') #this should point to the
#main html page

@app.route('/start_snake')
def start_snake():
    subprocess.Popen([sys.executable, "snake_easy_mode.py"])
    return render_template("snake_loading.html")

@app.route('/start_snake_hard')
def start_snake_hard():
    subprocess.Popen([sys.executable, "snake_hard_mode.py"])
    return render_template("snake_hard_loading.html")


@app.route('/start_pong')
def start_pong():
    subprocess.Popen([sys.executable, "pong_two_player_game.py"])
    return render_template("pong_loading.html")

@app.route('/start_tic_tac_toe')
def start_tic_tac_toe():
    subprocess.Popen([sys.executable, "tic_tac_toe.py"])
    return render_template("tic_tac_toe_loading.html")

@app.route('/start_tic_tac_toe_ai')
def start_tic_tac_toe_ai():
    subprocess.Popen([sys.executable, "tic_tac_toe_human_vs_ai.py"])
    return render_template("tic_tac_toe_ai_loading.html")

@app.route('/snake_menu')
def snake_menu():
    return render_template('snake_menu.html')

@app.route('/tic_tac_toe_menu')
def tic_tac_toe_menu():
    return render_template('tic_tac_toe_menu.html')

@app.route('/pong_menu')
def pong_menu():
    return render_template('pong_menu.html')

@app.route('/about')
def about():
    return render_template('About.html')




if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for
from def_fight import game

app = Flask(__name__)

d = {'player_1': 0, 'player_2': 0, 'tie': 0}


@app.route('/')
def hello():
    return redirect(url_for('enter_page'))


@app.route('/round2', methods=['POST'])
def round2() -> 'html':
    player_1 = request.form['player_1']
    player_2 = request.form['player_2']
    result = str(game(player_1, player_2))
    d[result] += 1
    print(d)
    obj = ['rock', 'scissors', 'paper']
    return render_template('round2.html',
                           obj=obj,
                           player_1=player_1,
                           player_2=player_2,
                           result=result, )


@app.route('/round3', methods=['POST'])
def round3() -> 'html':
    player_1 = request.form['player_1']
    player_2 = request.form['player_2']
    result = str(game(player_1, player_2))
    d[result] += 1
    print(d)
    obj = ['rock', 'scissors', 'paper']
    return render_template('round3.html',
                           obj=obj,
                           player_1=player_1,
                           player_2=player_2,
                           result=result, )


@app.route('/results', methods=['POST'])
def results() -> 'str':
    player_1 = request.form['player_1']
    player_2 = request.form['player_2']
    title = "Here is your result:"
    result = str(game(player_1, player_2))
    d[result] += 1
    print(d)
    if d['player_1'] > d['player_2']:
        result = "Player 1 has won!"
        count = str(d['player_1']) + " : " + str(d['player_2'])
        return render_template('result.html',
                               title=title,
                               count=count,
                               result=result, )
    elif d['player_2'] > d['player_1']:
        result = "Player 2 has won!"
        count = str(d['player_1']) + " : " + str(d['player_2'])
        return render_template('result.html',
                               title=title,
                               count=count,
                               result=result, )
    else:
        result = "Tie! No one has won."
        count = str(d['player_1']) + " : " + str(d['player_2'])
        return render_template('result.html',
                               title=title,
                               count=count,
                               result=result, )


@app.route('/enter')
def enter_page() -> 'html':
    rounds = "Round 1!"
    obj = ['rock', 'scissors', 'paper']
    return render_template('enter.html',
                           rounds=rounds,
                           obj=obj,
                           title="Welcome to my first project: 'Rock, Scissors, Paper'")


app.run()

from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def index_page():  # put application's code here
    return render_template("index.html")


@app.route('/movie')
def movie_page():
    datalist = []
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select * from movie250"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()

    return render_template("movie.html", movies=datalist)


@app.route('/score')
def score_page():
    score = []
    score_count = []
    con = sqlite3.connect('movie.db')
    cur = con.cursor()
    sql = "select score, count(score) from movie250 group by score"
    data = cur.execute(sql)
    for item in data:
        # 不允许有print()类型的语句
        score.append(item[0])
        score_count.append(item[1])
    cur.close()
    con.close()

    return render_template("score.html", score=score, score_count=score_count)


@app.route('/team')
def team():
    return render_template("team.html")


@app.route('/word')
def word():
    return render_template("word.html")


if __name__ == '__main__':
    app.run()

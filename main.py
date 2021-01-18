from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/bot')
def bot():
    return render_template('bot.html')

@app.route('/graphics')
def graphics():
    return render_template('graphics.html')

@app.route('/info')
def infp():
    return render_template('info.html')

if __name__ == '__main__':
    app.run(debug=True)
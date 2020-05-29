from flask import Flask, render_template, redirect, request
from Data.textProcessing import poemFind

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/losuj/<category>', methods=['POST', 'GET'])
def losuj(category):
    text = poemFind(category)
    if category == "milosc":
        category = "miłość"
    elif category == "przyjazn":
        category = "przyjaźń"
    elif category == "zyczenia":
        category = "życzenia"
    elif category == "dladzieci":
        category = "dla dzieci"
    elif category == "zycie":
        category = "życie"
    return render_template('poem_text.html', text=text, category=category)


if (__name__) == "__main__":
    app.run(debug=True)

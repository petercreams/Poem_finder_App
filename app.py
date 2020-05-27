from flask import Flask, render_template, redirect, request
from Data.textProcessing import poemFind

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/losuj', methods=['POST'])
def losuj():
    wybory = request.form.getlist('check')

    if len(wybory) > 1:
        return "Wybierz jedną kategorię!"

    elif len(wybory) == 1:
        # return render_template('poem_text.html')
        # return wybory[0]
        text = poemFind(wybory[0])
        return render_template('poem_text.html', text=text)
    else:
        redirect('/')
        return render_template('index.html')

    # else:
    #     return render_template('index.html')


if (__name__) == "__main__":
    app.run(debug=True)

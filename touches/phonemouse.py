from flask import Flask
from pynput.mouse import Button, Controller

cont = Controller()

app = Flask(__name__)
count = 0

@app.route('/ping')
def metric():
    global count
    count += 1
    return str(count)

@app.route('/click')
def health():
    cont.click(Button.left)

@app.route('/move/<int:x>/<int:y>')
def move(x, y):
    cont.position = (x, y)
    return "ok"

app.run()
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def home():
    return render_template('my_template.html')

@app.route('/home')
def home():
    return render_template('my_template.html')

@app.route('/regions', methods=['GET'])
def regions():
    return render_template('regions.html')
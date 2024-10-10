from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/yes')
def yes():
    return render_template('sucess.html')

if __name__ == '__main__':
    app.run(debug=True)
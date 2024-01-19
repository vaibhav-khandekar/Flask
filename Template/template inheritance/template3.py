from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index3_home.html')

@app.route('/<name>')
def name(name):
    return render_template('index3_name.html',name = name)

if __name__ == '__main__':
    app.run(debug = True)

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>hello vaibhav whatsup??</h1>'

@app.route('/info') # 127.0.0.1:5000/info
def info():
   return 'myself Vaibhav Khandekar'

@app.route('/user/<name>') # 127.0.0.1:5000/user/<name>
def user(name):
   return '<h3>this is page for {}</h3>'.format(name)

@app.route('/uppercase/<name>') # 127.0.0.1:5000/uppercase/<name>
def uppercase(name):
   return '<h3>name in uppercase : {}</h3>'.format(name.upper())

@app.route('/uppercase2/<name>') # 127.0.0.1:5000/uppercase2/<name>
def uppercase2(name):
   return '<h3>100th letter : {}</h3>'.format(name[100])

if __name__ == '__main__':
    app.run(debug = True)

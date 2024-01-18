from flask import Flask
app = Flask(__name__)

@app.route('/') # 127.0.0.1:5000/
def index():
   return 'Hello guys good evening'

if __name__ == '__main__':
   app.run(debug = True)

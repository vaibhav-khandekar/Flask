from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/') # 127.0.0.1:5000
def index():
   return render_template('base.html')

if __name__ == '__main__':
   app.run(debug = True)

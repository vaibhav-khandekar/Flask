from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/') # 127.0.0.1:5000
def index():
   sample_variable = "Vaibhav"
   return render_template('index.html',my_variable = sample_variable)

if __name__ == '__main__':
   app.run(debug = True)

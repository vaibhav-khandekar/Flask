# template variables

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    sample_variable = 'Vaibhav'
    letters = list(sample_variable)
    dictionary = {'name':'Vaibhav Khandekar','location':'Mumbai'}
    return render_template('index1.html',my_variable = sample_variable, letters = letters, dictionary = dictionary)

if __name__ == '__main__':
    app.run(debug = True)

# template control flow

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    # user logged in
    user_logged_in = True

    # lists
    my_list = [1,2,3,4,5,6,7,8,9]
    name_list = ['vaibhav','khandekar','baban']
    return render_template('index2.html',my_list = my_list, name_list = name_list,user_logged_in = user_logged_in)

if __name__ == '__main__':
    app.run(debug = True)

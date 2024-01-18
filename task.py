from flask import Flask
app = Flask(__name__)

@app.route('/latin-name/<name>') # 127.0.0.1:5000/latin-name/<name>
def latin_name(name):
    if name[-1] == 'y':
        return '<h2> your latin name is {} </h2>'.format(name[:-1]+'iful')
    else:
        return '<h2> your latin name is {} </h2>'.format(name+'y')

if __name__ == '__main__':
    app.run(debug = True)

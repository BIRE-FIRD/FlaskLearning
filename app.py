from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'aaaa'

@app.route('/test')
def test():
    return 'bbbb'

if __name__ == '__main__':
    app.run()
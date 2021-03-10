import flask
import dotenv
import os

if os.path.exists('.env'):
    dotenv.load_dotenv('.env')

app = flask.Flask(__name__)

app.config['LISTEN_HOST'] = os.getenv('LISTEN_HOST', '0.0.0.0')
app.config['LISTEN_PORT'] = int(os.getenv('LISTEN_PORT', '5000'))

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == "__main__":
    app.run(app.config['LISTEN_HOST'], app.config['LISTEN_PORT'])

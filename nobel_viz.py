# nobel_viz.py
from flask import Flask, send_from_directory

app = Flask(__name__)


# Serves a file from the directory—in this case, the local directory
# (.)]—specified in the first argument.
@app.route('/')
def root():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(port=8080)

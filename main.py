from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/index_html', methods=["GET", "POST"])
def index_html():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8081')
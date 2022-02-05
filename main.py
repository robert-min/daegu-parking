from flask import Flask, render_template
from db_model.mysql import PyMyDao

app = Flask(__name__)

@app.route('/index_html')
def index_html():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8081')
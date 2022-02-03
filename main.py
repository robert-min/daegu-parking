from flask import Flask, render_template
from db_model.mysql import PyMyDao

app = Flask(__name__)

@app.route('/html_test')
def index_html():
    ilList = PyMyDao().getIlParking()
    return render_template('index.html', ilList=ilList)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')
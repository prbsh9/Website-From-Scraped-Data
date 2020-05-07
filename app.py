from flask import Flask
from flask import render_template
from nepnews_soup import newsToJson  # this will get news in json format

app = Flask(__name__)
posts = newsToJson()

@app.route('/')
@app.route('/home')
def index():
    return render_template('tajanews.html', newsHaru=posts)


if __name__ == '__main__':
    app.run(debug=True)

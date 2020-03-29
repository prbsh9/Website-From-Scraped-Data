from flask import Flask
from flask import render_template
from nepnews_soup import newsToJson  # this will get news in json format
# import json

app = Flask(__name__)
posts = newsToJson()
# print(posts)
# jsonFile = open('newsNep.json', encoding='utf8', errors='ignore')
# posts = json.load(jsonFile)


@app.route('/')
@app.route('/home')
def index():
    return render_template('tajanews.html', newsHaru=posts)


# print(posts)
if __name__ == '__main__':
    # app.run(host= '192.168.10.76', debug=True)
    app.run(debug=True)

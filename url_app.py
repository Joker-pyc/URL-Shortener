from flask import Flask, render_template, request
import pyshorteners

app = Flask(__name__)

def shorten_url(long_url):
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(long_url)
    return short_url

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        long_url = request.form['long_url']
        short_url = shorten_url(long_url)
        return render_template('index.html', short_url=short_url)
    return render_template('index.html', short_url=None)

if __name__ == '__main__':
    app.run(debug=True)

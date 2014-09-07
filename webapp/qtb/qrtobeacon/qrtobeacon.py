from parse_rest.datatypes import Object
import parse_rest
from parse_rest.connection import register
from flask import render_template
from flask import Flask, url_for

class Code(Object):
    pass

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/beacon/', methods=['GET', 'POST'])
def beacon():
    if request.method == 'POST':
        # Register with Parse server.
        datURL = request.form['url']
        register("FDoBXtYkrZ6aM4oqdm7pXn2ZsKApqCXdHuSTNZwu", "rdwk2DsLdlLqjyQZZyDKCRDHTi4fClqCOcz0e4HT")
        thisCode = Code(url = datURL, major = datMajor, minor = datMinor)
        thisCode.save()
    return render_template('beacon.html', thisBeacon = thisCode)


if __name__ == "__main__":
    app.run()

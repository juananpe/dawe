from flask import Flask
from flask.ext.cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
@cross_origin()
def libros():
    with open('libros.json', 'r') as f:
        dat = f.read()

    return (dat)
#    resp = Response(dat, status=200, mimetype='application/json')
#    return resp 

if __name__ == "__main__":
    app.run(threaded=True)

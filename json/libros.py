from flask import Flask
app = Flask(__name__)

@app.route("/")
def libros():
    with open('libros.json', 'r') as f:
        dat = f.read()
    
    # resp = Response(response=dat, status=200, mimetype="application/json")
    return dat
    #return(resp)

if __name__ == "__main__":
    app.run()

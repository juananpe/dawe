from flask import Flask
app = Flask(__name__)

@app.route("/")
def libros():
    with open('libros.json', 'r') as f:
        dat = f.read()
    
    return dat

if __name__ == "__main__":
    app.run()

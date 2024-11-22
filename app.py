
from flask import Flask
app = Flask(__name__)


@app.route("/")
def HolaFlask():
    return "<h1>¡Hola Flask!</h1> <hr>"


@app.route("/notas/<float:nota1>/<float:nota2>/<float:nota3>")
def notas(nota1=0, nota2=0, nota3=0):
    resultado = (nota1*30/100 + nota2*30/100 + nota3*40/100)
    return f"<h1>El resultado es: {resultado}</h1> <hr>"

if __name__ == "__main__":
   
    app.run(debug=True)

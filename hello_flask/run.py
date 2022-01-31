from flask import Flask, escape, request

app = Flask(__name__)

@app.route("/<numero>", methods = ['GET','POST'])
def Ola(numero):
    return 'Olá, Mundo ! {}'.format (numero)
if __name__ == "__main__":
    app.run(debug=True)


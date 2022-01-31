from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/<int:id>')
def pessoas (id):
      soma= 1 + id
      return {'id':id, 'Nome':'Rafael', 'profissao':'desenvolvedor'}

#@app.route('/soma/<int:valor1>/<int:valor2>/')
#def soma(valor1,valor2):
#    return jsonify({'soma': valor1 + valor2})
@app.route ('/soma', methods = ['POST'])

def soma():
    return 'soma'

if __name__ == '__main__':
    app.run(debug=True)
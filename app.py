from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    nota1 = float(request.form['nota1'])
    nota2 = float(request.form['nota2'])
    nota3 = float(request.form['nota3'])
    nota4 = float(request.form['nota4'])
    
    media = (nota1 + nota2 + nota3 + nota4) / 4
    
    return render_template('resultado.html', media=media)

if __name__ == '__main__':
    app.run(debug=True)
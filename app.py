from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # Página inicial

@app.route("/calcular", methods=["POST"])
def calcular():
    # Lógica da calculadora será implementada aqui
    pass

if __name__ == "__main__":
    app.run(debug=True)


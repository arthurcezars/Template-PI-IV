from flask import Flask, render_template
import  requests

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    url = f"https://impostometro.com.br/Contador/Tributo?estado={'es'}&municipio={'vitoria'}&esfera=federal&tributo=cide&dataInicial=01/01/2021"
    response = requests.get(url)
    dados = response.json()
    teste = ["https://impostometro.com.br/widget/contador/es?municipio=vitoria", "https://impostometro.com.br/widget/contador/es?municipio=serra"]
    return render_template("index.html", impostos=teste)


if __name__ == '__main__':
    app.run()

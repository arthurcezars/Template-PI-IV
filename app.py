from doctest import debug

from flask import Flask, render_template, request
import  requests

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():  # put application's code here
    estado_escolhido = request.args.get("estados") # Pega o estado que o usuario pesquisar.

    # Pesquisa na api que retorna o JSON com os dados.
    url = f"https://impostometro.com.br/Contador/Tributo?estado={'es'}&municipio={'vitoria'}&esfera=federal&tributo=cide&dataInicial=01/01/2021"
    response = requests.get(url)
    dados = response.json()

    print(estado_escolhido)
    # Pesquisa na api que retorna o link para o iframe (somente visual, não retornar mais nenhum dado).
    if (estado_escolhido == None):
        tela_imposto = [f"https://impostometro.com.br/widget/contador/"]
    else:
        tela_imposto = [f"https://impostometro.com.br/widget/contador/{estado_escolhido.lower()}"]

    return render_template("index.html", impostos=tela_imposto)


if __name__ == '__main__':
    app.run(debug=True)

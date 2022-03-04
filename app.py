

import requests
from flask import Flask, render_template, request
from led_control import temperatura, executarFita


app = Flask(__name__)

estados = ['ac', 'al', 'am', 'ap', 'ba', 'ce', 'df', 'es', 'go', 'ma', 'mg',
           'ms', 'mt', 'pa', 'pb', 'pe', 'pi', 'pr', 'rj', 'rn', 'ro', 'rr',
           'rs', 'sc', 'se', 'sp', 'to']
arrecadacao_brasil = 0
for i in range(len(estados)):
    url = f"https://impostometro.com.br/Contador/Estado?estado={estados[i]}&dataInicial=01/01/2021"

    payload = {}
    headers = {
        'Host': 'impostometro.com.br',
        'Cookie': '__utma=96219524.641163375.1631403844.1631403844.1631403844.1; __utmz=96219524.1631403844.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
        'sec-ch-ua': '"Opera GX";v="81", " Not;A Brand";v="99", "Chromium";v="95"',
        'accept': 'application/json, text/javascript, /; q=0.01',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 OPR/81.0.4196.52',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://impostometro.com.br/',
        'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    print(estados[i])
    print(response.text)
    data = response.json()
    arrecadacao_brasil += int(data['Valor'])
print(arrecadacao_brasil)

@app.route('/', methods=["GET", "POST"])
def index():  # put application's code here
    estado_escolhido = request.args.get("estados") # Pega o estado que o usuario pesquisar.

    print(estado_escolhido)
    # Pesquisa na api que retorna o link para o iframe (somente visual, não retornar mais nenhum dado).
    if (estado_escolhido == None):
        tela_imposto = [f"https://impostometro.com.br/widget/contador/"]
        print(arrecadacao_brasil)
        #temperatura(100)
        executarFita(temperatura(100))
    else:
        tela_imposto = [f"https://impostometro.com.br/widget/contador/{estado_escolhido.lower()}"]
        # Pesquisa na api que retorna o JSON com os dados.
        url = f"https://impostometro.com.br/Contador/Estado?estado={estado_escolhido.lower()}&dataInicial=01/01/2021"
        payload = {}
        headers = {
            'Host': 'impostometro.com.br',
            'Cookie': '__utma=96219524.641163375.1631403844.1631403844.1631403844.1; __utmz=96219524.1631403844.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
            'sec-ch-ua': '"Opera GX";v="81", " Not;A Brand";v="99", "Chromium";v="95"',
            'accept': 'application/json, text/javascript, /; q=0.01',
            'x-requested-with': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 OPR/81.0.4196.52',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://impostometro.com.br/',
            'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        dados = response.json()

        arrecadacao = int(dados['Valor'])
        print(arrecadacao)
        referencia = int((arrecadacao * 100) / arrecadacao_brasil)
        print(referencia)
        #temperatura(referencia)
        executarFita(temperatura(referencia))

    return render_template("index.html", impostos=tela_imposto)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

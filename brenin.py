import requests

url = "https://impostometro.com.br/Contador/Estado?estado=df&dataInicial=01/01/2021"

payload={}
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

print(response.text)
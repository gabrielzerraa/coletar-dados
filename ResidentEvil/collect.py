# %%

import requests
from bs4 import BeautifulSoup

url = 'https://www.residentevildatabase.com/personagens/albert-wesker/'

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_gid=GA1.2.510509082.1718997808; _ga=GA1.1.1367306953.1718997807; __gads=ID=06b102cd787d8d6f:T=1718997851:RT=1719000161:S=ALNI_MYpaH55AmS_-VwYgRYWq1HGrMtmHA; __gpi=UID=00000a2fee99d4a4:T=1718997851:RT=1719000161:S=ALNI_MbJzx03MfKqff5K7Dcuj2ZiUFTbSQ; __eoi=ID=fa734989e0a93171:T=1718997851:RT=1719000161:S=AA-AfjaJY0FwwvMTdc8vyMmoOlUk; _ga_DJLCSW50SC=GS1.1.1719000117.2.1.1719000121.56.0.0; _ga_D6NF5QC4QT=GS1.1.1719000117.2.1.1719000121.56.0.0; FCNEC=%5B%5B%22AKsRol8n8zRzZZvFCupdTA-_lWEdIvqSZmb0Kb6fl54836qxlFqZPFzylIAXHUyKqGLdqplBabFzurl83Tl4wXfrdjuOiFz45LcRgzJtWsEtYqxM6cMiJT_kVBV5RVedGDKbmgxh5xSUQgIeRGGT6cGTEapTr5PXtA%3D%3D%22%5D%5D',
    'priority': 'u=0, i',
    'referer': 'https://www.residentevildatabase.com/personagens/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

resp = requests.get(url, headers=headers)

# %%

soup = BeautifulSoup(resp.text)
soup
# %%
div_page = soup.find('div', class_ = 'td-page-content')
# %%
paragrafo = div_page.find_all('p')[1]
paragrafo
# %%
ems = paragrafo.find_all('em')
ems
# %%
ems[0].text
# %%
data = {}
for i in ems:
    chave, valor = i.text.split(':')
    chave = chave.strip(' ')
    data[chave] = valor.strip(' ')
data
# %%
data['Peso']
# %%

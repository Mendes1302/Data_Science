from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import psycopg2 as sql

def data_base(data_name, data_uf):
    conn = sql.connect(host='localhost', database='teste',
    user='your_user', password='your_password')
    cursor = conn.cursor()

    for i in range(0, len(data_name)):
        cursor.execute(f"INSERT INTO cidade (id, nome, uf) VALUES ('{i}', '{data_name[i]}', '{data_uf[i]}');")
        conn.commit()
    cursor.close()
    conn.close()
    print("OK!!")



array_UF = list()
array_NAME = list()

try:
    html = urlopen("https://mundoeducacao.uol.com.br/geografia/estados-brasil.htm")
    res = BeautifulSoup(html.read(),"html.parser")
    tag = str(res.findAll("tbody"))
    start = "<p style=\"text-align:center\"><strong>Sigla</strong></p>"
    end = "</tbody>, <tbody>"
    tag = tag[tag.find(start)+len(start):tag.find(end)].replace("\n", "")
    indx1 = indx2 = indx3 = indx4 = c = 0
    while True:
        indx1 = tag.find("center\">", indx2)+len("center\">")
        indx2 = tag.find("</p>", indx1)
        if indx2-indx1 == 2:
            c += 1
            array_UF.append(tag[indx1: indx2])
            if c == 27:
                break
        else:
            indx3 = tag.find(".htm\">", indx4)+len(".htm\">")
            indx4 = tag.find("</a>", indx3)
            array_NAME.append(tag[indx3: indx4])
    data_base(array_NAME, array_UF)
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")


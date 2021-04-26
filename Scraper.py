import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv

date = datetime.today()
date_text = date.strftime('%d/%m/%Y Hora %H:%M')
date_csv = date.strftime('%d/%m')

URL = 'https://dolarhoje.com/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = str(soup.find(id='nacional'))
final = results[40:44].replace(',','.')


#Save CSV
with open('log.csv', 'a', newline='') as csvfile :
    columnNames = ['Quotation', 'Day']
    writer = csv.DictWriter(csvfile, fieldnames=columnNames)
    cl_str = str(columnNames)
    cond = int((len(cl_str)))
    if (cond > 1):
        writer = csv.writer(csvfile)
        wr = [str(final), str(date_csv)]
        writer.writerow(wr)

#Save Log
with open("log.txt", "a") as arq:
    arq.write( '%s | O valor do dolar estava R$%s\n' %(date_text,final))

print("+-----------------------------------+")
print(f"|O valor de 1 dolar hoje é de R${final}")
print("+-----------------------------------+")
print("+-----------------------------------+")
print("|     %s         |"% date_text)
print("+-----------------------------------+")





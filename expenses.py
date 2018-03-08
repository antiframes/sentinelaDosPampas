from lxml import html
import requests
import pandas as pd
deps = pd.read_csv('depids.csv')
def get_month(dep,depid,mon,yr):
    url = 'http://ww1.al.rs.gov.br/'+dep+'/DesktopModules/alrsTranspRelatorioGastos/Impressao.aspx?Tipo=1&IdCategoriaCota='+str(depid)+'&DataGasto='+str(mon)+'/11/'+str(yr)+'%200:00:00'
    print(url)
    page = requests.get(url)
    tree = html.fromstring(page.content)
    expenses = tree.xpath('//table[@class="grdvwgastosinterno"]//span/text()')
    titles = tree.xpath('//table[@class="grdvwgastosinterno"]//td/text()')
    titles2 = []

    for title in titles:
        nt = title.strip(' \n\r')
        if len(nt)>0:
            titles2.append(title)
    for i in range(len(expenses)):
        print(titles2[i],expenses[i])
    print()
    print()
    
    
#get_month(zanchin.dep,str(zanchin.id),'1','2017')

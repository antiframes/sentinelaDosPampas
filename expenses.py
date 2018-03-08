from lxml import html
import requests
import pandas as pd
import time
deplist = pd.read_csv('2_prepared_data/deps.csv',sep=',')

#declarando colunas do dataframe final
depids = []
deps = []
date =[]
exptype = [] #tipo de gasto
price = []

def get_month(dep,depid,mon,yr):
    if (len(mon)==1):
        mon='0'+mon
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
        depids.append(depid)
        deps.append(dep)
        date.append(str(yr)+'-'+str(mon)+'-01')#salvar como data
        exptype.append(titles2[i])
        exp = expenses[i].split(' ')[1].replace('.','').replace(',','.')
        price.append(float(exp))
    time.sleep(0.5)#vamos ser gentis com o servidor ;)
zanchin = deplist.iloc[0]

for i in (range(len(deplist))):
    deputado = deplist.iloc[i]
    for j in [2015,2016,2017]:
        for k in range(1,13):
            get_month(deputado.dep,str(deputado.id),str(k),str(j))

#construir dataframe e salvar em csv
d = {'depid':depids,'dep':deps, 'date':date,'exptype':exptype,'price':price}
df = pd.DataFrame(data=d)
df.to_csv('2_prepared_data/expenses.csv',index=False,sep=',')

import pandas as pd
import urllib
import urllib.request
from lxml import html

#Pegar lista de deputados
deps = pd.read_csv('2_prepared_data/diarias1.csv')



#Resumo das viagens
requisicao = []
destino = []
ida = []
volta = []
solicitante = []
qtdiarias = []
valor = []
valtotal = [] # soma das diarias
numpassagens = []

#Notas fiscais
requisicao1 = []
cnpj =[]
cidade = []
data = []
valor1=[]

def to_number(s):
    return float(s.replace('.','').replace(',','.'))
def to_date(s):
    d = s.split('/')
    return d[2]+'-'+d[1]+'-'+d[0]

for d in range(len(deps)):
    dep = deps.iloc[d]
    print(dep.dep,dep.ano)
    req = urllib.request.urlopen(dep.link)
    res = str(req.read())
    tree = html.fromstring(res)
    links = tree.xpath('//table[@class="tablediarias"]//a/@href')
    for l in links:
        req = urllib.request.urlopen(l)
        res = str(req.read())
        tree = html.fromstring(res)

	#Pegar informações da primeira tabela
        table1 = tree.xpath('(//table[@class="tablediarias"])[1]//td/text()')

        reqdata = tree.xpath('(//table[@class="tablediarias"])//span/text()')
        requisicao.append(reqdata[0])
        destino.append(table1[2])
        ida.append(table1[3])
        volta.append(table1[4])
        solicitante.append(table1[5])
        qtdiarias.append(to_number(table1[6]))
        valor.append(to_number(table1[7].split(' ')[1]))
        
        #DESCOBRIR SE OUTRAS DUAS TABELAS EXISTEM
        table1 = tree.xpath('(//table[@class="tablediarias"]/@id)')
        tablenames = [x.split('_')[-1] for x in table1 ]
        grdvwNotas_pos=-1
        grdvwBilhetes_pos=-1
        for i in range(len(tablenames)):
            if tablenames[i]=='grdvwNotas':
                grdvwNotas_pos=i+1
            if tablenames[i]=='grdvwBilhetes':
                grdvwBilhetes_pos=i+1
                
        vtotal = 0
	#TABELA DE NOTAS
        if (grdvwNotas_pos>-1):
            table2 = tree.xpath('(//table[@class="tablediarias"])['+str(grdvwNotas_pos)+']//td/text()')
            trows = len(tree.xpath('(//table[@class="tablediarias"])['+str(grdvwNotas_pos)+']//tr'))
            for i in range(int(len(table2)/5)):
                base = i*5
                requisicao1.append(reqdata[0])
                cnpj.append(table2[base+1])
                cidade.append(table2[base+2].rstrip())
                data.append(to_date(table2[base+3]))
                v = to_number(table2[base+4].split(' ')[1])
                vtotal+=v
                valor1.append(v)
        valtotal.append(vtotal)
        
	#Contar número de passagens aéreas
        numpas = 0
        if (grdvwBilhetes_pos>-1):
            table2 = tree.xpath('(//table[@class="tablediarias"])[3]//tr')
            numpas=len(table2)-1
        numpassagens.append(numpas)



#Construir e salvar Data Frames
d1 = {'requisicao':requisicao,'destino':destino,'ida':ida,'volta':volta,'solicitante':solicitante,'qtdiarias':qtdiarias,'valor':valor,'valtotal':valtotal,'numpassagens':numpassagens}
d2 = {'requisicao':requisicao1,'cnpj':cnpj,'cidade':cidade,'data':data,'valor':valor1}

df1 = pd.DataFrame(data=d1)
df2 = pd.DataFrame(data=d2)
df1.to_csv('2_prepared_data/diarias2.csv',index=False)
df2.to_csv('2_prepared_data/diarias3.csv',index=False)

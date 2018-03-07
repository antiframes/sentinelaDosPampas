import urllib
import urllib.request
import re

#abrir página da lista de deputados
dep_list = open('1_original_data/Lista de Deputados.html','r')
src = dep_list.read()
dep_list.close()

#pegar links das páginas dos deputados
deps = re.findall(r'ww1\.al\.rs\.gov\.br\/[a-zA-Z_]+',src)
deps = list(set(deps))#remover links duplicados
deps2 = []
for dep in deps:
    name = dep.split('/')[1]#limpar sites
    deps2.append(name)
    
deps2.append('marcelvanhattem')#saiu do cargo 2 dias atrás e, por isso, não apareceu na lista

depids=[]
#pegar id dos deputados
for dep in deps2:
    print(dep)
    url = 'http://ww1.al.rs.gov.br/'+dep+'/Transpar%C3%AAncia/Gastos.aspx'
    req = urllib.request.urlopen(url)
    res = str(req.read())
    depid = re.findall(r'IdCategoriaCota=[0-9]+',res)[0]
    depid = depid.split('=')[1]
    depids.append(depid)
    
outfile = open('depids.csv','w')
outfile.write('dep,id\n')
for i in range(len(deps2)):
    outfile.write(deps2[i]+','+depids[i]+'\n')
    
outfile.close()

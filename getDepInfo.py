s = open('1_original_data/Lista de Deputados.html','r')
from lxml import html
tree = html.fromstring(s)
tree = html.fromstring(str(s))
s
str(s)
tree = html.fromstring(s.read())
s.close()
parties = tree.xpath('//span[@class="lbllstdeputadosiglapartido"]/text()')
deps = tree.xpath('//a[@class="hlklstdeputado"]/text()')
depids = tree.xpath('//a[@class="hlklstdeputado"]')
for i in range(len(depids)):
    depids[i] = depids[i].attrib['href'].split('/')[3]
    
    
    
    
outfile = open('depinfo.csv','w')
outfile.write("depid,depname,depparty\n")
for i in range(len(deps)):
    outfile.write(parties[i]+','+deps[i]+','+depids[i]+'\n')
outfile.close()

def to_number(s):
	s=s.replace('.','')
	s=s.replace(',','.')
	return float(s)
ano = []
deps = []
links = []
quantidade = []
valor = []
recolhidas=[]
for year in (2015,2016,2017):
	infile = open('1_original_data/diarias'+str(year)+'.html','r')
	data = infile.read()
	infile.close()
	from lxml import html
	tree = html.fromstring(data)
	items=tree.xpath('//td/text()')
	items2 = []
	for line in items:
		n = line.strip(' \n\r')
		if len(n)>0:
			items2.append(line)
		
	deps1 = tree.xpath('//a/text()')
	del deps1[0:4]
	deps+=deps1
	links1 = tree.xpath('//a/@href')
	del links1[0:4]
	links+=links1
	j = 0
	for i in range(len(links1)):
		quantidade.append(to_number(items2[j]))
		valor.append(to_number(items2[j+1].split(' ')[1]))
		recolhidas.append(to_number(items2[j+2]))
		j+=3
		
	for i in range(len(links1)):
		ano.append(year)

d = {'dep':deps,'link':links,'quantidade':quantidade,'valor':valor,'recolhidas':recolhidas,'ano':ano}
import pandas as pd
df = pd.DataFrame(data=d)
df.to_csv('2_prepared_data/diarias1.csv',index=False,sep=',')
quit()

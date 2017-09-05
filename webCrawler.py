import re
import sys
import os

#para executar: python nome.py www.sitequalquer.com.br tag
#ex: python webCrawler.py www.utfpr.edu.br a
#obtem todo conteudo que estiver na tag <a     </a>

def main():
	
	url = sys.argv[1]
	os.system('wget ' + url + ' -O page.html')
	f = open('page.html', 'r')

	#fi = open('saida2.txt','w')

	texto = f.read()
	teste = ''

	tag = sys.argv[2]

	tag = "[<]["+tag+"].*[<][/]["+tag+"][>]"

	for x in range(0,len(texto)):
		if texto[x] != '\n':
			teste = teste + texto[x]

	result = re.findall(r'' +tag,teste)
		
	print result
	#fi.write(result)

	f.close()
	#fi.close()


if __name__ == "__main__":
	main()
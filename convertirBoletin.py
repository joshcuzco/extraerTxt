#convertir pdf a imagen
from pdf2image import convert_from_path
#
import extractText as eT
import dataProcessing as dP
#
import sys

if __name__=="__main__":
	files=[['1979',10,10,'b1']]

	for f in files:
		filename='Boletin_'+f[0]+'_insivumeh.pdf'
		fp=f[1]
		lp=f[2]
		tipo=f[3]

		pages=convert_from_path(filename,first_page=fp,last_page=lp)
		for page in pages:
			page_text=eT.get_text(page)
			dP.process_page(page_text,tipo)

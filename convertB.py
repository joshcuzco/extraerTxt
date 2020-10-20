#convertir pdf a imagen
from pdf2image import convert_from_path
#
import dataProcessing as dP

"""
Convierte boletines anuales en archivos de valores separados por comas.
"""

def convert(year,fp,lp,tipo):
	filename='Boletin_'+year+'_insivumeh.pdf'
	pages=convert_from_path('boletines_anuales/'+filename,first_page=fp,last_page=lp)
	if tipo=='b2s':
		filename='sensibles_'+filename
	with open('outs/'+filename.replace('.pdf','.csv'),'w') as output:
		output.write('#año,mes,dia,hora,min,seg,latitud,longitud,profundidad,rem,erh,erz,magnitud,dm,ada,no,int\n')
	for page in pages:
		page_text=dP.process_page(page,year,tipo)
		with open('outs/'+filename.replace('.pdf','.csv'),'a') as output:
			output.write(page_text)

if __name__=="__main__":
	#test lists
#	files=[['1979',10,10,'b1']]
#	files=[['1982',32,32,'b2']]
#	files=[['1982',29,29,'b2s']]
	#el weno
#	files=[['1977',9,24,'b1'],['1978',19,44,'b1'],['1979',7,90,'b1']]
#	files=[['1980',12,66,'b1'],['1981',25,75,'b1'],['1982',32,123,'b2'],['1983',22,105,'b2']]
	files=[['1982',29,31,'b2s'],['1983',19,21,'b2s']]
	#hay un pinche listado de sensibles en 1978, páginas 12-18

	for f in files:
		year=f[0]
		fp=f[1]
		lp=f[2]
		tipo=f[3]
		convert(year,fp,lp,tipo)
		print(year+'>> sin problemas')

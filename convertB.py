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
	files=[['1982',29,29,'b2s']]

	for f in files:
		year=f[0]
		fp=f[1]
		lp=f[2]
		tipo=f[3]
		convert(year,fp,lp,tipo)

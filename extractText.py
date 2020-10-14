#librereias para procesar imagen
try:
	from PIL import Image
except ImportError:
	import Image
from PIL import ImageFilter as IF
#motor OCR
import pytesseract
#convertir pdf a imagen
from pdf2image import convert_from_path
#otras librerias de python
import sys
import re

'''
Núcleo de extracción de texto. Tomo una página, aplica un filtro,
analiza la orientación, la rota si es necesario y obtiene el texto.
'''

def get_text(page):
	'''
	Extrae el texto como una sola string con OCR.
	'''
	rotate(page)
	#page segmentation mode:
	# 6    Asume un único bloque uniforme de texto.
	pagesegmode=r'--psm 6'
	#cargar y procesar imagen
	pageIm=Image.open('temp.jpg')
	pageIm=pageIm.filter(IF.UnsharpMask())
	#ocr
	text=pytesseract.image_to_string(pageIm,lang='spa',config=pagesegmode)
	return text

def rotate(page):
	'''
	Detecta la orientación del texto y rota la página respectivamente.
	'''
	page.save('temp.jpg')
	osd_info=pytesseract.image_to_osd(Image.open('temp.jpg'))
	rot=re.search('(?<=Rotate: )\d+',osd_info).group(0)
	rot=int(rot)
	if rot!=0:
		mask=Image.new('L',page.size,255)
		page=page.rotate(360-rot,expand=True)
		mask=mask.rotate(360-rot,expand=True)
		page.save('temp.jpg','JPEG')

if __name__=="__main__":
	filename=sys.argv[1]
	
	if '.pdf' in filename:
		try:
			fp=int(sys.argv[2])
		except IndexError:
			fp=None
		try:
			lp=int(sys.argv[3])
		except IndexError:
			lp=None

		pages=convert_from_path(filename,first_page=fp,last_page=lp)
		for page in pages:
			page_text=get_text(page)
			print(page_text)
	else:
		page=Image.open(filename)
		page_text=get_text(page)
		print(page_text)

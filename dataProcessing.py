import extractText as eT

"""
Convierte una página en un conjunto de objetos evento y los escribe
en un archivo de texto.
"""

class event:
	def __init__(self):
		#tiempo de origen
		self.a='';	self.mes='';	self.d='';	self.h='';	self.min='';	self.seg='';
		#coordenadas
		self.lat='';	self.lon='';	self.prof='';
		#errores
		self.rem='';	self.erh='';	self.erz='';
		#magnitud
		self.mag=''
		#número de estaciones usadas para detectar el evento
		self.no=''
		#distancia a la estación más cercana
		self.dm=''
		#separación azimutal máxima entre estaciones
		self.ada=''
		#otros datos
		self.region=''; self.intmer='';
			
	def tipob1(self,line,year,month):
			#boletines hasta 1981
			#la línea en una página tipo b1 se ve
			#dia hr min seg lat long prof mag dm ada rem erh erv region
			# 0  1   2   3   4   5    6    7  8   9  10  11  12  13
			try:
				self.a=year
				self.mes=month
				self.d=jd(line[0])
				self.h=jd(line[1])
				self.min=jd(line[2])
				self.seg=jd(line[3])
				#
				self.lat=coord(line[4])
				self.lon=coord(line[5])
				self.prof=jd(line[6])
				#
				self.mag=jd(line[7])
				#
				self.dm=jd(line[8])
				self.ada=jd(line[9])
				#
				self.rem=jd(line[10])
				self.erh=jd(line[11])
				self.erv=jd(line[12])
			except IndexError:
				pass

	def tipob2(self,line,year,intensity=''):
		#boletines desde 1982
		#la línea en una página tipo b2 se ve
		#mes dia hr min seg lat long prof mag no dm ada rem erh erz region
		# 0   1  2   3   4   5   6    7    8  9  10 11  12  13  14    15
		if intensity:
			self.intmer=intensity
		try:
			self.a=year
			self.mes=jd(line[0])
			self.d=jd(line[1])
			self.h=jd(line[2])
			self.min=jd(line[3])
			self.seg=jd(line[4])
			#
			self.lat=coord(line[5])
			self.lon=coord(line[6])
			self.prof=jd(line[7])
			#
			self.mag=jd(line[8])
			#
			self.no=jd(line[9])
			self.dm=jd(line[10])
			self.ada=jd(line[11])
			#
			self.rem=jd(line[12])
			self.erh=jd(line[13])
			self.erz=jd(line[14])
		except IndexError:
			pass

	def attributelist(self):
		return [self.a,self.mes,self.d,self.h,self.min,self.seg,self.lat,self.lon,self.prof,self.rem,self.erh,self.erz,self.mag,self.dm,self.ada,self.no,self.intmer]

	def dataline(self):
		self.dl=','.join(self.attributelist())+'\n'
		return self.dl

def jd(text):
	'''
	Solo quiero los dígitos.
	'''
	return ''.join(c for c in text if c.isdigit() or c=='.')

def alldigits(text):
	'''
	Saber si todos los caracteres en una cadena son dígitos o punto.
	'''
	for c in text:
		if not (c.isdigit() or c=='.'):
			return False
	return True

def coord(text):
	'''
	Las coordenadas están en grad'min.dmin.
	Las convierte en grad.dgrad.
	'''
	try:
		crd=''.join(c for c in text if c.isdigit())
		grad=float(crd[0:2])
		mins=float(crd[2:4]+'.'+crd[4:])
		return str(grad+mins/60)
	except (ValueError,IndexError):
		return ''

def search_month(text):
	'''
	Algunas páginas especifican el mes textualmente.
	'''
	year={'ENERO':'01','FEBRERO':'02','MARZO':'03','ABRIL':'04','MAYO':'05','JUNIO':'06','JULIO':'07','AGOSTO':'08','SEPTIEMBRE':'09','OCTUBRE':'10','NOVIEMBRE':'11','DICIEMBRE':'12'}
	months=year.keys()
	for month in months:
		if month in text:
			return year[month]

def process_page(page,year,tipo):
	'''
	Convertir el texto extraido en data usable.
	'''
	text=eT.get_text(page)
	output=''

	if tipo=='b1':
		month=search_month(text)

	lines=text.split('\n')
	for line in lines:
		line=line.replace(',','.')
		line_elements=line.split()

		try:
			l=int(line_elements[0])
		except (ValueError, IndexError):
			continue

		if tipo=='b2s':
			intensity=line_elements.pop()
			discard=line_elements.pop(0)

		while not alldigits(line_elements[-1]):
			discard=line_elements.pop()
	
		s=event()
		if tipo=='b1':
			s.tipob1(line_elements,year,month)
		if tipo=='b2':
			s.tipob2(line_elements,year)
		if tipo=='b2s':
			s.tipob2(line_elements,year,intensity)

		dataline=s.dataline()
		output=output+dataline

	return output







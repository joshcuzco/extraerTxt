class event:
	def __init__(self):
		if tipo=='b1':
			#tiempo de origen
			self.a=''
			self.mes=''
			self.d=''
			self.h=''
			self.min=''
			#coordenadas
			self.lat=''
			self.lon=''
			self.prof=''
			#errores
			self.rem=''
			self.erh=''
			self.erz=''
			#magnitud
			self.mag=''
			#número de estaciones usadas para detectar el evento
			self.no=''
			#distancia a la estación más cercana
			self.dm=''
			#separación azimutal máxima entre estaciones
			self.ada=''
			#otros datos
			self.region=''
			self.intmer=''
			
	def tipob1(line):
			

def search_month(text):
	'''
	Algunas páginas especifican el mes textualmente.
	'''
	year={'ENERO':'01','FEBRERO':'02','MARZO':'03','ABRIL':'04','MAYO':'05','JUNIO':'06','JULIO':'07','AGOSTO':'08','SEPTIEMBRE':'09','OCTUBRE':'10','NOVIEMBRE':'11','DICIEMBRE':'12'}
	months=year.keys()
	for month in months:
		if month in text:
			return year[month]

def process_page(text,tipo):
	'''
	Convertir el texto extraido en data usable.
	'''
	if tipo=='b1':
		month=search_month(text)

		lines=text.split('\n')
		for line in lines:
			line_elements=line.split()
			try:
				l=int(line_elements[0])
			except (ValueError, IndexError):
				continue
			s=event.tipob1(line)

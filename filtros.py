import os

def valid_line(line):
	return (check_date(line) and check_coords(line) and check_errors(line) and check_mag(line))

#time checking---------------------------------------------------
def check_date(line):
	date=line.split(',')[0:6]
	try:
		mes=float(date[1])
		d=float(date[2])
		h=float(date[3])
		m=float(date[4])
		s=float(date[5])
	except ValueError:
		return False

	return valid_date(mes,d,h,m,s)

def valid_date(mes,d,h,m,s):
	if not date_integers(mes,d,h,m):
		return False

	if not valid_calendar(mes,12):
		return False
	month_days=get_month_days(mes)

	return (valid_calendar(d,month_days) and valid_time(h,23) and valid_time(m,59) and valid_time(s,59))

def date_integers(mes,d,h,m):
	return (mes.is_integer() and d.is_integer() and h.is_integer() and m.is_integer())

def get_month_days(mes):
	if mes==2:
		return 29
	if (mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12):
		return 31
	if (mes==4 or mes==6 or mes==9 or mes==11):
		return 30

def valid_calendar(n,n_max):
	if (n==0 or n>n_max):
		return False
	return True

def valid_time(n,n_max):
	if n>n_max:
		return False
	return True

#coord checking--------------------------------------------------
def check_coords(line):
	coords=line.split(',')[6:9]
	for coord in coords:
		if coord=='':
			return False
	return True

#error checking--------------------------------------------------
def check_errors(line):
	errs=line.split(',')[9:12]
	for err in errs:
		if err=='':
			return False
	return True

#magnitude checking----------------------------------------------
def check_mag(line):
	mag=line.split(',')[12]
	if (mag=='' or float(mag)>10):
		return False
	return True

#----------------------------------------------------------------

if __name__=="__main__":
	files=os.listdir('outs/')

	for filename in files:
		with open('outs/'+filename,'r') as f:
			content=f.readlines()
		for line in content:
			if line[0]=='#':
				with open('filtered/rev'+filename,'w') as f:
					f.write(line)
				with open('discarded/dis'+filename,'w') as f:
					f.write(line)
				continue

			if valid_line(line):
				with open('filtered/rev'+filename,'a') as f:
					f.write(line)
			else:
				with open('discarded/dis'+filename,'a') as f:
					f.write(line)

		print(filename+' >> sin problemas')

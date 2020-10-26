import os

def valid_time(n,n_max):
	if (n==0 or n>n_max):
		return False
	return True

def check_date(mes,d,h,m,s):
	valid_date=True
	if not valid_time(mes,12):
		valid_date=False
	if not valid_time(d,31):
		valid_date=False
	if not valid_time(h,23):
		valid_date=False
	if not valid_time(m,59):
		valid_date=False
	if not valid_time(s,59):
		valid_date=False
	return valid_date

def valid_line(line):
	check_date()
	check_errors()
	check_prof_mag()

if __name__=="__main__":
	files=os.listdir('outs/')

	for filename in files:
		with open('outs/'+filename,'r') as f:
			content=f.readlines()
		for line in content:
			if line[0]=='#':
				continue

			a=valid_line(line)

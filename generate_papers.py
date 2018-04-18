import csv

f=open('citations.csv','rb')
reader=csv.reader(f)

any='ccc'
for row in reader:
	if not(any==row[6]):
		any=row[6]
		print '= '+any
	print ': {'+row[1]+'} '+row[0]

f.close()

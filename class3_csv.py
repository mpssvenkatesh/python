import csv


fname = 'class3Example.csv'

f = open(fname, 'r')

data = csv.reader(f)

lsData = list(data)

for line in lsData:
    print(line)

f.close()

f = open('class3Example.csv', 'a', newline='')

ls1 = ['Kevin', '30', 'CSIT']
ls2 = ['Dave', '45', 'BA']
ls3 = ['Dom', '50', 'MBA']

pen = csv.writer(f, delimiter='@', lineterminator='\n\n\n')
pen.writerows([ls1, ls2, ls3])

f.close()


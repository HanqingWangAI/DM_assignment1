# encoding=utf-8
import numpy as np
import csv
from matplotlib import pyplot as plt

database = []
database.append('Data/NFL Play by Play 2009-2017 (v4).csv')
database.append('Data/Building_Permits.csv')

event = []

NA = ['NA','None','','NONE','none','Na']

def main(database_id):
    with open('Data/nominal_%d'%database_id,'r') as fp:
        nominal = [int(n)-1 for n in fp.read().split(' ')]

    with open(database[database_id],encoding='utf-8') as fp:
        reader =  csv.reader(fp)
        for row in reader:
            event.append(row)

    num_att = len(event[0])
    cnt = len(event)
    print(len(nominal))
    with open('frequency_%d.txt'%database_id,'w',encoding='utf-8') as fp:
        for n in nominal:
            dic = {}
            
            attr = event[0][n]
            for i in range(1, cnt):
                x =  len(event[i])
                val = event[i][n]
                if val in dic:
                    dic[val] += 1
                else:
                    dic[val] = 1
            fp.write('Attribute %s\n'%attr)
            for val in dic:
                fp.write('%s %d\n'%(val,dic[val]))

    with open('numeric_%d.md'%database_id,'w',encoding='utf-8') as fp:
        fp.write('| attr_name | Max | Min | Mean | Median | Q1 | Q3 | NA |\n')
        fp.write('|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|\n')

        for i in range(0, num_att):
            if i in nominal:
                continue
            name = event[0][i]
            # print(i, name)
            count = 0
            lost = 0
            ar = []
            for j in range(1,cnt):
                val = event[j][i]
                if val in NA:
                    lost += 1
                else:
                    ar.append(float(val))
                    count += 1
            
            ar = np.array(sorted(ar))
            maxx = ar.max()
            minn = ar.min()
            mean = ar.mean()
            medi = ar[int(count/2)]
            q1 = ar[int(count/4)]
            q3 = ar[int(count/4*3)]
            fp.write('|%s|%.2f|%.2f|%.2f|%.2f|%.2f|%.2f|%d|\n'%(name,maxx,minn,mean,medi,q1,q3,lost))
    
    xx = np.sort(np.random.standard_normal(100000))
    x = []
    for i in range(100):
        x.append(xx[int(100000*(1.0*(i)/100))])
    x = np.array(x) 

    
    for i in range(0, num_att):
            if i in nominal:
                continue
            name = event[0][i]

            # print(i, name)
            count = 0
            lost = 0
            ar = []
            for j in range(1,cnt):
                val = event[j][i]
                if val in NA:
                    lost += 1
                else:
                    ar.append(float(val))
                    count += 1
            
            ar = np.array(sorted(ar))
            
            plt.hist(ar,20)
            plt.savefig('Figures/%s_%d.png'%(name,database_id))
            plt.close()
            y = []
            for j in range(100):
                y.append(ar[int(count*(1.0*(j)/100))])
            y = np.array(y)
            plt.scatter(x,y)
            plt.savefig('Figures/qq_%s_%d.png'%(name,database_id))
            plt.close()
            plt.boxplot([ar],labels=[name])
            plt.savefig('Figures/box_%s_%d.png'%(name,database_id))
            plt.close()
    
    
def showfigures(database_id):
    width = '300px'
    with open('Data/nominal_%d'%database_id,'r') as fp:
        nominal = [int(n)-1 for n in fp.read().split(' ')]

    with open(database[database_id],encoding='utf-8') as fp:
        reader =  csv.reader(fp)
        for row in reader:
            event.append(row)
            break
    num_att = len(event[0])

    with open('Show_figures_%d.md'%database_id,'w') as fp:

        for i in range(0, num_att):
                if i in nominal:
                    continue
                name = event[0][i]
                fp.write('<img src="Figures/%s_%d.png" width="%s">\n'%(name,database_id,width))
                fp.write('<img src="Figures/qq_%s_%d.png" width="%s">\n'%(name,database_id,width))
                fp.write('<img src="Figures/box_%s_%d.png" width="%s">\n'%(name,database_id,width))
                fp.write('<center>%s Histogram, Q-Q plot, Boxplot</center><br>\n'%name)

if __name__  == '__main__':
    # main(1)
    showfigures(1)

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
    width = '250px'
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
                fp.write('\n\n**%s**\n\n'%name)

                fp.write('<table>\n')
                fp.write('<tr>\n')
                fp.write('<th><img src="Figures/%s_%d.png" width="%s"><p>Histogram</p></th>\n'%(name,database_id,width))
                fp.write('<th><img src="Figures/qq_%s_%d.png" width="%s"><p>Q-Q plot</p></th>\n'%(name,database_id,width))
                fp.write('<th><img src="Figures/box_%s_%d.png" width="%s"><p>Boxplot</p></th>\n'%(name,database_id,width))
                fp.write('</tr>\n')
                fp.write('</table>\n')
                fp.write('\n\n--------------------\n<br>\n')

def impute(database_id):
    from sklearn.linear_model import LinearRegression
    from utils.skmice import MiceImputer
    from sklearn.neighbors import NearestNeighbors
    cnt = 0
    with open('Data/NA_%d'%database_id,'r') as fp:
        nas = [int(n)-1 for n in fp.read().split(' ')]

    with open(database[database_id],encoding='utf-8') as fp:
    # with open(database[database_id]) as fp:
        reader =  csv.reader(fp)
        for row in reader:
            event.append(row)
            cnt += 1

    num_att = len(event[0])

    # Impute with the most frequence value
    for i in nas:
        name = event[0][i]
        dic = {}
        maxx = 0
        max_val = 0
        lost = 0
        ar = []
        for j in range(1,cnt):
            val = event[j][i]
            if val not in NA:
                val = float(val)
                ar.append(val)
                if val in dic:
                    dic[val] += 1
                else:
                    dic[val] = 1
                if maxx < dic[val]:
                    maxx = dic[val]
                    max_val = val
            else:
                lost += 1
        
        for j in range(lost):
            ar.append(max_val)
        
        ar = np.array(ar)
        plt.hist(ar,20)
        plt.savefig('Figures/mf_%s_%d.png'%(name,database_id))
        plt.close()
    

    # Impute with the corelation matrix
    ar = []
    for i in nas:
        name = event[0][i]
        temp = []

        for j in range(1,cnt):
            val = event[j][i]
            if val not in NA:
                val = float(val)
                temp.append(val)
            else:
                temp.append(np.nan)

        ar.append(temp)
    
    ar = np.array(ar)
    ar = np.transpose(ar)
    # print(ar.shape)

    # ar = ar[:101,:]
    # cnt = ar.shape[0]
    batch_num = 1000
    imputer = MiceImputer()
    batchsize = int((cnt)/batch_num)
    for i in range(batch_num):
        print(i)
        if i == batch_num - 1:
            ar[i*batchsize:,:] = imputer.transform(ar[i*batchsize:,:], LinearRegression, 5)
        else:
            ar[i*batchsize:(i+1)*batchsize,:] = imputer.transform(ar[i*batchsize:(i+1)*batchsize,:], LinearRegression, 5)
    # print(ar.shape)
    for _,i in enumerate(nas):
        # print(name)
        # print(ar[:,_])
        name = event[0][i]
        plt.hist(ar[:,_],20)
        plt.savefig('Figures/cm_%s_%d.png'%(name,database_id))
        plt.close()
    
    # Impute using KNN
    ar = []
    for i in nas:
        name = event[0][i]
        temp = []

        for j in range(1,cnt):
            val = event[j][i]
            if val not in NA:
                val = float(val)
                temp.append(val)
            else:
                temp.append(np.nan)

        ar.append(temp)
    
    ar = np.array(ar)
    ar = np.transpose(ar)

    batchsize = int((cnt)/1000)
    for i in range(1000):
        if i == 999:
            batch = np.array(ar[i*batchsize:,:])
        else:
            batch = np.array(ar[i*batchsize:(i+1)*batchsize,:])
        
        mask = np.isnan(batch)

        index = np.where(mask==True)
        batch[index[0],index[1]] = 0

        neig = NearestNeighbors(n_neighbors=5, algorithm="ball_tree").fit(batch)

        for _, j in enumerate(index[0]):
            d, pos = neig.kneighbors([batch[j]])
            pos = pos[0]
            for a in range(1,5):
                if batch[pos[a],index[1][_]] != 0:
                    batch[j,index[1][_]] = batch[pos[a],index[1][_]]
        
        if i == 999:
            ar[i*batchsize:,:] = batch
        else:
            ar[i*batchsize:(i+1)*batchsize,:] = batch

    for _,i in enumerate(nas):
        name = event[0][i]
        plt.hist(ar[:,_],20)
        plt.savefig('Figures/knn_%s_%d.png'%(name,database_id))
        plt.close()

def impute_figures(database_id):
    width = '200px'
    with open('Data/NA_%d'%database_id,'r') as fp:
        nas = [int(n)-1 for n in fp.read().split(' ')]
        
    with open(database[database_id],encoding='utf-8') as fp:
        reader =  csv.reader(fp)
        for row in reader:
            event.append(row)
            break
    num_att = len(event[0])
    
    with open('Impute_figures_%d.md'%database_id,'w',encoding='utf-8') as fp:

        for i in nas:
                name = event[0][i]
                fp.write('\n\n**%s**\n\n'%name)

                fp.write('<table>\n')
                fp.write('<tr>\n')
                fp.write('<th><img src="Figures/%s_%d.png" width="%s"><p>剔除缺失</p></th>\n'%(name,database_id,width))
                fp.write('<th><img src="Figures/mf_%s_%d.png" width="%s"><p>高频填补</p></th>\n'%(name,database_id,width))
                fp.write('<th><img src="Figures/cm_%s_%d.png" width="%s"><p>相关属性填补</p></th>\n'%(name,database_id,width))
                fp.write('<th><img src="Figures/knn_%s_%d.png" width="%s"><p>KNN填补</p></th>\n'%(name,database_id,width))
                fp.write('</tr>\n')
                fp.write('</table>\n')
                fp.write('\n\n--------------------\n<br>\n')


if __name__  == '__main__':
    # main(1)
    # showfigures(1)
    impute(1)
    # impute_figures(1)
import random
import math
import os
import sys
class data:
    def __init__(self, temperature,humidity,light,co2,class_value):

        self.temperature = temperature
        self.humidity=humidity
        self.light=light
        self.co2=co2
        self.class_value=class_value
    def change(self):
        self.temperature=0.000
def write_to_file(errors):
    f=open("error_Matrix_KModified.txt","w")
    for i in range(len(errors)):
        for j in range(len(errors[i])-1):
            f.write(str(errors[i][j])+' ')
        f.write(str(errors[i][j]))
        f.write('\n')
    f.close()

def readInputs():
    f=open("occupancy_data/datatraining.txt","r")
    k=f.readline()
    for line in f:
        ls=line.split(",")
        k=list(ls[len(ls)-1])
        d=data(float(ls[2]),float(ls[3]),float(ls[4]),float(ls[5]),int(k[0]))
        required_data.append(d)
    f.close()
def partition(copy_data,n):
        division=len(copy_data)/float(n)
        return [copy_data[int(round(division*i)) : int(round(division*(i+1)))] for i in xrange(n)]

def diff_value(l1,l2):
    return math.sqrt(pow(l1.temperature-l2.temperature,2)+pow(l1.humidity-l2.humidity,2)+pow(l1.light-l2.light,2)+pow(l1.co2-l2.co2,2))

def evaluate_nearest_class(temp,k2):
    w1=0
    w2=0
    weight=0
    for i in range(k2):
        if temp[k2-1][0]-temp[0][0]==0:
            weight=1
        else:
            weight=(temp[k2-1][0]-temp[i][0])/(temp[k2-1][0]-temp[0][0])
        if temp[i][1]==1:
            w1+=weight
        else:
            w2+=weight
    if w1>w2:
        return 1
    else:
        return 0
def calculate_distance(validation,train,k1):
    count=0
    for valid_value in validation:
        dist=[]
        for train_value in train:
            dist.append([diff_value(valid_value,train_value),train_value.class_value])
        dist.sort(key=lambda x:x[0])

        if valid_value.class_value==evaluate_nearest_class(dist,k1):
            count+=1
    return (float(len(validation)-count))/(float(len(validation)))



def euclidean(validation,train):
    error=[]
    for k in range(1,11):
        error.append(calculate_distance(validation,train,k))
    return error
def calculate_k_value(errors):
    mean=float(float(errors[0][0]+errors[1][0]+errors[2][0])/(float(len(errors))))
    k_value=1
    means.append(mean)
    for j in range(1,len(errors[0])):
        sum1=float(float(errors[0][j]+errors[1][j]+errors[2][j])/(float(len(errors))))
        means.append(sum1)
        if(sum1<mean):
            mean=sum1
            k_value=j+1
    return k_value


if __name__ == '__main__':
    errors=[]
    means=[]
    required_data=[]
    readInputs()
    copy_data=required_data
    random.shuffle(copy_data)
    cross_validation_data=partition(copy_data,3)
    print len(required_data)
    for i in range(3):
        validation=cross_validation_data[i]
        train=[]
        for j in filter(lambda x:x!=i,range(3)):
            train+=cross_validation_data[j]
        print len(train)
        errors.append(euclidean(validation,train))

    write_to_file(errors)
    final_k=calculate_k_value(errors)
    print errors
    print final_k

    print ".......................Training the network is finished.........................."
    print ".......................Starting the testing ........................."

#os.system("python datatest.py "+str(final_k))
